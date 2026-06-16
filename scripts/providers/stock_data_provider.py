from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from app.services.data_providers.auto_download import DownloadedSeries, refresh_market_data


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_WATCHLIST_PATH = PROJECT_ROOT / "config" / "stock_watchlist.json"
DEFAULT_WATCHLIST: tuple[str, ...] = ()
FINNHUB_BASE_URL = "https://finnhub.io/api/v1"
FINNHUB_TIMEOUT_SECONDS = 10


def load_stock_watchlist(path: Path | None = None) -> dict[str, Any]:
    path = path or DEFAULT_WATCHLIST_PATH
    if not path.exists():
        return {
            "watchlist": [],
            "benchmark_map": {},
            "sector_etf_map": {},
            "company_map": {},
            "source": "missing_watchlist_config",
        }
    payload = json.loads(path.read_text(encoding="utf-8"))
    env_watchlist = _watchlist_from_env()
    configured_watchlist = payload.get("watchlist", [])
    watchlist = [str(symbol).upper().strip() for symbol in (env_watchlist or configured_watchlist) if str(symbol).strip()]
    watchlist = watchlist[:20]
    benchmark_map = {
        str(symbol).upper(): str(benchmark).upper()
        for symbol, benchmark in (payload.get("benchmark_map") or {}).items()
        if str(symbol).upper() in watchlist
    }
    sector_etf_map = {
        str(symbol).upper(): str(etf).upper()
        for symbol, etf in (payload.get("sector_etf_map") or {}).items()
        if str(symbol).upper() in watchlist
    }
    company_map = {
        str(symbol).upper(): str(name)
        for symbol, name in (payload.get("company_map") or {}).items()
        if str(symbol).upper() in watchlist
    }
    return {
        "watchlist": watchlist,
        "benchmark_map": {symbol: benchmark_map.get(symbol, "QQQ") for symbol in watchlist},
        "sector_etf_map": sector_etf_map,
        "company_map": company_map,
        "source": str(path),
    }


