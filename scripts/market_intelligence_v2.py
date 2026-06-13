from __future__ import annotations

import math
from datetime import datetime, timezone
from typing import Any

from app.services.data_providers.auto_download import DownloadedSeries, is_real_market_data


TARGET_SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
SUPPORT_SYMBOLS = ("^VIX", "HYG", "LQD", "TLT", "UUP", "^TNX")
HORIZONS = (3, 5, 10, 20, 60)


def build_market_intelligence_v2(
    *,
    series_by_symbol: dict[str, DownloadedSeries],
    overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    analogs: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    data_quality = build_data_quality_report(series_by_symbol, overview.get("as_of"))
    feature_snapshot = build_feature_snapshot_v2(series_by_symbol)
    model_confidence_by_symbol: dict[str, Any] = {}

    for symbol in TARGET_SYMBOLS:
        overview_symbol = overview.get("symbols", {}).get(symbol)
        simulated_symbol = simulated_paths.get("symbols", {}).get(symbol)
        if not overview_symbol or not simulated_symbol:
            continue

        analog = analogs.get(symbol, {})
        support = build_period_specific_analog_support(analog)
        state_engine = build_market_state_engine_v2(
            symbol=symbol,
            overview_symbol=overview_symbol,
            feature_snapshot=feature_snapshot.get("symbols", {}).get(symbol, {}),
            analog_support=support,
        )
        confidence = build_model_confidence_score(
            data_quality=data_quality,
            analog=analog,
            analog_support=support,
            state_engine=state_engine,
            overview_symbol=overview_symbol,
        )
        horizon_predictions = build_horizon_predictions(
            simulated_symbol.get("horizon_summary", {}),
            overview_symbol,
            support,
            confidence,
        )
        judgment = build_integrated_judgment(symbol, state_engine, horizon_predictions, support, confidence)
        scenario_weights = build_scenario_weights(overview_symbol, state_engine, support, confidence)
        path_confidence = path_confidence_level(confidence, support, data_quality)

        overview_symbol.update(
            {
                "market_state": state_engine["primary_state"],
                "market_state_v2": state_engine,
                "historical_support_by_horizon": support,
                "model_confidence": confidence,
                "prediction_horizons": horizon_predictions,
                "current_integrated_judgment": judgment,
                "feature_snapshot_v2": feature_snapshot.get("symbols", {}).get(symbol, {}),
            }
        )
        simulated_symbol.update(
            {
                "market_state": state_engine["primary_state"],
                "market_state_v2": state_engine,
                "historical_support_by_horizon": support,
                "model_confidence": confidence,
                "prediction_horizons": horizon_predictions,
                "current_integrated_judgment": judgment,
                "scenario_weights": scenario_weights,
                "path_confidence": path_confidence,
                "path_source_notes": [
                    "历史相似路径：取当前最相似样本后续 3d/5d/10d/20d/60d 的真实表现。",
                    "反抽情景：使用相似样本中 20d 表现较好的四分位路径。",
                    "偏空情景：使用相似样本中 20d 表现较差的四分位路径。",
                    "基准情景：使用相似样本平均路径；所有路径都是概率情景，不是确定预测。",
                ],
                "data_quality": data_quality.get("summary", {}),
            }
        )
        _update_scenario_card_weights(simulated_symbol, scenario_weights)
        model_confidence_by_symbol[symbol] = confidence

    overview["data_quality_summary"] = data_quality.get("summary", {})
    overview["model_confidence_by_symbol"] = model_confidence_by_symbol
    simulated_paths["data_quality_summary"] = data_quality.get("summary", {})
    return {
        "version": "market_intelligence_engine_v2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "data_quality_report": data_quality,
        "feature_snapshot_v2": feature_snapshot,
        "model_confidence_by_symbol": model_confidence_by_symbol,
        "warnings": [
            "Alpha v1 threshold is frozen at 0.32534311 and was not changed.",
            "Options, breadth, macro and flow are explicitly marked unavailable unless real data exists.",
            "Historical analogs are explanation and validation aids, not proof of alpha.",
        ],
    }


def build_data_quality_report(series_by_symbol: dict[str, DownloadedSeries], as_of: str | None) -> dict[str, Any]:
    required = TARGET_SYMBOLS + SUPPORT_SYMBOLS
    source_rows: dict[str, Any] = {}
    latest_dates = [_latest_date(series_by_symbol.get(symbol)) for symbol in required]
    clean_latest = [value for value in latest_dates if value]
    reference_date = max(clean_latest) if clean_latest else as_of

    for symbol in required:
        series = series_by_symbol.get(symbol)
        latest_date = _latest_date(series)
        source = series.source if series else "missing"
        rows = len(series.rows) if series else 0
        real_data = bool(series and is_real_market_data(series))
        fallback_used = source.startswith("local-cache") or "fallback" in source
        source_rows[symbol] = {
            "symbol": symbol,
            "source": source,
            "rows": rows,
            "latest_date": latest_date,
            "real_data": real_data,
            "fallback_used": fallback_used,
            "stale_data": _is_stale(latest_date, reference_date),
            "missing_data": rows == 0,
            "point_in_time_safe": bool(series and series.point_in_time_safe and real_data),
        }

    coverage = _coverage_categories(source_rows)
    completeness_score = _data_completeness_score(coverage, source_rows)
    unavailable = [
        name
        for name, payload in coverage.items()
        if payload["status"] == "not_available"
    ]
    real_market_data = all(source_rows[symbol]["real_data"] for symbol in required)
    any_synthetic = any(row["source"] == "synthetic-fallback" for row in source_rows.values())
    any_fallback = any(row["fallback_used"] for row in source_rows.values())
    any_stale = any(row["stale_data"] for row in source_rows.values())
    any_missing = any(row["missing_data"] for row in source_rows.values())

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "as_of": reference_date or as_of,
        "summary": {
            "data_source_status": "real_market_data" if real_market_data else "partial_or_failed",
            "real_market_data": real_market_data,
            "fallback_used": any_fallback,
            "synthetic_used": any_synthetic,
            "stale_data": any_stale,
            "missing_data": any_missing,
            "data_completeness_score": completeness_score,
            "unavailable_categories": unavailable,
            "latest_date": reference_date,
        },
        "sources": source_rows,
        "coverage_categories": coverage,
        "notes": [
            "price/volatility/credit/rates/liquidity currently use public market proxies.",
            "options breadth macro flow are not treated as available unless real feeds are connected.",
            "synthetic fallback is never allowed to create a live signal.",
        ],
    }


