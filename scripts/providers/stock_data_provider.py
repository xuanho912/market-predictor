from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.services.data_providers.auto_download import DownloadedSeries, refresh_market_data


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_WATCHLIST_PATH = PROJECT_ROOT / "config" / "stock_watchlist.json"
DEFAULT_WATCHLIST = ("JD", "KC", "NVDA", "TSLA")


def load_stock_watchlist(path: Path | None = None) -> dict[str, Any]:
    path = path or DEFAULT_WATCHLIST_PATH
    if not path.exists():
        return {
            "watchlist": list(DEFAULT_WATCHLIST),
            "benchmark_map": {symbol: "QQQ" for symbol in DEFAULT_WATCHLIST},
            "sector_etf_map": {},
            "source": "default_watchlist",
        }
    payload = json.loads(path.read_text(encoding="utf-8"))
    watchlist = [str(symbol).upper().strip() for symbol in payload.get("watchlist", []) if str(symbol).strip()]
    watchlist = watchlist[:20] or list(DEFAULT_WATCHLIST)
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
    return {
        "watchlist": watchlist,
        "benchmark_map": {symbol: benchmark_map.get(symbol, "QQQ") for symbol in watchlist},
        "sector_etf_map": sector_etf_map,
        "source": str(path),
    }


def fetch_stock_data_bundle(
    *,
    watchlist_config: dict[str, Any] | None = None,
    lookback_days: int = 520,
) -> dict[str, Any]:
    config = watchlist_config or load_stock_watchlist()
    watchlist = tuple(config.get("watchlist") or DEFAULT_WATCHLIST)
    benchmark_map = dict(config.get("benchmark_map") or {})
    sector_etf_map = dict(config.get("sector_etf_map") or {})
    support_symbols = tuple(sorted(set(benchmark_map.values()) | set(sector_etf_map.values()) | {"SPY", "QQQ"}))
    download_symbols = tuple(dict.fromkeys(watchlist + support_symbols))
    downloaded = refresh_market_data(symbols=download_symbols, lookback_days=lookback_days)
    raw_series = {series.symbol.upper(): series for series in downloaded}

    symbols: dict[str, Any] = {}
    provider_status: dict[str, Any] = {}
    for symbol in watchlist:
        series = raw_series.get(str(symbol).upper())
        provider_status[symbol] = _series_status(series)
        symbols[symbol] = {
            "symbol": symbol,
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
                "fundamentals": "missing",
                "earnings": "missing",
                "company_news": "missing",
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
        "symbols": symbols,
        "support_symbols": support,
        "provider_status": provider_status,
        "summary": {
            "requested_symbols": len(watchlist),
            "available_symbols": available,
            "missing_symbols": [symbol for symbol, item in symbols.items() if item["status"] != "available"],
            "synthetic_blocked_symbols": [symbol for symbol, item in symbols.items() if item.get("synthetic_blocked")],
            "data_quality_score": round(100.0 * available / max(len(watchlist), 1), 2),
            "fundamentals_available": False,
            "earnings_available": False,
            "company_news_available": False,
            "single_stock_options_available": False,
        },
        "guardrails": [
            "Synthetic stock data is blocked and cannot create a live stock forecast.",
            "Company fundamentals, earnings, news and options are marked missing unless a real provider is connected.",
            "Stock forecasts are probabilistic scenario paths, not buy/sell recommendations.",
        ],
    }


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
