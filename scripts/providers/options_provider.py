from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
BACKEND_ROOT = PROJECT_ROOT / "backend"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.services.data_providers.auto_download import DownloadedSeries, is_real_market_data


TARGET_SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
VOL_SYMBOLS = ("^VIX", "^VIX9D", "^VIX3M", "^VIX6M", "^VVIX", "^SKEW")


def fetch_options_bundle(
    *,
    series_by_symbol: dict[str, DownloadedSeries],
    target_symbols: tuple[str, ...] = TARGET_SYMBOLS,
) -> dict[str, Any]:
    closes = {symbol: _closes(series_by_symbol.get(symbol)) for symbol in set(target_symbols + VOL_SYMBOLS)}
    source_status = {symbol: _source_status(symbol, series_by_symbol.get(symbol)) for symbol in VOL_SYMBOLS}
    market = _market_options_snapshot(closes, source_status)
    symbols = {
        symbol: _symbol_options_snapshot(symbol, closes.get(symbol, []), market)
        for symbol in target_symbols
    }
    summary = _summary_payload(market, source_status)
    return {
        "provider": "options_volatility_structure",
        "version": "market_intelligence_options_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": summary,
        "market": market,
        "symbols": symbols,
        "sources": source_status,
        "warnings": [
            "This provider uses real volatility-index proxies when available.",
            "Put/call ratio and dealer gamma are marked missing unless a stable real feed exists.",
            "Options data is explanatory input for probabilistic forecasting, not a standalone alpha.",
        ],
    }


def render_options_status_markdown(bundle: dict[str, Any]) -> str:
    summary = bundle.get("summary") or {}
    market = bundle.get("market") or {}
    lines = [
        "# Options / Volatility Structure Status",
        "",
        f"Generated at: `{bundle.get('generated_at')}`",
        "",
        "## Summary",
        "",
        f"- options_available: `{summary.get('options_available')}`",
        f"- options_partial: `{summary.get('options_partial')}`",
        f"- options_missing: `{summary.get('options_missing')}`",
        f"- options_stale: `{summary.get('options_stale')}`",
        f"- options_source: `{summary.get('options_source')}`",
        f"- vix_term_available: `{summary.get('vix_term_available')}`",
        f"- vvix_available: `{summary.get('vvix_available')}`",
        f"- skew_available: `{summary.get('skew_available')}`",
        f"- put_call_available: `{summary.get('put_call_available')}`",
        f"- gamma_available: `{summary.get('gamma_available')}`",
        f"- options_quality_score: `{summary.get('options_quality_score')}`",
        "",
        "## Market Snapshot",
        "",
        f"- VIX: `{market.get('vix_level')}`",
        f"- VIX9D: `{market.get('vix9d')}`",
        f"- VIX3M: `{market.get('vix3m')}`",
        f"- VIX6M: `{market.get('vix6m')}`",
        f"- VVIX: `{market.get('vvix')}`",
        f"- SKEW: `{market.get('skew')}`",
        f"- term_structure_state: `{market.get('term_structure_state')}`",
        f"- volatility_reversal_score: `{market.get('volatility_reversal_score')}`",
        f"- panic_release_score: `{market.get('panic_release_score')}`",
        f"- tail_risk_score: `{market.get('tail_risk_score')}`",
        f"- option_stress_score: `{market.get('option_stress_score')}`",
        f"- failed_bounce_options_risk: `{market.get('failed_bounce_options_risk')}`",
        "",
        "## Sources",
        "",
        "| symbol | status | latest_date | latest_value | source | real_data | stale |",
        "|---|---|---|---:|---|---:|---:|",
    ]
    for symbol, row in sorted((bundle.get("sources") or {}).items()):
        lines.append(
            "| "
            f"{symbol} | {row.get('status')} | {row.get('latest_date') or ''} | "
            f"{row.get('latest_value') if row.get('latest_value') is not None else ''} | "
            f"{row.get('source')} | {row.get('real_data')} | {row.get('stale_data')} |"
        )
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- If only VIX term data is available, options coverage is partial, not full.",
            "- Missing put/call and gamma are explicit missing evidence; they are not inferred.",
            "- Options structure can change path weights and risk, but it does not change Alpha v1.",
            "",
        ]
    )
    return "\n".join(lines)


