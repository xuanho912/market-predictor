from __future__ import annotations

from dataclasses import dataclass


def _clamp01(value: float) -> float:
    return min(max(value, 0.0), 1.0)


def _score(value: float) -> float:
    return round(100.0 * _clamp01(value), 1)


def _weighted_score(values: dict[str, float], weights: dict[str, float]) -> float:
    total_weight = sum(weights.values())
    if total_weight <= 0:
        raise ValueError("weights must sum to a positive value")
    weighted = sum(_clamp01(values.get(name, 0.0)) * weight for name, weight in weights.items()) / total_weight
    return _score(weighted)


PULLBACK_RISK_WEIGHTS = {
    "valuation_overheat": 0.15,
    "momentum_extension": 0.15,
    "breadth_deterioration": 0.15,
    "vix_options_risk": 0.10,
    "positioning_crowding": 0.15,
    "rates_up": 0.10,
    "dollar_strength": 0.05,
    "earnings_downgrades": 0.10,
    "news_event_risk": 0.05,
}

CRISIS_RISK_WEIGHTS = {
    "credit_gdp_gap": 0.15,
    "credit_spreads": 0.20,
    "bank_stress": 0.15,
    "funding_market_stress": 0.15,
    "nonbank_leverage": 0.10,
    "dollar_liquidity": 0.10,
    "macro_recession_risk": 0.10,
    "policy_response_lag": 0.05,
}

BOUNCE_QUALITY_WEIGHTS = {
    "drawdown_depth": 0.10,
    "panic_extreme": 0.15,
    "volume_expansion": 0.10,
    "breadth_repair": 0.15,
    "credit_spread_stabilization": 0.20,
    "vix_reversal": 0.10,
    "policy_liquidity_improvement": 0.10,
    "bad_news_resilience": 0.10,
}


@dataclass(frozen=True)
class ScoreInputs:
    pullback: dict[str, float]
    crisis: dict[str, float]
    bounce_quality: dict[str, float]


def pullback_risk_score(values: dict[str, float]) -> float:
    return _weighted_score(values, PULLBACK_RISK_WEIGHTS)


def crisis_risk_score(values: dict[str, float]) -> float:
    return _weighted_score(values, CRISIS_RISK_WEIGHTS)


def bounce_quality_score(values: dict[str, float]) -> float:
    return _weighted_score(values, BOUNCE_QUALITY_WEIGHTS)


def compute_core_scores(inputs: ScoreInputs) -> dict[str, float]:
    return {
        "pullback_risk_score": pullback_risk_score(inputs.pullback),
        "crisis_risk_score": crisis_risk_score(inputs.crisis),
        "bounce_quality_score": bounce_quality_score(inputs.bounce_quality),
    }
