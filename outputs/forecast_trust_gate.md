# Forecast Trust Gate

Generated at: `2026-06-22T15:21:15.994798+00:00`

This report answers whether the current Market Prediction Dashboard is dependable as a forecasting tool. It is not trading advice.

## Current Status

- status: `BLOCKED_STALE_DATA`
- trust_score: `0`
- would_rely_for_real_money: `False`
- use_boundary: Do not use the displayed forecast as today's forecast until data freshness is restored.
- latest_market_date: `2026-06-16`
- expected_latest_trading_date: `2026-06-18`
- data_completeness_score: `67.0`

## Forward Samples

- 1d: `9`
- 3d: `0`
- 5d: `0`
- 10d: `0`
- 20d: `0`
- 60d: `0`

## Blockers

- `stale_or_failed_data` (critical): 数据已过期，当前预测不可作为今日判断。 核心行情最新日期为 2026-06-16，按美股交易日应至少更新到 2026-06-18。
- `data_completeness_below_gate` (high): Data completeness is 67.0, below the 85/100 reliance gate.
- `insufficient_forward_samples` (critical): Forward validation samples are not enough to rely on the model as a high-confidence forecasting system.
- `primary_path_not_validated` (high): Primary-vs-secondary path advantage is not yet proven on enough forward samples.

## Warnings

- `high_confidence_not_validated` (medium): High-confidence forecasts have not proven they are more accurate than ordinary forecasts.
- `deviation_learning_needed` (medium): Deviation sample is still too small to know whether errors are under control.

## Symbol Readiness

- SPY: `blocked_by_global_gate` | primary `bounce_path` 0.391 | reason: Global trust gate is not ready.
- QQQ: `blocked_by_global_gate` | primary `bounce_path` 0.3541 | reason: Global trust gate is not ready.
- IWM: `blocked_by_global_gate` | primary `bounce_path` 0.3481 | reason: Global trust gate is not ready.
- DIA: `blocked_by_global_gate` | primary `bounce_path` 0.3927 | reason: Global trust gate is not ready.

## Next Actions

- Restore latest market data and rerun GitHub Actions before reading the dashboard as today's forecast.
- Keep accumulating immutable forward forecasts until minimum sample gates are met.
- Do not promote any model until primary-vs-secondary path accuracy is proven by forward samples.
- Keep confidence capped until high-confidence buckets outperform ordinary samples.
- Route repeated deviation themes into a challenger model rather than editing baseline_v1.

## Guardrails

- This gate does not modify Alpha v1 threshold, baseline_v1 or historical forecast records.
- This is forecast reliability assessment, not trading advice.
- A blocked gate means the dashboard can still be used for research, but not as a dependable forecast tool.