def build_feature_snapshot_v2(series_by_symbol: dict[str, DownloadedSeries]) -> dict[str, Any]:
    closes = {symbol: _closes(series_by_symbol.get(symbol)) for symbol in TARGET_SYMBOLS + SUPPORT_SYMBOLS}
    vix = closes.get("^VIX", [])
    hyg = closes.get("HYG", [])
    lqd = closes.get("LQD", [])
    tlt = closes.get("TLT", [])
    uup = closes.get("UUP", [])
    tnx = closes.get("^TNX", [])
    spy = closes.get("SPY", [])
    qqq = closes.get("QQQ", [])
    iwm = closes.get("IWM", [])
    dia = closes.get("DIA", [])
    symbols: dict[str, Any] = {}

    for symbol in TARGET_SYMBOLS:
        target = closes.get(symbol, [])
        vix_level = _last(vix)
        vix_change_5d = _change(vix, 5)
        vix_change_20d = _change(vix, 20)
        vix_percentile = _percentile_rank(vix, vix_level, 252)
        credit_relative = _relative_return(hyg, lqd, 20)
        hyg_drawdown = _drawdown(hyg, 60)
        tnx_change_20d = _change(tnx, 20)
        tlt_return_20d = _return(tlt, 20)
        uup_return_20d = _return(uup, 20)
        volatility_stress = _clip((vix_percentile or 0.5) + max(vix_change_20d or 0.0, 0.0) * 2.0, 0.0, 1.0)
        credit_deterioration = _clip((-credit_relative * 5.0) + (-hyg_drawdown * 2.5), 0.0, 1.0)
        liquidity_stress = _clip(
            volatility_stress * 0.35
            + max(uup_return_20d, 0.0) * 4.0
            + max(tnx_change_20d, 0.0) * 0.03
            + max(-tlt_return_20d, 0.0) * 2.0,
            0.0,
            1.0,
        )

        symbols[symbol] = {
            "price": {
                "current_price": _last(target),
                "return_20d": _return(target, 20),
                "return_60d": _return(target, 60),
                "drawdown_depth": _drawdown(target, 60),
                "rsi_14": _rsi(target, 14),
                "realized_vol_20d": _realized_vol(target, 20),
            },
            "volatility_options": {
                "vix_level": vix_level,
                "vix_change_5d": vix_change_5d,
                "vix_change_20d": vix_change_20d,
                "vix_percentile_1y": vix_percentile,
                "vix_term_structure": "not_available",
                "vvix": "not_available",
                "put_call_ratio": "not_available",
                "spx_skew": "not_available",
            },
            "credit": {
                "hy_oas": "not_available",
                "ig_oas": "not_available",
                "hyg_lqd_relative_strength_20d": credit_relative,
                "hyg_drawdown_60d": hyg_drawdown,
                "credit_deterioration_score": credit_deterioration,
            },
            "rates_liquidity": {
                "ten_year_yield_proxy": _last(tnx),
                "two_year_yield": "not_available",
                "ten_year_minus_two_year": "not_available",
                "ten_year_minus_three_month": "not_available",
                "tnx_change_20d": tnx_change_20d,
                "tlt_return_20d": tlt_return_20d,
                "uup_return_20d": uup_return_20d,
                "real_yield_proxy": "not_available",
                "liquidity_stress_proxy": liquidity_stress,
            },
            "breadth": {
                "advance_decline": "not_available",
                "new_highs_new_lows": "not_available",
                "percent_above_20_50_200_ma": "not_available",
                "equal_weight_vs_cap_weight": "not_available",
                "sector_participation": "not_available",
            },
            "market_structure": {
                "small_cap_vs_large_cap_20d": _relative_return(iwm, spy, 20),
                "growth_vs_large_cap_20d": _relative_return(qqq, spy, 20),
                "dow_vs_spy_20d": _relative_return(dia, spy, 20),
                "sector_rotation": "not_available",
                "defensive_vs_cyclical": "not_available",
            },
            "macro": {"status": "not_available"},
            "flow": {"status": "not_available"},
        }

    return {
        "version": "market_intelligence_engine_v2_features",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "symbols": symbols,
    }