def _market_options_snapshot(closes: dict[str, list[float]], source_status: dict[str, Any]) -> dict[str, Any]:
    vix = closes.get("^VIX", [])
    vix9d = closes.get("^VIX9D", [])
    vix3m = closes.get("^VIX3M", [])
    vix6m = closes.get("^VIX6M", [])
    vvix = closes.get("^VVIX", [])
    skew = closes.get("^SKEW", [])
    vix_level = _last(vix)
    vix9d_level = _last(vix9d)
    vix3m_level = _last(vix3m)
    vix6m_level = _last(vix6m)
    vvix_level = _last(vvix)
    skew_level = _last(skew)
    vix_pct = _percentile_rank(vix, vix_level, 252)
    vvix_pct = _percentile_rank(vvix, vvix_level, 252)
    skew_pct = _percentile_rank(skew, skew_level, 252)
    vix_change_5d = _change(vix, 5)
    vix_change_20d = _change(vix, 20)
    front_spread = _spread(vix9d_level, vix_level)
    three_month_spread = _spread(vix3m_level, vix_level)
    six_month_spread = _spread(vix6m_level, vix_level)
    term_state = _term_structure_state(vix_level, vix9d_level, vix3m_level, vix6m_level)
    term_stress = _term_structure_stress(term_state, front_spread, three_month_spread)
    volatility_reversal = _volatility_reversal_score(vix_pct, vix_change_5d, vix_change_20d, term_state)
    panic_release = _panic_release_score(vix_pct, vix_change_5d, vix_change_20d, term_state)
    tail_risk = _tail_risk_score(vvix_pct, skew_pct, term_stress)
    option_stress = _clip(vix_pct * 0.32 + tail_risk * 0.30 + term_stress * 0.26 + (0.12 if vix_change_5d > 0 else 0.0) - panic_release * 0.10, 0.0, 1.0)
    failed_bounce_risk = _clip(option_stress * 0.55 + max(0.0, vix_change_5d) * 0.025 + term_stress * 0.25 + tail_risk * 0.20, 0.0, 1.0)
    quality = _options_quality_score(source_status)
    return {
        "vix_level": vix_level,
        "vix_change_5d": vix_change_5d,
        "vix_change_20d": vix_change_20d,
        "vix_percentile_1y": vix_pct,
        "vix9d": vix9d_level,
        "vix3m": vix3m_level,
        "vix6m": vix6m_level,
        "vvix": vvix_level,
        "vvix_percentile_1y": vvix_pct,
        "skew": skew_level,
        "skew_percentile_1y": skew_pct,
        "vix9d_minus_vix": front_spread,
        "vix3m_minus_vix": three_month_spread,
        "vix6m_minus_vix": six_month_spread,
        "term_structure_state": term_state,
        "vix_term_structure_stress": term_stress,
        "volatility_reversal_score": round(volatility_reversal, 4),
        "panic_release_score": round(panic_release, 4),
        "tail_risk_score": round(tail_risk, 4),
        "option_stress_score": round(option_stress, 4),
        "failed_bounce_options_risk": round(failed_bounce_risk, 4),
        "options_quality_score": quality,
        "options_supports_bounce": volatility_reversal >= 0.58 and option_stress <= 0.55,
        "options_conflicts_bounce": option_stress >= 0.62 or term_state in {"stress", "backwardation"},
        "options_reason": _options_reason(term_state, volatility_reversal, option_stress, panic_release),
        "options_risk_note": _options_risk_note(term_state, tail_risk, failed_bounce_risk),
        "put_call_ratio": None,
        "put_call_status": "missing",
        "gamma_exposure": None,
        "gamma_status": "missing",
        "options_data_note": "VIX term, VVIX and SKEW are used only when real market data is available; put/call and gamma remain missing.",
    }


def _symbol_options_snapshot(symbol: str, closes: list[float], market: dict[str, Any]) -> dict[str, Any]:
    realized_vol = _realized_vol(closes, 20)
    implied = (market.get("vix_level") / 100.0) if market.get("vix_level") is not None else None
    implied_vs_realized = implied - realized_vol if implied is not None and realized_vol is not None else None
    return {
        **market,
        "symbol": symbol,
        "realized_volatility_20d": realized_vol,
        "implied_vs_realized_proxy": implied_vs_realized,
    }


