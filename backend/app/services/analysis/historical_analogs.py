from __future__ import annotations

import math
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BACKEND_ROOT = Path(__file__).resolve().parents[3]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.services.data_providers.auto_download import DownloadedSeries, is_real_market_data, refresh_market_data
from app.services.validation.forward_alpha_tracker import ALPHA_STATUS, FROZEN_BOUNCE_THRESHOLD, SIGNAL_NAME, load_check_rows


TARGET_SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
SUPPORT_SYMBOLS = ("^VIX", "HYG", "LQD", "TLT", "UUP", "^TNX")
HORIZONS = (3, 5, 10, 20, 60)
MIN_ANALOG_SAMPLE = 8
SIMILARITY_FEATURES = (
    "return_20d",
    "return_60d",
    "drawdown_depth",
    "rsi_14",
    "vix_level",
    "vix_change_5d",
    "vix_change_20d",
    "credit_spread_proxy",
    "hyg_lqd_relative_strength",
    "tlt_return_20d",
    "uup_return_20d",
    "tnx_change_20d",
    "liquidity_proxy",
    "bounce_probability",
    "volatility_contribution",
    "market_stress_score",
)
ANALOG_WARNING = "Historical analogs are not proof of alpha and cannot upgrade alpha_v1 without forward validation."


@dataclass(frozen=True)
class PriceSeries:
    symbol: str
    source: str
    point_in_time_safe: bool
    close_by_date: dict[str, float]


def build_historical_analog_report(
    symbol: str = "SPY",
    *,
    top_k: int = 20,
    alpha_v1_only: bool = False,
    regime_filtered: bool = False,
) -> dict[str, Any]:
    normalized = _normalize_symbol(symbol)
    top_k = max(1, min(int(top_k), 100))
    series_by_symbol = _load_price_series()
    data_status = _data_source_status(series_by_symbol)
    if data_status != "real_market_data":
        return _failed_report(normalized, data_status)

    memory = build_historical_market_memory(normalized, series_by_symbol)
    if len(memory) < MIN_ANALOG_SAMPLE + 1:
        return _low_memory_report(normalized, memory, data_status)

    current = _apply_official_alpha_snapshot(normalized, memory[-1])
    candidates = [sample for sample in memory if sample["date"] < current["date"] and _has_future_returns(sample)]
    if alpha_v1_only:
        candidates = [sample for sample in candidates if sample["alpha_v1_triggered"]]
    if regime_filtered:
        candidates = [sample for sample in candidates if sample["market_regime"] == current["market_regime"]]

    if not candidates:
        return _no_candidate_report(normalized, current, data_status, alpha_v1_only, regime_filtered)

    ranked = _rank_analogs(current, candidates)
    top_cases = ranked[:top_k]
    top_payload = [_case_payload(current, case) for case in top_cases]
    distribution = _historical_distribution(top_cases)
    same_regime_count = sum(1 for sample in candidates if sample["market_regime"] == current["market_regime"])
    support = _historical_support(current, distribution, len(top_cases))

    return {
        "symbol": normalized,
        "as_of": current["date"],
        "data_source_status": data_status,
        "data_sources": {name: series.source for name, series in sorted(series_by_symbol.items())},
        "current_regime": current["market_regime"],
        "alpha_v1_status": ALPHA_STATUS,
        "signal_name": SIGNAL_NAME,
        "threshold": FROZEN_BOUNCE_THRESHOLD,
        "current_bounce_probability": current["bounce_probability"],
        "distance_to_threshold": FROZEN_BOUNCE_THRESHOLD - current["bounce_probability"],
        "current_alpha_v1_triggered": current["alpha_v1_triggered"],
        "similarity_methods": {
            "zscore_euclidean": "similarity_score_euclidean",
            "cosine": "similarity_score_cosine",
            "regime_filtered_nearest_neighbors": "same_regime_rank",
            "combined": "similarity_score",
        },
        "sample_count": len(top_cases),
        "candidate_count": len(candidates),
        "same_regime_candidate_count": same_regime_count,
        "low_sample_warning": len(top_cases) < MIN_ANALOG_SAMPLE,
        "crisis_sample_warning": _crisis_sample_warning(current["market_regime"], same_regime_count),
        "top_similar_cases": top_payload,
        "historical_distribution": distribution,
        "interpretation": {
            "supports_bounce_alpha": support == "supportive",
            "historical_support": support,
            "confidence_note": _confidence_note(len(top_cases), alpha_v1_only, regime_filtered),
            "risk_note": _risk_note(current, distribution, same_regime_count),
            "not_proof_of_alpha": ANALOG_WARNING,
        },
    }


