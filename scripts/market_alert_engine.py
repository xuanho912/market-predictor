from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
VERSION = "market_alert_engine_v1"


ALERT_TYPES = (
    "Risk Expansion Alert",
    "Failed Bounce Alert",
    "Bounce Setup Alert",
    "Bottoming Setup Alert",
    "Trend Repair Alert",
)


def build_market_alerts(
    *,
    market_overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    forecast_price_levels: dict[str, Any],
    price_volume_structure: dict[str, Any],
    confluence_score: dict[str, Any],
    news_event_bundle: dict[str, Any] | None = None,
) -> dict[str, Any]:
    by_symbol: dict[str, Any] = {}
    flat_alerts: list[dict[str, Any]] = []
    for symbol in _symbols(market_overview, simulated_paths):
        symbol_alerts = _alerts_for_symbol(
            symbol=symbol,
            market_overview=market_overview,
            simulated_paths=simulated_paths,
            forecast_price_levels=forecast_price_levels,
            price_volume_structure=price_volume_structure,
            confluence_score=confluence_score,
            news_event_bundle=news_event_bundle or {},
        )
        by_symbol[symbol] = symbol_alerts
        flat_alerts.extend(symbol_alerts.get("alerts", []))

    ranked = sorted(flat_alerts, key=lambda item: (_level_rank(item.get("alert_level")), _num(item.get("alert_score"), 0) or 0), reverse=True)
    strongest = ranked[0] if ranked else None
    return {
        "version": VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "disclaimer": "Market alerts are forecast warnings and scenario-confirmation notes only. They are not trading signals or buy/sell/entry/exit guidance.",
        "summary": {
            "strongest_alert": strongest,
            "has_high_alert": bool(strongest and strongest.get("alert_level") in {"HIGH_CONVICTION", "EXTREME"}),
            "alert_count_by_level": _count_by_level(flat_alerts),
            "alert_count_by_type": _count_by_type(flat_alerts),
            "top_alerts": ranked[:8],
        },
        "symbols": by_symbol,
    }


def render_market_alerts_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Market Alerts",
        "",
        "These alerts are forecast-validation and scenario-confirmation warnings only. They are not trading recommendations.",
        "",
        f"- version: {payload.get('version')}",
        f"- generated_at: {payload.get('generated_at')}",
        "",
        "| Alert | Level | Score | Symbols | Top evidence | Validation |",
        "| --- | --- | ---: | --- | --- | --- |",
    ]
    for item in (payload.get("summary") or {}).get("top_alerts") or []:
        evidence = item.get("supporting_evidence") or []
        top = evidence[0].get("name") if evidence else "none"
        lines.append(
            f"| {item.get('alert_type')} | {item.get('alert_level')} | {_fmt_score(item.get('alert_score'))} | "
            f"{'/'.join(item.get('affected_symbols') or [])} | {top} | {item.get('validation_status')} |"
        )
    lines.append("")
    return "\n".join(lines)


def attach_alerts_to_symbols(
    market_overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    alerts_payload: dict[str, Any],
) -> None:
    by_symbol = alerts_payload.get("symbols") or {}
    for container in ((market_overview.get("symbols") or {}), (simulated_paths.get("symbols") or {})):
        for symbol, item in container.items():
            if symbol in by_symbol and isinstance(item, dict):
                item["market_alerts"] = by_symbol[symbol]


