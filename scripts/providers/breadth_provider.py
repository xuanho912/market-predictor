from __future__ import annotations

import argparse
import concurrent.futures
import json
import math
import os
import re
import time
import urllib.request
import urllib.parse
from dataclasses import dataclass
from datetime import date, datetime, timezone
from html import unescape
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CACHE_ROOT = Path(os.getenv("BREADTH_CACHE_DIR", PROJECT_ROOT / "data" / "breadth_cache"))
CONSTITUENT_CACHE_DIR = CACHE_ROOT / "constituents"
PRICE_CACHE_DIR = CACHE_ROOT / "prices"

TRUE_UNIVERSES = ("SPY", "QQQ", "DIA")
TARGET_UNIVERSES = TRUE_UNIVERSES + ("IWM",)
SECTOR_ETFS = ("XLK", "XLF", "XLY", "XLI", "XLE", "XLV", "XLP", "XLU", "XLB", "XLRE")
DOW_30_TICKERS = (
    "AAPL",
    "AMGN",
    "AMZN",
    "AXP",
    "BA",
    "CAT",
    "CRM",
    "CSCO",
    "CVX",
    "DIS",
    "GS",
    "HD",
    "HON",
    "IBM",
    "JNJ",
    "JPM",
    "KO",
    "MCD",
    "MMM",
    "MRK",
    "MSFT",
    "NKE",
    "NVDA",
    "PG",
    "SHW",
    "TRV",
    "UNH",
    "V",
    "VZ",
    "WMT",
)


@dataclass(frozen=True)
class ConstituentResult:
    symbol: str
    name: str
    tickers: list[str]
    source: str
    stale_constituents: bool
    error_type: str | None = None
    error_reason: str | None = None


def fetch_breadth_bundle(
    *,
    series_by_symbol: dict[str, Any] | None = None,
    lookback_days: int = 420,
) -> dict[str, Any]:
    """Build true/proxy breadth payload for the dashboard.

    No synthetic breadth is generated. If live data fails, the provider uses the
    latest successful cache and marks the relevant stale flags.
    """

    max_constituents = _env_int("BREADTH_MAX_CONSTITUENTS_PER_UNIVERSE")
    generated_at = datetime.now(timezone.utc).isoformat()
    constituent_results = {
        "SPY": load_constituents("SPY"),
        "QQQ": load_constituents("QQQ"),
        "DIA": load_constituents("DIA"),
    }

    universes: dict[str, Any] = {}
    for symbol in TRUE_UNIVERSES:
        result = constituent_results[symbol]
        tickers = result.tickers
        sample_limited = False
        if max_constituents and max_constituents > 0 and len(tickers) > max_constituents:
            tickers = tickers[:max_constituents]
            sample_limited = True
        price_payload = load_price_bundle(tickers, lookback_days=lookback_days)
        universes[symbol] = build_true_breadth_payload(
            symbol=symbol,
            constituent_result=result,
            price_payload=price_payload,
            index_series=(series_by_symbol or {}).get(symbol),
            sample_limited=sample_limited,
        )

    universes["IWM"] = build_iwm_proxy_payload(series_by_symbol or {})
    sector_payload = build_sector_participation_payload(series_by_symbol or {})
    internal_resonance = attach_internal_resonance(universes, sector_payload)
    summary = build_summary(universes, sector_payload)
    summary["market_internal_resonance"] = internal_resonance
    return {
        "provider": "true_breadth_provider",
        "version": "true_breadth_provider_v1",
        "generated_at": generated_at,
        "cache_root": str(CACHE_ROOT),
        "universe_order": list(TARGET_UNIVERSES),
        "universes": universes,
        "sector_participation_proxy": sector_payload,
        "summary": summary,
        "warnings": [
            "SPY/QQQ/DIA breadth uses constituent-level price data when available.",
            "IWM is proxy-only in v1; this is not full Russell 2000 constituent breadth.",
            "Market internal resonance is a confirmation layer, not a standalone alpha signal.",
            "Cached data is marked stale when live refresh fails or latest dates lag the reference date.",
            "No synthetic breadth is used for forecast signal generation.",
        ],
    }


def load_constituents(symbol: str) -> ConstituentResult:
    cache_file = CONSTITUENT_CACHE_DIR / f"{symbol.lower()}_constituents.json"
    if symbol == "DIA":
        result = ConstituentResult(
            symbol="DIA",
            name="Dow Jones 30",
            tickers=list(DOW_30_TICKERS),
            source="static-dow30-list",
            stale_constituents=False,
        )
        _write_constituent_cache(cache_file, result)
        return result

    try:
        if symbol == "SPY":
            tickers = _fetch_wikipedia_constituents(
                url="https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
                table_hint=("security", "gics sector", "symbol"),
                symbol_columns=("Symbol", "Ticker"),
            )
            name = "S&P 500"
            source = "wikipedia-sp500"
        elif symbol == "QQQ":
            tickers = _fetch_wikipedia_constituents(
                url="https://en.wikipedia.org/wiki/Nasdaq-100",
                table_hint=("company", "ticker", "gics sector"),
                symbol_columns=("Ticker", "Symbol"),
            )
            name = "Nasdaq 100"
            source = "wikipedia-nasdaq100"
        else:
            raise ValueError(f"unsupported constituent universe {symbol}")
        if not tickers:
            raise ValueError("empty constituent list")
        result = ConstituentResult(
            symbol=symbol,
            name=name,
            tickers=sorted(dict.fromkeys(_normalize_ticker(ticker) for ticker in tickers if ticker)),
            source=source,
            stale_constituents=False,
        )
        _write_constituent_cache(cache_file, result)
        return result
    except Exception as exc:
        cached = _read_constituent_cache(cache_file)
        if cached and cached.tickers:
            return ConstituentResult(
                symbol=symbol,
                name=cached.name,
                tickers=cached.tickers,
                source=f"local-cache-{cached.source}",
                stale_constituents=True,
                error_type=type(exc).__name__,
                error_reason=str(exc)[:240],
            )
        return ConstituentResult(
            symbol=symbol,
            name={"SPY": "S&P 500", "QQQ": "Nasdaq 100"}.get(symbol, symbol),
            tickers=[],
            source="missing",
            stale_constituents=True,
            error_type=type(exc).__name__,
            error_reason=str(exc)[:240],
        )


