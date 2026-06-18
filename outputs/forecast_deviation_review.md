# Forecast Deviation Review

Generated at: `2026-06-18T00:01:55.209655+00:00`

This report reviews forecast-vs-actual deviations after horizons complete. It is not a trading, PnL or execution report.

## Summary

- total_forecast_records: `20`
- completed_outcomes_reviewed: `12`
- material_deviation_count: `5`
- latest_forecast_date: `2026-06-17`
- latest_reviewed_forecast_date: `2026-06-16`
- latest_market_date: `2026-06-17`
- data_freshness_status: `fresh`
- largest_absolute_error: `0.021151`
- dominant_error_theme: `model_underestimated_downside_or_failed_bounce`
- evidence_level: `insufficient_samples`
- validation_status: `not_yet_validated`
- update_blockers: `[{'reason': 'no_future_market_close_yet', 'detail': 'Latest market date 2026-06-17 is not after latest forecast date 2026-06-17, so no completed 1d/3d/5d outcome can be scored yet.'}]`

## Latest Material Deviations

### SPY 1d from 2026-06-16

- primary_scenario: `bounce_path`
- expected_return: `0.002396`
- actual_return: `-0.012488`
- forecast_error: `-0.014884`
- severity: `large`
- primary_hit: `False`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### DIA 1d from 2026-06-16

- primary_scenario: `bounce_path`
- expected_return: `0.001248`
- actual_return: `-0.009857`
- forecast_error: `-0.011105`
- severity: `moderate`
- primary_hit: `False`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### IWM 1d from 2026-06-16

- primary_scenario: `bounce_path`
- expected_return: `0.000627`
- actual_return: `-0.007532`
- forecast_error: `-0.008159`
- severity: `moderate`
- primary_hit: `False`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### IWM 3d from 2026-06-12

- primary_scenario: `bounce_path`
- expected_return: `0.010671`
- actual_return: `-0.01048`
- forecast_error: `-0.021151`
- severity: `large`
- primary_hit: `False`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### IWM 3d from 2026-06-12

- primary_scenario: `bounce_path`
- expected_return: `0.010671`
- actual_return: `-0.01048`
- forecast_error: `-0.021151`
- severity: `large`
- primary_hit: `False`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。


## Guardrails

- This is forecast error attribution, not a trading or PnL report.
- Attribution is diagnostic and probabilistic; it is not proof of causality.
- Forecast fields are not rewritten. Only completed outcome fields are reviewed.
- Alpha v1 threshold remains frozen at 0.32534311.
