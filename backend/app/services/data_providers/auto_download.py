from __future__ import annotations

import csv
import contextlib
import io
import json
import math
import os
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any


DEFAULT_DOWNLOAD_SYMBOLS = ("SPY", "QQQ", "IWM", "DIA", "^VIX", "HYG", "LQD", "TLT", "UUP", "^TNX")
REAL_DATA_SOURCES = {"yfinance", "yahoo-chart", "stooq", "local-cache-yfinance", "local-cache-yahoo-chart", "local-cache-stooq"}


@dataclass(frozen=True)
class DownloadedSeries:
    symbol: str
    rows: list[dict[str, float | str]]
    source: str
    point_in_time_safe: bool


def refresh_market_data(symbols: tuple[str, ...] = DEFAULT_DOWNLOAD_SYMBOLS, lookback_days: int = 900) -> list[DownloadedSeries]:
    downloaded: list[DownloadedSeries] = []
    for symbol in symbols:
        series = _download_with_fallback(symbol, lookback_days)
        downloaded.append(series)
    return downloaded


def is_real_market_data(series: DownloadedSeries) -> bool:
    return series.source in REAL_DATA_SOURCES and bool(series.rows)


def _download_with_fallback(symbol: str, lookback_days: int) -> DownloadedSeries:
    for loader in (_download_yfinance, _download_yahoo_chart, _download_stooq):
        try:
            series = loader(symbol, lookback_days)
            if series.rows:
                _write_cache(series)
                return series
        except Exception:
            continue

    cached = _read_cache(symbol, lookback_days)
    if cached is not None:
        return cached

    return _synthetic_series(symbol, lookback_days, source="synthetic-fallback")


def _download_yfinance(symbol: str, lookback_days: int) -> DownloadedSeries:
    import yfinance as yf  # type: ignore[import-not-found]

    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        frame = yf.download(symbol, period=f"{lookback_days}d", auto_adjust=True, progress=False, timeout=8)
    if frame.empty:
        raise RuntimeError(f"empty yfinance result for {symbol}")
    rows = []
    for timestamp, row in frame.tail(lookback_days).iterrows():
        rows.append(
            {
                "date": timestamp.date().isoformat(),
                "open": float(row.get("Open", 0.0)),
                "high": float(row.get("High", 0.0)),
                "low": float(row.get("Low", 0.0)),
                "close": float(row.get("Close", 0.0)),
                "volume": float(row.get("Volume", 0.0)),
            }
        )
    return DownloadedSeries(symbol=symbol, rows=_clean_rows(rows)[-lookback_days:], source="yfinance", point_in_time_safe=True)


def _download_yahoo_chart(symbol: str, lookback_days: int) -> DownloadedSeries:
    encoded = urllib.parse.quote(symbol, safe="")
    period2 = int(time.time()) + 86400
    period1 = period2 - int(lookback_days * 3.0 * 86400)
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{encoded}?period1={period1}&period2={period2}&interval=1d"
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    payload = json.loads(urllib.request.urlopen(request, timeout=20).read().decode("utf-8"))
    result = payload["chart"]["result"][0]
    timestamps = result.get("timestamp") or []
    quote = result["indicators"]["quote"][0]
    rows = []
    for index, timestamp in enumerate(timestamps):
        close = _value_at(quote, "close", index)
        if close is None:
            continue
        rows.append(
            {
                "date": datetime.fromtimestamp(timestamp, tz=timezone.utc).date().isoformat(),
                "open": _value_at(quote, "open", index) or close,
                "high": _value_at(quote, "high", index) or close,
                "low": _value_at(quote, "low", index) or close,
                "close": close,
                "volume": _value_at(quote, "volume", index) or 0.0,
            }
        )
    clean = _clean_rows(rows)[-lookback_days:]
    if not clean:
        raise RuntimeError(f"empty yahoo chart result for {symbol}")
    return DownloadedSeries(symbol=symbol, rows=clean, source="yahoo-chart", point_in_time_safe=True)