def build_period_specific_analog_support(analog: dict[str, Any]) -> dict[str, Any]:
    distribution = analog.get("historical_distribution", {})
    sample_count = int(distribution.get("sample_count") or analog.get("sample_count") or 0)
    by_horizon: dict[str, Any] = {}
    for horizon in HORIZONS:
        avg_return = _float_or_none(distribution.get(f"avg_return_{horizon}d"))
        median_return = _float_or_none(distribution.get(f"median_return_{horizon}d"))
        hit_rate = _float_or_none(distribution.get(f"hit_rate_{horizon}d"))
        worst = _float_or_none(distribution.get(f"worst_case_{horizon}d"))
        best = _float_or_none(distribution.get(f"best_case_{horizon}d"))
        support = _support_label(avg_return, hit_rate, sample_count)
        by_horizon[f"{horizon}d"] = {
            "support": support,
            "avg_return": avg_return,
            "median_return": median_return,
            "hit_rate": hit_rate,
            "worst_case": worst,
            "best_case": best,
            "sample_count": sample_count,
        }

    worst_path = _float_or_none(distribution.get("worst_path_max_adverse_excursion"))
    sample_quality = "high" if sample_count >= 20 else "medium" if sample_count >= 8 else "low"
    return {
        "by_horizon": by_horizon,
        "short_term_support": _combine_support([by_horizon["3d"]["support"], by_horizon["5d"]["support"], by_horizon["10d"]["support"]]),
        "medium_term_support": _combine_support([by_horizon["20d"]["support"], by_horizon["60d"]["support"]]),
        "worst_path_risk": _worst_path_risk(worst_path, by_horizon),
        "analog_sample_quality": sample_quality,
        "sample_count": sample_count,
        "low_sample_warning": sample_count < 8,
        "historical_analogs_are_not_proof": True,
    }


