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
    fred_bundle: dict[str, Any] | None = None,
    options_bundle: dict[str, Any] | None = None,
) -> dict[str, Any]:
    finnhub_bundle = finnhub_bundle or {}
    fred_bundle = fred_bundle or {}
    options_bundle = options_bundle or {}
    prior_quality = prior_intelligence["data_quality_report"]
    data_quality = build_data_quality_report_v4(prior_quality, finnhub_bundle, fred_bundle, options_bundle)
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
            "internal_resonance": _internal_resonance_payload(features),
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
        "fred_status": _fred_status_summary(fred_bundle),
        "options_status": _options_status_summary(options_bundle),
        "warnings": [
            "Alpha v1 threshold remains frozen at 0.32534311.",
            "V4 strong edge requires multi-source confirmation; missing evidence caps confidence.",
            "Options structure is partial unless real VIX term and tail-risk proxies are available; put/call and gamma remain missing.",
            "Breadth uses SPY/QQQ/DIA constituent data when available; IWM and flow remain explicitly proxy-based.",
        ],
        "prior_engine": prior_intelligence.get("version", "market_intelligence_engine_v3"),
    }


def build_data_quality_report_v4(prior_quality: dict[str, Any], finnhub_bundle: dict[str, Any], fred_bundle: dict[str, Any] | None = None, options_bundle: dict[str, Any] | None = None) -> dict[str, Any]:
    fred_bundle = fred_bundle or {}
    options_bundle = options_bundle or {}
    report = _deepcopy(prior_quality)
    coverage = report.get("coverage_categories", {})
    sources = report.get("sources", {})
    summary = report.setdefault("summary", {})
    score = _data_completeness_score_v4(coverage, sources)
    missing_sources = [name for name, row in sources.items() if row.get("missing_data")]
    unavailable = [name for name, payload in coverage.items() if payload.get("status") in {"missing", "not_available"}]
    fred_success = list(fred_bundle.get("successful_series") or [])
    fred_failed = list(fred_bundle.get("failed_series") or [])
    true_breadth_sources = [name for name in ("breadth_SPY", "breadth_QQQ", "breadth_DIA") if sources.get(name, {}).get("real_data")]
    breadth_quality_values = [
        float(sources.get(name, {}).get("breadth_quality_score") or 0.0)
        for name in ("breadth_SPY", "breadth_QQQ", "breadth_DIA", "breadth_IWM")
        if sources.get(name)
    ]
    avg_breadth_quality = round(sum(breadth_quality_values) / len(breadth_quality_values), 2) if breadth_quality_values else 0
    options_summary = _options_status_summary(options_bundle)
    flow_rows = [sources.get(name, {}) for name in ("flow_SPY", "flow_QQQ", "flow_IWM", "flow_DIA") if sources.get(name)]
    avg_flow_quality = round(sum(float(row.get("flow_quality_score") or 0.0) for row in flow_rows) / len(flow_rows), 2) if flow_rows else 0
    avg_flow_confirmation = round(sum(float(row.get("flow_confirmation_score") or 0.0) for row in flow_rows) / len(flow_rows), 2) if flow_rows else 0
    avg_flow_conflict = round(sum(float(row.get("flow_conflict_score") or 0.0) for row in flow_rows) / len(flow_rows), 2) if flow_rows else 0
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
            "fred_available": bool(fred_bundle.get("available")) or _provider_status(sources, ("DGS10", "DGS2", "DGS3MO", "HY_OAS", "IG_OAS")) != "missing",
            "fred_missing": bool(fred_bundle.get("missing")) and _provider_status(sources, ("DGS10", "DGS2", "DGS3MO", "HY_OAS", "IG_OAS")) == "missing",
            "fred_rate_limited": bool(fred_bundle.get("rate_limited")),
            "fred_fallback_used": bool(fred_bundle.get("fallback_used")) or any(str(sources.get(name, {}).get("source", "")).startswith("local-cache-fred") for name in ("DGS10", "DGS2", "DGS3MO", "HY_OAS", "IG_OAS")),
            "fred_successful_series": fred_success or [name for name in ("DGS10", "DGS2", "DGS3MO", "HY_OAS", "IG_OAS", "BAA_SPREAD", "FINANCIAL_STRESS", "RECESSION") if sources.get(name, {}).get("real_data")],
            "fred_failed_series": fred_failed,
            "fred_provider_status": _provider_status(sources, ("DGS10", "DGS2", "DGS3MO", "HY_OAS", "IG_OAS", "BAA_SPREAD", "FINANCIAL_STRESS", "RECESSION")),
            "breadth_provider_status": coverage.get("breadth", {}).get("status", "missing"),
            "true_breadth_available": len(true_breadth_sources) >= 3,
            "true_breadth_symbols": [name.replace("breadth_", "") for name in true_breadth_sources],
            "breadth_proxy_only": coverage.get("breadth", {}).get("status") == "proxy",
            "average_breadth_quality_score": avg_breadth_quality,
            "options_provider_status": "available" if options_summary["options_available"] else "partial" if options_summary["options_partial"] else coverage.get("options", {}).get("status", "missing"),
            "options_structure_status": "available" if options_summary["options_available"] else "partial" if options_summary["options_partial"] else coverage.get("options", {}).get("status", "missing"),
            "options_available": options_summary["options_available"],
            "vix_term_available": options_summary["vix_term_available"],
            "vvix_available": options_summary["vvix_available"],
            "skew_available": options_summary["skew_available"],
            "put_call_available": options_summary["put_call_available"],
            "gamma_available": options_summary["gamma_available"],
            "gamma_exposure_available": options_summary["gamma_available"],
            "options_partial": options_summary["options_partial"],
            "options_missing": options_summary["options_missing"],
            "options_stale": options_summary["options_stale"],
            "options_source": options_summary["options_source"],
            "options_quality_score": options_summary["options_quality_score"],
            "flow_provider_status": coverage.get("flow", {}).get("status", "missing"),
            "flow_proxy_only": coverage.get("flow", {}).get("status") == "proxy",
            "true_flow_available": False,
            "average_flow_quality_score": avg_flow_quality,
            "overall_flow_confirmation_score": avg_flow_confirmation,
            "overall_flow_conflict_score": avg_flow_conflict,
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
    volatility_reversal = _score01(vol.get("volatility_reversal_score"), 0.35)
    panic_release = _score01(vol.get("panic_release_score"), 0.35)
    tail_risk = _score01(vol.get("tail_risk_score"), options_stress)
    options_quality = _score01(vol.get("options_quality_score"), 0.0)
    term_state = str(vol.get("term_structure_state") or "missing")
    credit_stability = _float(credit.get("credit_stabilization_score"), 0.0)
    credit_deterioration = _float(credit.get("credit_deterioration_score"), 0.0)
    breadth_improvement = _score01(breadth.get("breadth_improvement_score"))
    breadth_confirmation = _score01(breadth.get("breadth_confirmation_score"), breadth_improvement)
    breadth_conflict = _score01(breadth.get("breadth_conflict_score"))
    breadth_quality = _score01(breadth.get("breadth_quality_score"), 0.5)
    internal_resonance = _internal_resonance_payload(features)
    resonance_score = _score01(internal_resonance.get("resonance_score"))
    resonance_quality = _score01(internal_resonance.get("resonance_quality_score"), breadth_quality)
    resonance_state = str(internal_resonance.get("resonance_state") or "unknown")
    surface_only = resonance_state == "surface_only"
    flow_confirmation = _score01(flow.get("flow_confirmation_score"), 0.0)
    flow_conflict = _score01(flow.get("flow_conflict_score"), _score01(flow.get("risk_off_rotation_score"), 0.0))
    flow_quality = _score01(flow.get("flow_quality_score"), 0.0)
    flow_risk_off = _score01(flow.get("risk_off_flow_score"), _score01(flow.get("risk_off_rotation_score"), 0.0))
    crowding_proxy = _score01(flow.get("crowding_proxy_score"), 0.0)
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
    if breadth_confirmation >= 0.55:
        support("breadth confirmation", 0.12, "Constituent/proxy breadth is improving or confirming the path.")
    elif breadth_conflict >= 0.55 or breadth_improvement <= 0.40:
        conflict("breadth weak", 0.12, "Breadth is weak, deteriorating or diverging from price.")
    else:
        miss("breadth confirmation", "Breadth evidence is mixed.")
    if breadth_quality < 0.45:
        conflict("breadth data quality", 0.06, "Breadth coverage or freshness is too weak for high confidence.")
    if resonance_state == "aligned" and resonance_score >= 0.65:
        support("market internal resonance", 0.13, "Constituent breadth, sector participation and equal-weight/small-cap proxies broadly confirm the path.")
    elif surface_only:
        conflict("index surface strength", 0.14, "Index strength is not broadly confirmed by internals; this raises failed-bounce risk.")
    elif resonance_state in {"mixed", "weak"}:
        miss("market internal resonance", "Market internals are not strongly aligned.")
    if resonance_quality < 0.45:
        conflict("internal resonance quality", 0.05, "Internal-resonance evidence is too low quality for high confidence.")
    if volatility_reversal >= 0.58 and panic_release >= 0.45 and options_stress <= 0.55:
        support("options volatility repair", 0.10, "VIX term/volatility structure supports panic release or bounce repair.")
    elif options_stress <= 0.45:
        support("options stress", 0.07, "Options/volatility structure is not in high stress.")
    elif options_stress >= 0.65 or term_state in {"stress", "backwardation"}:
        conflict("options stress", 0.12, "Options/volatility structure is stressed or inverted.")
    else:
        miss("options stress", "Options proxy is mixed.")
    if tail_risk >= 0.62:
        conflict("tail risk", 0.08, "VVIX/SKEW or term-structure tail-risk proxies remain elevated.")
    if options_quality < 0.35:
        miss("options structure", "Options evidence is missing or too partial for high confidence.")
    if not vol.get("put_call_available"):
        miss("put/call ratio", "Put/call ratio is not connected; it is not inferred.")
    if not vol.get("gamma_available"):
        miss("gamma exposure", "Dealer gamma exposure is not connected; it is not inferred.")
    if macro_event_risk:
        conflict("macro event risk", 0.08, "Macro/event calendar risk is elevated.")
    else:
        support("macro event risk", 0.05, "No major macro event flag.")
    if flow_confirmation >= 0.58 and flow_quality >= 0.45:
        support("flow / positioning proxy", 0.09, "Proxy flow/positioning confirms risk appetite or broad participation.")
    elif flow_conflict >= 0.55 or flow_risk_off >= 0.58:
        conflict("flow / positioning proxy", 0.10, "Proxy flow/positioning favors defensive/risk-off rotation or weak participation.")
    else:
        miss("flow / positioning proxy", "Flow proxy is mixed.")
    if crowding_proxy >= 0.70:
        conflict("crowding proxy", 0.05, "ETF relative volume / volume z-score suggests crowding risk.")
    if flow_quality < 0.35:
        miss("flow proxy quality", "Flow proxy coverage is too weak for high confidence.")
    if not flow.get("true_flow_available"):
        miss("true flow feed", "True fund-flow / positioning feed is not connected; current flow evidence is proxy-only.")
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
        "internal_resonance_score": int(round(resonance_score * 100)),
        "internal_resonance_state": resonance_state,
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
    breadth = features.get("breadth", {})
    rates = features.get("rates_liquidity", {})
    macro = features.get("macro_event_calendar", {})
    flow = features.get("flow_positioning_proxy", {})
    confirmation = signal_confirmation["confirmation_score"] / 100.0
    current_price = _float(price.get("current_price") or overview_symbol.get("current_price"), 0.0)
    recent_low = _recent_low(series, fallback=current_price)
    bounce_prior = prior_predictors.get("bounce_predictor", {})
    downside_prior = prior_predictors.get("downside_continuation_predictor", {})
    reversal_prior = prior_predictors.get("trend_reversal_predictor", {})
    risk_prior = prior_predictors.get("risk_expansion_predictor", {})
    credit_deterioration = _float(credit.get("credit_deterioration_score"), 0.0)
    breadth_confirmation = _score01(breadth.get("breadth_confirmation_score"), _score01(breadth.get("breadth_improvement_score")))
    breadth_conflict = _score01(breadth.get("breadth_conflict_score"), _score01(breadth.get("breadth_deterioration_score")))
    breadth_quality = _score01(breadth.get("breadth_quality_score"), 0.5)
    internal_resonance = _internal_resonance_payload(features)
    resonance_score = _score01(internal_resonance.get("resonance_score"))
    resonance_state = str(internal_resonance.get("resonance_state") or "unknown")
    resonance_support = resonance_score if resonance_state == "aligned" else resonance_score * 0.45 if resonance_state == "mixed" else 0.0
    surface_only = 1.0 if resonance_state == "surface_only" else 0.0
    volatility_risk = _options_stress_score(vol)
    volatility_reversal = _score01(vol.get("volatility_reversal_score"), 0.35)
    panic_release = _score01(vol.get("panic_release_score"), 0.35)
    tail_risk = _score01(vol.get("tail_risk_score"), volatility_risk)
    failed_options_risk = _score01(vol.get("failed_bounce_options_risk"), volatility_risk)
    options_quality = _score01(vol.get("options_quality_score"), 0.0)
    term_state = str(vol.get("term_structure_state") or "missing")
    flow_confirmation = _score01(flow.get("flow_confirmation_score"), 0.0)
    flow_conflict = _score01(flow.get("flow_conflict_score"), _score01(flow.get("risk_off_rotation_score"), 0.0))
    flow_quality = _score01(flow.get("flow_quality_score"), 0.0)
    crowding_proxy = _score01(flow.get("crowding_proxy_score"), 0.0)
    liquidity_risk = _float(rates.get("liquidity_stress_proxy"), 0.0)
    macro_risk = 1.0 if macro.get("macro_event_risk_flag") else 0.0

    bounce_probability = _clip(
        _float(bounce_prior.get("probability"), 0.0) * 0.56
        + confirmation * 0.16
        + breadth_confirmation * 0.09
        + resonance_support * 0.09
        + volatility_reversal * 0.06
        + panic_release * 0.05
        + flow_confirmation * 0.05
        - tail_risk * 0.04
        - surface_only * 0.05,
        0.0,
        0.95,
    )
    downside_probability = _clip(
        _float(downside_prior.get("probability"), 0.0) * 0.56
        + (1.0 - confirmation) * 0.11
        + volatility_risk * 0.08
        + failed_options_risk * 0.07
        + breadth_conflict * 0.09
        + flow_conflict * 0.06
        + crowding_proxy * 0.03
        + surface_only * 0.06
        + (0.04 if term_state in {"stress", "backwardation"} else 0.0),
        0.0,
        0.95,
    )
    reversal_probability = _clip(
        _float(reversal_prior.get("probability"), 0.0) * 0.58
        + (1.0 if analog_support.get("medium_term_support") == "supportive" else 0.35) * 0.13
        + confirmation * 0.08
        + breadth_confirmation * 0.08
        + resonance_support * 0.09
        + volatility_reversal * 0.04
        + flow_confirmation * 0.04
        - surface_only * 0.04,
        0.0,
        0.95,
    )
    risk_probability = _clip(
        _float(risk_prior.get("probability"), 0.0) * 0.52
        + credit_deterioration * 0.14
        + volatility_risk * 0.08
        + tail_risk * 0.07
        + failed_options_risk * 0.05
        + liquidity_risk * 0.06
        + macro_risk * 0.04
        + breadth_conflict * 0.05
        + flow_conflict * 0.05
        + crowding_proxy * 0.03
        + surface_only * 0.04,
        0.0,
        0.95,
    )

    return {
        "bounce_predictor": {
            **bounce_prior,
            "bounce_probability": round(bounce_probability, 4),
            "probability": round(bounce_probability, 4),
            "best_horizon": bounce_prior.get("best_horizon", "3d-10d"),
            "key_drivers": bounce_prior.get("main_drivers", []),
            "invalidation_conditions": bounce_prior.get("invalidation_conditions", []),
            "conflicting_evidence": [item for item in signal_confirmation["conflicting_evidence"] if item["name"] in {"VIX direction", "credit deterioration", "breadth weak", "failed bounce risk"}],
            "breadth_confirmation": round(breadth_confirmation, 4),
            "breadth_quality": round(breadth_quality, 4),
            "volatility_reversal_score": round(volatility_reversal, 4),
            "panic_release_score": round(panic_release, 4),
            "tail_risk_score": round(tail_risk, 4),
            "options_quality": round(options_quality, 4),
            "term_structure_state": term_state,
            "internal_resonance_score": round(resonance_score, 4),
            "internal_resonance_state": resonance_state,
            "flow_confirmation_score": round(flow_confirmation, 4),
            "flow_conflict_score": round(flow_conflict, 4),
            "flow_quality_score": round(flow_quality, 4),
            "crowding_proxy_score": round(crowding_proxy, 4),
        },
        "downside_continuation_predictor": {
            **downside_prior,
            "downside_continuation_probability": round(downside_probability, 4),
            "probability": round(downside_probability, 4),
            "break_level": round(recent_low, 2) if recent_low else None,
            "risk_triggers": ["VIX rising", "HYG/LQD weakens", "breadth deterioration", f"{symbol} breaks recent low", "macro event surprise"],
            "invalidation_conditions": downside_prior.get("invalidation_conditions", []),
            "breadth_conflict": round(breadth_conflict, 4),
            "breadth_quality": round(breadth_quality, 4),
            "failed_bounce_options_risk": round(failed_options_risk, 4),
            "tail_risk_score": round(tail_risk, 4),
            "options_quality": round(options_quality, 4),
            "term_structure_state": term_state,
            "internal_resonance_score": round(resonance_score, 4),
            "internal_resonance_state": resonance_state,
            "flow_confirmation_score": round(flow_confirmation, 4),
            "flow_conflict_score": round(flow_conflict, 4),
            "flow_quality_score": round(flow_quality, 4),
            "crowding_proxy_score": round(crowding_proxy, 4),
        },
        "trend_reversal_predictor": {
            **reversal_prior,
            "trend_reversal_probability": round(reversal_probability, 4),
            "probability": round(reversal_probability, 4),
            "confirmation_requirements": ["20d/60d analog support remains positive", "constituent/proxy breadth keeps improving", "credit proxy stays stable", "price holds above recent low"],
            "regime_support": analog_support.get("medium_term_support", "neutral"),
            "breadth_confirmation": round(breadth_confirmation, 4),
            "breadth_quality": round(breadth_quality, 4),
            "volatility_reversal_score": round(volatility_reversal, 4),
            "options_quality": round(options_quality, 4),
            "term_structure_state": term_state,
            "internal_resonance_score": round(resonance_score, 4),
            "internal_resonance_state": resonance_state,
            "flow_confirmation_score": round(flow_confirmation, 4),
            "flow_conflict_score": round(flow_conflict, 4),
            "flow_quality_score": round(flow_quality, 4),
            "crowding_proxy_score": round(crowding_proxy, 4),
        },
        "risk_expansion_predictor": {
            **risk_prior,
            "risk_expansion_probability": round(risk_probability, 4),
            "probability": round(risk_probability, 4),
            "credit_risk": round(credit_deterioration, 4),
            "volatility_risk": round(volatility_risk, 4),
            "liquidity_risk": round(liquidity_risk, 4),
            "macro_event_risk": round(macro_risk, 4),
            "breadth_risk": round(breadth_conflict, 4),
            "breadth_quality": round(breadth_quality, 4),
            "tail_risk_score": round(tail_risk, 4),
            "failed_bounce_options_risk": round(failed_options_risk, 4),
            "options_quality": round(options_quality, 4),
            "term_structure_state": term_state,
            "internal_resonance_score": round(resonance_score, 4),
            "internal_resonance_state": resonance_state,
            "flow_confirmation_score": round(flow_confirmation, 4),
            "flow_conflict_score": round(flow_conflict, 4),
            "flow_quality_score": round(flow_quality, 4),
            "crowding_proxy_score": round(crowding_proxy, 4),
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
    breadth_quality = max(float((payload or {}).get("breadth_quality") or 0.0) for payload in predictors_v4.values()) * 100.0 if predictors_v4 else 50.0
    options_quality = max(float((payload or {}).get("options_quality") or 0.0) for payload in predictors_v4.values()) * 100.0 if predictors_v4 else 0.0
    flow_quality = max(float((payload or {}).get("flow_quality_score") or 0.0) for payload in predictors_v4.values()) * 100.0 if predictors_v4 else 0.0
    flow_conflict = max(float((payload or {}).get("flow_conflict_score") or 0.0) for payload in predictors_v4.values()) * 100.0 if predictors_v4 else 0.0
    resonance_scores = [float((payload or {}).get("internal_resonance_score") or 0.0) for payload in predictors_v4.values()]
    resonance_score = max(resonance_scores) * 100.0 if resonance_scores else 50.0
    surface_only = any((payload or {}).get("internal_resonance_state") == "surface_only" for payload in predictors_v4.values())
    raw = prior * 0.12 + completeness * 0.24 + confirmation * 0.28 + analog * 0.08 + (1.0 - spread) * 100.0 * 0.06 + breadth_quality * 0.07 + resonance_score * 0.07 + options_quality * 0.04 + flow_quality * 0.04
    if completeness < 80:
        raw = min(raw, 69.0)
    if confirmation < 70:
        raw = min(raw, 68.0)
    if breadth_quality < 50:
        raw = min(raw, 64.0)
    if options_quality < 35:
        raw = min(raw, 72.0)
    if surface_only:
        raw = min(raw, 68.0)
    if flow_quality < 45:
        raw = min(raw, 73.0)
    if flow_conflict >= 65:
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
    if breadth_quality < 65:
        why.append("市场宽度数据质量或覆盖率仍限制预测可信度。")
    if options_quality < 45:
        why.append("Options / volatility structure evidence is partial or missing; put/call and gamma are not connected.")
    if flow_quality < 55:
        why.append("Flow / positioning evidence is proxy-only or incomplete; true fund-flow data is not connected.")
    if flow_conflict >= 65:
        why.append("Flow / positioning proxy conflicts with the primary forecast path.")
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
            "breadth_quality": breadth_quality / 100.0,
            "internal_resonance": resonance_score / 100.0,
            "options_quality": options_quality / 100.0,
            "flow_quality": flow_quality / 100.0,
            "flow_conflict": flow_conflict / 100.0,
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
    tail_risk = predictors_v4["risk_expansion_predictor"].get("tail_risk_score", 0.0)
    failed_options_risk = predictors_v4["risk_expansion_predictor"].get("failed_bounce_options_risk", 0.0)
    options_quality = max(float((payload or {}).get("options_quality") or 0.0) for payload in predictors_v4.values()) if predictors_v4 else 0.0
    flow_conflict = max(float((payload or {}).get("flow_conflict_score") or 0.0) for payload in predictors_v4.values()) if predictors_v4 else 0.0
    flow_quality = max(float((payload or {}).get("flow_quality_score") or 0.0) for payload in predictors_v4.values()) if predictors_v4 else 0.0
    internal_resonance = _internal_resonance_payload(features)
    surface_only = internal_resonance.get("resonance_state") == "surface_only"
    strong_conflict = credit_risk >= 0.65 or vol_risk >= 0.72 or tail_risk >= 0.72 or failed_options_risk >= 0.72
    conditions = {
        "data_completeness_ge_80": completeness >= 80,
        "signal_confirmation_ge_70": confirmation >= 70,
        "historical_analog_not_conflicting": not analog_conflict,
        "confidence_score_ge_65": confidence_score >= 65,
        "current_regime_identified": regime_known,
        "macro_event_risk_not_high": not macro_high,
        "credit_volatility_no_strong_conflict": not strong_conflict,
        "market_internals_not_surface_only": not surface_only,
        "options_structure_not_missing": options_quality >= 0.25,
        "flow_proxy_not_conflicting": flow_conflict < 0.62 or flow_quality < 0.35,
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
    breadth = features.get("breadth", {})
    vol = features.get("volatility_options", {})
    flow = features.get("flow_positioning_proxy", {})
    macro_risk = 1.0 if macro.get("macro_event_risk_flag") else 0.0
    breadth_confirmation = _score01(breadth.get("breadth_confirmation_score"), _score01(breadth.get("breadth_improvement_score")))
    breadth_conflict = _score01(breadth.get("breadth_conflict_score"), _score01(breadth.get("breadth_deterioration_score")))
    breadth_quality = _score01(breadth.get("breadth_quality_score"), 0.5)
    internal_resonance = _internal_resonance_payload(features)
    resonance_score = _score01(internal_resonance.get("resonance_score"))
    resonance_state = str(internal_resonance.get("resonance_state") or "unknown")
    resonance_support = resonance_score if resonance_state == "aligned" else resonance_score * 0.45 if resonance_state == "mixed" else 0.0
    surface_only = 1.0 if resonance_state == "surface_only" else 0.0
    volatility_reversal = _score01(vol.get("volatility_reversal_score"), 0.35)
    panic_release = _score01(vol.get("panic_release_score"), 0.35)
    options_stress = _options_stress_score(vol)
    tail_risk = _score01(vol.get("tail_risk_score"), options_stress)
    failed_options_risk = _score01(vol.get("failed_bounce_options_risk"), options_stress)
    options_quality = _score01(vol.get("options_quality_score"), 0.0)
    flow_confirmation = _score01(flow.get("flow_confirmation_score"), 0.0)
    flow_conflict = _score01(flow.get("flow_conflict_score"), _score01(flow.get("risk_off_rotation_score"), 0.0))
    flow_quality = _score01(flow.get("flow_quality_score"), 0.0)
    crowding_proxy = _score01(flow.get("crowding_proxy_score"), 0.0)
    analog_score = _analog_score(analog_support)
    conflict_penalty = min(len(signal_confirmation["conflicting_evidence"]) / 8.0, 1.0)
    raw = {
        "base_path_weight": 0.12 + (1.0 - abs(confirmation - 0.50) * 2.0) * 0.15 + (1.0 - completeness) * 0.09 + conflict_penalty * 0.09 + max(0.0, 0.55 - breadth_quality) * 0.07 + max(0.0, 0.45 - options_quality) * 0.05 + max(0.0, 0.45 - flow_quality) * 0.04 + (1.0 if resonance_state in {"mixed", "weak"} else 0.0) * 0.05,
        "bounce_path_weight": 0.08 + bounce * 0.26 + confirmation * 0.12 + analog_score * 0.09 + reversal * 0.06 + breadth_confirmation * 0.08 + resonance_support * 0.08 + volatility_reversal * 0.06 + panic_release * 0.04 + flow_confirmation * 0.05,
        "bearish_path_weight": 0.08 + downside * 0.22 + risk * 0.15 + (1.0 - confirmation) * 0.10 + macro_risk * 0.06 + conflict_penalty * 0.06 + breadth_conflict * 0.07 + surface_only * 0.07 + options_stress * 0.06 + tail_risk * 0.04 + failed_options_risk * 0.05 + flow_conflict * 0.06 + crowding_proxy * 0.03,
        "analog_path_weight": 0.10 + analog_score * 0.22 + completeness * 0.08 + (0.08 if analog_support.get("analog_sample_quality") == "high" else 0.02) + resonance_score * 0.03 + max(0.0, 0.65 - tail_risk) * 0.02 + flow_quality * 0.02,
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
                "breadth_confirmation": round(breadth_confirmation, 4),
                "breadth_conflict": round(breadth_conflict, 4),
                "breadth_quality": round(breadth_quality, 4),
                "internal_resonance": round(resonance_score, 4),
                "internal_resonance_state": resonance_state,
                "volatility_reversal": round(volatility_reversal, 4),
                "panic_release": round(panic_release, 4),
                "options_stress": round(options_stress, 4),
                "tail_risk": round(tail_risk, 4),
                "failed_bounce_options_risk": round(failed_options_risk, 4),
                "options_quality": round(options_quality, 4),
                "flow_confirmation": round(flow_confirmation, 4),
                "flow_conflict": round(flow_conflict, 4),
                "flow_quality": round(flow_quality, 4),
                "crowding_proxy": round(crowding_proxy, 4),
            },
            "weight_source_notes": [
                "V4 path weights come from the four independent predictors, signal confirmation, historical analog distribution, data completeness, macro event risk, options/volatility structure and proxy flow/positioning.",
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
            features = symbol_state.get("feature_snapshot_v3") or {}
            breadth = features.get("breadth") or {}
            flow = features.get("flow_positioning_proxy") or {}
            internal = symbol_state.get("internal_resonance") or _internal_resonance_payload(features)
            predictors = symbol_state.get("predictors_v4") or {}
            strongest_predictor = _strongest_predictor_name(predictors)
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
                    "secondary_probability": (ranking.get("secondary") or {}).get("probability"),
                    "probability_gap": ranking.get("probability_gap"),
                    "close_call": bool(ranking.get("close_call")),
                    "strongest_predictor": strongest_predictor,
                    "breadth_confirmation_score": _score01(breadth.get("breadth_confirmation_score"), _score01(breadth.get("breadth_improvement_score"))) * 100.0,
                    "breadth_conflict_score": _score01(breadth.get("breadth_conflict_score"), _score01(breadth.get("breadth_deterioration_score"))) * 100.0,
                    "breadth_improvement_score": _score01(breadth.get("breadth_improvement_score")) * 100.0,
                    "breadth_quality_score": _score01(breadth.get("breadth_quality_score"), 0.0) * 100.0,
                    "true_breadth": bool(breadth.get("is_true_breadth")),
                    "breadth_proxy": bool(breadth.get("is_proxy")),
                    "internal_resonance_score": _float(internal.get("resonance_score"), 0.0),
                    "internal_resonance_state": internal.get("resonance_state"),
                    "broad_participation": bool(internal.get("broad_participation")),
                    "surface_strength_without_participation": bool(internal.get("surface_strength_without_participation")),
                    "flow_confirmation_score": _score01(flow.get("flow_confirmation_score"), 0.0) * 100.0,
                    "flow_conflict_score": _score01(flow.get("flow_conflict_score"), _score01(flow.get("risk_off_rotation_score"), 0.0)) * 100.0,
                    "flow_quality_score": _score01(flow.get("flow_quality_score"), 0.0) * 100.0,
                    "flow_proxy": bool(flow.get("is_proxy", True)),
                    "true_flow_available": bool(flow.get("true_flow_available")),
                }
            )
            rows.append(row)
    forward_counts = _forward_completion_counts()
    report = {
        "version": "market_intelligence_engine_v4_high_confidence_edge_report",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "historical_proxy_and_forward_pending",
        "sample_size": len(rows),
        "forward_completed_sample_size": forward_counts["completed_rows"],
        "completed_sample_counter": forward_counts,
        "minimum_sample_gate": forward_counts["by_horizon"],
        "forward_validation_notice": (
            "当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。"
            if forward_counts["max_completed_count"] < 20
            else "Forward samples have started to mature, but alpha status remains research-only until stability is proven."
        ),
        "by_edge_status": {status: _edge_bucket_metrics([row for row in rows if row["edge_status"] == status]) for status in ("STRONG_EDGE", "MODERATE_EDGE", "WEAK_EDGE", "NO_EDGE", "RISK_WARNING")},
        "signal_confirmation_top_10": _edge_bucket_metrics(_top_fraction(rows, "signal_confirmation_score", 0.10)),
        "confidence_top_10": _edge_bucket_metrics(_top_fraction(rows, "confidence_score", 0.10)),
        "confidence_validation": _confidence_validation(rows),
        "primary_scenario_hit_rate": _primary_scenario_hit_rate(rows),
        "primary_vs_secondary": _primary_vs_secondary_proxy(rows, forward_counts),
        "close_call_samples": _close_call_stats(rows),
        "breadth_forward_validation": _breadth_forward_validation(rows, forward_counts),
        "internal_resonance_forward_validation": _internal_resonance_forward_validation(rows, forward_counts),
        "flow_forward_validation": _flow_forward_validation(rows, forward_counts),
        "by_symbol": {symbol: _edge_bucket_metrics([row for row in rows if row["symbol"] == symbol]) for symbol in TARGET_SYMBOLS},
        "by_regime": _by_regime(rows),
        "conclusion": _edge_report_conclusion(rows, forward_counts),
        "notes": [
            "This report is not proof of alpha; it is a proxy check until forward-only samples mature.",
            "If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.",
            "Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.",
            "Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.",
            "Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.",
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
        f"Forward validation notice: `{report.get('forward_validation_notice')}`",
        f"Conclusion: `{report.get('conclusion')}`",
        "",
        "## Forward Sample Gates",
        "",
    ]
    for horizon, payload in (report.get("minimum_sample_gate") or {}).items():
        lines.append(f"- {horizon}: completed `{payload.get('completed_count')}`, gate `{payload.get('evidence_gate')}`")
    lines.extend(
        [
            "",
            "## By Edge Status",
            "",
        ]
    )
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
    lines.append("### confidence validation")
    lines.append(f"- `{report.get('confidence_validation')}`")
    lines.append("")
    lines.append("## Scenario Checks")
    lines.append("")
    lines.append(f"- primary_scenario_hit_rate: `{report.get('primary_scenario_hit_rate')}`")
    lines.append(f"- primary_vs_secondary: `{report.get('primary_vs_secondary')}`")
    lines.append(f"- close_call_samples: `{report.get('close_call_samples')}`")
    lines.append("")
    lines.append("## Breadth Forward Validation")
    lines.append("")
    breadth = report.get("breadth_forward_validation") or {}
    lines.append(f"- status: `{breadth.get('status')}`")
    lines.append(f"- evidence_note: `{breadth.get('evidence_note')}`")
    for key in (
        "breadth_confirmed_signals",
        "breadth_conflicted_signals",
        "breadth_confirmed_bounce_signals",
        "breadth_conflicted_bounce_signals",
        "breadth_confirmed_reversal_signals",
        "breadth_conflicted_reversal_signals",
        "bounce_with_breadth_support",
        "bounce_without_breadth_support",
        "trend_reversal_with_breadth_support",
        "failed_bounce_risk_with_breadth_conflict",
    ):
        lines.append("")
        lines.append(f"### {key}")
        lines.extend(_metrics_markdown(breadth.get(key, {})))
    lines.append("")
    lines.append("## Internal Resonance Forward Validation")
    lines.append("")
    resonance = report.get("internal_resonance_forward_validation") or {}
    lines.append(f"- status: `{resonance.get('status')}`")
    lines.append(f"- evidence_note: `{resonance.get('evidence_note')}`")
    for key in (
        "aligned_internal_resonance",
        "mixed_internal_resonance",
        "surface_only_strength",
        "bounce_with_internal_resonance",
        "bounce_surface_only",
    ):
        lines.append("")
        lines.append(f"### {key}")
        lines.extend(_metrics_markdown(resonance.get(key, {})))
    lines.append("")
    lines.append("## Flow / Positioning Proxy Forward Validation")
    lines.append("")
    flow = report.get("flow_forward_validation") or {}
    lines.append(f"- status: `{flow.get('status')}`")
    lines.append(f"- evidence_note: `{flow.get('evidence_note')}`")
    for key in (
        "flow_confirmed_signals",
        "flow_conflicted_signals",
        "bounce_with_flow_support",
        "bounce_with_flow_conflict",
        "risk_path_with_flow_conflict",
    ):
        lines.append("")
        lines.append(f"### {key}")
        lines.extend(_metrics_markdown(flow.get(key, {})))
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
    true_breadth_rows = [source_rows.get(name, {}) for name in ("breadth_SPY", "breadth_QQQ", "breadth_DIA")]
    true_breadth_available = all(row.get("real_data") and not row.get("missing_data") for row in true_breadth_rows)
    breadth_quality_values = [_float(row.get("breadth_quality_score"), 0.0) or 0.0 for row in true_breadth_rows if row]
    avg_breadth_quality = sum(breadth_quality_values) / len(breadth_quality_values) if breadth_quality_values else 0.0
    if true_breadth_available and avg_breadth_quality >= 80:
        score += 2.0
    elif coverage.get("breadth", {}).get("status") == "proxy":
        score = min(score, 87.0)
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


def _fred_status_summary(bundle: dict[str, Any]) -> dict[str, Any]:
    return {
        "available": bool(bundle.get("available")),
        "configured": bool(bundle.get("configured")),
        "rate_limited": bool(bundle.get("rate_limited")),
        "fallback_used": bool(bundle.get("fallback_used")),
        "cache_used": bool(bundle.get("cache_used")),
        "successful_series": list(bundle.get("successful_series") or []),
        "failed_series": list(bundle.get("failed_series") or []),
    }


def _options_status_summary(bundle: dict[str, Any]) -> dict[str, Any]:
    summary = (bundle or {}).get("summary") or {}
    return {
        "options_available": bool(summary.get("options_available")),
        "vix_term_available": bool(summary.get("vix_term_available")),
        "vvix_available": bool(summary.get("vvix_available")),
        "skew_available": bool(summary.get("skew_available")),
        "put_call_available": bool(summary.get("put_call_available")),
        "gamma_available": bool(summary.get("gamma_available")),
        "options_partial": bool(summary.get("options_partial")),
        "options_missing": bool(summary.get("options_missing", not bool(bundle))),
        "options_stale": bool(summary.get("options_stale")),
        "options_source": summary.get("options_source") or "missing",
        "options_quality_score": summary.get("options_quality_score") or 0,
        "missing_symbols": list(summary.get("missing_symbols") or []),
    }


def _edge_summary_v4(status: str) -> str:
    if status == "STRONG_EDGE":
        return "多源确认较强，可以给出较明确的概率路径，但仍不是下单依据。"
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


def _internal_resonance_payload(features: dict[str, Any]) -> dict[str, Any]:
    breadth = features.get("breadth") or {}
    components = breadth.get("internal_resonance_components") or {}
    raw_score = breadth.get("internal_resonance_score_raw")
    score = _score01(raw_score, _score01(breadth.get("market_internal_resonance_score"), _score01(breadth.get("breadth_confirmation_score")))) * 100.0
    quality = _score01(breadth.get("internal_resonance_quality_score_raw"), _score01(breadth.get("internal_resonance_quality_score"), _score01(breadth.get("breadth_quality_score"), 0.5))) * 100.0
    state = str(breadth.get("internal_resonance_state") or "unknown")
    label = str(breadth.get("internal_resonance_label") or state)
    surface_only = bool(breadth.get("surface_strength_without_participation")) or state == "surface_only"
    broad_participation = bool(breadth.get("broad_participation")) or state == "aligned"
    supports_bounce = bool(breadth.get("supports_bounce_or_repair")) or state == "aligned"
    supports_downside = bool(breadth.get("supports_downside_or_failed_bounce")) or surface_only
    return {
        "resonance_score": round(score, 2),
        "resonance_state": state,
        "resonance_label": label,
        "resonance_quality_score": round(quality, 2),
        "broad_participation": broad_participation,
        "surface_strength_without_participation": surface_only,
        "supports_bounce_or_repair": supports_bounce,
        "supports_downside_or_failed_bounce": supports_downside,
        "components": components,
        "reason": breadth.get("internal_resonance_reason"),
        "data_note": "Internal resonance checks whether constituent breadth, sector participation, equal-weight and small-cap proxies agree. It is not a standalone alpha.",
    }


def _options_stress_score(vol: dict[str, Any]) -> float:
    explicit = vol.get("option_stress_score")
    if explicit is not None:
        return _score01(explicit, 0.45)
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
            "mean_absolute_return": round(sum(abs(value) for value in values) / len(values), 6),
            "max_adverse_excursion": round(min(values), 6),
            "max_favorable_excursion": round(max(values), 6),
        }
    return payload


def _breadth_forward_validation(rows: list[dict[str, Any]], forward_counts: dict[str, Any]) -> dict[str, Any]:
    confirmed = [row for row in rows if _float(row.get("breadth_confirmation_score"), 0.0) >= 55.0]
    conflicted = [row for row in rows if _float(row.get("breadth_conflict_score"), 0.0) >= 55.0]
    bounce_rows = [row for row in rows if row.get("primary_scenario") == "bounce_path"]
    reversal_rows = [row for row in rows if row.get("strongest_predictor") == "trend_reversal_predictor"]
    downside_rows = [row for row in rows if row.get("strongest_predictor") == "downside_continuation_predictor" or row.get("primary_scenario") == "bearish_path"]
    enough_forward = forward_counts.get("max_completed_count", 0) >= 20
    status = "forward_ready" if enough_forward else "not_enough_forward_samples"
    bounce_confirmed = [row for row in bounce_rows if _float(row.get("breadth_confirmation_score"), 0.0) >= 55.0]
    bounce_conflicted = [row for row in bounce_rows if _float(row.get("breadth_conflict_score"), 0.0) >= 55.0]
    reversal_confirmed = [row for row in reversal_rows if _float(row.get("breadth_confirmation_score"), 0.0) >= 55.0]
    reversal_conflicted = [row for row in reversal_rows if _float(row.get("breadth_conflict_score"), 0.0) >= 55.0]
    return {
        "status": status,
        "completed_sample_counter": forward_counts,
        "evidence_note": (
            "Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof."
            if not enough_forward
            else "Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence."
        ),
        "breadth_confirmed_signals": _edge_bucket_metrics(confirmed),
        "breadth_conflicted_signals": _edge_bucket_metrics(conflicted),
        "breadth_confirmed_bounce_signals": _edge_bucket_metrics(bounce_confirmed),
        "breadth_conflicted_bounce_signals": _edge_bucket_metrics(bounce_conflicted),
        "breadth_confirmed_reversal_signals": _edge_bucket_metrics(reversal_confirmed),
        "breadth_conflicted_reversal_signals": _edge_bucket_metrics(reversal_conflicted),
        "bounce_with_breadth_support": _edge_bucket_metrics(bounce_confirmed),
        "bounce_without_breadth_support": _edge_bucket_metrics([row for row in bounce_rows if _float(row.get("breadth_confirmation_score"), 0.0) < 55.0]),
        "trend_reversal_with_breadth_support": _edge_bucket_metrics(reversal_confirmed),
        "failed_bounce_risk_with_breadth_conflict": _edge_bucket_metrics([row for row in downside_rows if _float(row.get("breadth_conflict_score"), 0.0) >= 55.0]),
        "core_question": "Does breadth confirmation improve forward hit rate / average return versus breadth conflict?",
        "forward_validation_required": not enough_forward,
    }


def _internal_resonance_forward_validation(rows: list[dict[str, Any]], forward_counts: dict[str, Any]) -> dict[str, Any]:
    aligned = [row for row in rows if row.get("internal_resonance_state") == "aligned"]
    mixed = [row for row in rows if row.get("internal_resonance_state") == "mixed"]
    surface_only = [row for row in rows if row.get("surface_strength_without_participation")]
    bounce_aligned = [row for row in rows if row.get("primary_scenario") == "bounce_path" and row.get("internal_resonance_state") == "aligned"]
    bounce_surface_only = [row for row in rows if row.get("primary_scenario") == "bounce_path" and row.get("surface_strength_without_participation")]
    enough_forward = forward_counts.get("max_completed_count", 0) >= 20
    return {
        "status": "forward_ready" if enough_forward else "not_enough_forward_samples",
        "evidence_note": (
            "Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate."
            if not enough_forward
            else "Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence."
        ),
        "aligned_internal_resonance": _edge_bucket_metrics(aligned),
        "mixed_internal_resonance": _edge_bucket_metrics(mixed),
        "surface_only_strength": _edge_bucket_metrics(surface_only),
        "bounce_with_internal_resonance": _edge_bucket_metrics(bounce_aligned),
        "bounce_surface_only": _edge_bucket_metrics(bounce_surface_only),
        "core_question": "Does broad internal resonance beat surface-only index strength in forward returns and path hit rate?",
        "forward_validation_required": not enough_forward,
    }


def _flow_forward_validation(rows: list[dict[str, Any]], forward_counts: dict[str, Any]) -> dict[str, Any]:
    confirmed = [row for row in rows if _float(row.get("flow_confirmation_score"), 0.0) >= 58.0 and _float(row.get("flow_quality_score"), 0.0) >= 45.0]
    conflicted = [row for row in rows if _float(row.get("flow_conflict_score"), 0.0) >= 55.0]
    bounce_rows = [row for row in rows if row.get("primary_scenario") == "bounce_path"]
    risk_rows = [row for row in rows if row.get("primary_scenario") == "bearish_path" or row.get("strongest_predictor") == "risk_expansion_predictor"]
    enough_forward = forward_counts.get("max_completed_count", 0) >= 20
    return {
        "status": "forward_ready" if enough_forward else "not_enough_forward_samples",
        "completed_sample_counter": forward_counts,
        "evidence_note": (
            "Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate."
            if not enough_forward
            else "Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence."
        ),
        "flow_confirmed_signals": _edge_bucket_metrics(confirmed),
        "flow_conflicted_signals": _edge_bucket_metrics(conflicted),
        "bounce_with_flow_support": _edge_bucket_metrics([row for row in bounce_rows if row in confirmed]),
        "bounce_with_flow_conflict": _edge_bucket_metrics([row for row in bounce_rows if row in conflicted]),
        "risk_path_with_flow_conflict": _edge_bucket_metrics([row for row in risk_rows if row in conflicted]),
        "core_question": "Does proxy flow confirmation improve forecast hit rate and path accuracy versus flow conflict?",
        "forward_validation_required": not enough_forward,
        "guardrail": "Proxy flow is not true fund flow or positioning. It can support scenario confirmation only after forward validation.",
    }


def _strongest_predictor_name(predictors: dict[str, Any]) -> str | None:
    if not predictors:
        return None
    return max(predictors.items(), key=lambda item: _float((item[1] or {}).get("probability"), 0.0))[0]


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


def _primary_vs_secondary_proxy(rows: list[dict[str, Any]], forward_counts: dict[str, Any]) -> dict[str, Any]:
    status = "forward_pending" if forward_counts.get("max_completed_count", 0) < 20 else "forward_ready"
    result: dict[str, Any] = {"status": status, "by_horizon": {}}
    for horizon in HORIZONS:
        primary_hits = secondary_hits = total = both_hit = both_miss = 0
        for row in rows:
            value = _float(row.get(f"forward_return_{horizon}d"), None)
            if value is None:
                continue
            primary_hit = _scenario_hit(row.get("primary_scenario"), value)
            secondary_hit = _scenario_hit(row.get("secondary_scenario"), value)
            if primary_hit is None or secondary_hit is None:
                continue
            total += 1
            primary_hits += int(primary_hit)
            secondary_hits += int(secondary_hit)
            both_hit += int(primary_hit and secondary_hit)
            both_miss += int((not primary_hit) and (not secondary_hit))
        result["by_horizon"][f"{horizon}d"] = {
            "sample_size": total,
            "primary_hit_rate": round(primary_hits / total, 4) if total else None,
            "secondary_hit_rate": round(secondary_hits / total, 4) if total else None,
            "primary_minus_secondary": round((primary_hits - secondary_hits) / total, 4) if total else None,
            "both_hit": both_hit,
            "both_miss": both_miss,
        }
    result["note"] = (
        "Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy."
        if status == "forward_pending"
        else "Forward sample gate has opened, but alpha status still requires stable performance over time."
    )
    return result


def _close_call_stats(rows: list[dict[str, Any]]) -> dict[str, Any]:
    close_rows = [row for row in rows if row.get("close_call")]
    non_close_rows = [row for row in rows if not row.get("close_call")]
    return {
        "close_call_sample_size": len(close_rows),
        "non_close_call_sample_size": len(non_close_rows),
        "close_call_metrics": _edge_bucket_metrics(close_rows),
        "non_close_call_metrics": _edge_bucket_metrics(non_close_rows),
        "note": "close_call rows are tracked separately because path probabilities differ by less than eight percentage points.",
    }


def _confidence_validation(rows: list[dict[str, Any]]) -> dict[str, Any]:
    high_conf = _top_fraction(rows, "confidence_score", 0.10)
    high_conf_ids = {id(row) for row in high_conf}
    ordinary = [row for row in rows if id(row) not in high_conf_ids]
    strong = [row for row in rows if row.get("edge_status") == "STRONG_EDGE"]
    moderate = [row for row in rows if row.get("edge_status") == "MODERATE_EDGE"]
    return {
        "strong_edge": _edge_bucket_metrics(strong),
        "moderate_edge": _edge_bucket_metrics(moderate),
        "confidence_top_10": _edge_bucket_metrics(high_conf),
        "ordinary_confidence": _edge_bucket_metrics(ordinary),
        "validation_question": "Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?",
        "status": "forward_validation_required",
    }


def _by_regime(rows: list[dict[str, Any]]) -> dict[str, Any]:
    regimes: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        regimes.setdefault(str(row.get("regime") or "unknown"), []).append(row)
    return {regime: _edge_bucket_metrics(items) for regime, items in regimes.items()}


def _edge_report_conclusion(rows: list[dict[str, Any]], forward_counts: dict[str, Any] | None = None) -> str:
    if forward_counts and forward_counts.get("max_completed_count", 0) < 20:
        return "forward_validation_insufficient_keep_confidence_capped"
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


def _forward_completion_counts() -> dict[str, Any]:
    path = PROJECT_ROOT / "outputs" / "forward_alpha_v1_signals.csv"
    counts = {f"{horizon}d": {"completed_count": 0, "evidence_gate": "insufficient"} for horizon in HORIZONS}
    completed_rows = 0
    if path.exists():
        with path.open("r", encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                if row.get("signal_status") == "completed":
                    completed_rows += 1
                for horizon in HORIZONS:
                    if _float(row.get(f"forward_return_{horizon}d"), None) is not None:
                        counts[f"{horizon}d"]["completed_count"] += 1
    for payload in counts.values():
        payload["evidence_gate"] = _sample_gate(int(payload["completed_count"]))
    max_completed = max((int(payload["completed_count"]) for payload in counts.values()), default=0)
    return {
        "completed_rows": completed_rows,
        "max_completed_count": max_completed,
        "by_horizon": counts,
    }


def _sample_gate(count: int) -> str:
    if count < 20:
        return "insufficient"
    if count <= 50:
        return "early_evidence"
    if count <= 100:
        return "moderate_evidence"
    return "stronger_evidence"


def _scenario_hit(scenario: Any, forward_return: float) -> bool | None:
    direction = _scenario_direction(scenario)
    if direction == 0:
        return None
    if forward_return == 0:
        return False
    return (forward_return > 0 and direction > 0) or (forward_return < 0 and direction < 0)


def _scenario_direction(scenario: Any) -> int:
    if scenario in {"bounce_path", "analog_average_path", "expected_path"}:
        return 1
    if scenario == "bearish_path":
        return -1
    return 0


def _metrics_markdown(payload: dict[str, Any]) -> list[str]:
    lines = [f"- sample_size: `{payload.get('sample_size', 0)}`"]
    for horizon, row in (payload.get("by_horizon") or {}).items():
        lines.append(
            f"- {horizon}: sample `{row.get('sample_size', 0)}`, hit `{row.get('hit_rate')}`, avg `{row.get('avg_return')}`, median `{row.get('median_return')}`, mae `{row.get('mean_absolute_return')}`"
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


def _score01(value: Any, default: float = 0.0) -> float:
    parsed = _float(value, None)
    if parsed is None:
        return default
    if parsed > 1.0:
        parsed = parsed / 100.0
    return _clip(parsed, 0.0, 1.0)


def _clip(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _deepcopy(payload: dict[str, Any]) -> dict[str, Any]:
    import copy

    return copy.deepcopy(payload)
