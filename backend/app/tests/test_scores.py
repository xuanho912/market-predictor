from app.services.signals.risk_score import (
    BOUNCE_QUALITY_WEIGHTS,
    CRISIS_RISK_WEIGHTS,
    PULLBACK_RISK_WEIGHTS,
    bounce_quality_score,
    crisis_risk_score,
    pullback_risk_score,
)


def test_score_weights_sum_to_one() -> None:
    assert round(sum(PULLBACK_RISK_WEIGHTS.values()), 6) == 1.0
    assert round(sum(CRISIS_RISK_WEIGHTS.values()), 6) == 1.0
    assert round(sum(BOUNCE_QUALITY_WEIGHTS.values()), 6) == 1.0


def test_scores_are_zero_to_one_hundred() -> None:
    values = {name: 0.5 for name in PULLBACK_RISK_WEIGHTS}
    assert pullback_risk_score(values) == 50.0

    crisis_values = {name: 1.0 for name in CRISIS_RISK_WEIGHTS}
    assert crisis_risk_score(crisis_values) == 100.0

    bounce_values = {name: 0.0 for name in BOUNCE_QUALITY_WEIGHTS}
    assert bounce_quality_score(bounce_values) == 0.0
