from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date, timedelta


@dataclass(frozen=True)
class WalkForwardSplit:
    train_start: date
    train_end: date
    calibration_start: date
    calibration_end: date
    test_start: date
    test_end: date


def generate_walk_forward_splits(
    start: date,
    end: date,
    train_days: int,
    calibration_days: int,
    test_days: int,
    step_days: int,
) -> list[WalkForwardSplit]:
    splits: list[WalkForwardSplit] = []
    train_start = start
    while True:
        train_end = train_start + timedelta(days=train_days)
        calibration_start = train_end + timedelta(days=1)
        calibration_end = calibration_start + timedelta(days=calibration_days)
        test_start = calibration_end + timedelta(days=1)
        test_end = test_start + timedelta(days=test_days)
        if test_end > end:
            break
        splits.append(
            WalkForwardSplit(
                train_start=train_start,
                train_end=train_end,
                calibration_start=calibration_start,
                calibration_end=calibration_end,
                test_start=test_start,
                test_end=test_end,
            )
        )
        train_start = train_start + timedelta(days=step_days)
    return splits


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate walk-forward validation splits.")
    parser.add_argument("--sample", action="store_true", help="Print sample splits.")
    args = parser.parse_args()

    if args.sample:
        splits = generate_walk_forward_splits(
            start=date(2010, 1, 1),
            end=date(2020, 12, 31),
            train_days=365 * 5,
            calibration_days=365,
            test_days=180,
            step_days=180,
        )
        for split in splits[:5]:
            print(split)
        print(f"generated_splits={len(splits)}")
    else:
        print("Walk-forward module ready. Pass --sample to preview splits.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
