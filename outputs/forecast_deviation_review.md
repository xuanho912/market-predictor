# Forecast Deviation Review

Generated at: `2026-06-16T08:39:54.055622+00:00`

This report reviews forecast-vs-actual deviations after horizons complete. It is not a trading, PnL or execution report.

## Summary

- total_forecast_records: `12`
- completed_outcomes_reviewed: `0`
- material_deviation_count: `0`
- latest_forecast_date: `2026-06-15`
- latest_reviewed_forecast_date: `None`
- latest_market_date: `2026-06-15`
- data_freshness_status: `fresh`
- largest_absolute_error: `None`
- dominant_error_theme: `not_enough_completed_outcomes`
- evidence_level: `insufficient_samples`
- validation_status: `not_yet_validated`
- update_blockers: `[{'reason': 'no_future_market_close_yet', 'detail': 'Latest market date 2026-06-15 is not after latest forecast date 2026-06-15, so no completed 1d/3d/5d outcome can be scored yet.'}, {'reason': 'completed_actuals_without_comparable_expected_path', 'detail': 'Some actual returns have been backfilled, but the matching historical forecast record does not contain an expected path for that horizon, so success/failure cannot be scored without rewriting old forecast fields.'}]`

## Latest Material Deviations

- No material completed deviations yet. Forward samples are still accumulating.

## Guardrails

- This is forecast error attribution, not a trading or PnL report.
- Attribution is diagnostic and probabilistic; it is not proof of causality.
- Forecast fields are not rewritten. Only completed outcome fields are reviewed.
- Alpha v1 threshold remains frozen at 0.32534311.
