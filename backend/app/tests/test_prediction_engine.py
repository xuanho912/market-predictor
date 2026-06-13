from app.services.prediction_engine import HORIZONS, SUPPORTED_SYMBOLS, build_prediction


def test_prediction_snapshot_has_required_outputs() -> None:
    snapshot = build_prediction(SUPPORTED_SYMBOLS[0])

    assert snapshot.symbol == "SPY"
    assert {forecast.horizon for forecast in snapshot.horizons} == set(HORIZONS)
    assert 0 <= snapshot.pullback_risk_score <= 100
    assert 0 <= snapshot.crisis_risk_score <= 100
    assert 0 <= snapshot.bounce_quality_score <= 100
    assert snapshot.top_reasons
    assert snapshot.historical_similar_days
    assert snapshot.risk_source_breakdown


def test_horizon_probabilities_sum_to_one() -> None:
    snapshot = build_prediction("QQQ")
    for forecast in snapshot.horizons:
        total = forecast.up_probability + forecast.down_probability + forecast.sideways_probability
        assert abs(total - 1.0) < 0.001
