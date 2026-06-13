from __future__ import annotations

from enum import StrEnum


class MarketRegime(StrEnum):
    BULL_TREND = "bull_trend"
    BEAR_TREND = "bear_trend"
    SIDEWAYS = "sideways"
    PANIC = "panic"
    OVERSOLD_BOUNCE = "oversold_bounce"
    TOPPING = "topping"
    BOTTOMING = "bottoming"
    RECOVERY = "recovery"
    LIQUIDITY_CRUNCH = "liquidity_crunch"
    CREDIT_STRESS = "credit_stress"
    CRISIS_MODE = "crisis_mode"


REGIME_VALUES = tuple(regime.value for regime in MarketRegime)


def rsi_oversold_interpretation(regime: MarketRegime, rsi: float) -> str:
    if rsi > 30:
        return "neutral"
    if regime in {MarketRegime.BULL_TREND, MarketRegime.OVERSOLD_BOUNCE, MarketRegime.BOTTOMING, MarketRegime.RECOVERY}:
        return "bounce_probability_positive"
    if regime in {MarketRegime.PANIC, MarketRegime.CREDIT_STRESS, MarketRegime.LIQUIDITY_CRUNCH, MarketRegime.CRISIS_MODE}:
        return "downside_continuation_risk"
    return "regime_dependent"


def classify_rule_based_regime(
    trend_score: float,
    breadth_score: float,
    credit_stress: float,
    liquidity_stress: float,
    volatility_stress: float,
    bank_relative_strength: float,
) -> MarketRegime:
    if credit_stress > 0.75 and liquidity_stress > 0.75 and volatility_stress > 0.75 and bank_relative_strength < -0.5:
        return MarketRegime.CRISIS_MODE
    if liquidity_stress > 0.75:
        return MarketRegime.LIQUIDITY_CRUNCH
    if credit_stress > 0.70:
        return MarketRegime.CREDIT_STRESS
    if volatility_stress > 0.80 and trend_score < -0.50:
        return MarketRegime.PANIC
    if trend_score > 0.50 and breadth_score > 0.30:
        return MarketRegime.BULL_TREND
    if trend_score < -0.50 and breadth_score < -0.30:
        return MarketRegime.BEAR_TREND
    if trend_score > 0.30 and breadth_score < -0.30:
        return MarketRegime.TOPPING
    if trend_score < -0.20 and breadth_score > 0.20 and credit_stress < 0.50:
        return MarketRegime.BOTTOMING
    if trend_score > 0.20 and credit_stress < 0.50 and liquidity_stress < 0.50:
        return MarketRegime.RECOVERY
    return MarketRegime.SIDEWAYS