def _download_stooq(symbol: str, lookback_days: int) -> DownloadedSeries:
    mapped = _stooq_symbol(symbol)
    url = f"https://stooq.com/q/d/l/?s={urllib.parse.quote(mapped)}&i=d"
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    text = urllib.request.urlopen(request, timeout=20).read().decode("utf-8")
    rows = []
    for row in csv.DictReader(text.splitlines()):
        if not row.get("Date") or row.get("Close") in (None, "", "0"):
            continue
        rows.append(
            {
                "date": row["Date"],
                "open": float(row.get("Open") or row["Close"]),
                "high": float(row.get("High") or row["Close"]),
                "low": float(row.get("Low") or row["Close"]),
                "close": float(row["Close"]),
                "volume": float(row.get("Volume") or 0.0),
            }
        )
    clean = _clean_rows(rows)[-lookback_days:]
    if not clean:
        raise RuntimeError(f"empty stooq result for {symbol}")
    return DownloadedSeries(symbol=symbol, rows=clean, source="stooq", point_in_time_safe=True)


def _stooq_symbol(symbol: str) -> str:
    mapping = {
        "SPY": "spy.us",
        "QQQ": "qqq.us",
        "IWM": "iwm.us",
        "DIA": "dia.us",
        "HYG": "hyg.us",
        "LQD": "lqd.us",
        "TLT": "tlt.us",
        "UUP": "uup.us",
        "^VIX": "^vix",
        "^VIX9D": "^vix9d",
        "^VIX3M": "^vix3m",
        "^VIX6M": "^vix6m",
        "^VVIX": "^vvix",
        "^SKEW": "^skew",
        "^TNX": "^tnx",
        "RSP": "rsp.us",
        "SPHB": "sphb.us",
        "SPLV": "splv.us",
        "XLC": "xlc.us",
        "XLY": "xly.us",
        "XLP": "xlp.us",
        "XLE": "xle.us",
        "XLF": "xlf.us",
        "XLV": "xlv.us",
        "XLI": "xli.us",
        "XLK": "xlk.us",
        "XLB": "xlb.us",
        "XLU": "xlu.us",
        "XLRE": "xlre.us",
    }
    return mapping.get(symbol, symbol.lower())


def _value_at(payload: dict[str, list[Any]], field: str, index: int) -> float | None:
    values = payload.get(field) or []
    if index >= len(values) or values[index] is None:
        return None
    return float(values[index])


def _clean_rows(rows: list[dict[str, float | str]]) -> list[dict[str, float | str]]:
    by_date = {str(row["date"]): row for row in rows if row.get("date") and float(row.get("close") or 0.0) > 0}
    return [by_date[key] for key in sorted(by_date)]


def _cache_dir() -> Path:
    configured = os.getenv("MARKET_DATA_CACHE_DIR")
    if configured:
        return Path(configured)
    return Path(os.getenv("PREDICTION_STORE_PATH", "./data")) / "market_data_cache"


def _cache_file(symbol: str) -> Path:
    safe = symbol.replace("^", "INDEX_").replace("/", "_")
    return _cache_dir() / f"{safe}.json"


def _write_cache(series: DownloadedSeries) -> None:
    if series.source not in {"yfinance", "yahoo-chart", "stooq"}:
        return
    path = _cache_file(series.symbol)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "symbol": series.symbol,
        "source": series.source,
        "cached_at": datetime.now(timezone.utc).isoformat(),
        "rows": series.rows,
    }
    path.write_text(json.dumps(payload), encoding="utf-8")


def _read_cache(symbol: str, lookback_days: int) -> DownloadedSeries | None:
    path = _cache_file(symbol)
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    source = str(payload.get("source", "unknown"))
    rows = _clean_rows(list(payload.get("rows", [])))[-lookback_days:]
    if source not in {"yfinance", "yahoo-chart", "stooq"} or not rows:
        return None
    return DownloadedSeries(symbol=symbol, rows=rows, source=f"local-cache-{source}", point_in_time_safe=True)


def _synthetic_series(symbol: str, lookback_days: int, source: str) -> DownloadedSeries:
    seed = sum(ord(character) for character in symbol) / 10.0
    start = date.today() - timedelta(days=lookback_days)
    price = 100.0 + seed
    rows: list[dict[str, float | str]] = []
    for index in range(lookback_days):
        daily_return = 0.0004 + 0.006 * math.sin(index / 19.0 + seed)
        price *= 1 + daily_return
        rows.append(
            {
                "date": (start + timedelta(days=index)).isoformat(),
                "open": round(price * (1 - 0.002), 4),
                "high": round(price * (1 + 0.006), 4),
                "low": round(price * (1 - 0.006), 4),
                "close": round(price, 4),
                "volume": float(1_000_000 + 100_000 * abs(math.sin(index / 11.0 + seed))),
            }
        )
    return DownloadedSeries(symbol=symbol, rows=rows, source=source, point_in_time_safe=False)