def load_price_bundle(tickers: list[str], *, lookback_days: int) -> dict[str, Any]:
    tickers = sorted(dict.fromkeys(_normalize_ticker(ticker) for ticker in tickers if ticker))
    PRICE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cached: dict[str, list[dict[str, Any]]] = {ticker: _read_price_cache(ticker) for ticker in tickers}
    fresh_cutoff_days = _env_int("BREADTH_PRICE_FRESH_DAYS", 5) or 5
    needs_short_update: list[str] = []
    needs_full_update: list[str] = []
    for ticker in tickers:
        rows = cached.get(ticker) or []
        if _rows_are_recent(rows, fresh_cutoff_days):
            continue
        if len(rows) >= 240:
            needs_short_update.append(ticker)
        else:
            needs_full_update.append(ticker)

    downloaded: dict[str, list[dict[str, Any]]] = {}
    errors: dict[str, str] = {}
    if needs_short_update:
        rows_by_ticker, batch_errors = _download_yfinance_batch(needs_short_update, period="3mo")
        downloaded.update(rows_by_ticker)
        errors.update(batch_errors)
    if needs_full_update:
        rows_by_ticker, batch_errors = _download_yfinance_batch(needs_full_update, period="2y")
        downloaded.update(rows_by_ticker)
        errors.update(batch_errors)

    final_rows: dict[str, list[dict[str, Any]]] = {}
    stale_tickers: list[str] = []
    failed_tickers: list[str] = []
    for ticker in tickers:
        cached_rows = cached.get(ticker) or []
        new_rows = downloaded.get(ticker) or []
        if new_rows:
            merged = _merge_price_rows(cached_rows, new_rows)[-lookback_days:]
            _write_price_cache(ticker, merged)
            final_rows[ticker] = merged
        elif cached_rows:
            final_rows[ticker] = cached_rows[-lookback_days:]
            if ticker in needs_short_update or ticker in needs_full_update:
                stale_tickers.append(ticker)
        else:
            failed_tickers.append(ticker)

    latest_dates = [_last_date(rows) for rows in final_rows.values()]
    latest_dates = [value for value in latest_dates if value]
    return {
        "rows_by_ticker": final_rows,
        "expected_tickers": len(tickers),
        "tickers_with_price_data": len(final_rows),
        "failed_tickers": failed_tickers,
        "stale_tickers": stale_tickers,
        "download_errors": errors,
        "stale_price_data": bool(stale_tickers),
        "missing_ratio": round((len(tickers) - len(final_rows)) / len(tickers), 4) if tickers else 1.0,
        "latest_date": max(latest_dates) if latest_dates else None,
        "source": "yfinance-incremental-cache" if downloaded else "local-cache-prices",
    }


def build_true_breadth_payload(
    *,
    symbol: str,
    constituent_result: ConstituentResult,
    price_payload: dict[str, Any],
    index_series: Any,
    sample_limited: bool,
) -> dict[str, Any]:
    rows_by_ticker: dict[str, list[dict[str, Any]]] = price_payload.get("rows_by_ticker") or {}
    expected = max(int(price_payload.get("expected_tickers") or len(constituent_result.tickers)), 1)
    used = int(price_payload.get("tickers_with_price_data") or len(rows_by_ticker))
    coverage_ratio = used / expected if expected else 0.0
    metrics = calculate_breadth_metrics(rows_by_ticker, index_series=index_series)
    stale_constituents = bool(constituent_result.stale_constituents)
    stale_price_data = bool(price_payload.get("stale_price_data")) or _date_is_stale(price_payload.get("latest_date"))
    scores = calculate_breadth_scores(
        metrics=metrics,
        coverage_ratio=coverage_ratio,
        stale_constituents=stale_constituents,
        stale_price_data=stale_price_data,
        sample_limited=sample_limited,
    )
    quality = scores["breadth_quality_score"]
    is_true = symbol in TRUE_UNIVERSES and used >= 10 and coverage_ratio >= 0.45
    status = "available" if is_true and quality >= 65 else "partial" if is_true else "missing"
    if stale_price_data and status == "available":
        status = "stale"
    return {
        "symbol": symbol,
        "name": constituent_result.name,
        "is_true_breadth": is_true,
        "is_proxy": False,
        "status": status,
        "source": constituent_result.source,
        "price_source": price_payload.get("source"),
        "latest_date": price_payload.get("latest_date"),
        "constituents_expected": expected,
        "constituents_used": used,
        "coverage_ratio": round(coverage_ratio, 4),
        "sample_limited": sample_limited,
        "stale_constituents": stale_constituents,
        "stale_price_data": stale_price_data,
        "missing_ratio": price_payload.get("missing_ratio"),
        "failed_tickers_sample": list(price_payload.get("failed_tickers") or [])[:40],
        "stale_tickers_sample": list(price_payload.get("stale_tickers") or [])[:40],
        "constituent_error_type": constituent_result.error_type,
        "constituent_error_reason": constituent_result.error_reason,
        "metrics": metrics,
        "scores": scores,
        "data_note": "True constituent breadth when status is available/stale/partial; stale flags must be respected.",
    }


