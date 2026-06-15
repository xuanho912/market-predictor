from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
VERSION = "confluence_engine_v1"


def build_confluence_score(
    *,
    market_overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    intelligence_v4: dict[str, Any],
    forecast_price_levels: dict[str, Any],
    price_volume_structure: dict[str, Any],
    breadth_bundle: dict[str, Any] | None = None,
    options_bundle: dict[str, Any] | None = None,
    flow_bundle: dict[str, Any] | None = None,
    news_event_bundle: dict[str, Any] | None = None,
) -> dict[str, Any]:
    symbols = _symbols(market_overview, simulated_paths)
    by_symbol: dict[str, Any] = {}
    for symbol in symbols:
        by_symbol[symbol] = _symbol_confluence(
            symbol=symbol,
            market_overview=market_overview,
            simulated_paths=simulated_paths,
            intelligence_v4=intelligence_v4,
            forecast_price_levels=forecast_price_levels,
            price_volume_structure=price_volume_structure,
            breadth_bundle=breadth_bundle or {},
            options_bundle=options_bundle or {},
            flow_bundle=flow_bundle or {},
            news_event_bundle=news_event_bundle or {},
        )
    confluence_scores = [_num(item.get("confluence_score")) for item in by_symbol.values() if _num(item.get("confluence_score")) is not None]
    strongest = max(by_symbol.items(), key=lambda item: _num(item[1].get("confluence_score"), -1) or -1)[0] if by_symbol else None
    return {
        "version": VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "disclaimer": "Confluence is a forecast-confirmation layer, not a trading signal or execution recommendation.",
        "summary": {
            "average_confluence_score": _round(_mean(confluence_scores)),
            "strongest_confluence_symbol": strongest,
            "strong_confluence_symbols": [
                symbol for symbol, item in by_symbol.items() if item.get("confluence_level") in {"strong", "dominant"}
            ],
            "mixed_or_no_edge_symbols": [
                symbol for symbol, item in by_symbol.items() if item.get("confluence_level") in {"mixed", "weak"}
            ],
        },
        "symbols": by_symbol,
    }


def render_confluence_score_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Confluence Score",
        "",
        "This report explains whether current forecast paths have multi-source confirmation. It is not a trading system.",
        "",
        f"- version: {payload.get('version')}",
        f"- generated_at: {payload.get('generated_at')}",
        f"- strongest_confluence_symbol: {(payload.get('summary') or {}).get('strongest_confluence_symbol')}",
        "",
        "| Symbol | Dominant path | Confluence | Level | Main supports | Main conflicts |",
        "| --- | --- | ---: | --- | --- | --- |",
    ]
    for symbol, item in sorted((payload.get("symbols") or {}).items()):
        supports = ", ".join(evidence.get("source", "") for evidence in (item.get("supporting_evidence") or [])[:4])
        conflicts = ", ".join(evidence.get("source", "") for evidence in (item.get("conflicting_evidence") or [])[:4])
        lines.append(
            f"| {symbol} | {item.get('dominant_path')} | {_fmt_score(item.get('confluence_score'))} | "
            f"{item.get('confluence_level')} | {supports or 'none'} | {conflicts or 'none'} |"
        )
    lines.append("")
    return "\n".join(lines)


def attach_confluence_to_symbols(
    market_overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    confluence_payload: dict[str, Any],
) -> None:
    by_symbol = confluence_payload.get("symbols") or {}
    for container in ((market_overview.get("symbols") or {}), (simulated_paths.get("symbols") or {})):
        for symbol, item in container.items():
            if symbol in by_symbol and isinstance(item, dict):
                item["confluence"] = by_symbol[symbol]


