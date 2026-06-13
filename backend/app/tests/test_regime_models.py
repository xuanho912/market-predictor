from app.services.models.regime_models import predict_regime_ensemble


def test_regime_ensemble_selects_probabilities() -> None:
    features = {
        "breadth_repair": 0.7,
        "breadth_deterioration": 0.2,
        "credit_spreads": 0.3,
        "vix_options_risk": 0.4,
    }
    prediction = predict_regime_ensemble(features, "bull_market")

    assert prediction.selected_model == "bull_model"
    assert abs(prediction.up_probability + prediction.down_probability + prediction.sideways_probability - 1.0) < 1e-9
