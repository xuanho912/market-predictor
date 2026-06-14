from __future__ import annotations

import csv
import json
import os
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
FRED_API_URL = "https://api.stlouisfed.org/fred/series/observations"
FRED_CSV_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv"
DEFAULT_TIMEOUT_SECONDS = 8
MAX_RETRIES = 1
BACKOFF_SECONDS = 1.4

DEFAULT_FRED_SERIES: dict[str, str] = {
    "HY_OAS": "BAMLH0A0HYM2",
    "IG_OAS": "BAMLC0A0CM",
    "BAA_SPREAD": "BAA10Y",
    "DGS10": "DGS10",
    "DGS2": "DGS2",
    "DGS3MO": "DGS3MO",
    "DFII10": "DFII10",
    "FINANCIAL_STRESS": "STLFSI4",
    "RECESSION": "USREC",
}


def fetch_fred_bundle(lookback_days: int = 1800, series_map: dict[str, str] | None = None) -> dict[str, Any]:
    token = os.getenv("FRED_API_KEY", "").strip()
    generated_at = datetime.now(timezone.utc).isoformat()
    series_ids = series_map or DEFAULT_FRED_SERIES
    start_date = (datetime.now(timezone.utc).date() - timedelta(days=lookback_days * 2)).isoformat()
    client = _FredClient(token=token, start_date=start_date, lookback_days=lookback_days)
    series_payloads: dict[str, Any] = {}
    with ThreadPoolExecutor(max_workers=min(6, max(len(series_ids), 1))) as executor:
        futures = {executor.submit(client.fetch_series, name=name, series_id=series_id): name for name, series_id in series_ids.items()}
        for future in as_completed(futures):
            name = futures[future]
            try:
                series_payloads[name] = future.result()
            except Exception as exc:
                series_payloads[name] = {
                    "name": name,
                    "series_id": series_ids[name],
                    "rows": [],
                    "row_count": 0,
                    "latest_date": None,
                    "source": "fred",
                    "status": "missing",
                    "real_data": False,
                    "fallback_used": False,
                    "stale_data": True,
                    "missing_data": True,
                    "error_type": type(exc).__name__,
                }
    status = client.status(series_payloads)
    return {
        "provider": "fred",
        "generated_at": generated_at,
        "configured": bool(token),
        "available": status["successful_series_count"] > 0,
        "missing": status["successful_series_count"] == 0,
        "rate_limited": status["rate_limited"],
        "fallback_used": status["fallback_used"],
        "cache_used": status["cache_used"],
        "failed_series": status["failed_series"],
        "successful_series": status["successful_series"],
        "successful_series_count": status["successful_series_count"],
        "expected_series_count": len(series_ids),
        "series": series_payloads,
        "derived": _derive_fred_metrics(series_payloads),
    }