def _symbol_confluence(
    *,
    symbol: str,
    market_overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    intelligence_v4: dict[str, Any],
    forecast_price_levels: dict[str, Any],
    price_volume_structure: dict[str, Any],
    breadth_bundle: dict[str, Any],
    options_bundle: dict[str, Any],
    flow_bundle: dict[str, Any],
    news_event_bundle: dict[str, Any],
) -> dict[str, Any]:
    symbol_payload = _symbol_payload(symbol, market_overview, simulated_paths)
    ranking = symbol_payload.get("scenario_ranking") or {}
    primary = ranking.get("primary") or {}
    primary_scenario = str(primary.get("scenario") or ranking.get("primary_scenario") or "unknown")
    secondary = ranking.get("secondary") or {}
    edge_status = str(symbol_payload.get("market_edge_status") or "NO_EDGE")
    probability_gap = _num(ranking.get("primary_secondary_gap") or ranking.get("probability_gap"), 0.0) or 0.0
    signal_confirmation = symbol_payload.get("signal_confirmation") or {}
    signal_confirmation_score = _score100(
        signal_confirmation.get("signal_confirmation_score")
        or symbol_payload.get("signal_confirmation_score")
        or (intelligence_v4.get("signal_confirmation_by_symbol") or {}).get(symbol, {}).get("signal_confirmation_score")
    )
    model_confidence = _score100((symbol_payload.get("model_confidence") or {}).get("confidence_score"))
    data_completeness = _score100(((intelligence_v4.get("data_quality_report") or {}).get("summary") or {}).get("data_completeness_score"))
    predictors = symbol_payload.get("predictors_v4") or symbol_payload.get("predictors") or {}
    price_volume = (price_volume_structure.get("symbols") or {}).get(symbol, {})
    price_levels = (forecast_price_levels.get("symbols") or {}).get(symbol, {})
    news_impact = ((news_event_bundle.get("symbol_impacts") or news_event_bundle.get("symbol_impact") or {}).get(symbol) or {})

    supporting: list[dict[str, Any]] = []
    conflicting: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []

    _add_signal_evidence(supporting, conflicting, signal_confirmation)
    _add_price_volume_evidence(symbol, primary_scenario, supporting, conflicting, price_volume)
    _add_breadth_evidence(symbol, primary_scenario, supporting, conflicting, missing, symbol_payload, breadth_bundle)
    _add_credit_rates_evidence(symbol, primary_scenario, supporting, conflicting, symbol_payload)
    _add_options_evidence(symbol, primary_scenario, supporting, conflicting, missing, options_bundle)
    _add_flow_evidence(symbol, primary_scenario, supporting, conflicting, missing, flow_bundle)
    _add_news_evidence(symbol, primary_scenario, supporting, conflicting, missing, news_event_bundle, news_impact)
    _add_historical_evidence(symbol, primary_scenario, supporting, conflicting, symbol_payload)

    if data_completeness < 80:
        missing.append({"source": "data_quality", "name": "数据完整度不足", "detail": f"data completeness {data_completeness}/100"})
    if probability_gap < 0.08:
        conflicting.append({"source": "scenario_gap", "name": "主次路径差距小", "score": _round(probability_gap * 100), "detail": "路径分歧较大，不宜给强结论。"})
    else:
        supporting.append({"source": "scenario_gap", "name": "主次路径差距可观察", "score": _round(probability_gap * 100), "detail": f"primary-secondary gap {probability_gap:.1%}"})

    support_score = _weighted_evidence_score(supporting)
    conflict_score = _weighted_evidence_score(conflicting)
    raw_score = (
        signal_confirmation_score * 0.26
        + model_confidence * 0.16
        + data_completeness * 0.12
        + min(100, probability_gap * 260) * 0.12
        + support_score * 0.26
        - conflict_score * 0.20
        + 12
    )
    confluence_score = _clamp_score(raw_score)
    if len(supporting) < 3:
        confluence_score = min(confluence_score, 58)
    if len(conflicting) >= 4 or conflict_score >= 62:
        confluence_score = min(confluence_score, 56)
    if edge_status == "NO_EDGE":
        confluence_score = min(confluence_score, 52)
    if data_completeness < 70:
        confluence_score = min(confluence_score, 55)

    dominant_path = _dominant_path(primary_scenario, predictors, confluence_score, edge_status)
    level = _confluence_level(confluence_score, conflict_score, probability_gap)
    key_conflicts = [item for item in conflicting if _num(item.get("score"), 0) >= 45]
    return {
        "symbol": symbol,
        "version": VERSION,
        "dominant_path": dominant_path,
        "primary_scenario": primary_scenario,
        "primary_label": primary.get("label"),
        "primary_probability": _round(primary.get("probability")),
        "secondary_scenario": secondary.get("scenario"),
        "secondary_probability": _round(secondary.get("probability")),
        "probability_gap": _round(probability_gap),
        "edge_status": edge_status,
        "confluence_score": confluence_score,
        "confluence_level": level,
        "supporting_evidence": sorted(supporting, key=lambda item: _num(item.get("score"), 0) or 0, reverse=True)[:12],
        "conflicting_evidence": sorted(conflicting, key=lambda item: _num(item.get("score"), 0) or 0, reverse=True)[:12],
        "missing_evidence": missing[:10],
        "key_conflict_count": len(key_conflicts),
        "strong_conclusion_allowed": bool(
            confluence_score >= 70
            and signal_confirmation_score >= 65
            and probability_gap >= 0.08
            and data_completeness >= 80
            and len(key_conflicts) <= 2
        ),
        "related_price_levels": _related_levels(price_levels),
        "confluence_summary": _summary(symbol, dominant_path, confluence_score, level, supporting, conflicting, missing),
        "not_trading_advice": "This is forecast confirmation only, not a buy/sell/entry/exit or position-sizing recommendation.",
    }


