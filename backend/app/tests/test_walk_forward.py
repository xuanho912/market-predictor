from datetime import date

from app.services.backtesting.walk_forward import generate_walk_forward_splits


def test_walk_forward_splits_are_ordered() -> None:
    splits = generate_walk_forward_splits(
        start=date(2020, 1, 1),
        end=date(2022, 12, 31),
        train_days=365,
        calibration_days=90,
        test_days=30,
        step_days=30,
    )

    assert splits
    first = splits[0]
    assert first.train_start < first.train_end < first.calibration_start
    assert first.calibration_start < first.calibration_end < first.test_start
    assert first.test_start < first.test_end