def build_market_state_engine_v2(
    *,
    symbol: str,
    overview_symbol: dict[str, Any],
    feature_snapshot: dict[str, Any],
    analog_support: dict[str, Any],
) -> dict[str, Any]:
    price = feature_snapshot.get("price", {})
    vol = feature_snapshot.get("volatility_options", {})
    credit = feature_snapshot.get("credit", {})
    rates = feature_snapshot.get("rates_liquidity", {})
    bounce = float(overview_symbol.get("bounce_probability") or 0.0)
    downside = float(overview_symbol.get("downside_continuation_probability") or 0.0)
    reversal = float(overview_symbol.get("trend_reversal_probability") or 0.0)
    live_signal = bool(overview_symbol.get("live_signal"))
    return_20d = _float_or_none(price.get("return_20d")) or 0.0
    return_60d = _float_or_none(price.get("return_60d")) or 0.0
    drawdown = _float_or_none(price.get("drawdown_depth")) or 0.0
    rsi = _float_or_none(price.get("rsi_14")) or 50.0
    vix_pct = _float_or_none(vol.get("vix_percentile_1y")) or 0.5
    credit_stress = _float_or_none(credit.get("credit_deterioration_score")) or 0.0
    liquidity_stress = _float_or_none(rates.get("liquidity_stress_proxy")) or 0.0
    short_support = analog_support.get("short_term_support", "neutral")
    medium_support = analog_support.get("medium_term_support", "neutral")
    worst_risk = analog_support.get("worst_path_risk", "medium")

    oversold = _clip((45.0 - rsi) / 25.0 + abs(min(drawdown, 0.0)) * 3.0, 0.0, 1.0)
    stress = _clip(vix_pct * 0.45 + credit_stress * 0.30 + liquidity_stress * 0.25, 0.0, 1.0)
    trend_strength = _clip(return_60d * 3.0 + max(return_20d, 0.0) * 2.0, 0.0, 1.0)
    weak_analog = 1.0 if short_support == "weak" else 0.4 if short_support == "neutral" else 0.0
    supportive_analog = 1.0 if medium_support == "supportive" else 0.4 if medium_support == "neutral" else 0.0

    raw_scores = {
        "risk_on": 0.20 + trend_strength * 0.45 + max(0.0, 0.55 - stress) * 0.35,
        "risk_off": 0.18 + downside * 0.35 + stress * 0.45,
        "oversold_bounce": 0.20 + bounce * 0.40 + oversold * 0.25 + (0.15 if live_signal else 0.0) + supportive_analog * 0.10,
        "failed_bounce_risk": 0.18 + bounce * 0.18 + downside * 0.30 + stress * 0.25 + weak_analog * 0.18,
        "downside_continuation": 0.18 + downside * 0.42 + weak_analog * 0.18 + stress * 0.22,
        "sideways": 0.34 + max(0.0, 0.04 - abs(return_20d)) * 4.0 + (0.10 if short_support == "neutral" else 0.0),
        "recovery": 0.18 + reversal * 0.35 + supportive_analog * 0.22 + max(0.0, 0.60 - stress) * 0.20,
        "panic": 0.08 + max(0.0, stress - 0.65) * 0.75 + (0.10 if worst_risk == "high" else 0.0),
        "no_edge": 0.20 + (0.20 if bounce < 0.25 else 0.0) + (0.15 if analog_support.get("analog_sample_quality") == "low" else 0.0),
    }
    probabilities = _normalize(raw_scores)
    primary_state = max(probabilities, key=probabilities.get)
    states = {
        name: {
            "probability": round(prob, 4),
            "reason": _state_reason(name, symbol),
            "supporting_features": _state_supporting_features(name, live_signal, short_support, medium_support, stress, oversold, downside),
            "conflicting_features": _state_conflicting_features(name, short_support, medium_support, stress, credit_stress, liquidity_stress),
            "confidence": round(_clip(prob * 0.7 + (1.0 - abs(0.5 - stress)) * 0.15 + 0.15, 0.0, 1.0), 4),
        }
        for name, prob in probabilities.items()
    }
    return {
        "version": "market_state_engine_v2",
        "primary_state": primary_state,
        "states": states,
        "stress_inputs": {
            "vix_percentile": vix_pct,
            "credit_deterioration_score": credit_stress,
            "liquidity_stress_proxy": liquidity_stress,
            "combined_market_stress": stress,
            "oversold_score": oversold,
        },
    }


def build_horizon_predictions(
    horizon_summary: dict[str, Any],
    overview_symbol: dict[str, Any],
    analog_support: dict[str, Any],
    confidence: dict[str, Any],
) -> dict[str, Any]:
    predictions: dict[str, Any] = {}
    bounce = float(overview_symbol.get("bounce_probability") or 0.0)
    failed_base = float(overview_symbol.get("downside_continuation_probability") or 0.0)
    confidence_scalar = float(confidence.get("confidence_score") or 0.0) / 100.0
    for horizon in HORIZONS:
        key = f"{horizon}d"
        summary = horizon_summary.get(key, {})
        support = analog_support.get("by_horizon", {}).get(key, {})
        expected = _float_or_none(summary.get("expected_return")) or support.get("avg_return") or 0.0
        worst = _float_or_none(support.get("worst_case"))
        best = _float_or_none(support.get("best_case"))
        up_probability = _clip(float(summary.get("up_probability") or 0.5), 0.01, 0.99)
        down_probability = _clip(float(summary.get("down_probability") or 0.5), 0.01, 0.99)
        if support.get("support") == "weak":
            down_probability = _clip(down_probability + 0.08, 0.01, 0.99)
            up_probability = _clip(up_probability - 0.05, 0.01, 0.99)
        elif support.get("support") == "supportive":
            up_probability = _clip(up_probability + 0.06, 0.01, 0.99)
            down_probability = _clip(down_probability - 0.04, 0.01, 0.99)
        total = up_probability + down_probability
        if total > 1:
            up_probability, down_probability = up_probability / total, down_probability / total
        predictions[key] = {
            "expected_direction": _expected_direction(expected, up_probability, down_probability, support.get("support")),
            "expected_return": expected,
            "expected_return_range": [
                worst if worst is not None else expected - 0.02,
                best if best is not None else expected + 0.02,
            ],
            "up_probability": up_probability,
            "down_probability": down_probability,
            "bounce_probability": _clip(bounce + (0.05 if support.get("support") == "supportive" else -0.04 if support.get("support") == "weak" else 0.0), 0.0, 1.0),
            "failed_bounce_risk": _clip(failed_base + (0.10 if support.get("support") == "weak" else 0.0), 0.0, 1.0),
            "confidence": round(_clip(confidence_scalar * (0.9 if support.get("sample_count", 0) >= 8 else 0.65), 0.0, 1.0), 4),
            "historical_support": support.get("support", "neutral"),
        }
    return predictions


