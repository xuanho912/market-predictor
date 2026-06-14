from __future__ import annotations

import csv
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.services.data_providers.auto_download import DownloadedSeries
from scripts.market_intelligence_v3 import HORIZONS, TARGET_SYMBOLS


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def build_market_intelligence_v4(
    *,
    series_by_symbol: dict[str, DownloadedSeries],
    overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    analogs: dict[str, dict[str, Any]],
    prior_intelligence: dict[str, Any],
    finnhub_bundle: dict[str, Any] | None = None,
) -> dict[str, Any]:
    finnhub_bundle = finnhub_bundle or {}
    prior_quality = prior_intelligence["data_quality_report"]
    data_quality = build_data_quality_report_v4(prior_quality, finnhub_bundle)
    confirmation_by_symbol: dict[str, Any] = {}
    predictors_by_symbol: dict[str, Any] = {}
    confidence_by_symbol: dict[str, Any] = {}
    edge_by_symbol: dict[str, Any] = {}

    for symbol in TARGET_SYMBOLS:
        overview_symbol = overview.get("symbols", {}).get(symbol, {})
        simulated_symbol = simulated_paths.get("symbols", {}).get(symbol, {})
        features = simulated_symbol.get("feature_snapshot_v3") or overview_symbol.get("feature_snapshot_v3") or {}
        analog_support = simulated_symbol.get("historical_support_by_horizon") or {}
        existing_predictors = simulated_symbol.get("predictors") or {}
        existing_confidence = simulated_symbol.get("model_confidence") or {}
        if not overview_symbol or not simulated_symbol:
            continue

        confirmation = build_signal_confirmation_engine(
            overview_symbol=overview_symbol,
            features=features,
            analog_support=analog_support,
            predictors=existing_predictors,
            data_quality=data_quality,
        )
        predictors_v4 = build_predictors_v4(
            symbol=symbol,
            series=series_by_symbol.get(symbol),
            overview_symbol=overview_symbol,
            features=features,
            analog_support=analog_support,
            prior_predictors=existing_predictors,
            signal_confirmation=confirmation,
        )
        confidence = build_confidence_v4(
            prior_confidence=existing_confidence,
            data_quality=data_quality,
            signal_confirmation=confirmation,
            analog_support=analog_support,
            predictors_v4=predictors_v4,
        )
        edge_status = build_edge_status_v4(
            overview_symbol=overview_symbol,
            features=features,
            data_quality=data_quality,
            signal_confirmation=confirmation,
            confidence=confidence,
            analog_support=analog_support,
            predictors_v4=predictors_v4,
        )
        path_weight_model = build_path_weight_model_v4(
            existing_weights=simulated_symbol.get("path_weight_model") or {},
            predictors_v4=predictors_v4,
            signal_confirmation=confirmation,
            analog_support=analog_support,
            data_quality=data_quality,
            features=features,
        )
        scenario_ranking = build_scenario_ranking_v4(
            symbol=symbol,
            path_weight_model=path_weight_model,
            predictors_v4=predictors_v4,
            signal_confirmation=confirmation,
            analog_support=analog_support,
            features=features,
        )

        patch = {
            "market_intelligence_version": "v4",
            "signal_confirmation": confirmation,
            "signal_confirmation_score": confirmation["confirmation_score"],
            "predictors_v4": predictors_v4,
            "market_edge_status": edge_status,
            "model_confidence": confidence,
            "path_weight_model": path_weight_model,
            "base_path_weight": path_weight_model["base_path_weight"],
            "bounce_path_weight": path_weight_model["bounce_path_weight"],
            "bearish_path_weight": path_weight_model["bearish_path_weight"],
            "analog_path_weight": path_weight_model["analog_path_weight"],
            "low_confidence_simulation": path_weight_model["low_confidence_simulation"],
            "scenario_weights": {
                "base_scenario": path_weight_model["base_path_weight"],
                "bounce_scenario": path_weight_model["bounce_path_weight"],
                "bearish_scenario": path_weight_model["bearish_path_weight"],
                "historical_analog_average": path_weight_model["analog_path_weight"],
            },
            "scenario_ranking": scenario_ranking,
            "current_integrated_judgment": build_daily_market_brief_v4(symbol, edge_status, scenario_ranking, confirmation, confidence),
        }
        overview_symbol.update(patch)
        simulated_symbol.update(patch)
        _update_scenario_card_weights(simulated_symbol, path_weight_model)
        confirmation_by_symbol[symbol] = confirmation
        predictors_by_symbol[symbol] = predictors_v4
        confidence_by_symbol[symbol] = confidence
        edge_by_symbol[symbol] = edge_status

    data_quality["summary"]["target_completeness_score"] = 85
    overview["data_quality_summary"] = data_quality["summary"]
    overview["model_confidence_by_symbol"] = confidence_by_symbol
    overview["signal_confirmation_by_symbol"] = confirmation_by_symbol
    overview["edge_status_by_symbol"] = edge_by_symbol
    simulated_paths["data_quality_summary"] = data_quality["summary"]

    edge_report = build_high_confidence_edge_report(analogs, simulated_paths)
    return {
        "version": "market_intelligence_engine_v4",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "data_quality_report": data_quality,
        "signal_confirmation_by_symbol": confirmation_by_symbol,
        "predictor_outputs_by_symbol": predictors_by_symbol,
        "model_confidence_by_symbol": confidence_by_symbol,
        "edge_status_by_symbol": edge_by_symbol,
        "high_confidence_edge_report": edge_report,
        "finnhub_status": {
            "available": bool(finnhub_bundle.get("available")),
            "configured": bool(finnhub_bundle.get("configured")),
            "rate_limited": bool(finnhub_bundle.get("rate_limited")),
            "cache_used": bool(finnhub_bundle.get("cache_used")),
        },
        "warnings": [
            "Alpha v1 threshold remains frozen at 0.32534311.",
            "V4 strong edge requires multi-source confirmation; missing evidence caps confidence.",
            "Breadth and flow remain ETF/sector proxies unless a true constituent or fund-flow feed is added.",
        ],
        "prior_engine": prior_intelligence.get("version", "market_intelligence_engine_v3"),
    }