def build_iwm_proxy_payload(series_by_symbol: dict[str, Any]) -> dict[str, Any]:
    iwm = _series_closes(series_by_symbol.get("IWM"))
    spy = _series_closes(series_by_symbol.get("SPY"))
    rsp = _series_closes(series_by_symbol.get("RSP"))
    small_large = _relative_return(iwm, spy, 20)
    equal_weight = _relative_return(rsp, spy, 20)
    iwm_5d = _return(iwm, 5)
    iwm_20d = _return(iwm, 20)
    latest_date = _series_latest_date(series_by_symbol.get("IWM")) or _series_latest_date(series_by_symbol.get("SPY"))
    improvement = _clip(50 + max(small_large, -0.08) * 350 + max(iwm_5d, -0.08) * 250 + max(equal_weight, -0.06) * 180, 0, 100)
    deterioration = _clip(50 + max(-small_large, -0.08) * 400 + max(-iwm_20d, -0.10) * 250, 0, 100)
    quality = 64 if iwm and spy else 35
    return {
        "symbol": "IWM",
        "name": "Russell 2000",
        "is_true_breadth": False,
        "is_proxy": True,
        "status": "proxy" if quality >= 50 else "missing",
        "source": "iwm-spy-relative-strength-proxy",
        "latest_date": latest_date,
        "constituents_expected": None,
        "constituents_used": None,
        "coverage_ratio": None,
        "stale_constituents": False,
        "stale_price_data": _date_is_stale(latest_date),
        "metrics": {
            "percent_above_20d": None,
            "percent_above_50d": None,
            "percent_above_200d": None,
            "advancers": None,
            "decliners": None,
            "advance_decline_ratio": None,
            "up_volume_down_volume_ratio": None,
            "new_highs_20d": None,
            "new_lows_20d": None,
            "new_highs_52w": None,
            "new_lows_52w": None,
            "percent_above_20d_change_5d": None,
            "percent_above_50d_change_10d": None,
            "improvement_acceleration": None,
            "price_rising_breadth_weakening": None,
            "price_falling_breadth_improving": None,
            "iwm_spy_relative_strength_20d": round(small_large, 6),
            "rsp_spy_relative_strength_20d": round(equal_weight, 6),
            "iwm_return_5d": round(iwm_5d, 6),
            "iwm_return_20d": round(iwm_20d, 6),
        },
        "scores": {
            "breadth_improvement_score": round(improvement, 2),
            "breadth_deterioration_score": round(deterioration, 2),
            "breadth_confirmation_score": round(_clip(improvement * 0.75 + quality * 0.25, 0, 100), 2),
            "breadth_conflict_score": round(_clip(deterioration * 0.75 + (100 - quality) * 0.25, 0, 100), 2),
            "breadth_quality_score": quality,
        },
        "data_note": "Proxy only: IWM/SPY, RSP/SPY and IWM trend. Not full Russell 2000 constituent breadth.",
    }


def calculate_breadth_metrics(rows_by_ticker: dict[str, list[dict[str, Any]]], *, index_series: Any) -> dict[str, Any]:
    valid_rows = {ticker: rows for ticker, rows in rows_by_ticker.items() if len(rows) >= 2}
    percent_20 = _percent_above_ma(valid_rows, 20)
    percent_50 = _percent_above_ma(valid_rows, 50)
    percent_200 = _percent_above_ma(valid_rows, 200)
    prior_20_5 = _percent_above_ma_at_offset(valid_rows, 20, 5)
    prior_20_10 = _percent_above_ma_at_offset(valid_rows, 20, 10)
    prior_50_10 = _percent_above_ma_at_offset(valid_rows, 50, 10)
    advancers = 0
    decliners = 0
    up_volume = 0.0
    down_volume = 0.0
    highs_20 = lows_20 = highs_52w = lows_52w = 0
    for rows in valid_rows.values():
        close = _safe_float(rows[-1].get("close"))
        previous = _safe_float(rows[-2].get("close"))
        volume = _safe_float(rows[-1].get("volume")) or 0.0
        if close is None or previous is None:
            continue
        if close > previous:
            advancers += 1
            up_volume += volume
        elif close < previous:
            decliners += 1
            down_volume += volume
        last_20 = [_safe_float(row.get("close")) for row in rows[-20:]]
        last_20 = [value for value in last_20 if value is not None]
        last_252 = [_safe_float(row.get("close")) for row in rows[-252:]]
        last_252 = [value for value in last_252 if value is not None]
        if last_20 and close >= max(last_20):
            highs_20 += 1
        if last_20 and close <= min(last_20):
            lows_20 += 1
        if len(last_252) >= 120 and close >= max(last_252):
            highs_52w += 1
        if len(last_252) >= 120 and close <= min(last_252):
            lows_52w += 1

    change_20_5 = (percent_20 - prior_20_5) if percent_20 is not None and prior_20_5 is not None else None
    change_20_10 = (prior_20_5 - prior_20_10) if prior_20_5 is not None and prior_20_10 is not None else None
    change_50_10 = (percent_50 - prior_50_10) if percent_50 is not None and prior_50_10 is not None else None
    acceleration = (change_20_5 - change_20_10) if change_20_5 is not None and change_20_10 is not None else None
    index_closes = _series_closes(index_series)
    index_return_5d = _return(index_closes, 5)
    price_rising_breadth_weakening = index_return_5d > 0 and (change_20_5 or 0.0) < -0.03
    price_falling_breadth_improving = index_return_5d < 0 and (change_20_5 or 0.0) > 0.03

    return {
        "percent_above_20d": _round_or_none(percent_20, 4),
        "percent_above_50d": _round_or_none(percent_50, 4),
        "percent_above_200d": _round_or_none(percent_200, 4),
        "advancers": advancers,
        "decliners": decliners,
        "advance_decline_ratio": round(advancers / max(decliners, 1), 4),
        "up_volume_down_volume_ratio": round(up_volume / max(down_volume, 1.0), 4) if up_volume or down_volume else None,
        "new_highs_20d": highs_20,
        "new_lows_20d": lows_20,
        "new_highs_52w": highs_52w,
        "new_lows_52w": lows_52w,
        "percent_above_20d_change_5d": _round_or_none(change_20_5, 4),
        "percent_above_50d_change_10d": _round_or_none(change_50_10, 4),
        "improvement_acceleration": _round_or_none(acceleration, 4),
        "index_return_5d": round(index_return_5d, 6),
        "price_rising_breadth_weakening": price_rising_breadth_weakening,
        "price_falling_breadth_improving": price_falling_breadth_improving,
    }