def _alerts_for_symbol(
    *,
    symbol: str,
    market_overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    forecast_price_levels: dict[str, Any],
    price_volume_structure: dict[str, Any],
    confluence_score: dict[str, Any],
    news_event_bundle: dict[str, Any],
) -> dict[str, Any]:
    payload = _symbol_payload(symbol, market_overview, simulated_paths)
    confluence = (confluence_score.get("symbols") or {}).get(symbol, {})
    price_volume = (price_volume_structure.get("symbols") or {}).get(symbol, {})
    price_levels = (forecast_price_levels.get("symbols") or {}).get(symbol, {})
    news_impact = ((news_event_bundle.get("symbol_impacts") or news_event_bundle.get("symbol_impact") or {}).get(symbol) or {})
    alerts = [
        _risk_expansion_alert(symbol, payload, confluence, price_volume, price_levels, news_impact),
        _failed_bounce_alert(symbol, payload, confluence, price_volume, price_levels, news_impact),
        _bounce_setup_alert(symbol, payload, confluence, price_volume, price_levels, news_impact),
        _bottoming_setup_alert(symbol, payload, confluence, price_volume, price_levels, news_impact),
        _trend_repair_alert(symbol, payload, confluence, price_volume, price_levels, news_impact),
    ]
    ranked = sorted(alerts, key=lambda item: (_level_rank(item.get("alert_level")), _num(item.get("alert_score"), 0) or 0), reverse=True)
    return {
        "symbol": symbol,
        "version": VERSION,
        "strongest_alert": ranked[0] if ranked else None,
        "alerts": ranked,
        "top_required_confirmation": ranked[0].get("required_confirmation", []) if ranked else [],
        "top_invalidation_conditions": ranked[0].get("invalidation_conditions", []) if ranked else [],
    }


def _risk_expansion_alert(symbol: str, payload: dict[str, Any], confluence: dict[str, Any], pv: dict[str, Any], levels: dict[str, Any], news: dict[str, Any]) -> dict[str, Any]:
    predictors = payload.get("predictors_v4") or payload.get("predictors") or {}
    snapshot = payload.get("feature_snapshot_v3") or {}
    options = snapshot.get("volatility_options") or {}
    credit = snapshot.get("credit") or {}
    breadth = snapshot.get("breadth") or {}
    flow = snapshot.get("flow_positioning_proxy") or {}
    supporting: list[dict[str, Any]] = []
    conflicting: list[dict[str, Any]] = []
    risk_expansion = _predictor_score(predictors, "risk_expansion", "risk_expansion_probability")
    downside = _score100(payload.get("downside_continuation_probability"))
    if risk_expansion >= 45:
        supporting.append(_ev("risk_expansion_predictor", "风险扩散预测器升高", risk_expansion))
    if downside >= 55:
        supporting.append(_ev("downside_predictor", "下跌延续概率升高", downside))
    if _score100(options.get("tail_risk_score")) >= 55 or _score100(options.get("option_stress_score")) >= 55:
        supporting.append(_ev("options", "尾部/波动率压力升高", max(_score100(options.get("tail_risk_score")), _score100(options.get("option_stress_score")))))
    if _score100(credit.get("credit_stress_score")) >= 45:
        supporting.append(_ev("credit", "信用压力升高", _score100(credit.get("credit_stress_score"))))
    if _score100(breadth.get("breadth_conflict_score_raw") or breadth.get("breadth_conflict_score")) >= 45:
        supporting.append(_ev("breadth", "市场宽度恶化或冲突", _score100(breadth.get("breadth_conflict_score_raw") or breadth.get("breadth_conflict_score"))))
    if _score100(flow.get("risk_off_flow_score")) >= 55:
        supporting.append(_ev("flow", "risk-off flow proxy 增强", _score100(flow.get("risk_off_flow_score"))))
    if _score100(pv.get("breakdown_risk_score")) >= 55:
        supporting.append(_ev("price_volume", "价格/成交量跌破风险", _score100(pv.get("breakdown_risk_score"))))
    if news.get("news_conflicts_primary_scenario"):
        supporting.append(_ev("news", "新闻事件偏风险路径", 60, news.get("explanation")))
    if _score100(credit.get("credit_stabilization_score")) >= 65:
        conflicting.append(_ev("credit", "信用仍稳定", _score100(credit.get("credit_stabilization_score"))))
    if _score100(breadth.get("breadth_confirmation_score_raw") or breadth.get("breadth_confirmation_score")) >= 65:
        conflicting.append(_ev("breadth", "宽度仍有确认", _score100(breadth.get("breadth_confirmation_score_raw") or breadth.get("breadth_confirmation_score"))))
    score = _alert_score(22, supporting, conflicting, confluence)
    return _alert(
        alert_type="Risk Expansion Alert",
        symbol=symbol,
        score=score,
        supporting=supporting,
        conflicting=conflicting,
        required_confirmation=["VIX/VVIX/SKEW 继续上升", "HYG/LQD 明显转弱", f"{symbol} 跌破近期低点或风险路径接管价"],
        invalidation=["VIX 回落且信用稳定", "市场宽度重新改善", "价格重新站回主路径确认价"],
        levels=levels,
        confidence=_confidence(score, supporting, conflicting),
    )