def build_data_quality_report_v4(prior_quality: dict[str, Any], finnhub_bundle: dict[str, Any]) -> dict[str, Any]:
    report = _deepcopy(prior_quality)
    coverage = report.get("coverage_categories", {})
    sources = report.get("sources", {})
    summary = report.setdefault("summary", {})
    score = _data_completeness_score_v4(coverage, sources)
    missing_sources = [name for name, row in sources.items() if row.get("missing_data")]
    unavailable = [name for name, payload in coverage.items() if payload.get("status") in {"missing", "not_available"}]
    summary.update(
        {
            "data_completeness_score": score,
            "target_completeness_score": 85,
            "v4_target_met": score >= 85,
            "unavailable_categories": unavailable,
            "missing_key_sources": missing_sources,
            "finnhub_available": bool(finnhub_bundle.get("available")),
            "finnhub_missing": bool(finnhub_bundle.get("missing")) or not bool(finnhub_bundle.get("configured")),
            "finnhub_rate_limited": bool(finnhub_bundle.get("rate_limited")),
            "fred_provider_status": _provider_status(sources, ("DGS10", "DGS2", "DGS3MO", "HY_OAS", "IG_OAS")),
            "breadth_provider_status": coverage.get("breadth", {}).get("status", "missing"),
            "options_provider_status": coverage.get("options", {}).get("status", "missing"),
            "flow_provider_status": coverage.get("flow", {}).get("status", "missing"),
            "quality_note": (
                "V4 score rewards real FRED/Finnhub/market data, gives partial credit to explicitly labeled proxies, "
                "and keeps missing options/flow/breadth details visible."
            ),
        }
    )
    report["version"] = "market_intelligence_engine_v4_data_quality"
    report["generated_at"] = datetime.now(timezone.utc).isoformat()
    notes = list(report.get("notes") or [])
    notes.append("V4 target is 85/100. If not reached, the blocking items are listed in missing_key_sources and unavailable_categories.")
    report["notes"] = notes
    return report