def calculate_breadth_scores(
    *,
    metrics: dict[str, Any],
    coverage_ratio: float,
    stale_constituents: bool,
    stale_price_data: bool,
    sample_limited: bool,
) -> dict[str, float]:
    p20 = _safe_float(metrics.get("percent_above_20d")) or 0.0
    p50 = _safe_float(metrics.get("percent_above_50d")) or 0.0
    p200 = _safe_float(metrics.get("percent_above_200d")) or 0.0
    change20 = _safe_float(metrics.get("percent_above_20d_change_5d")) or 0.0
    change50 = _safe_float(metrics.get("percent_above_50d_change_10d")) or 0.0
    acceleration = _safe_float(metrics.get("improvement_acceleration")) or 0.0
    adv_ratio = min((_safe_float(metrics.get("advance_decline_ratio")) or 1.0) / 3.0, 1.0)
    highs20 = float(metrics.get("new_highs_20d") or 0)
    lows20 = float(metrics.get("new_lows_20d") or 0)
    high_low_balance = (highs20 + 1.0) / (highs20 + lows20 + 2.0)
    divergence_penalty = 18.0 if metrics.get("price_rising_breadth_weakening") else 0.0
    divergence_bonus = 8.0 if metrics.get("price_falling_breadth_improving") else 0.0

    improvement = _clip(
        p20 * 32.0
        + p50 * 25.0
        + p200 * 12.0
        + max(change20, 0.0) * 220.0
        + max(change50, 0.0) * 160.0
        + max(acceleration, 0.0) * 120.0
        + adv_ratio * 11.0
        + high_low_balance * 10.0
        + divergence_bonus
        - divergence_penalty,
        0.0,
        100.0,
    )
    deterioration = _clip(
        (1.0 - p20) * 26.0
        + (1.0 - p50) * 22.0
        + (1.0 - p200) * 10.0
        + max(-change20, 0.0) * 230.0
        + max(-change50, 0.0) * 150.0
        + max(-acceleration, 0.0) * 100.0
        + (1.0 - adv_ratio) * 10.0
        + (1.0 - high_low_balance) * 12.0
        + divergence_penalty,
        0.0,
        100.0,
    )
    quality = _clip(coverage_ratio * 78.0 + 22.0, 0.0, 100.0)
    if stale_constituents:
        quality -= 10.0
    if stale_price_data:
        quality -= 18.0
    if sample_limited:
        quality -= 20.0
    quality = _clip(quality, 0.0, 100.0)
    confirmation = _clip(improvement * 0.72 + quality * 0.20 + (100.0 - deterioration) * 0.08, 0.0, 100.0)
    conflict = _clip(deterioration * 0.76 + (100.0 - quality) * 0.16 + divergence_penalty * 0.50, 0.0, 100.0)
    return {
        "breadth_improvement_score": round(improvement, 2),
        "breadth_deterioration_score": round(deterioration, 2),
        "breadth_confirmation_score": round(confirmation, 2),
        "breadth_conflict_score": round(conflict, 2),
        "breadth_quality_score": round(quality, 2),
    }


def build_sector_participation_payload(series_by_symbol: dict[str, Any]) -> dict[str, Any]:
    rows = []
    for symbol in SECTOR_ETFS:
        closes = _series_closes(series_by_symbol.get(symbol))
        if len(closes) < 21:
            continue
        rows.append(
            {
                "symbol": symbol,
                "above_20d_ma": closes[-1] > _mean(closes[-20:]),
                "return_5d": round(_return(closes, 5), 6),
                "return_20d": round(_return(closes, 20), 6),
            }
        )
    participation = sum(1 for row in rows if row["above_20d_ma"]) / len(rows) if rows else None
    positive_5d = sum(1 for row in rows if row["return_5d"] > 0) / len(rows) if rows else None
    return {
        "source": "sector-etf-participation-proxy",
        "is_proxy": True,
        "sector_count": len(rows),
        "sector_participation_above_20d": _round_or_none(participation, 4),
        "sector_positive_5d_ratio": _round_or_none(positive_5d, 4),
        "sectors": rows,
        "data_note": "Sector ETF proxy, not constituent-level sector breadth.",
    }


def attach_internal_resonance(universes: dict[str, Any], sector_payload: dict[str, Any]) -> dict[str, Any]:
    """Attach per-universe and aggregate market-internal resonance scores.

    Resonance answers a different question than raw breadth: are constituents,
    equal-weight/small-cap proxies and sector participation pointing the same
    way, or is index strength mostly surface-level?
    """

    iwm_metrics = (universes.get("IWM") or {}).get("metrics") or {}
    equal_weight = _safe_float(iwm_metrics.get("rsp_spy_relative_strength_20d")) or 0.0
    small_large = _safe_float(iwm_metrics.get("iwm_spy_relative_strength_20d")) or 0.0
    sector_participation = _safe_float(sector_payload.get("sector_participation_above_20d"))
    sector_positive = _safe_float(sector_payload.get("sector_positive_5d_ratio"))
    sector_score = _clip(((sector_participation if sector_participation is not None else 0.5) * 0.6 + (sector_positive if sector_positive is not None else 0.5) * 0.4) * 100.0, 0.0, 100.0)

    symbol_scores: list[float] = []
    symbol_payloads: dict[str, Any] = {}
    for symbol, payload in universes.items():
        resonance = calculate_internal_resonance(
            symbol=symbol,
            payload=payload,
            sector_score=sector_score,
            sector_participation=sector_participation,
            sector_positive=sector_positive,
            equal_weight_relative=equal_weight,
            small_large_relative=small_large,
        )
        payload["internal_resonance"] = resonance
        symbol_payloads[symbol] = resonance
        if resonance.get("resonance_quality_score", 0) >= 45:
            symbol_scores.append(float(resonance.get("resonance_score") or 0.0))

    average_score = round(sum(symbol_scores) / len(symbol_scores), 2) if symbol_scores else 0.0
    surface_only_symbols = [symbol for symbol, item in symbol_payloads.items() if item.get("resonance_state") == "surface_only"]
    aligned_symbols = [symbol for symbol, item in symbol_payloads.items() if item.get("resonance_state") == "aligned"]
    if average_score >= 70 and len(surface_only_symbols) <= 1:
        state = "aligned"
        label = "market_internal_resonance"
    elif surface_only_symbols and average_score < 60:
        state = "surface_only"
        label = "index_surface_strength"
    elif average_score >= 45:
        state = "mixed"
        label = "partial_resonance"
    else:
        state = "weak"
        label = "no_internal_resonance"

    return {
        "resonance_score": average_score,
        "resonance_state": state,
        "label": label,
        "aligned_symbols": aligned_symbols,
        "surface_only_symbols": surface_only_symbols,
        "sector_score": round(sector_score, 2),
        "sector_participation_above_20d": _round_or_none(sector_participation, 4),
        "sector_positive_5d_ratio": _round_or_none(sector_positive, 4),
        "equal_weight_vs_cap_weight_20d": round(equal_weight, 6),
        "small_cap_vs_large_cap_20d": round(small_large, 6),
        "symbols": symbol_payloads,
        "data_note": "Resonance combines true/proxy breadth, sector ETF participation, RSP/SPY and IWM/SPY. It is not a standalone alpha.",
    }