def build_alpha_v1_analog_report(symbol: str = "SPY", *, top_k: int = 20) -> dict[str, Any]:
    return build_historical_analog_report(symbol, top_k=top_k, alpha_v1_only=True)


def build_similar_days_payload(symbol: str = "SPY", *, top_k: int = 20) -> dict[str, Any]:
    report = build_historical_analog_report(symbol, top_k=top_k)
    return {
        "symbol": report.get("symbol", _normalize_symbol(symbol)),
        "as_of": report.get("as_of"),
        "current_regime": report.get("current_regime"),
        "alpha_v1_status": report.get("alpha_v1_status", ALPHA_STATUS),
        "data_source_status": report.get("data_source_status"),
        "sample_count": report.get("sample_count", 0),
        "low_sample_warning": report.get("low_sample_warning", True),
        "top_similar_cases": report.get("top_similar_cases", []),
        "historical_distribution": report.get("historical_distribution", {}),
        "interpretation": report.get("interpretation", {}),
    }


def build_historical_market_memory(symbol: str, series_by_symbol: dict[str, PriceSeries] | None = None) -> list[dict[str, Any]]:
    normalized = _normalize_symbol(symbol)
    series_by_symbol = series_by_symbol or _load_price_series()
    target = series_by_symbol[normalized]
    required = [normalized, *SUPPORT_SYMBOLS]
    aligned_dates = _aligned_dates(series_by_symbol, required)
    memory: list[dict[str, Any]] = []
    for index in range(80, len(aligned_dates)):
        sample_date = aligned_dates[index]
        features = _build_feature_snapshot(normalized, sample_date, index, aligned_dates, series_by_symbol)
        if not features:
            continue
        close_price = target.close_by_date[sample_date]
        future_returns = {
            f"forward_return_{horizon}d": _forward_return(target, aligned_dates, index, horizon)
            for horizon in HORIZONS
        }
        max_favorable, max_adverse = _future_excursions(target, aligned_dates, index, max(HORIZONS))
        future_path = _future_path_flags(future_returns, max_favorable, max_adverse)
        memory.append(
            {
                "date": sample_date,
                "symbol": normalized,
                "close_price": close_price,
                "market_regime": _classify_regime(features),
                "price_features": _select(features, ("return_20d", "return_60d", "drawdown_depth", "rsi_14")),
                "volatility_features": _select(features, ("vix_level", "vix_change_5d", "vix_change_20d", "volatility_contribution")),
                "credit_features": _select(features, ("credit_spread_proxy", "hyg_lqd_relative_strength")),
                "liquidity_features": _select(features, ("liquidity_proxy", "market_stress_score")),
                "rates_macro_features": _select(features, ("tlt_return_20d", "uup_return_20d", "tnx_change_20d")),
                "breadth_features": _select(features, ("return_20d", "drawdown_depth")),
                "feature_vector": _select(features, SIMILARITY_FEATURES),
                "bounce_probability": features["bounce_probability"],
                "crash_probability": features["crash_probability"],
                "trend_probability": features["trend_probability"],
                "alpha_v1_triggered": features["bounce_probability"] >= FROZEN_BOUNCE_THRESHOLD,
                **future_returns,
                "max_favorable_excursion": max_favorable,
                "max_adverse_excursion": max_adverse,
                **future_path,
            }
        )
    return memory


def _load_price_series(lookback_days: int = 5200) -> dict[str, PriceSeries]:
    downloaded = refresh_market_data(symbols=TARGET_SYMBOLS + SUPPORT_SYMBOLS, lookback_days=lookback_days)
    return {series.symbol: _to_price_series(series) for series in downloaded}


def _apply_official_alpha_snapshot(symbol: str, current: dict[str, Any]) -> dict[str, Any]:
    official = _official_alpha_snapshot(symbol, current["date"])
    if not official:
        return current
    updated = dict(current)
    feature_vector = dict(updated["feature_vector"])
    feature_vector["bounce_probability"] = official["bounce_probability"]
    updated["feature_vector"] = feature_vector
    updated["bounce_probability"] = official["bounce_probability"]
    updated["alpha_v1_triggered"] = official["live_signal"]
    if official.get("regime"):
        updated["market_regime"] = official["regime"]
    return updated