def build_signal_confirmation_engine(
    *,
    overview_symbol: dict[str, Any],
    features: dict[str, Any],
    analog_support: dict[str, Any],
    predictors: dict[str, Any],
    data_quality: dict[str, Any],
) -> dict[str, Any]:
    supporting: list[dict[str, Any]] = []
    conflicting: list[dict[str, Any]] = []
    missing: list[dict[str, str]] = []

    def support(name: str, score: float, detail: str) -> None:
        supporting.append({"name": name, "score": round(score, 3), "detail": detail})

    def conflict(name: str, score: float, detail: str) -> None:
        conflicting.append({"name": name, "score": round(score, 3), "detail": detail})

    def miss(name: str, detail: str) -> None:
        missing.append({"name": name, "detail": detail})

    price = features.get("price", {})
    vol = features.get("volatility_options", {})
    credit = features.get("credit", {})
    breadth = features.get("breadth", {})
    macro = features.get("macro_event_calendar", {})
    flow = features.get("flow_positioning_proxy", {})
    coverage = data_quality.get("coverage_categories", {})
    bounce = float(overview_symbol.get("bounce_probability") or 0.0)
    failed = float(predictors.get("downside_continuation_predictor", {}).get("probability") or overview_symbol.get("downside_continuation_probability") or 0.0)
    vix5 = _float(vol.get("vix_change_5d"), 0.0)
    vix20 = _float(vol.get("vix_change_20d"), 0.0)
    options_stress = _options_stress_score(vol)
    credit_stability = _float(credit.get("credit_stabilization_score"), 0.0)
    credit_deterioration = _float(credit.get("credit_deterioration_score"), 0.0)
    breadth_improvement = _float(breadth.get("breadth_improvement_score"), 0.0)
    flow_risk_off = _float(flow.get("risk_off_rotation_score"), 0.0)
    trend_20d = _float(price.get("return_20d"), 0.0)
    medium_support = analog_support.get("medium_term_support")
    short_support = analog_support.get("short_term_support")
    macro_event_risk = bool(macro.get("macro_event_risk_flag"))

    if overview_symbol.get("live_signal") and bounce >= 0.32534311:
        support("Alpha v1 bounce signal", 0.12, "Frozen Alpha v1 is triggered; this remains research-only.")
    else:
        miss("Alpha v1 bounce signal", "No live Alpha v1 bounce signal.")
    if vix5 <= 0 and vix20 <= 0:
        support("VIX direction", 0.11, "VIX 5d/20d direction is not worsening.")
    else:
        conflict("VIX direction", 0.12, "VIX is rising or not confirming a bounce.")
    if credit_stability >= 0.55:
        support("credit stability", 0.12, "Credit proxy is stable or improving.")
    elif credit_deterioration >= 0.45:
        conflict("credit deterioration", 0.14, "Credit proxy is deteriorating.")
    else:
        miss("credit stability", "Credit signal is inconclusive.")
    if breadth_improvement >= 0.55:
        support("breadth improvement", 0.10, "Breadth proxy is improving.")
    elif breadth_improvement <= 0.40:
        conflict("breadth weak", 0.10, "Breadth proxy is weak.")
    else:
        miss("breadth improvement", "Breadth proxy is mixed.")
    if options_stress <= 0.45:
        support("options stress", 0.08, "Options/volatility proxy is not in high stress.")
    elif options_stress >= 0.65:
        conflict("options stress", 0.10, "Options/volatility proxy is stressed.")
    else:
        miss("options stress", "Options proxy is mixed.")
    if macro_event_risk:
        conflict("macro event risk", 0.08, "Macro/event calendar risk is elevated.")
    else:
        support("macro event risk", 0.05, "No major macro event flag.")
    if flow_risk_off <= 0.45:
        support("flow / positioning proxy", 0.07, "Rotation/flow proxy is not risk-off.")
    elif flow_risk_off >= 0.58:
        conflict("flow / positioning proxy", 0.09, "Rotation/flow proxy is risk-off.")
    else:
        miss("flow / positioning proxy", "Flow proxy is mixed.")
    if medium_support == "supportive":
        support("historical analog support", 0.12, "20d/60d analog support is positive.")
    elif short_support == "weak" and medium_support == "weak":
        conflict("historical analog support", 0.13, "Historical analogs conflict across horizons.")
    else:
        miss("historical analog support", "Historical analog support is mixed by horizon.")
    if trend_20d >= 0:
        support("price trend", 0.06, "20d price trend is not negative.")
    else:
        conflict("price trend", 0.07, "20d price trend is negative.")
    if failed >= 0.55:
        conflict("failed bounce risk", 0.13, "Failed-bounce/downside continuation risk is elevated.")
    elif failed <= 0.42:
        support("failed bounce risk", 0.06, "Failed-bounce risk is contained.")

    for category in ("options", "breadth", "flow", "macro", "news"):
        status = coverage.get(category, {}).get("status", "missing")
        if status in {"missing", "not_available"}:
            miss(category, f"{category} evidence is missing.")

    raw = 50.0 + sum(item["score"] for item in supporting) * 70.0 - sum(item["score"] for item in conflicting) * 75.0
    completeness = float(data_quality.get("summary", {}).get("data_completeness_score") or 0.0)
    if completeness < 80:
        raw = min(raw, 68.0)
    if len(missing) >= 4:
        raw = min(raw, 70.0)
    score = int(round(_clip(raw, 0.0, 100.0)))
    level = "strong" if score >= 70 and len(conflicting) <= 3 and completeness >= 80 else "mixed" if score >= 45 else "weak"
    return {
        "confirmation_score": score,
        "signal_confirmation_score": score,
        "confirmation_level": level,
        "supporting_evidence": supporting,
        "conflicting_evidence": conflicting,
        "missing_evidence": missing,
        "data_completeness_cap_applied": completeness < 80,
        "missing_evidence_cap_applied": len(missing) >= 4,
    }


def build_predictors_v4(
    *,
    symbol: str,
    series: DownloadedSeries | None,
    overview_symbol: dict[str, Any],
    features: dict[str, Any],
    analog_support: dict[str, Any],
    prior_predictors: dict[str, Any],
    signal_confirmation: dict[str, Any],
) -> dict[str, Any]:
    price = features.get("price", {})
    vol = features.get("volatility_options", {})
    credit = features.get("credit", {})
    rates = features.get("rates_liquidity", {})
    macro = features.get("macro_event_calendar", {})
    confirmation = signal_confirmation["confirmation_score"] / 100.0
    current_price = _float(price.get("current_price") or overview_symbol.get("current_price"), 0.0)
    recent_low = _recent_low(series, fallback=current_price)
    bounce_prior = prior_predictors.get("bounce_predictor", {})
    downside_prior = prior_predictors.get("downside_continuation_predictor", {})
    reversal_prior = prior_predictors.get("trend_reversal_predictor", {})
    risk_prior = prior_predictors.get("risk_expansion_predictor", {})
    credit_deterioration = _float(credit.get("credit_deterioration_score"), 0.0)
    volatility_risk = _options_stress_score(vol)
    liquidity_risk = _float(rates.get("liquidity_stress_proxy"), 0.0)
    macro_risk = 1.0 if macro.get("macro_event_risk_flag") else 0.0

    bounce_probability = _clip(_float(bounce_prior.get("probability"), 0.0) * 0.75 + confirmation * 0.25, 0.0, 0.95)
    downside_probability = _clip(_float(downside_prior.get("probability"), 0.0) * 0.70 + (1.0 - confirmation) * 0.15 + volatility_risk * 0.15, 0.0, 0.95)
    reversal_probability = _clip(_float(reversal_prior.get("probability"), 0.0) * 0.72 + (1.0 if analog_support.get("medium_term_support") == "supportive" else 0.35) * 0.18 + confirmation * 0.10, 0.0, 0.95)
    risk_probability = _clip(_float(risk_prior.get("probability"), 0.0) * 0.62 + credit_deterioration * 0.16 + volatility_risk * 0.10 + liquidity_risk * 0.08 + macro_risk * 0.04, 0.0, 0.95)

    return {
        "bounce_predictor": {
            **bounce_prior,
            "bounce_probability": round(bounce_probability, 4),
            "probability": round(bounce_probability, 4),
            "best_horizon": bounce_prior.get("best_horizon", "3d-10d"),
            "key_drivers": bounce_prior.get("main_drivers", []),
            "invalidation_conditions": bounce_prior.get("invalidation_conditions", []),
            "conflicting_evidence": [item for item in signal_confirmation["conflicting_evidence"] if item["name"] in {"VIX direction", "credit deterioration", "breadth weak", "failed bounce risk"}],
        },
        "downside_continuation_predictor": {
            **downside_prior,
            "downside_continuation_probability": round(downside_probability, 4),
            "probability": round(downside_probability, 4),
            "break_level": round(recent_low, 2) if recent_low else None,
            "risk_triggers": ["VIX rising", "HYG/LQD weakens", f"{symbol} breaks recent low", "macro event surprise"],
            "invalidation_conditions": downside_prior.get("invalidation_conditions", []),
        },
        "trend_reversal_predictor": {
            **reversal_prior,
            "trend_reversal_probability": round(reversal_probability, 4),
            "probability": round(reversal_probability, 4),
            "confirmation_requirements": ["20d/60d analog support remains positive", "breadth proxy keeps improving", "credit proxy stays stable", "price holds above recent low"],
            "regime_support": analog_support.get("medium_term_support", "neutral"),
        },
        "risk_expansion_predictor": {
            **risk_prior,
            "risk_expansion_probability": round(risk_probability, 4),
            "probability": round(risk_probability, 4),
            "credit_risk": round(credit_deterioration, 4),
            "volatility_risk": round(volatility_risk, 4),
            "liquidity_risk": round(liquidity_risk, 4),
            "macro_event_risk": round(macro_risk, 4),
        },
    }


