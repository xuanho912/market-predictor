# Forecast Deviation Review

Generated at: `2026-06-19T00:14:33.933209+00:00`

This report reviews forecast-vs-actual deviations after horizons complete. It is not a trading, PnL or execution report.

## Summary

- total_forecast_records: `24`
- completed_outcomes_reviewed: `20`
- material_deviation_count: `12`
- latest_forecast_date: `2026-06-18`
- latest_reviewed_forecast_date: `2026-06-17`
- latest_market_date: `2026-06-18`
- data_freshness_status: `fresh`
- largest_absolute_error: `0.034457`
- dominant_error_theme: `news_data_gap_limited_attribution`
- evidence_level: `early_evidence`
- validation_status: `early_evidence`
- update_blockers: `[{'reason': 'no_future_market_close_yet', 'detail': 'Latest market date 2026-06-18 is not after latest forecast date 2026-06-18, so no completed 1d/3d/5d outcome can be scored yet.'}]`

## Latest Material Deviations

### QQQ 1d from 2026-06-17

- primary_scenario: `bearish_path`
- expected_return: `-0.009392`
- actual_return: `0.025065`
- forecast_error: `0.034457`
- severity: `extreme`
- primary_hit: `False`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- diagnostic_note: 实际走势强于预测，可能低估了波动率回落和恐慌释放后的修复力度。

### SPY 1d from 2026-06-17

- primary_scenario: `bearish_path`
- expected_return: `-0.012327`
- actual_return: `0.007801`
- forecast_error: `0.020127`
- severity: `large`
- primary_hit: `False`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- diagnostic_note: 实际走势强于预测，可能低估了波动率回落和恐慌释放后的修复力度。

### IWM 1d from 2026-06-17

- primary_scenario: `bounce_path`
- expected_return: `0.000618`
- actual_return: `0.019698`
- forecast_error: `0.01908`
- severity: `large`
- primary_hit: `True`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, breadth_follow_through_underweighted, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- diagnostic_note: 实际走势强于预测，可能低估了波动率回落和恐慌释放后的修复力度。

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

### DIA 3d from 2026-06-15

- primary_scenario: `bounce_path`
- expected_return: `0.012177`
- actual_return: `-0.005632`
- forecast_error: `-0.017809`
- severity: `moderate`
- primary_hit: `False`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### QQQ 3d from 2026-06-15

- primary_scenario: `bounce_path`
- expected_return: `0.011731`
- actual_return: `-0.004543`
- forecast_error: `-0.016274`
- severity: `moderate`
- primary_hit: `False`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### IWM 3d from 2026-06-15

- primary_scenario: `bounce_path`
- expected_return: `0.016341`
- actual_return: `0.003224`
- forecast_error: `-0.013117`
- severity: `moderate`
- primary_hit: `False`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### SPY 3d from 2026-06-15

- primary_scenario: `bounce_path`
- expected_return: `0.001631`
- actual_return: `-0.010718`
- forecast_error: `-0.012349`
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