def _failed_bounce_alert(symbol: str, payload: dict[str, Any], confluence: dict[str, Any], pv: dict[str, Any], levels: dict[str, Any], news: dict[str, Any]) -> dict[str, Any]:
    predictors = payload.get("predictors_v4") or payload.get("predictors") or {}
    snapshot = payload.get("feature_snapshot_v3") or {}
    breadth = snapshot.get("breadth") or {}
    flow = snapshot.get("flow_positioning_proxy") or {}
    options = snapshot.get("volatility_options") or {}
    supporting: list[dict[str, Any]] = []
    conflicting: list[dict[str, Any]] = []
    failed = max(
        _predictor_score(predictors, "downside_continuation", "downside_continuation_probability"),
        _score100(payload.get("downside_continuation_probability")),
    )
    if failed >= 45:
        supporting.append(_ev("downside_predictor", "下跌延续/失败反抽风险偏高", failed))
    if _score100(pv.get("breakdown_risk_score")) >= 55:
        supporting.append(_ev("price_volume", "K线结构存在失败反抽风险", _score100(pv.get("breakdown_risk_score"))))
    if _score100(breadth.get("breadth_conflict_score_raw") or breadth.get("breadth_conflict_score")) >= 45:
        supporting.append(_ev("breadth", "反抽缺少内部参与确认", _score100(breadth.get("breadth_conflict_score_raw") or breadth.get("breadth_conflict_score"))))
    if _score100(flow.get("flow_conflict_score_raw") or flow.get("flow_conflict_score")) >= 45:
        supporting.append(_ev("flow", "flow proxy 与反抽路径冲突", _score100(flow.get("flow_conflict_score_raw") or flow.get("flow_conflict_score"))))
    if _score100(options.get("failed_bounce_options_risk")) >= 45:
        supporting.append(_ev("options", "波动率结构提示失败反抽风险", _score100(options.get("failed_bounce_options_risk"))))
    if news.get("news_conflicts_primary_scenario"):
        supporting.append(_ev("news", "新闻事件削弱主路径", 55, news.get("explanation")))
    if _score100(breadth.get("breadth_confirmation_score_raw") or breadth.get("breadth_confirmation_score")) >= 70:
        conflicting.append(_ev("breadth", "内部共振仍支持反抽", _score100(breadth.get("breadth_confirmation_score_raw") or breadth.get("breadth_confirmation_score"))))
    if _score100(options.get("panic_release_score")) >= 65:
        conflicting.append(_ev("options", "恐慌释放支持修复", _score100(options.get("panic_release_score"))))
    score = _alert_score(24, supporting, conflicting, confluence)
    return _alert(
        alert_type="Failed Bounce Alert",
        symbol=symbol,
        score=score,
        supporting=supporting,
        conflicting=conflicting,
        required_confirmation=["无法站上主路径确认价", "VIX 重新上升", "宽度/信用/flow 不再确认"],
        invalidation=["价格站上主路径确认价且成交量扩张", "宽度确认恢复", "HYG/LQD 稳定"],
        levels=levels,
        confidence=_confidence(score, supporting, conflicting),
    )