def build_confidence_v4(
    *,
    prior_confidence: dict[str, Any],
    data_quality: dict[str, Any],
    signal_confirmation: dict[str, Any],
    analog_support: dict[str, Any],
    predictors_v4: dict[str, Any],
) -> dict[str, Any]:
    prior = float(prior_confidence.get("confidence_score") or 0.0)
    completeness = float(data_quality.get("summary", {}).get("data_completeness_score") or 0.0)
    confirmation = float(signal_confirmation.get("confirmation_score") or 0.0)
    analog = 70.0 if analog_support.get("medium_term_support") == "supportive" else 45.0 if analog_support.get("medium_term_support") == "weak" else 55.0
    spread = _predictor_spread(predictors_v4)
    raw = prior * 0.18 + completeness * 0.30 + confirmation * 0.34 + analog * 0.08 + (1.0 - spread) * 100.0 * 0.10
    if completeness < 80:
        raw = min(raw, 69.0)
    if confirmation < 70:
        raw = min(raw, 68.0)
    if signal_confirmation.get("confirmation_level") == "weak":
        raw = min(raw, 55.0)
    score = int(round(_clip(raw, 0.0, 90.0)))
    why = []
    if completeness < 85:
        why.append("数据完整度未达到 v4 目标 85/100。")
    if confirmation < 70:
        why.append("多源确认分数未达到 strong edge 门槛。")
    if signal_confirmation.get("missing_evidence"):
        why.append("仍有关键证据缺失：" + " / ".join(item["name"] for item in signal_confirmation["missing_evidence"][:5]))
    if analog_support.get("short_term_support") == "weak":
        why.append("短周期 historical analog 仍有冲突。")
    return {
        **prior_confidence,
        "confidence_score": score,
        "confidence_level": "high" if score >= 75 else "medium" if score >= 55 else "low",
        "components": {
            "prior_confidence": prior / 100.0,
            "data_completeness": completeness / 100.0,
            "signal_confirmation": confirmation / 100.0,
            "analog_support": analog / 100.0,
            "predictor_consistency": 1.0 - spread,
        },
        "why_confidence_is_limited": why or ["多源确认、数据完整度和预测器分歧当前相对可接受，但仍不是确定性预测。"],
    }