def _summary_payload(market: dict[str, Any], source_status: dict[str, Any]) -> dict[str, Any]:
    vix_available = bool(source_status.get("^VIX", {}).get("real_data"))
    term_available = vix_available and any(source_status.get(symbol, {}).get("real_data") for symbol in ("^VIX9D", "^VIX3M", "^VIX6M"))
    vvix_available = bool(source_status.get("^VVIX", {}).get("real_data"))
    skew_available = bool(source_status.get("^SKEW", {}).get("real_data"))
    options_available = term_available and (vvix_available or skew_available)
    options_partial = vix_available or term_available or vvix_available or skew_available
    stale = any(row.get("stale_data") for row in source_status.values() if row.get("real_data"))
    missing_symbols = [symbol for symbol, row in source_status.items() if not row.get("real_data")]
    return {
        "options_available": bool(options_available),
        "vix_term_available": bool(term_available),
        "vvix_available": vvix_available,
        "skew_available": skew_available,
        "put_call_available": False,
        "gamma_available": False,
        "options_partial": bool(options_partial and not options_available),
        "options_missing": not bool(options_partial),
        "options_stale": stale,
        "options_source": "market_data_cache/yahoo/stooq" if options_partial else "missing",
        "options_quality_score": market.get("options_quality_score", 0),
        "missing_symbols": missing_symbols,
        "coverage_note": "partial unless VIX term plus VVIX/SKEW are available; put/call and gamma are still missing.",
    }


def _source_status(symbol: str, series: DownloadedSeries | None) -> dict[str, Any]:
    rows = len(series.rows) if series else 0
    real_data = bool(series and is_real_market_data(series))
    latest_row = series.rows[-1] if series and series.rows else {}
    source = series.source if series else "missing"
    fallback = source.startswith("local-cache") or "fallback" in source
    return {
        "symbol": symbol,
        "source": source,
        "status": "available" if real_data else "fallback" if fallback and rows else "missing",
        "rows": rows,
        "latest_date": latest_row.get("date"),
        "latest_value": _to_float(latest_row.get("close")),
        "real_data": real_data,
        "fallback_used": fallback,
        "stale_data": False,
        "missing_data": rows == 0 or not real_data,
        "point_in_time_safe": bool(series and series.point_in_time_safe and real_data),
    }


def _options_quality_score(source_status: dict[str, Any]) -> int:
    points = 0.0
    if source_status.get("^VIX", {}).get("real_data"):
        points += 30
    if source_status.get("^VIX3M", {}).get("real_data"):
        points += 20
    if source_status.get("^VIX9D", {}).get("real_data"):
        points += 12
    if source_status.get("^VIX6M", {}).get("real_data"):
        points += 8
    if source_status.get("^VVIX", {}).get("real_data"):
        points += 12
    if source_status.get("^SKEW", {}).get("real_data"):
        points += 10
    return int(round(_clip(points, 0.0, 92.0)))


def _term_structure_state(vix: float | None, vix9d: float | None, vix3m: float | None, vix6m: float | None) -> str:
    if vix is None or (vix3m is None and vix9d is None and vix6m is None):
        return "missing"
    if vix3m is not None and vix - vix3m >= 1.0:
        return "stress"
    if vix9d is not None and vix9d - vix >= 1.0 and (vix3m is None or vix >= vix3m - 0.5):
        return "stress"
    if vix3m is not None and vix > vix3m:
        return "backwardation"
    if vix3m is not None and vix3m - vix >= 1.0:
        return "contango"
    return "normal"


def _term_structure_stress(state: str, front_spread: float | None, three_month_spread: float | None) -> float:
    base = {"missing": 0.45, "normal": 0.35, "contango": 0.20, "backwardation": 0.72, "stress": 0.90}.get(state, 0.45)
    front = max(0.0, (front_spread or 0.0) / 4.0)
    inverted = max(0.0, -(three_month_spread or 0.0) / 4.0)
    return _clip(base + front * 0.10 + inverted * 0.12, 0.0, 1.0)