class _FredClient:
    def __init__(self, *, token: str, start_date: str, lookback_days: int) -> None:
        self._token = token
        self._start_date = start_date
        self._lookback_days = lookback_days
        self._rate_limited = False
        self._cache_used = False
        self._fallback_used = False

    def fetch_series(self, *, name: str, series_id: str) -> dict[str, Any]:
        sources = ("api", "public_csv") if self._token else ("public_csv",)
        last_error = None
        for source in sources:
            for attempt in range(MAX_RETRIES + 1):
                try:
                    rows = self._fetch_api(series_id) if source == "api" else self._fetch_public_csv(series_id)
                    if rows:
                        rows = rows[-self._lookback_days :]
                        _write_cache(_cache_file(series_id), {"series_id": series_id, "rows": rows})
                        if source == "public_csv":
                            self._fallback_used = bool(self._token)
                        return {
                            "name": name,
                            "series_id": series_id,
                            "rows": rows,
                            "row_count": len(rows),
                            "latest_date": rows[-1]["date"],
                            "source": "fred-api" if source == "api" else "fred-public-csv",
                            "status": "available",
                            "real_data": True,
                            "fallback_used": source == "public_csv" and bool(self._token),
                            "stale_data": False,
                            "missing_data": False,
                        }
                except Exception as exc:
                    last_error = exc
                    if "HTTP Error 429" in str(exc):
                        self._rate_limited = True
                        break
                    if attempt < MAX_RETRIES:
                        time.sleep(BACKOFF_SECONDS * (attempt + 1))
        cached = _read_cache(_cache_file(series_id))
        if cached:
            rows = list(cached.get("rows") or [])[-self._lookback_days :]
            if rows:
                self._cache_used = True
                return {
                    "name": name,
                    "series_id": series_id,
                    "rows": rows,
                    "row_count": len(rows),
                    "latest_date": rows[-1]["date"],
                    "source": "local-cache-fred",
                    "status": "available",
                    "real_data": True,
                    "fallback_used": True,
                    "stale_data": False,
                    "missing_data": False,
                }
        return {
            "name": name,
            "series_id": series_id,
            "rows": [],
            "row_count": 0,
            "latest_date": None,
            "source": "fred",
            "status": "rate_limited" if self._rate_limited else "missing",
            "real_data": False,
            "fallback_used": False,
            "stale_data": True,
            "missing_data": True,
            "error_type": type(last_error).__name__ if last_error else None,
        }

    def _fetch_api(self, series_id: str) -> list[dict[str, Any]]:
        params = {
            "series_id": series_id,
            "api_key": self._token,
            "file_type": "json",
            "observation_start": self._start_date,
        }
        url = f"{FRED_API_URL}?{urllib.parse.urlencode(params)}"
        request = urllib.request.Request(url, headers={"User-Agent": "market-predictor/1.0"})
        with urllib.request.urlopen(request, timeout=DEFAULT_TIMEOUT_SECONDS) as response:
            raw = response.read().decode("utf-8")
        payload = json.loads(raw)
        return _parse_api_observations(payload.get("observations") or [])

    def _fetch_public_csv(self, series_id: str) -> list[dict[str, Any]]:
        url = f"{FRED_CSV_URL}?{urllib.parse.urlencode({'id': series_id})}"
        request = urllib.request.Request(url, headers={"User-Agent": "market-predictor/1.0"})
        with urllib.request.urlopen(request, timeout=DEFAULT_TIMEOUT_SECONDS) as response:
            raw = response.read().decode("utf-8")
        return _parse_csv_rows(raw, series_id)

    def status(self, series_payloads: dict[str, Any]) -> dict[str, Any]:
        successful = [name for name, payload in series_payloads.items() if payload.get("real_data")]
        failed = [name for name, payload in series_payloads.items() if not payload.get("real_data")]
        return {
            "successful_series": successful,
            "failed_series": failed,
            "successful_series_count": len(successful),
            "rate_limited": self._rate_limited,
            "cache_used": self._cache_used,
            "fallback_used": self._fallback_used or self._cache_used or not bool(self._token),
        }


def _parse_api_observations(observations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in observations:
        value = _parse_float(item.get("value"))
        date_value = item.get("date")
        if value is None or not date_value:
            continue
        rows.append({"date": str(date_value), "value": value})
    return rows


def _parse_csv_rows(text: str, series_id: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in csv.DictReader(text.splitlines()):
        date_value = row.get("DATE") or row.get("observation_date") or row.get("date")
        value = _parse_float(row.get(series_id) or row.get("value"))
        if value is None or not date_value:
            continue
        rows.append({"date": str(date_value), "value": value})
    return rows


def _derive_fred_metrics(series_payloads: dict[str, Any]) -> dict[str, Any]:
    values = {name: _values(payload) for name, payload in series_payloads.items()}
    dgs10 = _last(values.get("DGS10", []))
    dgs2 = _last(values.get("DGS2", []))
    dgs3mo = _last(values.get("DGS3MO", []))
    hy = values.get("HY_OAS", [])
    ig = values.get("IG_OAS", [])
    stress = values.get("FINANCIAL_STRESS", [])
    recession = values.get("RECESSION", [])
    return {
        "ten_year_minus_two_year": (dgs10 - dgs2) if dgs10 is not None and dgs2 is not None else None,
        "ten_year_minus_three_month": (dgs10 - dgs3mo) if dgs10 is not None and dgs3mo is not None else None,
        "hy_oas_latest": _last(hy),
        "ig_oas_latest": _last(ig),
        "hy_oas_20d_change": _change(hy, 20),
        "ig_oas_20d_change": _change(ig, 20),
        "financial_stress_latest": _last(stress),
        "financial_stress_20d_change": _change(stress, 20),
        "recession_latest": _last(recession),
    }


def _values(payload: dict[str, Any]) -> list[float]:
    return [float(row["value"]) for row in payload.get("rows", []) if row.get("value") is not None]


def _change(values: list[float], lookback: int) -> float | None:
    if len(values) <= lookback:
        return None
    return values[-1] - values[-lookback - 1]


def _last(values: list[float]) -> float | None:
    return values[-1] if values else None


def _parse_float(value: Any) -> float | None:
    try:
        if value in {None, "", "."}:
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def _cache_file(series_id: str) -> Path:
    root = Path(os.getenv("FRED_CACHE_DIR", PROJECT_ROOT / "data" / "fred_cache"))
    return root / f"{series_id}.json"


def _write_cache(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")


def _read_cache(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