def _symbols(market_overview: dict[str, Any], simulated_paths: dict[str, Any]) -> list[str]:
    symbols = set(SYMBOLS)
    symbols.update((market_overview.get("symbols") or {}).keys())
    symbols.update((simulated_paths.get("symbols") or {}).keys())
    return sorted(symbols)


def _symbol_payload(symbol: str, market_overview: dict[str, Any], simulated_paths: dict[str, Any]) -> dict[str, Any]:
    payload = {}
    payload.update((market_overview.get("symbols") or {}).get(symbol) or {})
    payload.update((simulated_paths.get("symbols") or {}).get(symbol) or {})
    return payload


def _add_signal_evidence(supporting: list[dict[str, Any]], conflicting: list[dict[str, Any]], signal_confirmation: dict[str, Any]) -> None:
    for item in signal_confirmation.get("supporting_evidence") or []:
        supporting.append({"source": "signal_confirmation", "name": item.get("name"), "score": _score100(item.get("score")), "detail": item.get("detail")})
    for item in signal_confirmation.get("conflicting_evidence") or []:
        conflicting.append({"source": "signal_confirmation", "name": item.get("name"), "score": _score100(item.get("score")), "detail": item.get("detail")})


def _add_price_volume_evidence(
    symbol: str,
    primary_scenario: str,
    supporting: list[dict[str, Any]],
    conflicting: list[dict[str, Any]],
    price_volume: dict[str, Any],
) -> None:
    if not price_volume or price_volume.get("status") == "missing":
        return
    price_score = _score100(price_volume.get("price_structure_score"))
    volume_score = _score100(price_volume.get("volume_confirmation_score"))
    reversal_score = _score100(price_volume.get("reversal_candle_score"))
    breakdown_score = _score100(price_volume.get("breakdown_risk_score"))
    breakout_score = _score100(price_volume.get("breakout_confirmation_score"))
    is_constructive = primary_scenario in {"bounce_path", "expected_path", "analog_average_path"}
    if is_constructive:
        if price_score >= 58:
            supporting.append({"source": "price", "name": "价格结构支持主路径", "score": price_score, "detail": price_volume.get("interpretation")})
        if volume_score >= 55:
            supporting.append({"source": "volume", "name": "成交量确认", "score": volume_score, "detail": "成交量结构支持当前路径。"})
        if reversal_score >= 58:
            supporting.append({"source": "price", "name": "反转/回收K线", "score": reversal_score, "detail": "K线出现反转或回收结构。"})
        if breakdown_score >= 58:
            conflicting.append({"source": "price", "name": "跌破风险", "score": breakdown_score, "detail": "价格结构存在跌破或低收风险。"})
    else:
        if breakdown_score >= 50:
            supporting.append({"source": "price", "name": "下行结构支持风险路径", "score": breakdown_score, "detail": "价格结构更偏风险路径。"})
        if breakout_score >= 58 or reversal_score >= 58:
            conflicting.append({"source": "price", "name": "修复结构冲突", "score": max(breakout_score, reversal_score), "detail": "价格结构对风险路径构成冲突。"})
    if price_score < 45 and is_constructive:
        conflicting.append({"source": "price", "name": "价格结构未确认", "score": 100 - price_score, "detail": f"{symbol} 主路径尚未得到价格结构确认。"})