def _volatility_reversal_score(vix_pct: float, change_5d: float, change_20d: float, term_state: str) -> float:
    falling = 0.0
    if change_5d < 0:
        falling += min(abs(change_5d) / 6.0, 0.45)
    if change_20d <= 0:
        falling += min(abs(change_20d) / 10.0, 0.30)
    term_bonus = 0.18 if term_state in {"contango", "normal"} else -0.18 if term_state in {"stress", "backwardation"} else 0.0
    return _clip(0.32 + falling + term_bonus + max(vix_pct - 0.50, 0.0) * 0.12, 0.0, 1.0)


def _panic_release_score(vix_pct: float, change_5d: float, change_20d: float, term_state: str) -> float:
    if vix_pct < 0.55:
        high_vol_component = 0.15
    else:
        high_vol_component = min((vix_pct - 0.45) * 0.75, 0.45)
    fall_component = min(max(-change_5d, 0.0) / 7.0 + max(-change_20d, 0.0) / 16.0, 0.45)
    term_component = 0.18 if term_state in {"contango", "normal"} else 0.02
    return _clip(high_vol_component + fall_component + term_component, 0.0, 1.0)


def _tail_risk_score(vvix_pct: float, skew_pct: float, term_stress: float) -> float:
    return _clip(vvix_pct * 0.38 + skew_pct * 0.32 + term_stress * 0.30, 0.0, 1.0)


def _options_reason(term_state: str, reversal: float, stress: float, panic_release: float) -> str:
    if reversal >= 0.60 and stress <= 0.50:
        return "Volatility structure supports a bounce/recovery path because VIX is repairing and stress is contained."
    if stress >= 0.65:
        return "Volatility structure conflicts with a clean bounce because stress or term inversion is elevated."
    if panic_release >= 0.55:
        return "Panic release is improving, but confirmation still depends on credit and breadth."
    return f"Volatility structure is mixed; term state is {term_state}."


def _options_risk_note(term_state: str, tail_risk: float, failed_bounce: float) -> str:
    if failed_bounce >= 0.65 or term_state in {"stress", "backwardation"}:
        return "Failed-bounce risk rises if VIX term structure stays inverted or tail-risk proxies remain elevated."
    if tail_risk >= 0.60:
        return "Tail-risk proxies are still elevated, so bounce confidence is capped."
    return "Options structure does not show a strong failed-bounce warning, but put/call and gamma remain missing."


def _closes(series: DownloadedSeries | None) -> list[float]:
    if not series:
        return []
    values = [_to_float(row.get("close")) for row in series.rows]
    return [value for value in values if value is not None and value > 0]


def _last(values: list[float]) -> float | None:
    return values[-1] if values else None


def _change(values: list[float], period: int) -> float:
    if len(values) <= period or values[-period - 1] == 0:
        return 0.0
    return values[-1] - values[-period - 1]


def _spread(left: float | None, right: float | None) -> float | None:
    if left is None or right is None:
        return None
    return left - right


def _percentile_rank(values: list[float], current: float | None, window: int) -> float:
    if current is None:
        return 0.5
    sample = values[-window:] if len(values) >= window else values
    if not sample:
        return 0.5
    return sum(1 for value in sample if value <= current) / len(sample)


def _realized_vol(values: list[float], window: int) -> float | None:
    if len(values) <= window:
        return None
    returns: list[float] = []
    for left, right in zip(values[-window - 1:-1], values[-window:]):
        if left > 0 and right > 0:
            returns.append(math.log(right / left))
    if len(returns) < 2:
        return None
    mean = sum(returns) / len(returns)
    variance = sum((value - mean) ** 2 for value in returns) / (len(returns) - 1)
    return math.sqrt(variance) * math.sqrt(252)


def _to_float(value: Any) -> float | None:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(parsed) or math.isinf(parsed):
        return None
    return parsed


def _clip(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def main() -> int:
    payload = {
        "provider": "options_volatility_structure",
        "version": "market_intelligence_options_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "options_available": False,
            "vix_term_available": False,
            "vvix_available": False,
            "skew_available": False,
            "put_call_available": False,
            "gamma_available": False,
            "options_partial": False,
            "options_missing": True,
            "options_stale": False,
            "options_source": "standalone_no_market_series",
            "options_quality_score": 0,
        },
        "market": {},
        "symbols": {},
        "sources": {},
    }
    output = Path("frontend/public/options-status.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("options_provider standalone wrote missing status; export_static_alpha_v1.py provides real series input.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