def _official_alpha_snapshot(symbol: str, as_of: str) -> dict[str, Any] | None:
    rows = [row for row in load_check_rows() if row.get("symbol") == symbol and row.get("check_date") == as_of]
    if not rows:
        return None
    row = rows[-1]
    try:
        bounce_probability = float(row["bounce_probability"])
    except (KeyError, TypeError, ValueError):
        return None
    return {
        "bounce_probability": bounce_probability,
        "live_signal": str(row.get("live_signal", "")).lower() == "true",
        "regime": row.get("regime") or None,
    }


def _to_price_series(series: DownloadedSeries) -> PriceSeries:
    return PriceSeries(
        symbol=series.symbol,
        source=series.source,
        point_in_time_safe=series.point_in_time_safe and is_real_market_data(series),
        close_by_date={
            str(row["date"]): float(row["close"])
            for row in series.rows
            if row.get("date") and float(row.get("close") or 0.0) > 0
        },
    )


def _data_source_status(series_by_symbol: dict[str, PriceSeries]) -> str:
    required = set(TARGET_SYMBOLS + SUPPORT_SYMBOLS)
    if not required.issubset(series_by_symbol):
        return "failed"
    if all(series_by_symbol[symbol].point_in_time_safe for symbol in required):
        return "real_market_data"
    return "synthetic_fallback_no_signal"


def _aligned_dates(series_by_symbol: dict[str, PriceSeries], symbols: list[str]) -> list[str]:
    common: set[str] | None = None
    for symbol in symbols:
        dates = set(series_by_symbol[symbol].close_by_date)
        common = dates if common is None else common.intersection(dates)
    return sorted(common or [])


def _build_feature_snapshot(
    symbol: str,
    sample_date: str,
    index: int,
    dates: list[str],
    series_by_symbol: dict[str, PriceSeries],
) -> dict[str, float]:
    target = series_by_symbol[symbol]
    vix = series_by_symbol["^VIX"]
    hyg = series_by_symbol["HYG"]
    lqd = series_by_symbol["LQD"]
    tlt = series_by_symbol["TLT"]
    uup = series_by_symbol["UUP"]
    tnx = series_by_symbol["^TNX"]

    return_20d = _trailing_return(target, dates, index, 20)
    return_60d = _trailing_return(target, dates, index, 60)
    drawdown_depth = _drawdown(target, dates, index, 60)
    rsi_14 = _rsi(target, dates, index, 14)
    vix_level = vix.close_by_date[sample_date]
    vix_change_5d = _point_change(vix, dates, index, 5)
    vix_change_20d = _point_change(vix, dates, index, 20)
    hyg_20d = _trailing_return(hyg, dates, index, 20)
    lqd_20d = _trailing_return(lqd, dates, index, 20)
    tlt_20d = _trailing_return(tlt, dates, index, 20)
    uup_20d = _trailing_return(uup, dates, index, 20)
    tnx_change_20d = _point_change(tnx, dates, index, 20)
    credit_spread_proxy = lqd_20d - hyg_20d
    hyg_lqd_relative = hyg_20d - lqd_20d
    liquidity_proxy = tlt_20d - uup_20d
    volatility_contribution = _clip(vix_level / 45.0, 0.0, 1.0)
    stress = (
        volatility_contribution * 0.35
        + _clip(-drawdown_depth * 4.0, 0.0, 1.0) * 0.25
        + _clip(credit_spread_proxy * 10.0, 0.0, 1.0) * 0.25
        + _clip(uup_20d * 4.0, 0.0, 1.0) * 0.15
    )
    oversold = _clip((45.0 - rsi_14) / 25.0, 0.0, 1.0)
    vix_rolling_over = _clip(-vix_change_5d / 8.0, 0.0, 1.0)
    credit_stable = _clip(-credit_spread_proxy * 8.0 + 0.5, 0.0, 1.0)
    bounce_probability = _clip(
        0.10
        + oversold * 0.34
        + vix_rolling_over * 0.18
        + volatility_contribution * 0.14
        + credit_stable * 0.14
        + _clip(-return_20d * 3.0, 0.0, 1.0) * 0.10,
        0.0,
        1.0,
    )
    crash_probability = _clip(stress * 0.55 + _clip(credit_spread_proxy * 8.0, 0.0, 1.0) * 0.35, 0.0, 1.0)
    trend_probability = _clip(0.50 + return_20d * 3.0 + return_60d * 1.2 - volatility_contribution * 0.20, 0.0, 1.0)

    return {
        "return_20d": return_20d,
        "return_60d": return_60d,
        "drawdown_depth": drawdown_depth,
        "rsi_14": rsi_14,
        "vix_level": vix_level,
        "vix_change_5d": vix_change_5d,
        "vix_change_20d": vix_change_20d,
        "credit_spread_proxy": credit_spread_proxy,
        "hyg_lqd_relative_strength": hyg_lqd_relative,
        "tlt_return_20d": tlt_20d,
        "uup_return_20d": uup_20d,
        "tnx_change_20d": tnx_change_20d,
        "liquidity_proxy": liquidity_proxy,
        "bounce_probability": bounce_probability,
        "crash_probability": crash_probability,
        "trend_probability": trend_probability,
        "volatility_contribution": volatility_contribution,
        "market_stress_score": _clip(stress, 0.0, 1.0),
    }