def fetch_stock_data_bundle(
    *,
    watchlist_config: dict[str, Any] | None = None,
    lookback_days: int = 520,
) -> dict[str, Any]:
    config = watchlist_config or load_stock_watchlist()
    watchlist = tuple(config.get("watchlist") or ())
    benchmark_map = dict(config.get("benchmark_map") or {})
    sector_etf_map = dict(config.get("sector_etf_map") or {})
    company_map = dict(config.get("company_map") or {})
    if not watchlist:
        return {
            "provider": "stock_data_provider",
            "version": "stock_data_provider_v1",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "watchlist_source": config.get("source"),
            "watchlist": [],
            "benchmark_map": {},
            "sector_etf_map": {},
            "company_map": {},
            "symbols": {},
            "support_symbols": {},
            "provider_status": {},
            "summary": {
                "requested_symbols": 0,
                "available_symbols": 0,
                "missing_symbols": [],
                "synthetic_blocked_symbols": [],
                "data_quality_score": None,
                "company_profiles_available": 0,
                "fundamentals_available": False,
                "earnings_available": False,
                "company_news_available": False,
                "single_stock_options_available": False,
                "manual_ticker_input_required": True,
            },
            "guardrails": [
                "No default stock universe is generated. Use GitHub Actions workflow_dispatch ticker_list to create stock forecasts.",
                "Synthetic stock data is blocked and cannot create a live stock forecast.",
                "Stock forecasts are probabilistic scenario paths, not execution recommendations.",
            ],
        }
    company_profiles = _fetch_company_profiles(watchlist)
    company_news = _fetch_company_news_bundle(watchlist)
    earnings = _fetch_earnings_bundle(watchlist)
    fundamentals = _fetch_fundamentals_bundle(watchlist)
    support_symbols = tuple(sorted(set(benchmark_map.values()) | set(sector_etf_map.values()) | {"SPY", "QQQ"}))
    download_symbols = tuple(dict.fromkeys(watchlist + support_symbols))
    downloaded = refresh_market_data(symbols=download_symbols, lookback_days=lookback_days)
    raw_series = {series.symbol.upper(): series for series in downloaded}

    symbols: dict[str, Any] = {}
    provider_status: dict[str, Any] = {}
    for symbol in watchlist:
        series = raw_series.get(str(symbol).upper())
        profile = company_profiles.get(symbol) or {}
        news_payload = company_news.get(symbol) or {}
        earnings_payload = earnings.get(symbol) or {}
        fundamentals_payload = fundamentals.get(symbol) or {}
        profile_status = profile.get("status") or "missing"
        news_status = news_payload.get("status") or "missing"
        earnings_status = earnings_payload.get("status") or "missing"
        fundamentals_status = fundamentals_payload.get("status") or "missing"
        profile_payload = profile.get("profile") or {}
        provider_status[symbol] = _series_status(series)
        symbols[symbol] = {
            "symbol": symbol,
            "company_name": profile_payload.get("name") or company_map.get(symbol, symbol),
            "logo": profile_payload.get("logo"),
            "company_profile": profile,
            "company_news": news_payload,
            "earnings": earnings_payload,
            "fundamentals": fundamentals_payload,
            "benchmark": benchmark_map.get(symbol, "QQQ"),
            "sector_etf": sector_etf_map.get(symbol),
            "status": provider_status[symbol]["status"],
            "source": provider_status[symbol]["source"],
            "latest_date": provider_status[symbol]["latest_date"],
            "rows": _clean_rows(series) if _usable_series(series) else [],
            "synthetic_blocked": bool(series and not series.point_in_time_safe),
            "missing_reason": None if _usable_series(series) else _missing_reason(series),
            "data_categories": {
                "price": "available" if _usable_series(series) else "missing",
                "volume": "available" if _usable_series(series) else "missing",
                "relative_strength": "available" if _usable_series(series) else "missing",
                "company_profile": "available" if profile_status == "available" else profile_status,
                "fundamentals": "available" if fundamentals_status == "available" else fundamentals_status,
                "earnings": "available" if earnings_status == "available" else earnings_status,
                "company_news": "available" if news_status == "available" else news_status,
                "single_stock_options": "missing",
            },
        }

    support: dict[str, Any] = {}
    for symbol in support_symbols:
        series = raw_series.get(str(symbol).upper())
        support[symbol] = {
            "symbol": symbol,
            "status": "available" if _usable_series(series) else "missing",
            "source": series.source if series else None,
            "latest_date": _latest_date(series),
            "rows": _clean_rows(series) if _usable_series(series) else [],
        }

    available = sum(1 for item in symbols.values() if item["status"] == "available")
    return {
        "provider": "stock_data_provider",
        "version": "stock_data_provider_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "watchlist_source": config.get("source"),
        "watchlist": list(watchlist),
        "benchmark_map": benchmark_map,
        "sector_etf_map": sector_etf_map,
        "company_map": company_map,
        "symbols": symbols,
        "support_symbols": support,
        "provider_status": provider_status,
        "summary": {
            "requested_symbols": len(watchlist),
            "available_symbols": available,
            "missing_symbols": [symbol for symbol, item in symbols.items() if item["status"] != "available"],
            "synthetic_blocked_symbols": [symbol for symbol, item in symbols.items() if item.get("synthetic_blocked")],
            "data_quality_score": round(100.0 * available / max(len(watchlist), 1), 2),
            "company_profiles_available": sum(1 for item in company_profiles.values() if item.get("status") == "available"),
            "fundamentals_available": any(item.get("status") == "available" for item in fundamentals.values()),
            "earnings_available": any(item.get("status") == "available" for item in earnings.values()),
            "company_news_available": any(item.get("status") == "available" for item in company_news.values()),
            "company_news_available_symbols": sum(1 for item in company_news.values() if item.get("status") == "available"),
            "earnings_available_symbols": sum(1 for item in earnings.values() if item.get("status") == "available"),
            "fundamentals_available_symbols": sum(1 for item in fundamentals.values() if item.get("status") == "available"),
            "single_stock_options_available": False,
        },
        "guardrails": [
            "Synthetic stock data is blocked and cannot create a live stock forecast.",
            "Company news, earnings calendar and basic financial metrics use Finnhub when FINNHUB_API_KEY is available.",
            "Single-stock options remain missing unless a reliable real provider is connected.",
            "Stock forecasts are probabilistic scenario paths, not execution recommendations.",
        ],
    }


