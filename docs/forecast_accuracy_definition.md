# Forecast Accuracy Definition

This project defines high-precision forecasting as a validated property of the Market Prediction Dashboard, not as a claim that every day is predicted correctly.

## What High Precision Means

The system reaches the high precision standard only when forward validation shows that:

- It can identify `NO_EDGE` and avoid forcing a strong forecast when evidence is mixed.
- In `MODERATE_EDGE` / `STRONG_EDGE` samples, the primary scenario is closer to the realized path than the secondary scenario.
- High `signal_confirmation_score` samples clearly outperform low-confirmation samples.
- The 5d and 20d horizons show repeatable advantage.
- Scenario probabilities roughly match realized hit rates.
- Higher data completeness improves forecast stability, not only dashboard confidence.
- Predictor, signal, and data-source contributions can be evaluated through forward records, ablation, and model-version comparisons.
- Model upgrades are compared against `baseline_v1` rather than accepted by subjective judgment.

## Required Evidence

Forward validation is decisive. Historical replay can guide research priorities, but it cannot prove high precision.

Minimum evidence before claiming high precision:

- `3d` completed samples >= 20
- `5d` completed samples >= 20
- `10d` completed samples >= 30
- `20d` completed samples >= 50
- `60d` completed samples >= 50, preferably 100+

Metrics must be reported by horizon:

- Primary scenario hit rate
- Primary vs secondary accuracy spread
- Mean absolute path error
- Median absolute path error
- High-confidence forecast accuracy
- Signal confirmation top 10% performance
- Edge status performance
- Calibration quality
- Max adverse path control

## Current Status

Current status: `not_yet_validated`.

Reason:

- Forward completed samples are not yet sufficient.
- `baseline_v1` has just been frozen and needs forward records.
- Historical replay is currently `WEAK`, not proof of high precision.

## Non-Goals

High precision does not mean:

- Every forecast is correct.
- The model is a trading system.
- Alpha v1 is confirmed.
- Historical replay can replace forward validation.
- Adding new data automatically improves confidence.