def calculate_internal_resonance(
    *,
    symbol: str,
    payload: dict[str, Any],
    sector_score: float,
    sector_participation: float | None,
    sector_positive: float | None,
    equal_weight_relative: float,
    small_large_relative: float,
) -> dict[str, Any]:
    metrics = payload.get("metrics") or {}
    scores = payload.get("scores") or {}
    confirmation = float(scores.get("breadth_confirmation_score") or 0.0)
    conflict = float(scores.get("breadth_conflict_score") or 0.0)
    quality = float(scores.get("breadth_quality_score") or 0.0)
    p20 = _safe_float(metrics.get("percent_above_20d"))
    p50 = _safe_float(metrics.get("percent_above_50d"))
    p200 = _safe_float(metrics.get("percent_above_200d"))
    change20 = _safe_float(metrics.get("percent_above_20d_change_5d")) or 0.0
    adv_ratio = _safe_float(metrics.get("advance_decline_ratio"))
    highs20 = _safe_float(metrics.get("new_highs_20d")) or 0.0
    lows20 = _safe_float(metrics.get("new_lows_20d")) or 0.0
    high_low_score = ((highs20 + 1.0) / (highs20 + lows20 + 2.0)) * 100.0 if highs20 or lows20 else 50.0
    adv_score = _clip(((adv_ratio if adv_ratio is not None else 1.0) / 3.0) * 100.0, 0.0, 100.0)
    constituent_score = _clip(
        ((p20 if p20 is not None else 0.5) * 34.0)
        + ((p50 if p50 is not None else 0.5) * 28.0)
        + ((p200 if p200 is not None else 0.5) * 14.0)
        + adv_score * 0.12
        + high_low_score * 0.12,
        0.0,
        100.0,
    )
    equal_weight_score = _clip(50.0 + equal_weight_relative * 900.0, 0.0, 100.0)
    small_large_score = _clip(50.0 + small_large_relative * 900.0, 0.0, 100.0)
    participation_score = _clip(sector_score * 0.55 + equal_weight_score * 0.25 + small_large_score * 0.20, 0.0, 100.0)

    surface_strength = bool(
        metrics.get("price_rising_breadth_weakening")
        or (metrics.get("index_return_5d") or 0.0) > 0 and confirmation < 55.0
        or (metrics.get("index_return_5d") or 0.0) > 0 and (p20 is not None and p20 < 0.45)
        or equal_weight_relative < -0.006
        or small_large_relative < -0.010
    )
    broad_participation = confirmation >= 65.0 and constituent_score >= 60.0 and participation_score >= 55.0 and conflict < 45.0
    resonance_score = _clip(
        constituent_score * 0.32
        + confirmation * 0.24
        + participation_score * 0.20
        + quality * 0.14
        + max(change20, 0.0) * 450.0 * 0.10
        - max(conflict - 35.0, 0.0) * 0.18
        - (12.0 if surface_strength else 0.0),
        0.0,
        100.0,
    )
    resonance_quality = quality if payload.get("is_true_breadth") else min(quality, 68.0)
    if broad_participation and resonance_score >= 70:
        state = "aligned"
        label = "内部共振"
    elif surface_strength and resonance_score < 65:
        state = "surface_only"
        label = "指数表面强"
    elif resonance_score >= 50:
        state = "mixed"
        label = "部分共振"
    else:
        state = "weak"
        label = "内部未共振"
    supports_bounce = state == "aligned" or (state == "mixed" and confirmation > conflict and change20 >= 0.0)
    supports_downside = state == "surface_only" or conflict >= 58.0
    return {
        "resonance_score": round(resonance_score, 2),
        "resonance_state": state,
        "resonance_label": label,
        "resonance_quality_score": round(resonance_quality, 2),
        "broad_participation": bool(broad_participation),
        "surface_strength_without_participation": bool(surface_strength),
        "supports_bounce_or_repair": bool(supports_bounce),
        "supports_downside_or_failed_bounce": bool(supports_downside),
        "components": {
            "constituent_participation_score": round(constituent_score, 2),
            "sector_participation_score": round(sector_score, 2),
            "equal_weight_score": round(equal_weight_score, 2),
            "small_cap_score": round(small_large_score, 2),
            "participation_score": round(participation_score, 2),
            "confirmation_score": round(confirmation, 2),
            "conflict_score": round(conflict, 2),
            "quality_score": round(quality, 2),
            "sector_participation_above_20d": _round_or_none(sector_participation, 4),
            "sector_positive_5d_ratio": _round_or_none(sector_positive, 4),
            "equal_weight_vs_cap_weight_20d": round(equal_weight_relative, 6),
            "small_cap_vs_large_cap_20d": round(small_large_relative, 6),
        },
        "reason": _internal_resonance_reason(symbol, state, confirmation, conflict, p20, sector_participation, equal_weight_relative, small_large_relative),
        "data_note": "Point-in-time breadth/ETF proxy confirmation only; not a deterministic forecast.",
    }


