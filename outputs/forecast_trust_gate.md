# Forecast Trust Gate

Generated at: `2026-10-21T01:12:38.964127+00:00`

This report answers whether the current Market Prediction Dashboard is dependable as a forecasting tool. It is not trading advice.

## Current Status

- status: `RESEARCH_ONLY_PATH_EDGE_UNPROVEN`
- trust_score: `57`
- would_rely_for_real_money: `False`
- use_boundary: Use as a research radar and scenario explainer only; do not treat it as a dependable forecasting edge.
- latest_market_date: `2026-10-20`
- expected_latest_trading_date: `2026-10-20`
- data_completeness_score: `87.0`

## Forward Samples

- 1d: `360`
- 3d: `352`
- 5d: `344`
- 10d: `324`
- 20d: `284`
- 60d: `124`

## Blockers

- `primary_path_not_validated` (high): Primary-vs-secondary path advantage is not yet proven on enough forward samples.

## Warnings

- `high_confidence_not_validated` (medium): High-confidence forecasts have not proven they are more accurate than ordinary forecasts.
- `deviation_learning_needed` (medium): Material deviation rate is too high; confidence must remain capped.

## Symbol Readiness

- SPY: `blocked_by_global_gate` | primary `bearish_path` 0.332 | reason: Global trust gate is not ready.
- QQQ: `blocked_by_global_gate` | primary `bearish_path` 0.3993 | reason: Global trust gate is not ready.
- IWM: `blocked_by_global_gate` | primary `bearish_path` 0.4318 | reason: Global trust gate is not ready.
- DIA: `blocked_by_global_gate` | primary `bearish_path` 0.3161 | reason: Global trust gate is not ready.

## Next Actions

- Do not promote any model until primary-vs-secondary path accuracy is proven by forward samples.
- Keep confidence capped until high-confidence buckets outperform ordinary samples.
- Route repeated deviation themes into a challenger model rather than editing baseline_v1.

## Guardrails

- This gate does not modify Alpha v1 threshold, baseline_v1 or historical forecast records.
- This is forecast reliability assessment, not trading advice.
- A blocked gate means the dashboard can still be used for research, but not as a dependable forecast tool.