def _rank_analogs(current: dict[str, Any], candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    means, stdevs = _feature_stats(candidates)
    current_z = _z_vector(current["feature_vector"], means, stdevs)
    same_regime = sorted(
        [case for case in candidates if case["market_regime"] == current["market_regime"]],
        key=lambda case: _euclidean(current_z, _z_vector(case["feature_vector"], means, stdevs)),
    )
    same_regime_rank = {case["date"]: rank + 1 for rank, case in enumerate(same_regime)}
    ranked = []
    for case in candidates:
        case_z = _z_vector(case["feature_vector"], means, stdevs)
        euclidean_distance = _euclidean(current_z, case_z)
        euclidean_score = 1.0 / (1.0 + euclidean_distance)
        cosine_score = (_cosine(current_z, case_z) + 1.0) / 2.0
        regime_score = 1.0 if case["market_regime"] == current["market_regime"] else 0.0
        combined = euclidean_score * 0.55 + cosine_score * 0.30 + regime_score * 0.15
        enriched = dict(case)
        enriched.update(
            {
                "similarity_score": combined,
                "similarity_score_euclidean": euclidean_score,
                "similarity_score_cosine": cosine_score,
                "same_regime_rank": same_regime_rank.get(case["date"]),
            }
        )
        ranked.append(enriched)
    return sorted(ranked, key=lambda case: case["similarity_score"], reverse=True)


def _case_payload(current: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    payload = {
        "date": case["date"],
        "similarity_score": round(case["similarity_score"], 4),
        "similarity_score_euclidean": round(case["similarity_score_euclidean"], 4),
        "similarity_score_cosine": round(case["similarity_score_cosine"], 4),
        "same_regime_rank": case.get("same_regime_rank"),
        "regime": case["market_regime"],
        "bounce_probability": round(case["bounce_probability"], 6),
        "alpha_v1_triggered": case["alpha_v1_triggered"],
        "forward_return_3d": case["forward_return_3d"],
        "forward_return_5d": case["forward_return_5d"],
        "forward_return_10d": case["forward_return_10d"],
        "forward_return_20d": case["forward_return_20d"],
        "forward_return_60d": case["forward_return_60d"],
        "max_adverse_excursion": case["max_adverse_excursion"],
        "max_favorable_excursion": case["max_favorable_excursion"],
        "fell_then_recovered": case["fell_then_recovered"],
        "failed_bounce": case["failed_bounce"],
        "trend_reversal": case["trend_reversal"],
    }
    shared, differences = _shared_features_and_differences(current, case)
    payload["key_shared_features"] = shared
    payload["key_differences"] = differences
    return payload


def _historical_distribution(cases: list[dict[str, Any]]) -> dict[str, Any]:
    distribution: dict[str, Any] = {"sample_count": len(cases)}
    for horizon in HORIZONS:
        values = [case[f"forward_return_{horizon}d"] for case in cases if _is_finite(case.get(f"forward_return_{horizon}d"))]
        distribution[f"avg_return_{horizon}d"] = _mean(values)
        distribution[f"median_return_{horizon}d"] = _median(values)
        distribution[f"hit_rate_{horizon}d"] = _hit_rate(values)
        distribution[f"worst_case_{horizon}d"] = min(values) if values else None
        distribution[f"best_case_{horizon}d"] = max(values) if values else None
    distribution["worst_path_max_adverse_excursion"] = min(
        (case["max_adverse_excursion"] for case in cases if _is_finite(case.get("max_adverse_excursion"))),
        default=None,
    )
    distribution["best_path_max_favorable_excursion"] = max(
        (case["max_favorable_excursion"] for case in cases if _is_finite(case.get("max_favorable_excursion"))),
        default=None,
    )
    return distribution


def _historical_support(current: dict[str, Any], distribution: dict[str, Any], sample_count: int) -> str:
    avg_20d = distribution.get("avg_return_20d")
    hit_20d = distribution.get("hit_rate_20d")
    if not current["alpha_v1_triggered"] or sample_count < MIN_ANALOG_SAMPLE:
        return "weak_or_conflicting"
    if avg_20d is not None and hit_20d is not None and avg_20d > 0 and hit_20d >= 0.50:
        return "supportive"
    return "weak_or_conflicting"


def _shared_features_and_differences(current: dict[str, Any], case: dict[str, Any]) -> tuple[list[str], list[str]]:
    current_features = current["feature_vector"]
    case_features = case["feature_vector"]
    shared: list[str] = []
    differences: list[str] = []
    if current["market_regime"] == case["market_regime"]:
        shared.append(f"same regime: {current['market_regime']}")
    if current["alpha_v1_triggered"] and case["alpha_v1_triggered"]:
        shared.append("bounce_probability above frozen alpha_v1 threshold")
    if current_features["vix_level"] > 20 and case_features["vix_level"] > 20:
        shared.append("VIX elevated")
    if current_features["rsi_14"] < 45 and case_features["rsi_14"] < 45:
        shared.append("price oversold by RSI")
    if current_features["drawdown_depth"] < -0.04 and case_features["drawdown_depth"] < -0.04:
        shared.append("meaningful recent drawdown")
    if current_features["credit_spread_proxy"] <= 0.02 and case_features["credit_spread_proxy"] <= 0.02:
        shared.append("credit proxy not showing severe spread stress")

    if abs(current_features["credit_spread_proxy"] - case_features["credit_spread_proxy"]) > 0.025:
        differences.append("current credit proxy differs materially")
    if abs(current_features["uup_return_20d"] - case_features["uup_return_20d"]) > 0.03:
        differences.append("current dollar behavior differs")
    if abs(current_features["vix_level"] - case_features["vix_level"]) > 8:
        differences.append("current VIX level differs")
    if current["market_regime"] != case["market_regime"]:
        differences.append(f"regime differs: current {current['market_regime']} vs historical {case['market_regime']}")
    if not differences:
        differences.append("no large first-order difference across selected analog features")
    if not shared:
        shared.append("closest match is multi-factor, not a single obvious feature")
    return shared[:5], differences[:5]


def _classify_regime(features: dict[str, float]) -> str:
    if features["market_stress_score"] > 0.70 or (features["vix_level"] > 35 and features["drawdown_depth"] < -0.10):
        return "crisis"
    if features["vix_level"] > 28:
        return "high_volatility"
    if features["return_60d"] > 0.04 and features["drawdown_depth"] > -0.05:
        return "bull"
    if features["return_60d"] < -0.06 or features["drawdown_depth"] < -0.12:
        return "bear"
    return "low_volatility" if features["vix_level"] < 18 else "sideways"


def _trailing_return(series: PriceSeries, dates: list[str], index: int, lookback: int) -> float:
    if index < lookback:
        return 0.0
    current = series.close_by_date[dates[index]]
    past = series.close_by_date[dates[index - lookback]]
    return current / past - 1.0


def _point_change(series: PriceSeries, dates: list[str], index: int, lookback: int) -> float:
    if index < lookback:
        return 0.0
    return series.close_by_date[dates[index]] - series.close_by_date[dates[index - lookback]]


def _drawdown(series: PriceSeries, dates: list[str], index: int, lookback: int) -> float:
    start = max(0, index - lookback)
    values = [series.close_by_date[dates[position]] for position in range(start, index + 1)]
    peak = max(values)
    if peak <= 0:
        return 0.0
    return series.close_by_date[dates[index]] / peak - 1.0


def _rsi(series: PriceSeries, dates: list[str], index: int, lookback: int) -> float:
    if index < lookback:
        return 50.0
    gains: list[float] = []
    losses: list[float] = []
    for position in range(index - lookback + 1, index + 1):
        current = series.close_by_date[dates[position]]
        previous = series.close_by_date[dates[position - 1]]
        change = current - previous
        if change >= 0:
            gains.append(change)
        else:
            losses.append(abs(change))
    avg_gain = sum(gains) / lookback
    avg_loss = sum(losses) / lookback
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100.0 - 100.0 / (1.0 + rs)


def _forward_return(series: PriceSeries, dates: list[str], index: int, horizon: int) -> float | None:
    if index + horizon >= len(dates):
        return None
    start = series.close_by_date[dates[index]]
    end = series.close_by_date[dates[index + horizon]]
    return end / start - 1.0


def _future_excursions(series: PriceSeries, dates: list[str], index: int, horizon: int) -> tuple[float | None, float | None]:
    if index + horizon >= len(dates):
        return None, None
    start = series.close_by_date[dates[index]]
    returns = [series.close_by_date[dates[position]] / start - 1.0 for position in range(index + 1, index + horizon + 1)]
    return max(returns), min(returns)


def _future_path_flags(
    future_returns: dict[str, float | None],
    max_favorable: float | None,
    max_adverse: float | None,
) -> dict[str, bool]:
    forward_20d = future_returns.get("forward_return_20d")
    forward_60d = future_returns.get("forward_return_60d")
    return {
        "fell_then_recovered": bool(max_adverse is not None and max_adverse < -0.025 and forward_20d is not None and forward_20d > 0),
        "failed_bounce": bool(max_favorable is not None and max_favorable > 0.015 and forward_20d is not None and forward_20d < 0),
        "trend_reversal": bool(forward_20d is not None and forward_60d is not None and forward_20d > 0.02 and forward_60d > 0.04),
    }


def _feature_stats(candidates: list[dict[str, Any]]) -> tuple[dict[str, float], dict[str, float]]:
    means: dict[str, float] = {}
    stdevs: dict[str, float] = {}
    for name in SIMILARITY_FEATURES:
        values = [case["feature_vector"][name] for case in candidates if _is_finite(case["feature_vector"].get(name))]
        means[name] = _mean(values) or 0.0
        stdev = statistics.pstdev(values) if len(values) > 1 else 1.0
        stdevs[name] = stdev if stdev > 1e-9 else 1.0
    return means, stdevs


def _z_vector(features: dict[str, float], means: dict[str, float], stdevs: dict[str, float]) -> list[float]:
    return [(features[name] - means[name]) / stdevs[name] for name in SIMILARITY_FEATURES]


def _euclidean(left: list[float], right: list[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)) / max(1, len(left)))


def _cosine(left: list[float], right: list[float]) -> float:
    dot = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(a * a for a in left))
    right_norm = math.sqrt(sum(b * b for b in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)


def _has_future_returns(sample: dict[str, Any]) -> bool:
    return all(_is_finite(sample.get(f"forward_return_{horizon}d")) for horizon in HORIZONS)


def _select(features: dict[str, float], names: tuple[str, ...]) -> dict[str, float]:
    return {name: features[name] for name in names}


def _clip(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def _mean(values: list[float]) -> float | None:
    clean = [value for value in values if _is_finite(value)]
    return sum(clean) / len(clean) if clean else None


def _median(values: list[float]) -> float | None:
    clean = sorted(value for value in values if _is_finite(value))
    if not clean:
        return None
    mid = len(clean) // 2
    if len(clean) % 2:
        return clean[mid]
    return (clean[mid - 1] + clean[mid]) / 2.0


def _hit_rate(values: list[float]) -> float | None:
    clean = [value for value in values if _is_finite(value)]
    if not clean:
        return None
    return sum(1 for value in clean if value > 0) / len(clean)


def _is_finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(value)


def _normalize_symbol(symbol: str) -> str:
    normalized = symbol.upper().strip()
    if normalized not in TARGET_SYMBOLS:
        raise ValueError(f"Unsupported symbol: {symbol}. Supported: {', '.join(TARGET_SYMBOLS)}")
    return normalized


def _confidence_note(sample_count: int, alpha_v1_only: bool, regime_filtered: bool) -> str:
    scope = "alpha_v1-triggered analogs" if alpha_v1_only else "all historical analogs"
    if regime_filtered:
        scope += " in the current regime"
    if sample_count < MIN_ANALOG_SAMPLE:
        return f"Only {sample_count} {scope} found; treat this as a low-sample explanation, not evidence."
    return f"Uses {sample_count} {scope}. This is explanatory support only, not proof of alpha."


def _risk_note(current: dict[str, Any], distribution: dict[str, Any], same_regime_count: int) -> str:
    worst = distribution.get("worst_case_20d")
    pieces = [ANALOG_WARNING]
    if worst is not None and worst < -0.05:
        pieces.append(f"Closest analogs include a 20d loss as bad as {worst:.2%}.")
    if _crisis_sample_warning(current["market_regime"], same_regime_count):
        pieces.append("Crisis/high-volatility sample size is small; avoid over-interpreting the analog set.")
    return " ".join(pieces)


def _crisis_sample_warning(regime: str, same_regime_count: int) -> bool:
    return regime in {"crisis", "high_volatility"} and same_regime_count < MIN_ANALOG_SAMPLE


def _failed_report(symbol: str, data_status: str) -> dict[str, Any]:
    return {
        "symbol": symbol,
        "as_of": None,
        "data_source_status": data_status,
        "current_regime": "unknown",
        "alpha_v1_status": ALPHA_STATUS,
        "signal_name": SIGNAL_NAME,
        "threshold": FROZEN_BOUNCE_THRESHOLD,
        "sample_count": 0,
        "candidate_count": 0,
        "low_sample_warning": True,
        "top_similar_cases": [],
        "historical_distribution": {"sample_count": 0},
        "interpretation": {
            "supports_bounce_alpha": False,
            "historical_support": "weak_or_conflicting",
            "confidence_note": "Real historical market data is unavailable.",
            "risk_note": ANALOG_WARNING,
            "not_proof_of_alpha": ANALOG_WARNING,
        },
    }


def _low_memory_report(symbol: str, memory: list[dict[str, Any]], data_status: str) -> dict[str, Any]:
    current = memory[-1] if memory else {"date": None, "market_regime": "unknown"}
    return {
        "symbol": symbol,
        "as_of": current.get("date"),
        "data_source_status": data_status,
        "current_regime": current.get("market_regime", "unknown"),
        "alpha_v1_status": ALPHA_STATUS,
        "signal_name": SIGNAL_NAME,
        "threshold": FROZEN_BOUNCE_THRESHOLD,
        "sample_count": 0,
        "candidate_count": len(memory),
        "low_sample_warning": True,
        "top_similar_cases": [],
        "historical_distribution": {"sample_count": 0},
        "interpretation": {
            "supports_bounce_alpha": False,
            "historical_support": "weak_or_conflicting",
            "confidence_note": "Not enough point-in-time historical samples to compute analogs.",
            "risk_note": ANALOG_WARNING,
            "not_proof_of_alpha": ANALOG_WARNING,
        },
    }


def _no_candidate_report(
    symbol: str,
    current: dict[str, Any],
    data_status: str,
    alpha_v1_only: bool,
    regime_filtered: bool,
) -> dict[str, Any]:
    return {
        "symbol": symbol,
        "as_of": current["date"],
        "data_source_status": data_status,
        "current_regime": current["market_regime"],
        "alpha_v1_status": ALPHA_STATUS,
        "signal_name": SIGNAL_NAME,
        "threshold": FROZEN_BOUNCE_THRESHOLD,
        "current_bounce_probability": current["bounce_probability"],
        "distance_to_threshold": FROZEN_BOUNCE_THRESHOLD - current["bounce_probability"],
        "current_alpha_v1_triggered": current["alpha_v1_triggered"],
        "sample_count": 0,
        "candidate_count": 0,
        "low_sample_warning": True,
        "top_similar_cases": [],
        "historical_distribution": {"sample_count": 0},
        "interpretation": {
            "supports_bounce_alpha": False,
            "historical_support": "weak_or_conflicting",
            "confidence_note": _confidence_note(0, alpha_v1_only, regime_filtered),
            "risk_note": ANALOG_WARNING,
            "not_proof_of_alpha": ANALOG_WARNING,
        },
    }