def build_edge_status_v4(
    *,
    overview_symbol: dict[str, Any],
    features: dict[str, Any],
    data_quality: dict[str, Any],
    signal_confirmation: dict[str, Any],
    confidence: dict[str, Any],
    analog_support: dict[str, Any],
    predictors_v4: dict[str, Any],
) -> dict[str, Any]:
    completeness = int(data_quality.get("summary", {}).get("data_completeness_score") or 0)
    confirmation = int(signal_confirmation.get("confirmation_score") or 0)
    confidence_score = int(confidence.get("confidence_score") or 0)
    macro_high = bool(features.get("macro_event_calendar", {}).get("macro_event_risk_flag"))
    analog_conflict = analog_support.get("short_term_support") == "weak" and analog_support.get("medium_term_support") == "weak"
    regime_known = overview_symbol.get("market_state") not in {None, "", "unknown", "no_edge"}
    risk = predictors_v4["risk_expansion_predictor"]["probability"]
    credit_risk = predictors_v4["risk_expansion_predictor"].get("credit_risk", 0.0)
    vol_risk = predictors_v4["risk_expansion_predictor"].get("volatility_risk", 0.0)
    strong_conflict = credit_risk >= 0.65 or vol_risk >= 0.72
    conditions = {
        "data_completeness_ge_80": completeness >= 80,
        "signal_confirmation_ge_70": confirmation >= 70,
        "historical_analog_not_conflicting": not analog_conflict,
        "confidence_score_ge_65": confidence_score >= 65,
        "current_regime_identified": regime_known,
        "macro_event_risk_not_high": not macro_high,
        "credit_volatility_no_strong_conflict": not strong_conflict,
    }
    if risk >= 0.60 or strong_conflict:
        status = "RISK_WARNING"
    elif all(conditions.values()):
        status = "STRONG_EDGE"
    elif sum(conditions.values()) >= 5 and confirmation >= 58 and confidence_score >= 58:
        status = "MODERATE_EDGE"
    elif sum(conditions.values()) >= 3 and confidence_score >= 45:
        status = "WEAK_EDGE"
    else:
        status = "NO_EDGE"
    no_edge_note = "今天没有足够 edge，不应过度解读预测路径。" if status in {"NO_EDGE", "WEAK_EDGE"} else ""
    return {
        "market_edge_status": status,
        "has_usable_prediction_edge_today": status in {"MODERATE_EDGE", "STRONG_EDGE", "RISK_WARNING"},
        "conditions": conditions,
        "passed_conditions": sum(1 for value in conditions.values() if value),
        "summary": _edge_summary_v4(status),
        "no_edge_note": no_edge_note,
        "risk_warning": status == "RISK_WARNING",
    }


def build_path_weight_model_v4(
    *,
    existing_weights: dict[str, Any],
    predictors_v4: dict[str, Any],
    signal_confirmation: dict[str, Any],
    analog_support: dict[str, Any],
    data_quality: dict[str, Any],
    features: dict[str, Any],
) -> dict[str, Any]:
    confirmation = signal_confirmation["confirmation_score"] / 100.0
    completeness = float(data_quality.get("summary", {}).get("data_completeness_score") or 0.0) / 100.0
    bounce = predictors_v4["bounce_predictor"]["probability"]
    downside = predictors_v4["downside_continuation_predictor"]["probability"]
    reversal = predictors_v4["trend_reversal_predictor"]["probability"]
    risk = predictors_v4["risk_expansion_predictor"]["probability"]
    macro = features.get("macro_event_calendar", {})
    macro_risk = 1.0 if macro.get("macro_event_risk_flag") else 0.0
    analog_score = _analog_score(analog_support)
    conflict_penalty = min(len(signal_confirmation["conflicting_evidence"]) / 8.0, 1.0)
    raw = {
        "base_path_weight": 0.12 + (1.0 - abs(confirmation - 0.50) * 2.0) * 0.16 + (1.0 - completeness) * 0.10 + conflict_penalty * 0.10,
        "bounce_path_weight": 0.08 + bounce * 0.34 + confirmation * 0.16 + analog_score * 0.12 + reversal * 0.08,
        "bearish_path_weight": 0.08 + downside * 0.28 + risk * 0.18 + (1.0 - confirmation) * 0.12 + macro_risk * 0.06 + conflict_penalty * 0.08,
        "analog_path_weight": 0.10 + analog_score * 0.24 + completeness * 0.08 + (0.08 if analog_support.get("analog_sample_quality") == "high" else 0.02),
    }
    total = sum(max(value, 0.001) for value in raw.values())
    weights = {key: round(max(value, 0.001) / total, 4) for key, value in raw.items()}
    weights.update(
        {
            "low_confidence_simulation": completeness < 0.80 or confirmation < 0.60,
            "simulation_confidence_level": "high" if completeness >= 0.85 and confirmation >= 0.75 else "medium" if completeness >= 0.75 and confirmation >= 0.60 else "low",
            "weight_factors": {
                **(existing_weights.get("weight_factors") or {}),
                "signal_confirmation": round(confirmation, 4),
                "risk_expansion": round(risk, 4),
                "macro_event_risk": round(macro_risk, 4),
            },
            "weight_source_notes": [
                "V4 path weights come from the four independent predictors, signal confirmation, historical analog distribution, data completeness and macro event risk.",
                "If primary and secondary differ by less than 8 percentage points, close_call is true and single-path conviction should be reduced.",
            ],
        }
    )
    return weights