def _watchlist_from_env() -> list[str]:
    raw = os.getenv("STOCK_TICKER_LIST", "").strip()
    if not raw:
        return []
    symbols: list[str] = []
    for item in raw.replace(";", ",").split(","):
        symbol = item.strip().upper()
        if symbol and symbol not in symbols:
            symbols.append(symbol)
    return symbols[:20]


def _fetch_company_profiles(watchlist: tuple[str, ...]) -> dict[str, Any]:
    token = os.getenv("FINNHUB_API_KEY", "").strip()
    if not token:
        return {symbol: {"status": "missing_api_key", "source": "finnhub", "profile": None} for symbol in watchlist}
    profiles: dict[str, Any] = {}
    cache_dir = Path(os.getenv("FINNHUB_CACHE_DIR", PROJECT_ROOT / "data" / "finnhub_cache")) / "company_profiles"
    cache_dir.mkdir(parents=True, exist_ok=True)
    for symbol in watchlist:
        profiles[symbol] = _fetch_company_profile(symbol, token, cache_dir)
        time.sleep(0.15)
    return profiles


def _fetch_company_news_bundle(watchlist: tuple[str, ...]) -> dict[str, Any]:
    token = os.getenv("FINNHUB_API_KEY", "").strip()
    if not token:
        return {symbol: {"status": "missing_api_key", "source": "finnhub", "items": []} for symbol in watchlist}
    cache_dir = Path(os.getenv("FINNHUB_CACHE_DIR", PROJECT_ROOT / "data" / "finnhub_cache")) / "company_news"
    cache_dir.mkdir(parents=True, exist_ok=True)
    today = date.today()
    start = today - timedelta(days=7)
    output: dict[str, Any] = {}
    for symbol in watchlist:
        params = {"symbol": symbol.upper(), "from": start.isoformat(), "to": today.isoformat(), "token": token}
        payload = _fetch_finnhub_payload(symbol, "company-news", params, cache_dir, list)
        output[symbol] = _sanitize_company_news(payload, symbol)
        time.sleep(0.15)
    return output


def _fetch_earnings_bundle(watchlist: tuple[str, ...]) -> dict[str, Any]:
    token = os.getenv("FINNHUB_API_KEY", "").strip()
    if not token:
        return {symbol: {"status": "missing_api_key", "source": "finnhub", "calendar": []} for symbol in watchlist}
    cache_dir = Path(os.getenv("FINNHUB_CACHE_DIR", PROJECT_ROOT / "data" / "finnhub_cache")) / "earnings"
    cache_dir.mkdir(parents=True, exist_ok=True)
    today = date.today()
    end = today + timedelta(days=45)
    output: dict[str, Any] = {}
    for symbol in watchlist:
        params = {"symbol": symbol.upper(), "from": today.isoformat(), "to": end.isoformat(), "token": token}
        payload = _fetch_finnhub_payload(symbol, "calendar/earnings", params, cache_dir, dict)
        output[symbol] = _sanitize_earnings(payload, symbol, today)
        time.sleep(0.15)
    return output