def _internal_resonance_reason(
    symbol: str,
    state: str,
    confirmation: float,
    conflict: float,
    p20: float | None,
    sector_participation: float | None,
    equal_weight_relative: float,
    small_large_relative: float,
) -> str:
    p20_text = f"{p20:.0%}" if p20 is not None else "unknown"
    sector_text = f"{sector_participation:.0%}" if sector_participation is not None else "unknown"
    if state == "aligned":
        return f"{symbol} 内部共振：成分股 20d 上方比例 {p20_text}，行业参与 {sector_text}，confirmation {confirmation:.0f} 高于 conflict {conflict:.0f}。"
    if state == "surface_only":
        return f"{symbol} 指数表面强但内部没充分跟上：confirmation {confirmation:.0f}，conflict {conflict:.0f}，RSP/SPY {equal_weight_relative:.2%}，IWM/SPY {small_large_relative:.2%}。"
    if state == "mixed":
        return f"{symbol} 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。"
    return f"{symbol} 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。"


def build_summary(universes: dict[str, Any], sector_payload: dict[str, Any]) -> dict[str, Any]:
    true_available = [symbol for symbol in TRUE_UNIVERSES if universes.get(symbol, {}).get("is_true_breadth")]
    stale = [symbol for symbol, payload in universes.items() if payload.get("stale_price_data") or payload.get("stale_constituents")]
    qualities = [float((payload.get("scores") or {}).get("breadth_quality_score") or 0.0) for payload in universes.values()]
    avg_quality = sum(qualities) / len(qualities) if qualities else 0.0
    return {
        "provider_available": len(true_available) >= 2,
        "true_breadth_available": len(true_available) >= 3,
        "true_breadth_symbols": true_available,
        "breadth_proxy_only_symbols": [symbol for symbol, payload in universes.items() if payload.get("is_proxy")],
        "stale_data": bool(stale),
        "stale_symbols": stale,
        "average_breadth_quality_score": round(avg_quality, 2),
        "sector_proxy_available": bool(sector_payload.get("sector_count")),
        "data_note": "SPY/QQQ/DIA can be true constituent breadth; IWM remains proxy-only in this phase.",
    }


def render_breadth_status_markdown(bundle: dict[str, Any]) -> str:
    summary = bundle.get("summary") or {}
    lines = [
        "# Breadth Data Status",
        "",
        f"Generated at: {bundle.get('generated_at')}",
        "",
        f"Provider available: {summary.get('provider_available')}",
        f"True breadth available: {summary.get('true_breadth_available')}",
        f"True breadth symbols: {', '.join(summary.get('true_breadth_symbols') or []) or 'none'}",
        f"Proxy-only symbols: {', '.join(summary.get('breadth_proxy_only_symbols') or []) or 'none'}",
        f"Average breadth quality score: {summary.get('average_breadth_quality_score')}",
        f"Stale data: {summary.get('stale_data')}",
        "",
        "## Market Internal Resonance",
        "",
        f"- resonance_score: {(summary.get('market_internal_resonance') or {}).get('resonance_score')}",
        f"- resonance_state: {(summary.get('market_internal_resonance') or {}).get('resonance_state')}",
        f"- label: {(summary.get('market_internal_resonance') or {}).get('label')}",
        f"- aligned_symbols: {', '.join((summary.get('market_internal_resonance') or {}).get('aligned_symbols') or []) or 'none'}",
        f"- surface_only_symbols: {', '.join((summary.get('market_internal_resonance') or {}).get('surface_only_symbols') or []) or 'none'}",
        f"- sector_score: {(summary.get('market_internal_resonance') or {}).get('sector_score')}",
        f"- equal_weight_vs_cap_weight_20d: {(summary.get('market_internal_resonance') or {}).get('equal_weight_vs_cap_weight_20d')}",
        f"- small_cap_vs_large_cap_20d: {(summary.get('market_internal_resonance') or {}).get('small_cap_vs_large_cap_20d')}",
        "",
        "## Universe Status",
        "",
    ]
    for symbol in TARGET_UNIVERSES:
        payload = (bundle.get("universes") or {}).get(symbol, {})
        scores = payload.get("scores") or {}
        metrics = payload.get("metrics") or {}
        internal = payload.get("internal_resonance") or {}
        lines.extend(
            [
                f"### {symbol}",
                "",
                f"- status: {payload.get('status')}",
                f"- source: {payload.get('source')}",
                f"- latest_date: {payload.get('latest_date')}",
                f"- true_breadth: {payload.get('is_true_breadth')}",
                f"- proxy: {payload.get('is_proxy')}",
                f"- constituents used / expected: {payload.get('constituents_used')} / {payload.get('constituents_expected')}",
                f"- coverage_ratio: {payload.get('coverage_ratio')}",
                f"- stale_constituents: {payload.get('stale_constituents')}",
                f"- stale_price_data: {payload.get('stale_price_data')}",
                f"- percent_above_20d / 50d / 200d: {metrics.get('percent_above_20d')} / {metrics.get('percent_above_50d')} / {metrics.get('percent_above_200d')}",
                f"- advancers / decliners / A-D ratio: {metrics.get('advancers')} / {metrics.get('decliners')} / {metrics.get('advance_decline_ratio')}",
                f"- new highs/lows 20d: {metrics.get('new_highs_20d')} / {metrics.get('new_lows_20d')}",
                f"- new highs/lows 52w: {metrics.get('new_highs_52w')} / {metrics.get('new_lows_52w')}",
                f"- improvement / deterioration / confirmation / conflict / quality: {scores.get('breadth_improvement_score')} / {scores.get('breadth_deterioration_score')} / {scores.get('breadth_confirmation_score')} / {scores.get('breadth_conflict_score')} / {scores.get('breadth_quality_score')}",
                f"- internal_resonance: {internal.get('resonance_state')} / score {internal.get('resonance_score')} / {internal.get('reason')}",
                "",
            ]
        )
    lines.extend(
        [
            "## Notes",
            "",
            "- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.",
            "- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.",
            "- This report does not change Alpha v1 threshold or status.",
            "",
        ]
    )
    return "\n".join(lines)