def build_scenario_ranking_v4(
    *,
    symbol: str,
    path_weight_model: dict[str, Any],
    predictors_v4: dict[str, Any],
    signal_confirmation: dict[str, Any],
    analog_support: dict[str, Any],
    features: dict[str, Any],
) -> dict[str, Any]:
    scenarios = [
        ("expected_path", "综合期望情景", "base_path_weight", "3d-20d"),
        ("bounce_path", "反抽情景", "bounce_path_weight", "10d-20d"),
        ("bearish_path", "失败反抽情景", "bearish_path_weight", "3d-10d"),
        ("analog_average_path", "历史均值情景", "analog_path_weight", "20d-60d"),
    ]
    total = sum(max(float(path_weight_model.get(weight_key) or 0.0), 0.0) for _, _, weight_key, _ in scenarios) or 1.0
    ranked = []
    for scenario, label, weight_key, horizon in scenarios:
        probability = max(float(path_weight_model.get(weight_key) or 0.0), 0.0) / total
        ranked.append(
            {
                "scenario": scenario,
                "label": label,
                "probability": round(probability, 4),
                "reason": _scenario_reason_v4(scenario, predictors_v4, signal_confirmation, analog_support, features),
                "expected_horizon": horizon,
                "confidence": path_weight_model.get("simulation_confidence_level", "low"),
            }
        )
    ranked.sort(key=lambda item: item["probability"], reverse=True)
    primary, secondary, tertiary = ranked[0], ranked[1], ranked[2]
    risk = next((item for item in ranked if item["scenario"] == "bearish_path"), tertiary)
    gap = round(primary["probability"] - secondary["probability"], 4)
    return {
        "primary": primary,
        "secondary": secondary,
        "tertiary": tertiary,
        "all_scenarios": ranked,
        "primary_scenario": primary["scenario"],
        "secondary_scenario": secondary["scenario"],
        "risk_scenario": risk["scenario"],
        "scenario_probability": primary["probability"],
        "probability_gap": gap,
        "primary_secondary_gap": gap,
        "close_call": gap < 0.08,
        "path_reliability": path_weight_model.get("simulation_confidence_level", "low"),
        "switching_conditions": _switching_conditions(symbol, primary["scenario"], secondary["scenario"]),
        "primary_to_secondary_switch_conditions": _switching_conditions(symbol, primary["scenario"], secondary["scenario"]),
        "ranking_note": "V4 scenario ranking is derived from predictor probabilities, signal confirmation, historical analog distribution, data completeness and macro event risk. It is not a guaranteed forecast.",
        "close_call_note": "路径分歧较大，不能重押单一路径。" if gap < 0.08 else "",
    }


def build_high_confidence_edge_report(analogs: dict[str, dict[str, Any]], simulated_paths: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for symbol, analog in analogs.items():
        symbol_state = simulated_paths.get("symbols", {}).get(symbol, {})
        ranking = symbol_state.get("scenario_ranking", {})
        confirmation = symbol_state.get("signal_confirmation", {})
        confidence = symbol_state.get("model_confidence", {})
        edge_status = symbol_state.get("market_edge_status", {}).get("market_edge_status", "NO_EDGE")
        for case in analog.get("top_similar_cases", []):
            row = dict(case)
            row.update(
                {
                    "symbol": symbol,
                    "edge_status": edge_status,
                    "signal_confirmation_score": confirmation.get("confirmation_score", 0),
                    "confidence_score": confidence.get("confidence_score", 0),
                    "primary_scenario": ranking.get("primary_scenario"),
                    "secondary_scenario": ranking.get("secondary_scenario"),
                    "primary_probability": ranking.get("scenario_probability"),
                    "probability_gap": ranking.get("probability_gap"),
                }
            )
            rows.append(row)
    report = {
        "version": "market_intelligence_engine_v4_high_confidence_edge_report",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "historical_proxy_and_forward_pending",
        "sample_size": len(rows),
        "forward_completed_sample_size": _forward_completed_sample_size(),
        "by_edge_status": {status: _edge_bucket_metrics([row for row in rows if row["edge_status"] == status]) for status in ("STRONG_EDGE", "MODERATE_EDGE", "WEAK_EDGE", "NO_EDGE", "RISK_WARNING")},
        "signal_confirmation_top_10": _edge_bucket_metrics(_top_fraction(rows, "signal_confirmation_score", 0.10)),
        "confidence_top_10": _edge_bucket_metrics(_top_fraction(rows, "confidence_score", 0.10)),
        "primary_scenario_hit_rate": _primary_scenario_hit_rate(rows),
        "primary_vs_secondary": _primary_vs_secondary_proxy(rows),
        "by_symbol": {symbol: _edge_bucket_metrics([row for row in rows if row["symbol"] == symbol]) for symbol in TARGET_SYMBOLS},
        "by_regime": _by_regime(rows),
        "conclusion": _edge_report_conclusion(rows),
        "notes": [
            "This report is not proof of alpha; it is a proxy check until forward-only samples mature.",
            "If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.",
        ],
    }
    return report


def render_high_confidence_edge_report_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# High Confidence Edge Report",
        "",
        f"Generated at: `{report.get('generated_at')}`",
        "",
        f"Status: `{report.get('status')}`",
        f"Sample size: `{report.get('sample_size')}`",
        f"Forward completed sample size: `{report.get('forward_completed_sample_size')}`",
        f"Conclusion: `{report.get('conclusion')}`",
        "",
        "## By Edge Status",
        "",
    ]
    for status, payload in report.get("by_edge_status", {}).items():
        lines.append(f"### {status}")
        lines.extend(_metrics_markdown(payload))
        lines.append("")
    lines.append("## Top Confirmation / Confidence Buckets")
    lines.append("")
    lines.append("### signal_confirmation_score top 10%")
    lines.extend(_metrics_markdown(report.get("signal_confirmation_top_10", {})))
    lines.append("")
    lines.append("### confidence_score top 10%")
    lines.extend(_metrics_markdown(report.get("confidence_top_10", {})))
    lines.append("")
    lines.append("## Scenario Checks")
    lines.append("")
    lines.append(f"- primary_scenario_hit_rate: `{report.get('primary_scenario_hit_rate')}`")
    lines.append(f"- primary_vs_secondary: `{report.get('primary_vs_secondary')}`")
    lines.append("")
    lines.extend(f"- {note}" for note in report.get("notes", []))
    lines.append("")
    return "\n".join(lines)