def build_model_confidence_score(
    *,
    data_quality: dict[str, Any],
    analog: dict[str, Any],
    analog_support: dict[str, Any],
    state_engine: dict[str, Any],
    overview_symbol: dict[str, Any],
) -> dict[str, Any]:
    completeness = float(data_quality.get("summary", {}).get("data_completeness_score") or 0.0) / 100.0
    coverage = data_quality.get("coverage_categories", {})
    available_or_partial = sum(1 for payload in coverage.values() if payload.get("status") in {"available", "partial"})
    feature_availability = available_or_partial / max(len(coverage), 1)
    sample_count = int(analog_support.get("sample_count") or analog.get("sample_count") or 0)
    analog_sample_score = _clip(sample_count / 20.0, 0.0, 1.0)
    hit_values = [
        _float_or_none(payload.get("hit_rate"))
        for payload in analog_support.get("by_horizon", {}).values()
    ]
    clean_hits = [value for value in hit_values if value is not None]
    historical_hit_rate = sum(clean_hits) / len(clean_hits) if clean_hits else 0.50
    primary_probability = max((state.get("probability", 0.0) for state in state_engine.get("states", {}).values()), default=0.0)
    signal_agreement = _signal_agreement(overview_symbol, analog_support, state_engine)
    conflict_level = _conflict_level(overview_symbol, analog_support, state_engine)
    calibration_quality = 0.45
    raw_score = (
        completeness * 24.0
        + feature_availability * 14.0
        + analog_sample_score * 18.0
        + historical_hit_rate * 14.0
        + calibration_quality * 12.0
        + signal_agreement * 12.0
        + primary_probability * 6.0
        - conflict_level * 10.0
    )
    missing_hard_data = [
        name
        for name in ("options", "breadth", "macro", "flow")
        if coverage.get(name, {}).get("status") == "not_available"
    ]
    cap = 65.0 if missing_hard_data else 85.0
    score = int(round(_clip(raw_score, 0.0, cap)))
    level = "high" if score >= 75 else "medium" if score >= 50 else "low"
    why_limited = []
    if missing_hard_data:
        why_limited.append(f"缺少真实 {', '.join(missing_hard_data)} 数据，可信度上限被限制。")
    if calibration_quality < 0.60:
        why_limited.append("当前仍是 forward-only observation，概率校准样本不足。")
    if conflict_level > 0.45:
        why_limited.append("信号之间存在冲突，尤其是反抽与下跌延续风险同时存在。")
    if sample_count < 8:
        why_limited.append("历史相似样本数量偏少。")
    return {
        "confidence_score": score,
        "confidence_level": level,
        "components": {
            "data_completeness": completeness,
            "feature_availability": feature_availability,
            "analog_sample_size": analog_sample_score,
            "historical_hit_rate": historical_hit_rate,
            "calibration_quality": calibration_quality,
            "signal_agreement": signal_agreement,
            "conflict_level": conflict_level,
        },
        "why_confidence_is_limited": why_limited or ["当前没有明显硬性限制，但仍不是确定性预测。"],
    }


def build_integrated_judgment(
    symbol: str,
    state_engine: dict[str, Any],
    horizon_predictions: dict[str, Any],
    analog_support: dict[str, Any],
    confidence: dict[str, Any],
) -> str:
    state = state_engine.get("primary_state", "no_edge")
    support_5d = horizon_predictions.get("5d", {}).get("historical_support", "neutral")
    support_20d = horizon_predictions.get("20d", {}).get("historical_support", "neutral")
    support_60d = horizon_predictions.get("60d", {}).get("historical_support", "neutral")
    risk = analog_support.get("worst_path_risk", "medium")
    state_cn = _state_cn(state)
    return (
        f"{symbol} 当前综合状态偏向“{state_cn}”。"
        f"短线 5d 历史支持为 {support_5d}，20d 为 {support_20d}，60d 为 {support_60d}；"
        f"最坏路径风险为 {risk}。"
        f"模型可信度为 {confidence.get('confidence_level')}（{confidence.get('confidence_score')} 分）。"
        "这代表概率情景，不代表确定走势。"
    )