def _bounce_setup_alert(symbol: str, payload: dict[str, Any], confluence: dict[str, Any], pv: dict[str, Any], levels: dict[str, Any], news: dict[str, Any]) -> dict[str, Any]:
    snapshot = payload.get("feature_snapshot_v3") or {}
    price = snapshot.get("price") or {}
    options = snapshot.get("volatility_options") or {}
    credit = snapshot.get("credit") or {}
    breadth = snapshot.get("breadth") or {}
    flow = snapshot.get("flow_positioning_proxy") or {}
    supporting: list[dict[str, Any]] = []
    conflicting: list[dict[str, Any]] = []
    bounce = _score100(payload.get("bounce_probability"))
    if bounce >= 55:
        supporting.append(_ev("bounce_probability", "反抽概率偏高", bounce))
    if _num(price.get("rsi_14")) is not None and (_num(price.get("rsi_14")) or 50) <= 45:
        supporting.append(_ev("price", "市场偏超卖", int(100 - (_num(price.get("rsi_14")) or 50))))
    if _score100(options.get("panic_release_score")) >= 55:
        supporting.append(_ev("options", "VIX/波动率结构显示恐慌释放", _score100(options.get("panic_release_score"))))
    if _score100(credit.get("credit_stabilization_score")) >= 60:
        supporting.append(_ev("credit", "信用压力未继续恶化", _score100(credit.get("credit_stabilization_score"))))
    if _score100(breadth.get("breadth_confirmation_score_raw") or breadth.get("breadth_confirmation_score")) >= 60:
        supporting.append(_ev("breadth", "宽度改善支持反抽", _score100(breadth.get("breadth_confirmation_score_raw") or breadth.get("breadth_confirmation_score"))))
    if _score100(flow.get("risk_on_flow_score")) >= 60:
        supporting.append(_ev("flow", "risk-on flow proxy 改善", _score100(flow.get("risk_on_flow_score"))))
    if _score100(pv.get("reversal_candle_score")) >= 55 or _score100(pv.get("breakout_confirmation_score")) >= 55:
        supporting.append(_ev("price_volume", "K线/成交量支持反抽确认", max(_score100(pv.get("reversal_candle_score")), _score100(pv.get("breakout_confirmation_score")))))
    if news.get("news_supports_primary_scenario"):
        supporting.append(_ev("news", "新闻事件支持反抽路径", 60, news.get("explanation")))
    if _score100(pv.get("breakdown_risk_score")) >= 60:
        conflicting.append(_ev("price_volume", "价格结构仍有跌破风险", _score100(pv.get("breakdown_risk_score"))))
    if _score100(breadth.get("breadth_conflict_score_raw") or breadth.get("breadth_conflict_score")) >= 50:
        conflicting.append(_ev("breadth", "宽度冲突削弱反抽", _score100(breadth.get("breadth_conflict_score_raw") or breadth.get("breadth_conflict_score"))))
    score = _alert_score(26, supporting, conflicting, confluence)
    return _alert(
        alert_type="Bounce Setup Alert",
        symbol=symbol,
        score=score,
        supporting=supporting,
        conflicting=conflicting,
        required_confirmation=["价格站上主路径确认价", "成交量放大且收盘靠近高位", "VIX 继续回落，HYG/LQD 保持稳定"],
        invalidation=["跌破主路径失效价", "VIX 重新上升", "宽度确认转弱"],
        levels=levels,
        confidence=_confidence(score, supporting, conflicting),
    )