def _fetch_fundamentals_bundle(watchlist: tuple[str, ...]) -> dict[str, Any]:
    token = os.getenv("FINNHUB_API_KEY", "").strip()
    if not token:
        return {symbol: {"status": "missing_api_key", "source": "finnhub", "metrics": {}} for symbol in watchlist}
    cache_dir = Path(os.getenv("FINNHUB_CACHE_DIR", PROJECT_ROOT / "data" / "finnhub_cache")) / "fundamentals"
    cache_dir.mkdir(parents=True, exist_ok=True)
    output: dict[str, Any] = {}
    for symbol in watchlist:
        params = {"symbol": symbol.upper(), "metric": "all", "token": token}
        payload = _fetch_finnhub_payload(symbol, "stock/metric", params, cache_dir, dict)
        output[symbol] = _sanitize_fundamentals(payload, symbol)
        time.sleep(0.15)
    return output


def _fetch_finnhub_payload(
    symbol: str,
    endpoint: str,
    params: dict[str, Any],
    cache_dir: Path,
    expected_type: type,
) -> dict[str, Any]:
    cache_path = cache_dir / f"{symbol.upper()}.json"
    encoded = urllib.parse.urlencode(params)
    url = f"{FINNHUB_BASE_URL}/{endpoint}?{encoded}"
    error_type = None
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "market-predictor/1.0"})
            with urllib.request.urlopen(request, timeout=FINNHUB_TIMEOUT_SECONDS) as response:
                raw = response.read().decode("utf-8")
            payload = json.loads(raw) if raw else ({} if expected_type is dict else [])
            if isinstance(payload, expected_type):
                cache_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
                return {"status": "available", "source": "finnhub", "payload": payload, "cache_used": False}
            error_type = "unexpected_payload_type"
            break
        except Exception as exc:
            error_type = type(exc).__name__
            time.sleep(0.4 * (attempt + 1))
    cached = _read_json_cache(cache_path)
    if cached is not None:
        return {
            "status": "stale_cache",
            "source": "local-cache-finnhub",
            "payload": cached,
            "cache_used": True,
            "error_type": error_type,
        }
    return {"status": "failed", "source": "finnhub", "payload": None, "cache_used": False, "error_type": error_type}


def _fetch_company_profile(symbol: str, token: str, cache_dir: Path) -> dict[str, Any]:
    cache_path = cache_dir / f"{symbol.upper()}.json"
    params = urllib.parse.urlencode({"symbol": symbol.upper(), "token": token})
    url = f"{FINNHUB_BASE_URL}/stock/profile2?{params}"
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "market-predictor/1.0"})
        with urllib.request.urlopen(request, timeout=FINNHUB_TIMEOUT_SECONDS) as response:
            raw = response.read().decode("utf-8")
        payload = json.loads(raw) if raw else {}
        profile = _sanitize_profile(payload)
        if profile:
            cache_path.write_text(json.dumps(profile, ensure_ascii=False, indent=2), encoding="utf-8")
            return {"status": "available", "source": "finnhub", "profile": profile, "cache_used": False}
    except Exception as exc:
        cached = _read_profile_cache(cache_path)
        if cached:
            return {
                "status": "stale_cache",
                "source": "local-cache-finnhub",
                "profile": cached,
                "cache_used": True,
                "error_type": type(exc).__name__,
            }
        return {"status": "failed", "source": "finnhub", "profile": None, "cache_used": False, "error_type": type(exc).__name__}
    cached = _read_profile_cache(cache_path)
    if cached:
        return {"status": "stale_cache", "source": "local-cache-finnhub", "profile": cached, "cache_used": True}
    return {"status": "missing", "source": "finnhub", "profile": None, "cache_used": False}


def _sanitize_profile(payload: dict[str, Any]) -> dict[str, Any]:
    if not payload:
        return {}
    allowed = ("name", "ticker", "exchange", "finnhubIndustry", "marketCapitalization", "shareOutstanding", "logo", "weburl")
    return {key: payload.get(key) for key in allowed if payload.get(key) not in (None, "")}