def _fetch_wikipedia_constituents(*, url: str, table_hint: tuple[str, ...], symbol_columns: tuple[str, ...]) -> list[str]:
    html = _http_get_text(url, timeout=30)
    try:
        import pandas as pd
        from io import StringIO

        for frame in pd.read_html(StringIO(html)):
            columns = [str(col).strip() for col in frame.columns]
            normalized = {col.lower(): col for col in columns}
            joined = " ".join(col.lower() for col in columns)
            if all(hint in joined for hint in table_hint):
                for candidate in symbol_columns:
                    if candidate.lower() in normalized:
                        return [str(value).strip() for value in frame[normalized[candidate]].dropna().tolist()]
    except Exception:
        pass
    return _parse_wikipedia_tickers_fallback(html)


def _parse_wikipedia_tickers_fallback(html: str) -> list[str]:
    tables = re.findall(r"<table[^>]*>(.*?)</table>", html, flags=re.IGNORECASE | re.DOTALL)
    best: list[str] = []
    for table in tables:
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", table, flags=re.IGNORECASE | re.DOTALL)
        tickers: list[str] = []
        for row in rows[1:]:
            cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, flags=re.IGNORECASE | re.DOTALL)
            if not cells:
                continue
            cell_text = _strip_html(cells[0])
            ticker = _normalize_ticker(cell_text)
            if re.fullmatch(r"[A-Z][A-Z0-9.-]{0,7}", ticker):
                tickers.append(ticker)
        if len(tickers) > len(best):
            best = tickers
    return best


def _http_get_text(url: str, timeout: int = 30, attempts: int = 3) -> str:
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read().decode("utf-8", errors="replace")
        except Exception as exc:
            last_error = exc
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def _download_yfinance_batch(tickers: list[str], *, period: str) -> tuple[dict[str, list[dict[str, Any]]], dict[str, str]]:
    if not tickers:
        return {}, {}
    rows_by_ticker, errors = _download_yahoo_chart_batch(tickers, period=period)
    missing = [ticker for ticker in tickers if ticker not in rows_by_ticker]
    if not missing:
        return rows_by_ticker, {}
    try:
        import yfinance as yf
    except Exception as exc:
        errors.update({ticker: f"{errors.get(ticker, 'yahoo_chart_failed')};yfinance_import_error:{type(exc).__name__}" for ticker in missing})
        return rows_by_ticker, errors

    try:
        yfinance_cache = CACHE_ROOT / "yfinance_cache"
        yfinance_cache.mkdir(parents=True, exist_ok=True)
        if hasattr(yf, "set_tz_cache_location"):
            yf.set_tz_cache_location(str(yfinance_cache))
        data = yf.download(
            tickers=" ".join(missing),
            period=period,
            auto_adjust=True,
            group_by="ticker",
            progress=False,
            threads=False,
            timeout=30,
        )
    except Exception as exc:
        errors.update({ticker: f"{errors.get(ticker, 'yahoo_chart_failed')};yfinance_download_error:{type(exc).__name__}" for ticker in missing})
        return rows_by_ticker, errors

    for ticker in missing:
        rows = _extract_yfinance_rows(data, ticker, multi=len(missing) > 1)
        if rows:
            rows_by_ticker[ticker] = rows
            errors.pop(ticker, None)
        else:
            errors[ticker] = f"{errors.get(ticker, 'yahoo_chart_failed')};empty_yfinance_rows"
    return rows_by_ticker, errors


def _download_yahoo_chart_batch(tickers: list[str], *, period: str) -> tuple[dict[str, list[dict[str, Any]]], dict[str, str]]:
    rows_by_ticker: dict[str, list[dict[str, Any]]] = {}
    errors: dict[str, str] = {}
    workers = max(1, min(_env_int("BREADTH_DOWNLOAD_WORKERS", 8) or 8, 16))
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(_download_yahoo_chart_one, ticker, period): ticker for ticker in tickers}
        for future in concurrent.futures.as_completed(futures):
            ticker = futures[future]
            try:
                rows = future.result()
                if rows:
                    rows_by_ticker[ticker] = rows
                else:
                    errors[ticker] = "empty_yahoo_chart_rows"
            except Exception as exc:
                errors[ticker] = f"yahoo_chart_error:{type(exc).__name__}"
    return rows_by_ticker, errors


def _download_yahoo_chart_one(ticker: str, period: str) -> list[dict[str, Any]]:
    range_value = "3mo" if period == "3mo" else "2y"
    encoded = urllib.parse.quote(ticker, safe="")
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{encoded}?range={range_value}&interval=1d&events=history"
    text = _http_get_text(url, timeout=15, attempts=2)
    payload = json.loads(text)
    result = ((payload.get("chart") or {}).get("result") or [None])[0]
    if not result:
        return []
    timestamps = result.get("timestamp") or []
    quote = (((result.get("indicators") or {}).get("quote") or [{}])[0]) or {}
    closes = quote.get("close") or []
    volumes = quote.get("volume") or []
    rows: list[dict[str, Any]] = []
    for idx, timestamp in enumerate(timestamps):
        close = _safe_float(closes[idx] if idx < len(closes) else None)
        if close is None:
            continue
        volume = _safe_float(volumes[idx] if idx < len(volumes) else None)
        rows.append(
            {
                "date": datetime.fromtimestamp(int(timestamp), tz=timezone.utc).date().isoformat(),
                "close": round(close, 6),
                "volume": round(volume, 2) if volume is not None and math.isfinite(volume) else None,
            }
        )
    return rows


def _extract_yfinance_rows(data: Any, ticker: str, *, multi: bool) -> list[dict[str, Any]]:
    try:
        frame = data[ticker] if multi and hasattr(data, "columns") and ticker in data.columns.get_level_values(0) else data
        if frame is None or frame.empty:
            return []
        rows: list[dict[str, Any]] = []
        for idx, row in frame.iterrows():
            close = _safe_float(row.get("Close"))
            if close is None or not math.isfinite(close):
                continue
            volume = _safe_float(row.get("Volume"))
            rows.append(
                {
                    "date": idx.date().isoformat() if hasattr(idx, "date") else str(idx)[:10],
                    "close": round(close, 6),
                    "volume": round(volume, 2) if volume is not None and math.isfinite(volume) else None,
                }
            )
        return rows
    except Exception:
        return []