def build_daily_market_brief_v4(symbol: str, edge: dict[str, Any], ranking: dict[str, Any], confirmation: dict[str, Any], confidence: dict[str, Any]) -> str:
    primary = ranking["primary"]
    secondary = ranking["secondary"]
    gap = ranking["primary_secondary_gap"]
    no_edge = edge.get("no_edge_note")
    close = "路径分歧较大，不能重押单一路径。" if ranking.get("close_call") else ""
    return (
        f"{symbol} 当前 edge 状态：{edge['market_edge_status']}。"
        f"最大概率路径是“{primary['label']}”({primary['probability']:.0%})，第二路径是“{secondary['label']}”({secondary['probability']:.0%})，差距 {gap:.0%}。"
        f"多源确认分数 {confirmation['confirmation_score']}/100，模型可信度 {confidence['confidence_score']}/100。"
        f"{no_edge or close or '可以观察主路径，但仍需按失效条件动态切换。'}"
    )


def _data_completeness_score_v4(coverage: dict[str, Any], source_rows: dict[str, Any]) -> int:
    weights = {
        "price": 15,
        "volatility": 10,
        "options": 8,
        "breadth": 12,
        "credit": 12,
        "rates": 10,
        "liquidity": 8,
        "macro": 6,
        "news": 5,
        "flow": 7,
        "market_structure": 12,
    }
    values = {
        "available": 1.0,
        "partial": 0.70,
        "proxy": 0.78,
        "fallback": 0.45,
        "stale": 0.30,
        "missing": 0.0,
        "not_available": 0.0,
    }
    score = sum(weights[name] * values.get(coverage.get(name, {}).get("status"), 0.0) for name in weights)
    if any(row.get("source") == "synthetic-fallback" for row in source_rows.values()):
        score -= 25
    return int(round(_clip(score, 0.0, 100.0)))


def _provider_status(sources: dict[str, Any], names: tuple[str, ...]) -> str:
    available = sum(1 for name in names if sources.get(name, {}).get("real_data"))
    if available == len(names):
        return "available"
    if available:
        return "partial"
    return "missing"


def _edge_summary_v4(status: str) -> str:
    if status == "STRONG_EDGE":
        return "多源确认较强，可以给出较明确的概率路径，但仍不是交易指令。"
    if status == "MODERATE_EDGE":
        return "有一定预测优势，但仍需观察冲突信号和失效条件。"
    if status == "RISK_WARNING":
        return "风险扩散条件升高，重点不是追逐反抽，而是防止路径切换到风险情景。"
    if status == "WEAK_EDGE":
        return "预测优势偏弱，应以观察为主。"
    return "今天没有足够 edge，不应过度解读预测路径。"


def _scenario_reason_v4(
    scenario: str,
    predictors: dict[str, Any],
    confirmation: dict[str, Any],
    analog_support: dict[str, Any],
    features: dict[str, Any],
) -> str:
    if scenario == "bounce_path":
        return f"Bounce Predictor {predictors['bounce_predictor']['probability']:.0%}，多源确认 {confirmation['confirmation_score']}/100，20d/60d historical support 为 {analog_support.get('medium_term_support', 'neutral')}。"
    if scenario == "bearish_path":
        return f"Downside/Risk predictors 为 {predictors['downside_continuation_predictor']['probability']:.0%}/{predictors['risk_expansion_predictor']['probability']:.0%}，若波动率、信用或价格低点恶化，反抽会失败。"
    if scenario == "analog_average_path":
        return f"历史相似样本质量 {analog_support.get('analog_sample_quality', 'unknown')}，样本数 {analog_support.get('sample_count', 0)}，中期支持 {analog_support.get('medium_term_support', 'neutral')}。"
    return "综合期望用于平衡反抽、失败反抽、历史均值和数据不完整带来的不确定性。"


def _switching_conditions(symbol: str, primary: str, secondary: str) -> list[str]:
    if primary == "bounce_path":
        return ["VIX 重新上升", "HYG/LQD 转弱", f"{symbol} 跌破近期低点", "historical support 转弱"]
    if primary == "bearish_path":
        return ["VIX 快速回落", "信用代理企稳", "价格重新站回短期趋势", "breadth proxy 修复"]
    if primary == "analog_average_path":
        return ["历史相似样本分布转弱", "20d/60d 胜率跌破 50%", "当前与历史样本差异扩大", "宏观事件风险升高"]
    return ["signal confirmation 明显偏向某一路径", "edge status 升级或降级", "信用/波动率/宽度出现同向变化"]


def _update_scenario_card_weights(simulated_symbol: dict[str, Any], path_weight_model: dict[str, Any]) -> None:
    mapping = {
        "Base case": "base_path_weight",
        "Bounce case": "bounce_path_weight",
        "Bearish case": "bearish_path_weight",
        "Historical analog case": "analog_path_weight",
    }
    for card in simulated_symbol.get("scenario_cards", []):
        key = mapping.get(card.get("name"))
        if key:
            card["probability_weight"] = path_weight_model[key]


def _options_stress_score(vol: dict[str, Any]) -> float:
    vix_pct = _float(vol.get("vix_percentile_1y"), 0.5)
    vvix = _float(vol.get("vvix_percentile_1y"), vix_pct)
    skew = _float(vol.get("skew_percentile_1y"), vix_pct)
    term = _float(vol.get("vix_term_structure_stress"), 0.45)
    return _clip(vix_pct * 0.35 + vvix * 0.25 + skew * 0.20 + term * 0.20, 0.0, 1.0)