def _read_profile_cache(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    return payload if isinstance(payload, dict) and payload else None


def _read_json_cache(path: Path) -> Any | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _sanitize_company_news(result: dict[str, Any], symbol: str) -> dict[str, Any]:
    status = result.get("status") or "missing"
    items = result.get("payload") if isinstance(result.get("payload"), list) else []
    sanitized: list[dict[str, Any]] = []
    now_ts = datetime.now(timezone.utc).timestamp()
    risk_keywords = ("lawsuit", "probe", "investigation", "recall", "downgrade", "miss", "warning", "tariff", "ban")
    positive_keywords = ("beat", "upgrade", "raise", "partnership", "contract", "approval", "launch", "surge")
    risk_hits = 0
    positive_hits = 0
    count_24h = 0
    count_72h = 0
    for item in items[:20]:
        headline = str(item.get("headline") or "").strip()
        if not headline:
            continue
        dt = _float(item.get("datetime"))
        if dt:
            age_hours = max((now_ts - dt) / 3600.0, 0.0)
            if age_hours <= 24:
                count_24h += 1
            if age_hours <= 72:
                count_72h += 1
        lower = headline.lower()
        risk_hits += sum(1 for keyword in risk_keywords if keyword in lower)
        positive_hits += sum(1 for keyword in positive_keywords if keyword in lower)
        sanitized.append(
            {
                "headline": headline,
                "source": item.get("source"),
                "datetime": item.get("datetime"),
                "url": item.get("url"),
            }
        )
    sentiment_proxy = "neutral"
    if positive_hits > risk_hits:
        sentiment_proxy = "positive"
    elif risk_hits > positive_hits:
        sentiment_proxy = "negative"
    risk_score = min(100.0, 20.0 + count_24h * 8.0 + risk_hits * 12.0 - positive_hits * 5.0)
    return {
        "status": "available" if status in {"available", "stale_cache"} else status,
        "source": result.get("source"),
        "cache_used": result.get("cache_used", False),
        "symbol": symbol,
        "headline_count": len(sanitized),
        "news_count_24h": count_24h,
        "news_count_72h": count_72h,
        "major_company_headline": sanitized[0].get("headline") if sanitized else None,
        "news_sentiment_proxy": sentiment_proxy,
        "news_risk_score": round(max(0.0, risk_score), 2),
        "items": sanitized[:8],
        "error_type": result.get("error_type"),
    }


def _sanitize_earnings(result: dict[str, Any], symbol: str, today: date) -> dict[str, Any]:
    status = result.get("status") or "missing"
    payload = result.get("payload") if isinstance(result.get("payload"), dict) else {}
    calendar = payload.get("earningsCalendar") if isinstance(payload.get("earningsCalendar"), list) else []
    next_date = None
    for item in calendar:
        raw_date = item.get("date")
        if not raw_date:
            continue
        try:
            parsed = date.fromisoformat(str(raw_date))
        except ValueError:
            continue
        if parsed >= today and (next_date is None or parsed < next_date):
            next_date = parsed
    days_to = (next_date - today).days if next_date else None
    return {
        "status": "available" if status in {"available", "stale_cache"} else status,
        "source": result.get("source"),
        "cache_used": result.get("cache_used", False),
        "symbol": symbol,
        "next_earnings_date": next_date.isoformat() if next_date else None,
        "earnings_within_7d": bool(days_to is not None and days_to <= 7),
        "earnings_within_30d": bool(days_to is not None and days_to <= 30),
        "days_to_earnings": days_to,
        "calendar": calendar[:8],
        "error_type": result.get("error_type"),
    }


def _sanitize_fundamentals(result: dict[str, Any], symbol: str) -> dict[str, Any]:
    status = result.get("status") or "missing"
    payload = result.get("payload") if isinstance(result.get("payload"), dict) else {}
    metric = payload.get("metric") if isinstance(payload.get("metric"), dict) else {}
    selected = {
        "revenue_growth_ttm_yoy": _first_metric(metric, "revenueGrowthTTMYoy", "revenueGrowth5Y"),
        "eps_growth_ttm_yoy": _first_metric(metric, "epsGrowthTTMYoy", "epsGrowth5Y"),
        "forward_pe": _first_metric(metric, "peNormalizedAnnual", "peTTM"),
        "gross_margin_ttm": _first_metric(metric, "grossMarginTTM"),
        "net_margin_ttm": _first_metric(metric, "netProfitMarginTTM"),
        "debt_to_equity": _first_metric(metric, "totalDebt/totalEquityAnnual", "totalDebt/totalEquityQuarterly"),
        "current_ratio": _first_metric(metric, "currentRatioAnnual", "currentRatioQuarterly"),
    }
    has_any = any(value is not None for value in selected.values())
    return {
        "status": "available" if status in {"available", "stale_cache"} and has_any else status,
        "source": result.get("source"),
        "cache_used": result.get("cache_used", False),
        "symbol": symbol,
        "metrics": selected,
        "error_type": result.get("error_type"),
    }


def _first_metric(metric: dict[str, Any], *keys: str) -> float | None:
    for key in keys:
        value = _float(metric.get(key))
        if value is not None:
            return value
    return None


def render_stock_data_status_markdown(bundle: dict[str, Any]) -> str:
    lines = [
        "# Stock Data Provider Status",
        "",
        f"Generated at: `{bundle.get('generated_at')}`",
        "",
        f"- requested_symbols: `{(bundle.get('summary') or {}).get('requested_symbols')}`",
        f"- available_symbols: `{(bundle.get('summary') or {}).get('available_symbols')}`",
        f"- data_quality_score: `{(bundle.get('summary') or {}).get('data_quality_score')}`",
        "",
        "| Symbol | Status | Source | Latest Date | Missing Reason |",
        "| --- | --- | --- | --- | --- |",
    ]
    for symbol, payload in (bundle.get("symbols") or {}).items():
        lines.append(
            f"| {symbol} | {payload.get('status')} | {payload.get('source')} | "
            f"{payload.get('latest_date')} | {payload.get('missing_reason')} |"
        )
    lines.extend(
        [
            "",
            "This provider does not use synthetic data for live stock forecasts.",
            "",
        ]
    )
    return "\n".join(lines)


def _usable_series(series: DownloadedSeries | None) -> bool:
    return bool(series and series.point_in_time_safe and not str(series.source).startswith("synthetic") and series.rows)


def _series_status(series: DownloadedSeries | None) -> dict[str, Any]:
    if not series:
        return {"status": "missing", "source": None, "latest_date": None, "real_data": False}
    if not series.point_in_time_safe or str(series.source).startswith("synthetic"):
        return {"status": "synthetic_blocked", "source": series.source, "latest_date": _latest_date(series), "real_data": False}
    return {"status": "available", "source": series.source, "latest_date": _latest_date(series), "real_data": True}


def _missing_reason(series: DownloadedSeries | None) -> str:
    if not series:
        return "provider_failed"
    if not series.point_in_time_safe:
        return "synthetic_fallback_blocked"
    if not series.rows:
        return "empty_price_history"
    return "unknown"


def _latest_date(series: DownloadedSeries | None) -> str | None:
    if not series or not series.rows:
        return None
    return str(series.rows[-1].get("date")) if series.rows[-1].get("date") else None


def _clean_rows(series: DownloadedSeries | None) -> list[dict[str, Any]]:
    if not series:
        return []
    rows: list[dict[str, Any]] = []
    for row in series.rows:
        close = _float(row.get("close"))
        if not row.get("date") or close is None or close <= 0:
            continue
        rows.append(
            {
                "date": str(row.get("date")),
                "open": _float(row.get("open")) or close,
                "high": _float(row.get("high")) or close,
                "low": _float(row.get("low")) or close,
                "close": close,
                "volume": _float(row.get("volume")),
                "source": series.source,
            }
        )
    return rows


def _float(value: Any) -> float | None:
    try:
        if value is None:
            return None
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if number == number else None