def _write_constituent_cache(path: Path, result: ConstituentResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "symbol": result.symbol,
                "name": result.name,
                "tickers": result.tickers,
                "source": result.source,
                "cached_at": datetime.now(timezone.utc).isoformat(),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def _read_constituent_cache(path: Path) -> ConstituentResult | None:
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    return ConstituentResult(
        symbol=str(payload.get("symbol") or path.stem.split("_")[0]).upper(),
        name=str(payload.get("name") or path.stem),
        tickers=[_normalize_ticker(value) for value in payload.get("tickers", [])],
        source=str(payload.get("source") or "local-cache"),
        stale_constituents=True,
    )


def _price_cache_file(ticker: str) -> Path:
    safe = ticker.replace("/", "-").replace("\\", "-")
    return PRICE_CACHE_DIR / f"{safe}.json"


def _read_price_cache(ticker: str) -> list[dict[str, Any]]:
    path = _price_cache_file(ticker)
    if not path.exists():
        return []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        rows = payload.get("rows") if isinstance(payload, dict) else payload
        return sorted([row for row in rows if row.get("date") and _safe_float(row.get("close")) is not None], key=lambda row: row["date"])
    except Exception:
        return []


def _write_price_cache(ticker: str, rows: list[dict[str, Any]]) -> None:
    path = _price_cache_file(ticker)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"symbol": ticker, "cached_at": datetime.now(timezone.utc).isoformat(), "rows": rows}, ensure_ascii=False),
        encoding="utf-8",
    )


def _merge_price_rows(old: list[dict[str, Any]], new: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_date: dict[str, dict[str, Any]] = {}
    for row in old + new:
        row_date = row.get("date")
        close = _safe_float(row.get("close"))
        if not row_date or close is None:
            continue
        by_date[str(row_date)] = {
            "date": str(row_date),
            "close": round(close, 6),
            "volume": _safe_float(row.get("volume")),
        }
    return [by_date[key] for key in sorted(by_date)]


def _percent_above_ma(rows_by_ticker: dict[str, list[dict[str, Any]]], window: int) -> float | None:
    total = 0
    above = 0
    for rows in rows_by_ticker.values():
        closes = [_safe_float(row.get("close")) for row in rows]
        closes = [value for value in closes if value is not None]
        if len(closes) < window:
            continue
        total += 1
        if closes[-1] > _mean(closes[-window:]):
            above += 1
    return above / total if total else None


def _percent_above_ma_at_offset(rows_by_ticker: dict[str, list[dict[str, Any]]], window: int, offset: int) -> float | None:
    total = 0
    above = 0
    for rows in rows_by_ticker.values():
        closes = [_safe_float(row.get("close")) for row in rows]
        closes = [value for value in closes if value is not None]
        anchor = len(closes) - 1 - offset
        if anchor < window - 1:
            continue
        total += 1
        if closes[anchor] > _mean(closes[anchor - window + 1 : anchor + 1]):
            above += 1
    return above / total if total else None


def _rows_are_recent(rows: list[dict[str, Any]], fresh_days: int) -> bool:
    latest = _last_date(rows)
    if not latest:
        return False
    try:
        latest_date = date.fromisoformat(latest)
    except ValueError:
        return False
    return (date.today() - latest_date).days <= fresh_days


def _date_is_stale(value: str | None, max_days: int = 7) -> bool:
    if not value:
        return True
    try:
        parsed = date.fromisoformat(str(value)[:10])
    except ValueError:
        return True
    return (date.today() - parsed).days > max_days


def _last_date(rows: list[dict[str, Any]]) -> str | None:
    if not rows:
        return None
    return str(rows[-1].get("date") or "")[:10] or None


def _series_closes(series: Any) -> list[float]:
    rows = getattr(series, "rows", None) or []
    values: list[float] = []
    for row in rows:
        value = _safe_float(row.get("close"))
        if value is not None and math.isfinite(value):
            values.append(value)
    return values


def _series_latest_date(series: Any) -> str | None:
    rows = getattr(series, "rows", None) or []
    if not rows:
        return None
    return str(rows[-1].get("date") or "")[:10] or None


def _return(values: list[float], window: int) -> float:
    if len(values) <= window or values[-1 - window] == 0:
        return 0.0
    return values[-1] / values[-1 - window] - 1.0


def _relative_return(left: list[float], right: list[float], window: int) -> float:
    return _return(left, window) - _return(right, window)


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _clip(value: float, low: float, high: float) -> float:
    return min(max(value, low), high)


def _safe_float(value: Any) -> float | None:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def _round_or_none(value: float | None, digits: int) -> float | None:
    return round(value, digits) if value is not None and math.isfinite(value) else None


def _strip_html(value: str) -> str:
    text = re.sub(r"<[^>]+>", "", value)
    return unescape(text).strip()


def _normalize_ticker(value: Any) -> str:
    ticker = str(value).strip().upper()
    ticker = ticker.replace(".", "-")
    ticker = re.sub(r"[^A-Z0-9-]", "", ticker)
    return ticker


def _env_int(name: str, default: int | None = None) -> int | None:
    raw = os.getenv(name)
    if raw is None or raw == "":
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def main() -> int:
    parser = argparse.ArgumentParser(description="Build true/proxy breadth status JSON.")
    parser.add_argument("--output", default=str(PROJECT_ROOT / "frontend" / "public" / "breadth-status.json"))
    parser.add_argument("--report", default=str(PROJECT_ROOT / "outputs" / "breadth_data_status.md"))
    parser.add_argument("--lookback-days", type=int, default=420)
    args = parser.parse_args()
    bundle = fetch_breadth_bundle(lookback_days=args.lookback_days)
    output = Path(args.output)
    report = Path(args.report)
    output.parent.mkdir(parents=True, exist_ok=True)
    report.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
    report.write_text(render_breadth_status_markdown(bundle), encoding="utf-8")
    print(f"wrote {output}")
    print(f"wrote {report}")
    print(f"BREADTH_TRUE_AVAILABLE={str(bool(bundle.get('summary', {}).get('true_breadth_available'))).lower()}")
    print(f"BREADTH_AVERAGE_QUALITY={bundle.get('summary', {}).get('average_breadth_quality_score')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