def build_scenario_weights(
    overview_symbol: dict[str, Any],
    state_engine: dict[str, Any],
    analog_support: dict[str, Any],
    confidence: dict[str, Any],
) -> dict[str, float]:
    bounce = float(overview_symbol.get("bounce_probability") or 0.0)
    downside = float(overview_symbol.get("downside_continuation_probability") or 0.0)
    state = state_engine.get("primary_state", "no_edge")
    medium_support = analog_support.get("medium_term_support", "neutral")
    confidence_scalar = float(confidence.get("confidence_score") or 0) / 100.0
    raw = {
        "base_scenario": 0.28 + (1.0 - confidence_scalar) * 0.10,
        "bounce_scenario": 0.18 + bounce * 0.55 + (0.10 if medium_support == "supportive" else 0.0),
        "bearish_scenario": 0.16 + downside * 0.45 + (0.10 if state in {"risk_off", "panic", "failed_bounce_risk"} else 0.0),
        "historical_analog_average": 0.20 + (0.08 if analog_support.get("sample_count", 0) >= 20 else 0.0),
    }
    total = sum(raw.values())
    return {key: round(value / total, 4) for key, value in raw.items()}


def path_confidence_level(confidence: dict[str, Any], support: dict[str, Any], data_quality: dict[str, Any]) -> str:
    score = int(confidence.get("confidence_score") or 0)
    if support.get("low_sample_warning") or data_quality.get("summary", {}).get("data_completeness_score", 0) < 55:
        return "low"
    if score >= 65:
        return "medium"
    return "low"


def _update_scenario_card_weights(simulated_symbol: dict[str, Any], weights: dict[str, float]) -> None:
    mapping = {
        "Base case": "base_scenario",
        "Bounce case": "bounce_scenario",
        "Bearish case": "bearish_scenario",
        "Historical analog case": "historical_analog_average",
    }
    for card in simulated_symbol.get("scenario_cards", []):
        key = mapping.get(card.get("name"))
        if key:
            card["probability_weight"] = weights[key]


def _coverage_categories(source_rows: dict[str, Any]) -> dict[str, Any]:
    real = lambda symbol: bool(source_rows.get(symbol, {}).get("real_data"))
    target_count = sum(1 for symbol in TARGET_SYMBOLS if real(symbol))
    return {
        "price": _coverage_payload("available" if target_count == len(TARGET_SYMBOLS) else "partial", "SPY/QQQ/IWM/DIA OHLCV", target_count, len(TARGET_SYMBOLS)),
        "volatility": _coverage_payload("available" if real("^VIX") else "not_available", "VIX level/change/percentile proxy", int(real("^VIX")), 1),
        "credit": _coverage_payload("partial" if real("HYG") and real("LQD") else "not_available", "HYG/LQD proxy only; HY OAS and IG OAS not connected", int(real("HYG")) + int(real("LQD")), 4),
        "rates": _coverage_payload("partial" if real("^TNX") else "not_available", "10Y yield proxy via ^TNX; 2Y/3M curve not connected", int(real("^TNX")), 4),
        "liquidity": _coverage_payload("partial" if real("TLT") and real("UUP") else "not_available", "TLT/UUP/^TNX proxy only; reserves/repo/TGA not connected", int(real("TLT")) + int(real("UUP")) + int(real("^TNX")), 5),
        "breadth": _coverage_payload("not_available", "advance/decline, highs/lows, percent above MA not connected", 0, 5),
        "options": _coverage_payload("not_available", "VVIX, put/call, skew, gamma and option flow are not connected; VIX is counted under volatility only", 0, 5),
        "macro": _coverage_payload("not_available", "economic releases and revisions not connected", 0, 5),
        "flow": _coverage_payload("not_available", "ETF flow, dealer positioning and fund flow not connected", 0, 5),
        "market_structure": _coverage_payload("partial" if target_count == len(TARGET_SYMBOLS) else "not_available", "small/large and growth/value ETF proxy; sectors not connected", target_count, 8),
    }


def _coverage_payload(status: str, detail: str, available_items: int, expected_items: int) -> dict[str, Any]:
    return {
        "status": status,
        "detail": detail,
        "available_items": available_items,
        "expected_items": expected_items,
    }