def _analog_score(analog_support: dict[str, Any]) -> float:
    score = 0.45
    if analog_support.get("medium_term_support") == "supportive":
        score += 0.30
    elif analog_support.get("medium_term_support") == "weak":
        score -= 0.20
    if analog_support.get("short_term_support") == "supportive":
        score += 0.15
    elif analog_support.get("short_term_support") == "weak":
        score -= 0.10
    if analog_support.get("analog_sample_quality") == "high":
        score += 0.10
    return _clip(score, 0.0, 1.0)


def _recent_low(series: DownloadedSeries | None, fallback: float) -> float:
    if not series or not series.rows:
        return fallback
    closes = [_float(row.get("close"), 0.0) for row in series.rows[-20:]]
    closes = [value for value in closes if value > 0]
    return min(closes) if closes else fallback


def _predictor_spread(predictors: dict[str, Any]) -> float:
    values = [float(payload.get("probability") or 0.0) for payload in predictors.values()]
    if not values:
        return 1.0
    return max(values) - min(values)


def _top_fraction(rows: list[dict[str, Any]], key: str, fraction: float) -> list[dict[str, Any]]:
    if not rows:
        return []
    count = max(1, math.ceil(len(rows) * fraction))
    return sorted(rows, key=lambda row: float(row.get(key) or 0.0), reverse=True)[:count]


def _edge_bucket_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    payload: dict[str, Any] = {"sample_size": len(rows), "by_horizon": {}}
    for horizon in HORIZONS:
        values = [_float(row.get(f"forward_return_{horizon}d"), None) for row in rows]
        values = [value for value in values if value is not None]
        if not values:
            payload["by_horizon"][f"{horizon}d"] = {"sample_size": 0}
            continue
        payload["by_horizon"][f"{horizon}d"] = {
            "sample_size": len(values),
            "hit_rate": round(sum(1 for value in values if value > 0) / len(values), 4),
            "avg_return": round(sum(values) / len(values), 6),
            "median_return": round(sorted(values)[len(values) // 2], 6),
            "max_adverse_excursion": round(min(values), 6),
            "max_favorable_excursion": round(max(values), 6),
        }
    return payload


def _primary_scenario_hit_rate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for horizon in HORIZONS:
        hits = total = 0
        for row in rows:
            value = _float(row.get(f"forward_return_{horizon}d"), None)
            if value is None:
                continue
            scenario = row.get("primary_scenario")
            expected_positive = scenario in {"bounce_path", "analog_average_path", "expected_path"}
            expected_negative = scenario == "bearish_path"
            if expected_positive or expected_negative:
                total += 1
                hits += int((value > 0 and expected_positive) or (value < 0 and expected_negative))
        result[f"{horizon}d"] = {"sample_size": total, "hit_rate": round(hits / total, 4) if total else None}
    return result


def _primary_vs_secondary_proxy(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "status": "proxy_only",
        "note": "Primary vs secondary path closeness needs forward realized paths; current report uses historical analog direction as a proxy.",
        "primary_scenario_hit_rate": _primary_scenario_hit_rate(rows),
    }


def _by_regime(rows: list[dict[str, Any]]) -> dict[str, Any]:
    regimes: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        regimes.setdefault(str(row.get("regime") or "unknown"), []).append(row)
    return {regime: _edge_bucket_metrics(items) for regime, items in regimes.items()}


def _edge_report_conclusion(rows: list[dict[str, Any]]) -> str:
    strong = _edge_bucket_metrics([row for row in rows if row.get("edge_status") == "STRONG_EDGE"]).get("by_horizon", {}).get("20d", {})
    no_edge = _edge_bucket_metrics([row for row in rows if row.get("edge_status") == "NO_EDGE"]).get("by_horizon", {}).get("20d", {})
    if not strong.get("sample_size"):
        return "not_enough_strong_edge_samples"
    if no_edge.get("sample_size") and (strong.get("hit_rate") or 0) <= (no_edge.get("hit_rate") or 0):
        return "high_confidence_not_validated_keep_confidence_capped"
    return "historical_proxy_supports_higher_confidence_but_forward_validation_required"


def _forward_completed_sample_size() -> int:
    path = PROJECT_ROOT / "outputs" / "forward_alpha_v1_signals.csv"
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", newline="") as handle:
        return sum(1 for row in csv.DictReader(handle) if row.get("signal_status") == "completed")


def _metrics_markdown(payload: dict[str, Any]) -> list[str]:
    lines = [f"- sample_size: `{payload.get('sample_size', 0)}`"]
    for horizon, row in (payload.get("by_horizon") or {}).items():
        lines.append(
            f"- {horizon}: sample `{row.get('sample_size', 0)}`, hit `{row.get('hit_rate')}`, avg `{row.get('avg_return')}`, median `{row.get('median_return')}`"
        )
    return lines


def _float(value: Any, default: float | None = 0.0) -> float | None:
    try:
        if value is None:
            return default
        parsed = float(value)
        if math.isnan(parsed):
            return default
        return parsed
    except (TypeError, ValueError):
        return default


def _clip(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _deepcopy(payload: dict[str, Any]) -> dict[str, Any]:
    import copy

    return copy.deepcopy(payload)
