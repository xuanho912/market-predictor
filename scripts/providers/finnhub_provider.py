from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
BASE_URL = "https://finnhub.io/api/v1"
DEFAULT_TIMEOUT_SECONDS = 12
MAX_RETRIES = 2
BACKOFF_SECONDS = 1.2
RISK_KEYWORDS = (
    "crisis",
    "default",
    "downgrade",
    "bank stress",
    "liquidity",
    "recession",
    "inflation",
    "hawkish",
    "war",
    "tariff",
    "selloff",
    "plunge",
    "credit",
    "shutdown",
)


def fetch_finnhub_bundle(symbols: tuple[str, ...], lookback_days: int = 180) -> dict[str, Any]:
    token = os.getenv("FINNHUB_API_KEY", "").strip()
    now = datetime.now(timezone.utc).isoformat()
    if not token:
        return _empty_bundle(status="missing_api_key", generated_at=now)

    provider = _FinnhubClient(token)
    quote_payloads: dict[str, Any] = {}
    candle_payloads: dict[str, Any] = {}
    sentiment_payloads: dict[str, Any] = {}
    for symbol in symbols:
        quote_payloads[symbol] = provider.get("quote", {"symbol": symbol}, cache_key=f"quote_{symbol}")
        candle_payloads[symbol] = provider.get(
            "stock/candle",
            {
                "symbol": symbol,
                "resolution": "D",
                "from": str(int(time.time()) - lookback_days * 86400),
                "to": str(int(time.time())),
            },
            cache_key=f"candle_{symbol}_{lookback_days}",
        )
        sentiment_payloads[symbol] = provider.get("news-sentiment", {"symbol": symbol}, cache_key=f"sentiment_{symbol}")

    today = date.today()
    economic_calendar = provider.get(
        "calendar/economic",
        {"from": (today - timedelta(days=7)).isoformat(), "to": (today + timedelta(days=21)).isoformat()},
        cache_key="economic_calendar",
    )
    market_status = provider.get("stock/market-status", {"exchange": "US"}, cache_key="market_status_us")
    market_holiday = provider.get("stock/market-holiday", {"exchange": "US"}, cache_key="market_holiday_us")
    market_news = provider.get("news", {"category": "general"}, cache_key="market_news_general")
    provider_status = provider.status()
    news_items = _extract_news_items(market_news)
    economic_events = _extract_economic_events(economic_calendar)
    return {
        "provider": "finnhub",
        "generated_at": now,
        "configured": True,
        "available": provider_status["successful_requests"] > 0,
        "missing": False,
        "rate_limited": provider_status["rate_limited"],
        "cache_used": provider_status["cache_used"],
        "failed_requests": provider_status["failed_requests"],
        "successful_requests": provider_status["successful_requests"],
        "quotes": _sanitize_results(quote_payloads),
        "candles": _sanitize_results(candle_payloads),
        "news_sentiment": _sanitize_results(sentiment_payloads),
        "economic_calendar": {
            "status": economic_calendar["status"],
            "source": economic_calendar["source"],
            "events": economic_events[:50],
            "event_count": len(economic_events),
        },
        "market_status": {
            "status": market_status["status"],
            "source": market_status["source"],
            "payload": _drop_large_or_sensitive(market_status.get("data")),
        },
        "market_holiday": {
            "status": market_holiday["status"],
            "source": market_holiday["source"],
            "payload": _drop_large_or_sensitive(market_holiday.get("data")),
        },
        "market_news": {
            "status": market_news["status"],
            "source": market_news["source"],
            "items": news_items[:40],
            "news_risk_score": _news_risk_score(news_items),
        },
        "rates_data": {
            "status": "missing",
            "source": "finnhub",
            "detail": "No Treasury yield curve endpoint is used from Finnhub in this project; FRED remains required.",
        },
        "alternative_data": {
            "status": "missing",
            "source": "finnhub",
            "detail": "No alternative data endpoint is connected.",
        },
    }


