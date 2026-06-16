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
from datetime import date, datetime, time as dt_time, timedelta, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


DEFAULT_DOWNLOAD_SYMBOLS = ("SPY", "QQQ", "IWM", "DIA", "^VIX", "HYG", "LQD", "TLT", "UUP", "^TNX")
REAL_DATA_SOURCES = {
    "yfinance",
    "yahoo-chart",
    "stooq",
    "finnhub-quote-patch",
    "local-cache-yfinance",
    "local-cache-yahoo-chart",
    "local-cache-stooq",
    "local-cache-finnhub-quote-patch",
}
EASTERN = ZoneInfo("America/New_York")
MARKET_CLOSE_BUFFER = dt_time(16, 30)


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
    candidates: list[DownloadedSeries] = []
    expected_latest = _expected_latest_trading_date()
    for loader in (_download_yfinance, _download_yahoo_chart, _download_stooq):
        try:
            series = loader(symbol, lookback_days)
            if series.rows:
                candidates.append(series)
                if _latest_row_date(series) and _latest_row_date(series) >= expected_latest:
                    _write_cache(series)
                    return series
        except Exception:
            continue

    cached = _read_cache(symbol, lookback_days)
    if cached is not None:
        candidates.append(cached)

    quote_patch = _download_finnhub_quote_patch(symbol, lookback_days, candidates, expected_latest)
    if quote_patch is not None:
        _write_cache(quote_patch)
        return quote_patch

    if candidates:
        best = max(candidates, key=lambda item: (_latest_row_date(item) or date.min, _source_priority(item.source)))
        if best.source in {"yfinance", "yahoo-chart", "stooq", "finnhub-quote-patch"}:
            _write_cache(best)
        return best

    return _synthetic_series(symbol, lookback_days, source="synthetic-fallback")


def _latest_row_date(series: DownloadedSeries) -> date | None:
    if not series.rows:
        return None
    value = series.rows[-1].get("date")
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def _source_priority(source: str) -> int:
    if source == "finnhub-quote-patch":
        return 4
    if source in {"yfinance", "yahoo-chart", "stooq"}:
        return 3
    if source.startswith("local-cache-"):
        return 2
    return 1


def _download_finnhub_quote_patch(
    symbol: str,
    lookback_days: int,
    candidates: list[DownloadedSeries],
    expected_latest: date,
) -> DownloadedSeries | None:
    token = os.getenv("FINNHUB_API_KEY", "").strip()
    if not token or symbol.startswith("^"):
        return None
    base = max(candidates, key=lambda item: (_latest_row_date(item) or date.min, _source_priority(item.source)), default=None)
    if base is None or not base.rows:
        return None
    base_latest = _latest_row_date(base)
    if base_latest is not None and base_latest >= expected_latest:
        return None

    url = f"https://finnhub.io/api/v1/quote?{urllib.parse.urlencode({'symbol': symbol, 'token': token})}"
    request = urllib.request.Request(url, headers={"User-Agent": "market-predictor/1.0"})
    payload = json.loads(urllib.request.urlopen(request, timeout=12).read().decode("utf-8"))
    close = _scalar_value(payload.get("c"))
    if close is None or close <= 0:
        return None
    timestamp = int(payload.get("t") or time.time())
    quote_date = datetime.fromtimestamp(timestamp, tz=timezone.utc).astimezone(EASTERN).date()
    if quote_date < expected_latest:
        return None

    open_price = _scalar_value(payload.get("o")) or close
    high_price = _scalar_value(payload.get("h")) or max(open_price, close)
    low_price = _scalar_value(payload.get("l")) or min(open_price, close)
    patched_rows = list(base.rows)
    patched_row = {
        "date": quote_date.isoformat(),
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "close": close,
        "volume": 0.0,
    }
    if patched_rows and str(patched_rows[-1].get("date")) == patched_row["date"]:
        patched_rows[-1] = patched_row
    else:
        patched_rows.append(patched_row)
    return DownloadedSeries(
        symbol=symbol,
        rows=_clean_rows(patched_rows)[-lookback_days:],
        source="finnhub-quote-patch",
        point_in_time_safe=True,
    )


def _expected_latest_trading_date(now_utc: datetime | None = None) -> date:
    now_utc = now_utc or datetime.now(timezone.utc)
    now_et = now_utc.astimezone(EASTERN)
    candidate = now_et.date()
    if _is_us_market_trading_day(candidate) and now_et.time() >= MARKET_CLOSE_BUFFER:
        return candidate
    return _previous_us_market_trading_day(candidate)


def _is_us_market_trading_day(day: date) -> bool:
    if day.weekday() >= 5:
        return False
    return day not in _us_market_holidays(day.year)


def _previous_us_market_trading_day(day: date) -> date:
    candidate = day - timedelta(days=1)
    while not _is_us_market_trading_day(candidate):
        candidate -= timedelta(days=1)
    return candidate


def _us_market_holidays(year: int) -> set[date]:
    return {
        _observed(date(year, 1, 1)),
        _nth_weekday(year, 1, 0, 3),
        _nth_weekday(year, 2, 0, 3),
        _good_friday(year),
        _last_weekday(year, 5, 0),
        _observed(date(year, 6, 19)),
        _observed(date(year, 7, 4)),
        _nth_weekday(year, 9, 0, 1),
        _nth_weekday(year, 11, 3, 4),
        _observed(date(year, 12, 25)),
    }


def _observed(day: date) -> date:
    if day.weekday() == 5:
        return day - timedelta(days=1)
    if day.weekday() == 6:
        return day + timedelta(days=1)
    return day


def _nth_weekday(year: int, month: int, weekday: int, nth: int) -> date:
    candidate = date(year, month, 1)
    while candidate.weekday() != weekday:
        candidate += timedelta(days=1)
    return candidate + timedelta(days=7 * (nth - 1))


def _last_weekday(year: int, month: int, weekday: int) -> date:
    candidate = date(year, 12, 31) if month == 12 else date(year, month + 1, 1) - timedelta(days=1)
    while candidate.weekday() != weekday:
        candidate -= timedelta(days=1)
    return candidate


def _good_friday(year: int) -> date:
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return date(year, month, day) - timedelta(days=2)


def _download_yfinance(symbol: str, lookback_days: int) -> DownloadedSeries:
    import yfinance as yf  # type: ignore[import-not-found]

    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        frame = yf.download(symbol, period=f"{lookback_days}d", auto_adjust=True, progress=False, timeout=8)
    if frame.empty:
        raise RuntimeError(f"empty yfinance result for {symbol}")
    rows = []
    for timestamp, row in frame.tail(lookback_days).iterrows():
        close = _scalar_value(row.get("Close"))
        if close is None:
            continue
        rows.append(
            {
                "date": timestamp.date().isoformat(),
                "open": _scalar_value(row.get("Open")) or close,
                "high": _scalar_value(row.get("High")) or close,
                "low": _scalar_value(row.get("Low")) or close,
                "close": close,
                "volume": _scalar_value(row.get("Volume")) or 0.0,
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


def _scalar_value(value: Any) -> float | None:
    if value is None:
        return None
    if hasattr(value, "dropna"):
        try:
            value = value.dropna()
            if getattr(value, "empty", False):
                return None
            value = value.iloc[0]
        except Exception:
            return None
    try:
        if math.isnan(float(value)):
            return None
    except (TypeError, ValueError):
        return None
    return float(value)


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
    if series.source not in {"yfinance", "yahoo-chart", "stooq", "finnhub-quote-patch"}:
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
    if source not in {"yfinance", "yahoo-chart", "stooq", "finnhub-quote-patch"} or not rows:
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