def _bottoming_setup_alert(symbol: str, payload: dict[str, Any], confluence: dict[str, Any], pv: dict[str, Any], levels: dict[str, Any], news: dict[str, Any]) -> dict[str, Any]:
    snapshot = payload.get("feature_snapshot_v3") or {}
    price = snapshot.get("price") or {}
    options = snapshot.get("volatility_options") or {}
    credit = snapshot.get("credit") or {}
    breadth = snapshot.get("breadth") or {}
    supporting: list[dict[str, Any]] = []
    conflicting: list[dict[str, Any]] = []
    rsi = _num(price.get("rsi_14"), 50) or 50
    drawdown = abs(_num(price.get("drawdown_depth"), 0) or 0)
    if rsi <= 42 or drawdown >= 0.06:
        supporting.append(_ev("price", "超卖/回撤释放", min(100, int((50 - min(rsi, 50)) * 2 + drawdown * 500))))
    if _score100(options.get("panic_release_score")) >= 60:
        supporting.append(_ev("options", "恐慌释放", _score100(options.get("panic_release_score"))))
    if _score100(credit.get("credit_stabilization_score")) >= 60:
        supporting.append(_ev("credit", "信用压力停止恶化", _score100(credit.get("credit_stabilization_score"))))
    if _score100(breadth.get("breadth_improvement_score_raw") or breadth.get("breadth_improvement_score")) >= 60:
        supporting.append(_ev("breadth", "内部宽度改善", _score100(breadth.get("breadth_improvement_score_raw") or breadth.get("breadth_improvement_score"))))
    if _score100(pv.get("reversal_candle_score")) >= 60:
        supporting.append(_ev("price_volume", "反转K线/长下影", _score100(pv.get("reversal_candle_score"))))
    if news.get("news_conflicts_primary_scenario"):
        conflicting.append(_ev("news", "新闻仍偏风险", 55, news.get("explanation")))
    if _score100(credit.get("credit_stress_score")) >= 50:
        conflicting.append(_ev("credit", "信用压力仍高", _score100(credit.get("credit_stress_score"))))
    score = _alert_score(18, supporting, conflicting, confluence)
    return _alert(
        alert_type="Bottoming Setup Alert",
        symbol=symbol,
        score=score,
        supporting=supporting,
        conflicting=conflicting,
        required_confirmation=["坏消息不再打出新低", "宽度继续改善", "价格收复短期关键位"],
        invalidation=["信用重新恶化", "跌破风险路径接管价", "VIX/VVIX 再度上行"],
        levels=levels,
        confidence=_confidence(score, supporting, conflicting),
    )


def _trend_repair_alert(symbol: str, payload: dict[str, Any], confluence: dict[str, Any], pv: dict[str, Any], levels: dict[str, Any], news: dict[str, Any]) -> dict[str, Any]:
    snapshot = payload.get("feature_snapshot_v3") or {}
    breadth = snapshot.get("breadth") or {}
    credit = snapshot.get("credit") or {}
    flow = snapshot.get("flow_positioning_proxy") or {}
    options = snapshot.get("volatility_options") or {}
    supporting: list[dict[str, Any]] = []
    conflicting: list[dict[str, Any]] = []
    trend = _score100(payload.get("trend_reversal_probability"))
    if trend >= 55:
        supporting.append(_ev("trend_reversal_probability", "趋势修复概率偏高", trend))
    if _score100(pv.get("breakout_confirmation_score")) >= 55:
        supporting.append(_ev("price_volume", "突破/收复结构确认", _score100(pv.get("breakout_confirmation_score"))))
    if _score100(breadth.get("breadth_confirmation_score_raw") or breadth.get("breadth_confirmation_score")) >= 65:
        supporting.append(_ev("breadth", "50d/200d 宽度与内部参与修复", _score100(breadth.get("breadth_confirmation_score_raw") or breadth.get("breadth_confirmation_score"))))
    if _score100(credit.get("credit_stabilization_score")) >= 60:
        supporting.append(_ev("credit", "信用稳定支持修复", _score100(credit.get("credit_stabilization_score"))))
    if _score100(options.get("volatility_reversal_score")) >= 55 or _score100(options.get("panic_release_score")) >= 55:
        supporting.append(_ev("options", "波动率结构修复", max(_score100(options.get("volatility_reversal_score")), _score100(options.get("panic_release_score")))))
    if _score100(flow.get("risk_on_flow_score")) >= 60:
        supporting.append(_ev("flow", "risk-on rotation 扩散", _score100(flow.get("risk_on_flow_score"))))
    gap = _num((payload.get("scenario_ranking") or {}).get("primary_secondary_gap"), 0) or 0
    if gap >= 0.12:
        supporting.append(_ev("scenario_ranking", "主次路径差距扩大", min(100, int(gap * 300))))
    if _score100(pv.get("breakdown_risk_score")) >= 55:
        conflicting.append(_ev("price_volume", "跌破风险仍在", _score100(pv.get("breakdown_risk_score"))))
    if _score100(breadth.get("breadth_conflict_score_raw") or breadth.get("breadth_conflict_score")) >= 50:
        conflicting.append(_ev("breadth", "宽度冲突", _score100(breadth.get("breadth_conflict_score_raw") or breadth.get("breadth_conflict_score"))))
    score = _alert_score(20, supporting, conflicting, confluence)
    return _alert(
        alert_type="Trend Repair Alert",
        symbol=symbol,
        score=score,
        supporting=supporting,
        conflicting=conflicting,
        required_confirmation=["价格站上趋势修复确认价", "50d/200d 宽度继续改善", "主路径概率相对次路径继续拉开"],
        invalidation=["回落跌破主路径确认价", "宽度和信用确认消失", "VIX 重新上行"],
        levels=levels,
        confidence=_confidence(score, supporting, conflicting),
    )