class _FinnhubClient:
    def __init__(self, token: str) -> None:
        self._token = token
        self._successful_requests = 0
        self._failed_requests = 0
        self._rate_limited = False
        self._cache_used = False

    def get(self, endpoint: str, params: dict[str, str], cache_key: str) -> dict[str, Any]:
        safe_params = dict(params)
        safe_params["token"] = self._token
        url = f"{BASE_URL}/{endpoint}?{urllib.parse.urlencode(safe_params)}"
        cache_path = _cache_file(cache_key)
        last_error = None
        for attempt in range(MAX_RETRIES + 1):
            try:
                request = urllib.request.Request(url, headers={"User-Agent": "market-predictor/1.0"})
                with urllib.request.urlopen(request, timeout=DEFAULT_TIMEOUT_SECONDS) as response:
                    status_code = getattr(response, "status", 200)
                    raw = response.read().decode("utf-8")
                if status_code == 429:
                    self._rate_limited = True
                    return self._cached_or_status(cache_path, "rate_limited")
                payload = json.loads(raw) if raw else {}
                _write_cache(cache_path, payload)
                self._successful_requests += 1
                return {"status": "available", "source": "finnhub", "data": payload, "cache_used": False}
            except Exception as exc:
                last_error = exc
                if "HTTP Error 429" in str(exc):
                    self._rate_limited = True
                    return self._cached_or_status(cache_path, "rate_limited")
                if attempt < MAX_RETRIES:
                    time.sleep(BACKOFF_SECONDS * (attempt + 1))
        self._failed_requests += 1
        cached = self._cached_or_status(cache_path, "failed")
        cached["error_type"] = type(last_error).__name__ if last_error else "unknown"
        return cached

    def status(self) -> dict[str, Any]:
        return {
            "successful_requests": self._successful_requests,
            "failed_requests": self._failed_requests,
            "rate_limited": self._rate_limited,
            "cache_used": self._cache_used,
        }

    def _cached_or_status(self, cache_path: Path, status: str) -> dict[str, Any]:
        cached = _read_cache(cache_path)
        if cached is not None:
            self._cache_used = True
            return {"status": status, "source": "local-cache-finnhub", "data": cached, "cache_used": True}
        return {"status": status, "source": "finnhub", "data": None, "cache_used": False}


def _empty_bundle(status: str, generated_at: str) -> dict[str, Any]:
    return {
        "provider": "finnhub",
        "generated_at": generated_at,
        "configured": False,
        "available": False,
        "missing": True,
        "rate_limited": False,
        "cache_used": False,
        "failed_requests": 0,
        "successful_requests": 0,
        "quotes": {},
        "candles": {},
        "news_sentiment": {},
        "economic_calendar": {"status": status, "source": "finnhub", "events": [], "event_count": 0},
        "market_status": {"status": status, "source": "finnhub", "payload": None},
        "market_holiday": {"status": status, "source": "finnhub", "payload": None},
        "market_news": {"status": status, "source": "finnhub", "items": [], "news_risk_score": None},
        "rates_data": {"status": "missing", "source": "finnhub", "detail": "FRED remains required."},
        "alternative_data": {"status": "missing", "source": "finnhub"},
    }


def _sanitize_results(results: dict[str, dict[str, Any]]) -> dict[str, Any]:
    clean: dict[str, Any] = {}
    for symbol, result in results.items():
        payload = result.get("data")
        clean[symbol] = {
            "status": result.get("status"),
            "source": result.get("source"),
            "cache_used": result.get("cache_used", False),
            "payload": _drop_large_or_sensitive(payload),
        }
    return clean


def _drop_large_or_sensitive(payload: Any) -> Any:
    if payload is None:
        return None
    if isinstance(payload, list):
        return payload[:80]
    if isinstance(payload, dict):
        return {key: value for key, value in payload.items() if key.lower() not in {"token", "api_key", "apikey"}}
    return payload


def _extract_news_items(result: dict[str, Any]) -> list[dict[str, Any]]:
    payload = result.get("data")
    if not isinstance(payload, list):
        return []
    items: list[dict[str, Any]] = []
    for item in payload:
        if not isinstance(item, dict):
            continue
        items.append(
            {
                "datetime": item.get("datetime"),
                "headline": item.get("headline"),
                "source": item.get("source"),
                "category": item.get("category"),
                "summary": str(item.get("summary") or "")[:500],
            }
        )
    return items


def _extract_economic_events(result: dict[str, Any]) -> list[dict[str, Any]]:
    payload = result.get("data")
    if isinstance(payload, dict):
        events = payload.get("economicCalendar") or payload.get("events") or []
    elif isinstance(payload, list):
        events = payload
    else:
        events = []
    clean: list[dict[str, Any]] = []
    for event in events:
        if not isinstance(event, dict):
            continue
        clean.append(
            {
                "date": event.get("date") or event.get("time"),
                "event": event.get("event") or event.get("name"),
                "country": event.get("country"),
                "impact": event.get("impact"),
                "actual": event.get("actual"),
                "estimate": event.get("estimate"),
                "previous": event.get("prev") or event.get("previous"),
            }
        )
    return clean


def _news_risk_score(items: list[dict[str, Any]]) -> float | None:
    if not items:
        return None
    hits = 0
    for item in items[:40]:
        text = f"{item.get('headline') or ''} {item.get('summary') or ''}".lower()
        hits += sum(1 for keyword in RISK_KEYWORDS if keyword in text)
    return min(1.0, hits / 20.0)


def _cache_file(cache_key: str) -> Path:
    safe = "".join(character if character.isalnum() or character in {"_", "-"} else "_" for character in cache_key)
    configured = os.getenv("FINNHUB_CACHE_DIR")
    base = Path(configured) if configured else PROJECT_ROOT / "data" / "finnhub_cache"
    return base / f"{safe}.json"


def _write_cache(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"cached_at": datetime.now(timezone.utc).isoformat(), "payload": payload}, ensure_ascii=False),
        encoding="utf-8",
    )


def _read_cache(path: Path) -> Any | None:
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        return payload.get("payload")
    except Exception:
        return None
