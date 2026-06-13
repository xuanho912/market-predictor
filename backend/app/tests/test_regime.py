from app.services.signals.regime import MarketRegime, classify_rule_based_regime, rsi_oversold_interpretation


def test_rsi_interpretation_changes_by_regime() -> None:
    assert rsi_oversold_interpretation(MarketRegime.BULL_TREND, 29.0) == "bounce_probability_positive"
    assert rsi_oversold_interpretation(MarketRegime.CRISIS_MODE, 29.0) == "downside_continuation_risk"


def test_crisis_mode_requires_cross_asset_stress() -> None:
    regime = classify_rule_based_regime(
        trend_score=-0.8,
        breadth_score=-0.7,
        credit_stress=0.9,
        liquidity_stress=0.9,
        volatility_stress=0.9,
        bank_relative_strength=-0.8,
    )

    assert regime == MarketRegime.CRISIS_MODE