def _alert(
    *,
    alert_type: str,
    symbol: str,
    score: int,
    supporting: list[dict[str, Any]],
    conflicting: list[dict[str, Any]],
    required_confirmation: list[str],
    invalidation: list[str],
    levels: dict[str, Any],
    confidence: str,
) -> dict[str, Any]:
    level = _alert_level(score, supporting, conflicting)
    return {
        "alert_type": alert_type,
        "alert_level": level,
        "alert_score": score,
        "affected_symbols": [symbol],
        "supporting_evidence": sorted(supporting, key=lambda item: _num(item.get("score"), 0) or 0, reverse=True)[:8],
        "conflicting_evidence": sorted(conflicting, key=lambda item: _num(item.get("score"), 0) or 0, reverse=True)[:8],
        "required_confirmation": required_confirmation,
        "invalidation_conditions": invalidation,
        "related_price_levels": _related_price_levels(levels),
        "confidence": confidence,
        "validation_status": "not_yet_forward_validated",
        "not_trading_advice": "Forecast alert only; not a trade signal, buy/sell instruction, or position recommendation.",
    }


def _alert_score(base: float, supporting: list[dict[str, Any]], conflicting: list[dict[str, Any]], confluence: dict[str, Any]) -> int:
    support = _evidence_strength(supporting)
    conflict = _evidence_strength(conflicting)
    confluence_score = _num(confluence.get("confluence_score"), 50) or 50
    score = base + support * 0.58 + confluence_score * 0.18 - conflict * 0.36
    if len(supporting) < 3:
        score = min(score, 58)
    if len(conflicting) >= 3:
        score = min(score, 64)
    return _clamp_score(score)


def _alert_level(score: int, supporting: list[dict[str, Any]], conflicting: list[dict[str, Any]]) -> str:
    source_count = len({str(item.get("source")) for item in supporting})
    conflict_count = len([item for item in conflicting if (_num(item.get("score"), 0) or 0) >= 45])
    if source_count < 3:
        return "WATCH" if score >= 35 else "NO_ALERT"
    if score >= 85 and source_count >= 5 and conflict_count <= 1:
        return "EXTREME"
    if score >= 72 and source_count >= 4 and conflict_count <= 2:
        return "HIGH_CONVICTION"
    if score >= 55:
        return "WARNING"
    if score >= 35:
        return "WATCH"
    return "NO_ALERT"