def _add_breadth_evidence(
    symbol: str,
    primary_scenario: str,
    supporting: list[dict[str, Any]],
    conflicting: list[dict[str, Any]],
    missing: list[dict[str, Any]],
    symbol_payload: dict[str, Any],
    breadth_bundle: dict[str, Any],
) -> None:
    breadth = (((symbol_payload.get("feature_snapshot_v3") or {}).get("breadth")) or {})
    if not breadth:
        breadth = (((breadth_bundle.get("universes") or {}).get(symbol) or {}).get("scores") or {})
    if not breadth:
        missing.append({"source": "breadth", "name": "市场宽度缺失", "detail": "No breadth data available."})
        return
    confirmation = _score100(breadth.get("breadth_confirmation_score_raw") or breadth.get("breadth_confirmation_score"))
    conflict = _score100(breadth.get("breadth_conflict_score_raw") or breadth.get("breadth_conflict_score"))
    improvement = _score100(breadth.get("breadth_improvement_score_raw") or breadth.get("breadth_improvement_score"))
    is_constructive = primary_scenario in {"bounce_path", "expected_path", "analog_average_path"}
    if is_constructive and confirmation >= 55:
        supporting.append({"source": "breadth", "name": "市场内部共振/宽度确认", "score": confirmation, "detail": breadth.get("internal_resonance_reason") or "Breadth supports the current path."})
    if conflict >= 45:
        conflicting.append({"source": "breadth", "name": "宽度冲突", "score": conflict, "detail": "指数路径与内部参与度存在冲突。"})
    if not is_constructive and conflict >= 45:
        supporting.append({"source": "breadth", "name": "宽度恶化支持风险路径", "score": conflict, "detail": "Breadth deterioration supports downside/failed-bounce risk."})
    elif is_constructive and improvement >= 55:
        supporting.append({"source": "breadth", "name": "宽度改善", "score": improvement, "detail": "Breadth improvement supports bounce or repair."})


def _add_credit_rates_evidence(
    symbol: str,
    primary_scenario: str,
    supporting: list[dict[str, Any]],
    conflicting: list[dict[str, Any]],
    symbol_payload: dict[str, Any],
) -> None:
    snapshot = symbol_payload.get("feature_snapshot_v3") or {}
    credit = snapshot.get("credit") or {}
    rates = snapshot.get("rates_liquidity") or {}
    credit_stress = _score100(credit.get("credit_stress_score"))
    credit_stable = _score100(credit.get("credit_stabilization_score"))
    rates_pressure = _score100(rates.get("rates_pressure_score"))
    constructive = primary_scenario in {"bounce_path", "expected_path", "analog_average_path"}
    if constructive and credit_stable >= 55:
        supporting.append({"source": "credit", "name": "信用稳定", "score": credit_stable, "detail": "Credit stress is contained or improving."})
    if credit_stress >= 55:
        (conflicting if constructive else supporting).append({"source": "credit", "name": "信用压力", "score": credit_stress, "detail": "Credit stress raises risk-expansion probability."})
    if rates_pressure >= 70:
        conflicting.append({"source": "rates", "name": "利率压力", "score": rates_pressure, "detail": "Rates pressure is elevated."})


def _add_options_evidence(
    symbol: str,
    primary_scenario: str,
    supporting: list[dict[str, Any]],
    conflicting: list[dict[str, Any]],
    missing: list[dict[str, Any]],
    options_bundle: dict[str, Any],
) -> None:
    options = (options_bundle.get("symbols") or {}).get(symbol) or {}
    if not options:
        missing.append({"source": "options", "name": "期权/波动率结构缺失", "detail": "Options structure data unavailable."})
        return
    option_stress = _score100(options.get("option_stress_score"))
    panic_release = _score100(options.get("panic_release_score"))
    failed_risk = _score100(options.get("failed_bounce_options_risk"))
    constructive = primary_scenario in {"bounce_path", "expected_path", "analog_average_path"}
    if constructive and panic_release >= 55:
        supporting.append({"source": "options", "name": "波动率修复/恐慌释放", "score": panic_release, "detail": options.get("options_reason") or "Volatility structure supports repair."})
    if option_stress >= 55 or failed_risk >= 55:
        (conflicting if constructive else supporting).append({"source": "options", "name": "期权/尾部风险压力", "score": max(option_stress, failed_risk), "detail": options.get("options_risk_note") or "Options stress raises failed-bounce risk."})
    if not options.get("put_call_ratio"):
        missing.append({"source": "options", "name": "put/call 缺失", "detail": "Put/call ratio is not connected."})
    if not options.get("gamma_exposure"):
        missing.append({"source": "options", "name": "gamma 缺失", "detail": "Dealer gamma exposure is not connected."})