def _data_completeness_score(coverage: dict[str, Any], source_rows: dict[str, Any]) -> int:
    weights = {
        "price": 20,
        "volatility": 15,
        "credit": 15,
        "rates": 10,
        "liquidity": 10,
        "breadth": 10,
        "options": 5,
        "macro": 5,
        "flow": 5,
        "market_structure": 5,
    }
    status_value = {"available": 1.0, "partial": 0.55, "not_available": 0.0}
    score = sum(weights[name] * status_value.get(payload.get("status"), 0.0) for name, payload in coverage.items())
    if any(row.get("stale_data") for row in source_rows.values()):
        score -= 8
    if any(row.get("source") == "synthetic-fallback" for row in source_rows.values()):
        score -= 20
    return int(round(_clip(score, 0.0, 100.0)))


def _support_label(avg_return: float | None, hit_rate: float | None, sample_count: int) -> str:
    if sample_count < 8:
        return "low_sample"
    if avg_return is not None and hit_rate is not None and avg_return > 0 and hit_rate >= 0.55:
        return "supportive"
    if (avg_return is not None and avg_return < 0) or (hit_rate is not None and hit_rate < 0.50):
        return "weak"
    return "neutral"


def _combine_support(values: list[str]) -> str:
    if "weak" in values:
        return "weak"
    if values.count("supportive") >= 1:
        return "supportive"
    if "low_sample" in values:
        return "low_sample"
    return "neutral"


def _worst_path_risk(worst_path: float | None, by_horizon: dict[str, Any]) -> str:
    worst_values = [worst_path] + [payload.get("worst_case") for payload in by_horizon.values()]
    clean = [float(value) for value in worst_values if value is not None and math.isfinite(float(value))]
    if not clean:
        return "unknown"
    worst = min(clean)
    if worst <= -0.08:
        return "high"
    if worst <= -0.035:
        return "medium"
    return "low"


def _state_reason(state: str, symbol: str) -> str:
    reasons = {
        "risk_on": f"{symbol} 的趋势和压力代理更偏风险偏好。",
        "risk_off": "波动、信用或流动性压力偏高。",
        "oversold_bounce": "反抽概率、超跌程度和历史样本共同指向短中期反抽候选。",
        "failed_bounce_risk": "反抽信号存在，但下跌延续和压力代理仍有冲突。",
        "downside_continuation": "历史样本或压力代理显示下跌延续风险偏高。",
        "sideways": "方向信号不够集中，更像震荡观察。",
        "recovery": "中期历史样本和趋势修复概率更好。",
        "panic": "压力代理接近危机场景，需要降低推断强度。",
        "no_edge": "信号不足，当前不应强行预测。",
    }
    return reasons[state]


def _state_supporting_features(
    state: str,
    live_signal: bool,
    short_support: str,
    medium_support: str,
    stress: float,
    oversold: float,
    downside: float,
) -> list[str]:
    features: list[str] = []
    if live_signal:
        features.append("Alpha v1 当前触发反抽候选。")
    if short_support == "supportive" or medium_support == "supportive":
        features.append("历史相似样本存在正向支持。")
    if oversold > 0.45:
        features.append("价格处于相对超跌区间。")
    if stress > 0.55:
        features.append("波动/信用/流动性压力偏高。")
    if downside > 0.55:
        features.append("下跌延续概率偏高。")
    if not features:
        features.append("没有单一强特征，判断来自多因子组合。")
    return features[:4]


def _state_conflicting_features(
    state: str,
    short_support: str,
    medium_support: str,
    stress: float,
    credit_stress: float,
    liquidity_stress: float,
) -> list[str]:
    conflicts: list[str] = []
    if short_support == "weak" and state in {"oversold_bounce", "recovery", "risk_on"}:
        conflicts.append("短周期历史样本偏弱。")
    if medium_support == "weak" and state in {"oversold_bounce", "recovery", "risk_on"}:
        conflicts.append("中周期历史样本不支持。")
    if stress > 0.60 and state in {"oversold_bounce", "risk_on", "recovery"}:
        conflicts.append("市场压力仍偏高，反抽可能失败。")
    if credit_stress > 0.50:
        conflicts.append("信用代理恶化。")
    if liquidity_stress > 0.50:
        conflicts.append("流动性压力代理偏高。")
    if not conflicts:
        conflicts.append("当前未发现明显一阶冲突。")
    return conflicts[:4]


def _expected_direction(expected: float, up_probability: float, down_probability: float, support: str | None) -> str:
    if down_probability > up_probability + 0.08 or support == "weak":
        return "偏下行/反抽失败风险"
    if expected > 0 and up_probability >= down_probability:
        return "偏上行/反抽"
    if abs(expected) < 0.003:
        return "震荡"
    return "轻微上行" if expected > 0 else "轻微下行"