def _confidence(score: int, supporting: list[dict[str, Any]], conflicting: list[dict[str, Any]]) -> str:
    if score >= 72 and len(supporting) >= 4 and len(conflicting) <= 2:
        return "high"
    if score >= 50 and len(supporting) >= 3:
        return "medium"
    return "low"


def _related_price_levels(levels: dict[str, Any]) -> dict[str, Any]:
    trigger = levels.get("trigger_levels") or levels.get("path_trigger_levels") or {}
    return {
        key: trigger.get(key)
        for key in (
            "primary_confirmation_level",
            "primary_invalidation_level",
            "risk_scenario_activation_level",
            "trend_reversal_confirmation_level",
            "bounce_target_zone",
            "failed_bounce_warning_zone",
        )
        if trigger.get(key) is not None
    }


def _symbol_payload(symbol: str, market_overview: dict[str, Any], simulated_paths: dict[str, Any]) -> dict[str, Any]:
    payload = {}
    payload.update((market_overview.get("symbols") or {}).get(symbol) or {})
    payload.update((simulated_paths.get("symbols") or {}).get(symbol) or {})
    return payload


def _symbols(market_overview: dict[str, Any], simulated_paths: dict[str, Any]) -> list[str]:
    symbols = set(SYMBOLS)
    symbols.update((market_overview.get("symbols") or {}).keys())
    symbols.update((simulated_paths.get("symbols") or {}).keys())
    return sorted(symbols)


def _predictor_score(predictors: dict[str, Any], key: str, probability_key: str) -> int:
    predictor = predictors.get(key) or predictors.get(key.replace("_", "-")) or {}
    return _score100(predictor.get("probability") or predictor.get(probability_key))


def _ev(source: str, name: str, score: Any, detail: Any = None) -> dict[str, Any]:
    return {"source": source, "name": name, "score": _score100(score), "detail": detail or name}


def _evidence_strength(items: list[dict[str, Any]]) -> float:
    if not items:
        return 0.0
    return sum(_num(item.get("score"), 45) or 45 for item in items) / len(items)


def _count_by_level(alerts: list[dict[str, Any]]) -> dict[str, int]:
    return {level: sum(1 for alert in alerts if alert.get("alert_level") == level) for level in ("NO_ALERT", "WATCH", "WARNING", "HIGH_CONVICTION", "EXTREME")}


def _count_by_type(alerts: list[dict[str, Any]]) -> dict[str, int]:
    return {alert_type: sum(1 for alert in alerts if alert.get("alert_type") == alert_type) for alert_type in ALERT_TYPES}


def _level_rank(level: Any) -> int:
    return {"NO_ALERT": 0, "WATCH": 1, "WARNING": 2, "HIGH_CONVICTION": 3, "EXTREME": 4}.get(str(level), 0)


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


def _clamp_score(value: float) -> int:
    return int(round(max(0.0, min(100.0, value))))


def _fmt_score(value: Any) -> str:
    parsed = _num(value)
    return "NA" if parsed is None else f"{parsed:.0f}/100"


def main() -> int:
    public = PROJECT_ROOT / "frontend" / "public"
    dashboard = json.loads((public / "prediction-dashboard.json").read_text(encoding="utf-8"))
    payload = build_market_alerts(
        market_overview=dashboard.get("overview") or {},
        simulated_paths=dashboard.get("simulated_paths") or {},
        forecast_price_levels=_read_optional(public / "forecast-price-levels.json", dashboard.get("forecast_price_levels") or {}),
        price_volume_structure=_read_optional(public / "price-volume-structure.json", {}),
        confluence_score=_read_optional(public / "confluence-score.json", dashboard.get("confluence_score") or {}),
        news_event_bundle=dashboard.get("news_event_status") or {},
    )
    public_path = public / "market-alerts.json"
    output_path = PROJECT_ROOT / "outputs" / "market_alerts.md"
    public_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    output_path.write_text(render_market_alerts_markdown(payload), encoding="utf-8")
    print("wrote frontend/public/market-alerts.json")
    print("wrote outputs/market_alerts.md")
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
