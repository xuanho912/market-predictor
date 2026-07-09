# Forecast Trust Gate

Generated at: `2026-07-09T22:54:31.266292+00:00`

This report answers whether the current Market Prediction Dashboard is dependable as a forecasting tool. It is not trading advice.

## Current Status

- status: `RESEARCH_ONLY_FORWARD_VALIDATION_NEEDED`
- trust_score: `40`
- would_rely_for_real_money: `False`
- use_boundary: Use as a research radar and scenario explainer only; do not treat it as a dependable forecasting edge.
- latest_market_date: `2026-07-09`
- expected_latest_trading_date: `2026-07-09`
- data_completeness_score: `87.0`

## Forward Samples

- 1d: `72`
- 3d: `64`
- 5d: `56`
- 10d: `36`
- 20d: `0`
- 60d: `0`

## Blockers

- `insufficient_forward_samples` (critical): Forward validation samples are not enough to rely on the model as a high-confidence forecasting system.
- `primary_path_not_validated` (high): Primary-vs-secondary path advantage is not yet proven on enough forward samples.

## Warnings

- `high_confidence_not_validated` (medium): High-confidence forecasts have not proven they are more accurate than ordinary forecasts.
- `deviation_learning_needed` (medium): Material deviation rate is too high; confidence must remain capped.

## Symbol Readiness

- SPY: `blocked_by_global_gate` | primary `bounce_path` 0.3709 | reason: Global trust gate is not ready.
- QQQ: `blocked_by_global_gate` | primary `bounce_path` 0.3233 | reason: Global trust gate is not ready.
- IWM: `blocked_by_global_gate` | primary `bounce_path` 0.3557 | reason: Global trust gate is not ready.
- DIA: `blocked_by_global_gate` | primary `bounce_path` 0.4045 | reason: Global trust gate is not ready.

## Next Actions

- Keep accumulating immutable forward forecasts until minimum sample gates are met.
- Do not promote any model until primary-vs-secondary path accuracy is proven by forward samples.
- Keep confidence capped until high-confidence buckets outperform ordinary samples.
- Route repeated deviation themes into a challenger model rather than editing baseline_v1.

## Guardrails

- This gate does not modify Alpha v1 threshold, baseline_v1 or historical forecast records.
- This is forecast reliability assessment, not trading advice.
- A blocked gate means the dashboard can still be used for research, but not as a dependable forecast tool.