def _signal_agreement(overview_symbol: dict[str, Any], analog_support: dict[str, Any], state_engine: dict[str, Any]) -> float:
    agreement = 0.35
    state = state_engine.get("primary_state")
    if overview_symbol.get("live_signal") and state in {"oversold_bounce", "recovery"}:
        agreement += 0.25
    if analog_support.get("medium_term_support") == "supportive":
        agreement += 0.20
    if analog_support.get("short_term_support") == "weak":
        agreement -= 0.12
    if state in {"failed_bounce_risk", "downside_continuation", "panic"}:
        agreement -= 0.10
    return _clip(agreement, 0.0, 1.0)


def _conflict_level(overview_symbol: dict[str, Any], analog_support: dict[str, Any], state_engine: dict[str, Any]) -> float:
    conflict = 0.15
    if overview_symbol.get("live_signal") and analog_support.get("short_term_support") == "weak":
        conflict += 0.25
    if float(overview_symbol.get("bounce_probability") or 0.0) > 0.45 and float(overview_symbol.get("downside_continuation_probability") or 0.0) > 0.50:
        conflict += 0.20
    stress = state_engine.get("stress_inputs", {}).get("combined_market_stress", 0.0)
    if stress > 0.60:
        conflict += 0.20
    return _clip(conflict, 0.0, 1.0)


def _state_cn(state: str) -> str:
    return {
        "risk_on": "风险偏好",
        "risk_off": "风险偏弱",
        "oversold_bounce": "超跌反抽",
        "failed_bounce_risk": "反抽失败风险",
        "downside_continuation": "下跌延续",
        "sideways": "震荡观察",
        "recovery": "修复中",
        "panic": "恐慌压力",
        "no_edge": "暂无优势",
    }.get(state, state)


def _normalize(scores: dict[str, float]) -> dict[str, float]:
    clean = {key: max(0.001, float(value)) for key, value in scores.items()}
    total = sum(clean.values())
    return {key: value / total for key, value in clean.items()}


def _latest_date(series: DownloadedSeries | None) -> str | None:
    if not series or not series.rows:
        return None
    return max(str(row["date"]) for row in series.rows if row.get("date"))


def _is_stale(latest_date: str | None, reference_date: str | None) -> bool:
    if not latest_date or not reference_date:
        return True
    try:
        latest = datetime.fromisoformat(latest_date).date()
        reference = datetime.fromisoformat(reference_date).date()
    except ValueError:
        return True
    return (reference - latest).days > 5


def _closes(series: DownloadedSeries | None) -> list[float]:
    if not series:
        return []
    return [float(row["close"]) for row in series.rows if row.get("close") is not None and float(row.get("close") or 0.0) > 0]


def _last(values: list[float]) -> float | None:
    return values[-1] if values else None


def _return(values: list[float], lookback: int) -> float:
    if len(values) <= lookback or values[-lookback - 1] == 0:
        return 0.0
    return values[-1] / values[-lookback - 1] - 1.0


def _change(values: list[float], lookback: int) -> float:
    if len(values) <= lookback:
        return 0.0
    return values[-1] - values[-lookback - 1]


def _relative_return(left: list[float], right: list[float], lookback: int) -> float:
    return _return(left, lookback) - _return(right, lookback)


def _drawdown(values: list[float], lookback: int) -> float:
    if not values:
        return 0.0
    window = values[-lookback:] if len(values) >= lookback else values
    peak = max(window)
    return values[-1] / peak - 1.0 if peak else 0.0


def _percentile_rank(values: list[float], value: float | None, lookback: int) -> float | None:
    if value is None or not values:
        return None
    window = values[-lookback:] if len(values) >= lookback else values
    below = sum(1 for item in window if item <= value)
    return below / len(window) if window else None


def _rsi(values: list[float], period: int) -> float:
    if len(values) <= period:
        return 50.0
    gains: list[float] = []
    losses: list[float] = []
    for previous, current in zip(values[-period - 1 : -1], values[-period:]):
        change = current - previous
        gains.append(max(change, 0.0))
        losses.append(abs(min(change, 0.0)))
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))


def _realized_vol(values: list[float], lookback: int) -> float:
    if len(values) <= lookback:
        return 0.0
    returns = [
        values[index] / values[index - 1] - 1.0
        for index in range(len(values) - lookback, len(values))
        if values[index - 1] != 0
    ]
    if not returns:
        return 0.0
    mean = sum(returns) / len(returns)
    variance = sum((value - mean) ** 2 for value in returns) / len(returns)
    return math.sqrt(variance) * math.sqrt(252.0)


def _float_or_none(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _clip(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))
