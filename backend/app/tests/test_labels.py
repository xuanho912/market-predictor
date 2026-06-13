from app.services.labeling.labels import MANDATORY_LABELS, drawdown, future_return


def test_mandatory_labels_include_crisis_family() -> None:
    assert "crash_risk_60d" in MANDATORY_LABELS
    assert "crash_risk_120d" in MANDATORY_LABELS
    assert "systemic_crisis_180d" in MANDATORY_LABELS


def test_future_return() -> None:
    assert abs(future_return(100.0, 105.0) - 0.05) < 1e-12


def test_drawdown() -> None:
    assert round(drawdown([100.0, 110.0, 99.0, 120.0]), 4) == -0.1
