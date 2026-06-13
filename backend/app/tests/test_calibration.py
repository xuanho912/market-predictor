from app.services.models.calibration import (
    BrierScoreOptimizer,
    IsotonicRegressionCalibrator,
    PlattScaler,
    brier_score,
    calibration_curve,
    log_loss_score,
)


def test_probability_metrics_are_computed() -> None:
    y_true = [0, 0, 1, 1]
    probabilities = [0.1, 0.3, 0.7, 0.9]

    assert brier_score(y_true, probabilities) < 0.1
    assert log_loss_score(y_true, probabilities) < 0.4
    assert len(calibration_curve(y_true, probabilities, bins=4)) == 4


def test_calibrators_return_probabilities() -> None:
    y_true = [0, 0, 1, 1]
    probabilities = [0.2, 0.4, 0.6, 0.8]

    platt = PlattScaler(iterations=10).fit(probabilities, y_true)
    isotonic = IsotonicRegressionCalibrator().fit(probabilities, y_true)
    optimizer = BrierScoreOptimizer().fit(probabilities, y_true)

    for value in [platt.predict_one(0.7), isotonic.predict_one(0.7), optimizer.predict_one(0.7)]:
        assert 0 < value < 1