def _add_flow_evidence(
    symbol: str,
    primary_scenario: str,
    supporting: list[dict[str, Any]],
    conflicting: list[dict[str, Any]],
    missing: list[dict[str, Any]],
    flow_bundle: dict[str, Any],
) -> None:
    flow = (flow_bundle.get("symbols") or {}).get(symbol) or {}
    scores = flow.get("scores") or flow
    if not scores:
        missing.append({"source": "flow", "name": "flow/positioning 缺失", "detail": "No flow proxy available."})
        return
    confirmation = _score100(scores.get("flow_confirmation_score") or scores.get("confirmation"))
    conflict = _score100(scores.get("flow_conflict_score") or scores.get("conflict"))
    risk_on = _score100(scores.get("risk_on_flow_score"))
    risk_off = _score100(scores.get("risk_off_flow_score"))
    constructive = primary_scenario in {"bounce_path", "expected_path", "analog_average_path"}
    if constructive and max(confirmation, risk_on) >= 55:
        supporting.append({"source": "flow", "name": "risk-on flow proxy", "score": max(confirmation, risk_on), "detail": "Proxy flow/positioning supports risk appetite."})
    if max(conflict, risk_off) >= 55:
        (conflicting if constructive else supporting).append({"source": "flow", "name": "risk-off flow proxy", "score": max(conflict, risk_off), "detail": "Proxy flow/positioning points to risk-off pressure."})
    if flow.get("proxy_only", True):
        missing.append({"source": "flow", "name": "真实资金流缺失", "detail": "Current flow evidence is proxy-only, not true fund flow."})


def _add_news_evidence(
    symbol: str,
    primary_scenario: str,
    supporting: list[dict[str, Any]],
    conflicting: list[dict[str, Any]],
    missing: list[dict[str, Any]],
    news_event_bundle: dict[str, Any],
    impact: dict[str, Any],
) -> None:
    status = str(news_event_bundle.get("status") or "missing")
    if status in {"missing", "provider_failed"}:
        missing.append({"source": "news", "name": "新闻事件层缺失", "detail": f"news_event_status={status}"})
        return
    confirmation = ((news_event_bundle.get("price_reaction_confirmation") or {}).get("confirmation_score"))
    score = _score100(confirmation)
    if impact.get("news_supports_primary_scenario"):
        supporting.append({"source": "news", "name": "新闻事件支持主路径", "score": score, "detail": impact.get("explanation") or "News/event layer supports primary scenario."})
    if impact.get("news_conflicts_primary_scenario"):
        conflicting.append({"source": "news", "name": "新闻事件与主路径冲突", "score": score, "detail": impact.get("explanation") or "News/event layer conflicts with primary scenario."})
    if not ((news_event_bundle.get("price_reaction_confirmation") or {}).get("price_reaction_confirmed")) and status not in {"no_major_event"}:
        conflicting.append({"source": "news", "name": "新闻未获价格确认", "score": max(30, 100 - score), "detail": "News/event direction is not sufficiently confirmed by market reaction."})


def _add_historical_evidence(
    symbol: str,
    primary_scenario: str,
    supporting: list[dict[str, Any]],
    conflicting: list[dict[str, Any]],
    symbol_payload: dict[str, Any],
) -> None:
    historical = symbol_payload.get("historical_support_by_horizon") or {}
    mid_support = [str((historical.get(horizon) or {}).get("support") or historical.get(horizon) or "") for horizon in ("20d", "60d")]
    short_support = [str((historical.get(horizon) or {}).get("support") or historical.get(horizon) or "") for horizon in ("3d", "5d")]
    if any("supportive" in item for item in mid_support):
        supporting.append({"source": "historical_analog", "name": "中期历史相似支持", "score": 65, "detail": "20d/60d historical analog support is constructive."})
    if any("weak" in item for item in short_support):
        conflicting.append({"source": "historical_analog", "name": "短线历史相似冲突", "score": 45, "detail": "3d/5d analog support is weak or conflicting."})


def _dominant_path(primary_scenario: str, predictors: dict[str, Any], confluence_score: int, edge_status: str) -> str:
    if edge_status == "NO_EDGE" or confluence_score < 45:
        return "no_edge"
    if primary_scenario == "bounce_path":
        trend = _score100((predictors.get("trend_reversal") or {}).get("probability") or (predictors.get("trend_reversal") or {}).get("trend_reversal_probability"))
        bounce = _score100((predictors.get("bounce") or {}).get("probability") or (predictors.get("bounce") or {}).get("bounce_probability"))
        return "trend_repair" if trend >= max(72, bounce + 8) else "bounce"
    if primary_scenario == "bearish_path":
        risk = _score100((predictors.get("risk_expansion") or {}).get("probability") or (predictors.get("risk_expansion") or {}).get("risk_expansion_probability"))
        return "downside" if risk >= 65 else "failed_bounce"
    if primary_scenario == "analog_average_path":
        return "trend_repair" if confluence_score >= 65 else "no_edge"
    return "no_edge"


