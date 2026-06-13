from __future__ import annotations

import argparse


MVP_MODEL_FAMILIES = (
    "LogisticRegression",
    "RandomForestClassifier",
    "HistGradientBoostingClassifier",
    "CalibratedClassifierCV",
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Train a horizon-specific market prediction model.")
    parser.add_argument("--label", required=True, help="Target label, for example crash_risk_60d.")
    parser.add_argument("--horizon", required=True, help="Forecast horizon, for example 60d.")
    args = parser.parse_args()

    print(f"Training placeholder for label={args.label}, horizon={args.horizon}")
    print(f"MVP model families: {', '.join(MVP_MODEL_FAMILIES)}")
    print("Use walk-forward train/calibrate/test splits, class-imbalance handling, and probability calibration.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
