from __future__ import annotations

import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.services.data_providers.auto_download import DownloadedSeries


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TARGET_SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
SECTOR_SYMBOLS = ("XLC", "XLY", "XLP", "XLE", "XLF", "XLV", "XLI", "XLK", "XLB", "XLU", "XLRE")
RISK_ASSETS = ("SPY", "QQQ", "IWM", "HYG", "SPHB", "RSP")
DEFENSIVE_ASSETS = ("SPLV", "TLT", "UUP", "XLP", "XLU", "XLV")


def fetch_flow_bundle(*, series_by_symbol: dict[str, DownloadedSeries]) -> dict[str, Any]:
    symbols: dict[str, Any] = {}
    latest_dates: list[str] = []
    for symbol in TARGET_SYMBOLS:
        payload = _symbol_flow_payload(symbol, series_by_symbol)
        symbols[symbol] = payload
        if payload.get("latest_date"):
            latest_dates.append(str(payload["latest_date"]))

    summary = _summary(symbols)
    return {
        "provider": "flow_positioning_proxy",
        "version": "v5_proxy",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "latest_date": max(latest_dates) if latest_dates else None,
        "summary": summary,
        "symbols": symbols,
        "sources": _source_rows(series_by_symbol),
        "warnings": [
            "Flow / positioning is proxy-only. It uses ETF volume, relative volume, rotation, credit ETFs, rates ETFs and factor ETFs.",
            "No true fund-flow, prime brokerage, CFTC, dealer positioning or option-flow feed is connected.",
            "Proxy flow can improve information quality, but it is not proof of forecast accuracy.",
        ],
    }