def _confluence_level(score: int, conflict_score: float, probability_gap: float) -> str:
    if score >= 78 and conflict_score < 45 and probability_gap >= 0.12:
        return "dominant"
    if score >= 68 and conflict_score < 55:
        return "strong"
    if score >= 58:
        return "moderate"
    if score >= 45:
        return "mixed"
    return "weak"


def _weighted_evidence_score(items: list[dict[str, Any]]) -> float:
    if not items:
        return 0.0
    weights = {
        "signal_confirmation": 1.1,
        "price": 1.0,
        "volume": 0.9,
        "breadth": 1.15,
        "credit": 1.1,
        "options": 1.05,
        "flow": 0.95,
        "news": 1.0,
        "historical_analog": 0.85,
        "scenario_gap": 0.85,
    }
    total = 0.0
    denom = 0.0
    for item in items:
        weight = weights.get(str(item.get("source")), 0.8)
        total += (_num(item.get("score"), 45) or 45) * weight
        denom += weight
    return total / denom if denom else 0.0


def _related_levels(price_levels: dict[str, Any]) -> dict[str, Any]:
    levels = price_levels.get("trigger_levels") or price_levels.get("path_trigger_levels") or {}
    names = (
        "primary_confirmation_level",
        "primary_invalidation_level",
        "risk_scenario_activation_level",
        "trend_reversal_confirmation_level",
    )
    return {name: levels.get(name) for name in names if levels.get(name)}


def _summary(
    symbol: str,
    dominant_path: str,
    score: int,
    level: str,
    supporting: list[dict[str, Any]],
    conflicting: list[dict[str, Any]],
    missing: list[dict[str, Any]],
) -> str:
    support_names = "、".join(str(item.get("source")) for item in supporting[:4]) or "暂无强支持"
    conflict_names = "、".join(str(item.get("source")) for item in conflicting[:3]) or "暂无主要冲突"
    missing_note = "；仍缺 " + "、".join(str(item.get("source")) for item in missing[:3]) if missing else ""
    return f"{symbol} 当前多源共振为 {level}（{score}/100），主导路径为 {dominant_path}。支持来自 {support_names}；冲突来自 {conflict_names}{missing_note}。"


def _score100(value: Any) -> int:
    parsed = _num(value)
    if parsed is None:
        return 0
    if 0 <= parsed <= 1:
        parsed *= 100
    return _clamp_score(parsed)


def _num(value: Any, default: float | None = None) -> float | None:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return default
    return parsed if math.isfinite(parsed) else default


def _mean(values: list[float | None]) -> float | None:
    clean = [float(value) for value in values if value is not None and math.isfinite(float(value))]
    return sum(clean) / len(clean) if clean else None


def _round(value: Any, digits: int = 4) -> float | None:
    parsed = _num(value)
    return round(parsed, digits) if parsed is not None else None


def _clamp_score(value: float) -> int:
    return int(round(max(0.0, min(100.0, value))))


def _fmt_score(value: Any) -> str:
    parsed = _num(value)
    return "NA" if parsed is None else f"{parsed:.0f}/100"


def main() -> int:
    public = PROJECT_ROOT / "frontend" / "public"
    dashboard = json.loads((public / "prediction-dashboard.json").read_text(encoding="utf-8"))
    price_levels = _read_optional(public / "forecast-price-levels.json", dashboard.get("forecast_price_levels") or {})
    price_volume = _read_optional(public / "price-volume-structure.json", {})
    payload = build_confluence_score(
        market_overview=dashboard.get("overview") or {},
        simulated_paths=dashboard.get("simulated_paths") or {},
        intelligence_v4=dashboard.get("market_intelligence_v4") or {},
        forecast_price_levels=price_levels,
        price_volume_structure=price_volume,
        breadth_bundle=dashboard.get("breadth_status") or {},
        options_bundle=dashboard.get("options_status") or {},
        flow_bundle=dashboard.get("flow_positioning_status") or dashboard.get("flow_status") or {},
        news_event_bundle=dashboard.get("news_event_status") or {},
    )
    public_path = public / "confluence-score.json"
    output_path = PROJECT_ROOT / "outputs" / "confluence_score.md"
    public_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    output_path.write_text(render_confluence_score_markdown(payload), encoding="utf-8")
    print("wrote frontend/public/confluence-score.json")
    print("wrote outputs/confluence_score.md")
    return 0


def _read_optional(path: Path, fallback: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return fallback
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return fallback


if __name__ == "__main__":
    raise SystemExit(main())