def render_flow_status_markdown(bundle: dict[str, Any]) -> str:
    summary = bundle.get("summary") or {}
    lines = [
        "# Flow / Positioning Proxy Status",
        "",
        f"Generated at: `{bundle.get('generated_at')}`",
        f"Latest date: `{bundle.get('latest_date')}`",
        "",
        "## Summary",
        "",
        f"- flow_available: `{summary.get('flow_available')}`",
        f"- flow_proxy_only: `{summary.get('flow_proxy_only')}`",
        f"- true_flow_available: `{summary.get('true_flow_available')}`",
        f"- average_flow_quality_score: `{summary.get('average_flow_quality_score')}`",
        f"- overall_flow_confirmation_score: `{summary.get('overall_flow_confirmation_score')}`",
        f"- overall_flow_conflict_score: `{summary.get('overall_flow_conflict_score')}`",
        "",
        "## Symbol Detail",
        "",
        "| symbol | quality | confirmation | conflict | risk-on | risk-off | rel volume | note |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for symbol, payload in (bundle.get("symbols") or {}).items():
        scores = payload.get("scores") or {}
        metrics = payload.get("metrics") or {}
        lines.append(
            "| "
            + " | ".join(
                [
                    symbol,
                    str(scores.get("flow_quality_score")),
                    str(scores.get("flow_confirmation_score")),
                    str(scores.get("flow_conflict_score")),
                    str(scores.get("risk_on_flow_score")),
                    str(scores.get("risk_off_flow_score")),
                    str(metrics.get("etf_relative_volume_20d")),
                    str(payload.get("data_note")),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Guardrail",
            "",
            "- This is not true fund flow or true positioning.",
            "- Do not use proxy flow as an execution input.",
            "- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.",
            "",
        ]
    )
    return "\n".join(lines)


def _symbol_flow_payload(symbol: str, series_by_symbol: dict[str, DownloadedSeries]) -> dict[str, Any]:
    target = series_by_symbol.get(symbol)
    target_close = _closes(target)
    target_volume = _volumes(target)
    spy = _closes(series_by_symbol.get("SPY"))
    qqq = _closes(series_by_symbol.get("QQQ"))
    iwm = _closes(series_by_symbol.get("IWM"))
    hyg = _closes(series_by_symbol.get("HYG"))
    lqd = _closes(series_by_symbol.get("LQD"))
    tlt = _closes(series_by_symbol.get("TLT"))
    uup = _closes(series_by_symbol.get("UUP"))
    sphb = _closes(series_by_symbol.get("SPHB"))
    splv = _closes(series_by_symbol.get("SPLV"))
    rsp = _closes(series_by_symbol.get("RSP"))
    sectors = {name: _closes(series_by_symbol.get(name)) for name in SECTOR_SYMBOLS}

    volume_z = _zscore_last(target_volume, 20)
    relative_volume = _relative_volume(target_volume, 20)
    high_beta_vs_low_vol = _relative_return(sphb, splv, 20)
    small_vs_large = _relative_return(iwm, spy, 20)
    equal_weight_vs_cap = _relative_return(rsp, spy, 20)
    credit_risk_appetite = _relative_return(hyg, lqd, 20)
    risk_on_rotation = _basket_return([qqq, iwm, hyg, sphb], 20) - _basket_return([tlt, uup, splv], 20)
    defensive_vs_cyclical = _basket_return(
        [sectors.get("XLP", []), sectors.get("XLU", []), sectors.get("XLV", [])],
        20,
    ) - _basket_return(
        [sectors.get("XLY", []), sectors.get("XLI", []), sectors.get("XLF", []), sectors.get("XLE", [])],
        20,
    )
    sector_participation = _sector_participation(sectors)
    volume_confirmation = _volume_confirmation_score(volume_z, relative_volume, _return(target_close, 5))

    risk_on_score = _clip(
        0.42
        + max(risk_on_rotation, 0.0) * 4.0
        + max(high_beta_vs_low_vol, 0.0) * 3.0
        + max(small_vs_large, 0.0) * 2.5
        + max(equal_weight_vs_cap, 0.0) * 2.0
        + max(credit_risk_appetite, 0.0) * 3.0
        + sector_participation * 0.18
        + volume_confirmation * 0.08,
        0.0,
        1.0,
    )
    risk_off_score = _clip(
        0.32
        + max(-risk_on_rotation, 0.0) * 4.0
        + max(-high_beta_vs_low_vol, 0.0) * 3.0
        + max(-small_vs_large, 0.0) * 2.5
        + max(-credit_risk_appetite, 0.0) * 3.0
        + max(defensive_vs_cyclical, 0.0) * 3.0
        + max(-sector_participation + 0.5, 0.0) * 0.22,
        0.0,
        1.0,
    )
    crowding_score = _clip(abs(volume_z) / 3.0 * 0.45 + max(relative_volume - 1.25, 0.0) * 0.35, 0.0, 1.0)
    flow_confirmation = _clip(risk_on_score * 0.55 + volume_confirmation * 0.20 + max(credit_risk_appetite, 0.0) * 2.0 + sector_participation * 0.15, 0.0, 1.0)
    flow_conflict = _clip(risk_off_score * 0.58 + max(-credit_risk_appetite, 0.0) * 2.2 + max(defensive_vs_cyclical, 0.0) * 1.8 + max(-sector_participation + 0.45, 0.0) * 0.20, 0.0, 1.0)
    quality = _flow_quality_score(symbol, series_by_symbol)
    status = "proxy" if quality >= 45 else "missing"

    return {
        "symbol": symbol,
        "status": status,
        "is_proxy": True,
        "true_flow_available": False,
        "source": "market_data_proxy",
        "latest_date": _latest_date(target),
        "metrics": {
            "volume_zscore_20d": round(volume_z, 4),
            "etf_relative_volume_20d": round(relative_volume, 4),
            "volume_confirmation_score": round(volume_confirmation, 4),
            "high_beta_vs_low_vol_20d": round(high_beta_vs_low_vol, 6),
            "small_cap_vs_large_cap_20d": round(small_vs_large, 6),
            "equal_weight_vs_cap_weight_20d": round(equal_weight_vs_cap, 6),
            "credit_risk_appetite_20d": round(credit_risk_appetite, 6),
            "risk_on_rotation_20d": round(risk_on_rotation, 6),
            "defensive_vs_cyclical_20d": round(defensive_vs_cyclical, 6),
            "sector_participation_proxy": round(sector_participation, 4),
            "crowding_proxy_score": round(crowding_score, 4),
        },
        "scores": {
            "risk_on_flow_score": round(risk_on_score * 100.0, 2),
            "risk_off_flow_score": round(risk_off_score * 100.0, 2),
            "flow_confirmation_score": round(flow_confirmation * 100.0, 2),
            "flow_conflict_score": round(flow_conflict * 100.0, 2),
            "crowding_proxy_score": round(crowding_score * 100.0, 2),
            "flow_quality_score": round(quality, 2),
        },
        "data_note": "Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed.",
    }


def _summary(symbols: dict[str, Any]) -> dict[str, Any]:
    qualities = [_float((payload.get("scores") or {}).get("flow_quality_score"), 0.0) for payload in symbols.values()]
    confirmations = [_float((payload.get("scores") or {}).get("flow_confirmation_score"), 0.0) for payload in symbols.values()]
    conflicts = [_float((payload.get("scores") or {}).get("flow_conflict_score"), 0.0) for payload in symbols.values()]
    return {
        "flow_available": any(value >= 45 for value in qualities),
        "flow_proxy_only": True,
        "true_flow_available": False,
        "average_flow_quality_score": round(sum(qualities) / len(qualities), 2) if qualities else 0,
        "overall_flow_confirmation_score": round(sum(confirmations) / len(confirmations), 2) if confirmations else 0,
        "overall_flow_conflict_score": round(sum(conflicts) / len(conflicts), 2) if conflicts else 0,
        "flow_symbols": list(symbols),
        "missing_real_flow_feeds": ["ETF fund flow", "prime brokerage positioning", "CFTC positioning", "dealer gamma/option flow"],
        "data_note": "Flow is proxy-only and must be validated against future forecast accuracy.",
    }


def _source_rows(series_by_symbol: dict[str, DownloadedSeries]) -> dict[str, Any]:
    rows: dict[str, Any] = {}
    for symbol in sorted(set(TARGET_SYMBOLS + RISK_ASSETS + DEFENSIVE_ASSETS + SECTOR_SYMBOLS)):
        series = series_by_symbol.get(symbol)
        rows[symbol] = {
            "symbol": symbol,
            "source": getattr(series, "source", "missing") if series else "missing",
            "latest_date": _latest_date(series),
            "row_count": len(getattr(series, "rows", []) or []),
            "real_data": bool(series and getattr(series, "source", "") != "synthetic-fallback" and len(series.rows) > 30),
            "missing_data": not bool(series and len(series.rows) > 30),
        }
    return rows


def _flow_quality_score(symbol: str, series_by_symbol: dict[str, DownloadedSeries]) -> float:
    required = [symbol, "SPY", "QQQ", "IWM", "HYG", "LQD", "TLT", "UUP", "SPHB", "SPLV", "RSP"]
    available = 0
    for name in required:
        series = series_by_symbol.get(name)
        if series and len(series.rows) >= 60 and getattr(series, "source", "") != "synthetic-fallback":
            available += 1
    sector_available = sum(1 for name in SECTOR_SYMBOLS if series_by_symbol.get(name) and len(series_by_symbol[name].rows) >= 60)
    return _clip((available / len(required)) * 72.0 + (sector_available / len(SECTOR_SYMBOLS)) * 28.0, 0.0, 100.0)


def _closes(series: DownloadedSeries | None) -> list[float]:
    if not series:
        return []
    return [float(row.get("close") or 0.0) for row in series.rows if float(row.get("close") or 0.0) > 0.0]


def _volumes(series: DownloadedSeries | None) -> list[float]:
    if not series:
        return []
    values: list[float] = []
    for row in series.rows:
        volume = row.get("volume")
        try:
            parsed = float(volume or 0.0)
        except (TypeError, ValueError):
            parsed = 0.0
        if parsed > 0:
            values.append(parsed)
    return values


def _latest_date(series: DownloadedSeries | None) -> str | None:
    if not series or not series.rows:
        return None
    return str(series.rows[-1].get("date"))[:10]


def _return(values: list[float], window: int) -> float:
    if len(values) <= window or values[-window - 1] == 0:
        return 0.0
    return values[-1] / values[-window - 1] - 1.0


def _relative_return(left: list[float], right: list[float], window: int) -> float:
    return _return(left, window) - _return(right, window)


def _basket_return(series_list: list[list[float]], window: int) -> float:
    returns = [_return(values, window) for values in series_list if len(values) > window]
    return sum(returns) / len(returns) if returns else 0.0


def _relative_volume(values: list[float], window: int) -> float:
    if len(values) < window + 1:
        return 1.0
    recent = values[-1]
    baseline_values = values[-window - 1 : -1]
    baseline = sum(baseline_values) / len(baseline_values) if baseline_values else recent
    return recent / baseline if baseline else 1.0


def _zscore_last(values: list[float], window: int) -> float:
    if len(values) < window + 1:
        return 0.0
    sample = values[-window:]
    mean = sum(sample) / len(sample)
    variance = sum((value - mean) ** 2 for value in sample) / len(sample)
    stdev = math.sqrt(variance)
    return (sample[-1] - mean) / stdev if stdev else 0.0


def _volume_confirmation_score(volume_z: float, relative_volume: float, return_5d: float) -> float:
    directional_volume = 0.55 if return_5d >= 0 else 0.35
    volume_boost = _clip((relative_volume - 0.9) * 0.45 + max(volume_z, 0.0) * 0.08, -0.15, 0.25)
    return _clip(directional_volume + volume_boost, 0.0, 1.0)


def _sector_participation(sectors: dict[str, list[float]]) -> float:
    returns = [_return(values, 20) for values in sectors.values() if len(values) > 20]
    if not returns:
        return 0.0
    return sum(1 for value in returns if value > 0) / len(returns)


def _float(value: Any, default: float = 0.0) -> float:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return default
    return parsed if math.isfinite(parsed) else default


def _clip(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))
