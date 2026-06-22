# Forecast Deviation Review

Generated at: `2026-06-22T15:55:04.973197+00:00`

This report reviews forecast-vs-actual deviations after horizons complete. It is not a trading, PnL or execution report.

## Summary

- total_forecast_records: `24`
- raw_forecast_rows: `24`
- deduped_legacy_rows: `0`
- completed_outcomes_reviewed: `32`
- material_deviation_count: `18`
- latest_forecast_date: `2026-06-18`
- latest_reviewed_forecast_date: `2026-06-17`
- latest_market_date: `2026-06-22`
- data_freshness_status: `market_open_unconfirmed`
- largest_absolute_error: `0.034457`
- dominant_error_theme: `news_data_gap_limited_attribution`
- evidence_level: `early_evidence`
- validation_status: `early_evidence`
- update_blockers: `[{'reason': 'market_open_unconfirmed', 'detail': '当前行情日期来自美股盘中快照，尚未形成收盘确认数据。 盘中快照日期为 2026-06-22；正式 baseline_v1 预测记录应等美东 16:30 后重新生成。'}]`
- correction_policy: `past_forecasts_are_not_rewritten_only_actuals_and_error_fields_are_backfilled`
- model_learning_status: `insufficient_forward_evidence`

## Latest Material Deviations

### QQQ 1d from 2026-06-17

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.009392`
- actual_return: `0.025065`
- forecast_error: `0.034457`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, risk_on_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted, risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，复盘优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落或期货风险偏好改善。

### SPY 1d from 2026-06-17

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.012327`
- actual_return: `0.007801`
- forecast_error: `0.020127`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, risk_on_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted, risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，复盘优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落或期货风险偏好改善。

### IWM 1d from 2026-06-17

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.000618`
- actual_return: `0.019698`
- forecast_error: `0.01908`
- severity: `large`
- primary_hit: `True`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, breadth_follow_through_underweighted, risk_on_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted, breadth_follow_through_underweighted, risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，复盘优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落或期货风险偏好改善。

### SPY 1d from 2026-06-16

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.002396`
- actual_return: `-0.012488`
- forecast_error: `-0.014884`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### DIA 1d from 2026-06-16

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.001248`
- actual_return: `-0.009857`
- forecast_error: `-0.011105`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### IWM 1d from 2026-06-16

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.000627`
- actual_return: `-0.007532`
- forecast_error: `-0.008159`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### DIA 3d from 2026-06-15

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.012177`
- actual_return: `-0.005632`
- forecast_error: `-0.017809`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### QQQ 3d from 2026-06-15

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.011731`
- actual_return: `-0.004543`
- forecast_error: `-0.016274`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### IWM 3d from 2026-06-15

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.016341`
- actual_return: `0.003224`
- forecast_error: `-0.013117`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### SPY 3d from 2026-06-15

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.001631`
- actual_return: `-0.010718`
- forecast_error: `-0.012349`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### QQQ 1d from 2026-06-15

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.00391`
- actual_return: `-0.019005`
- forecast_error: `-0.022916`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### IWM 1d from 2026-06-15

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.005447`
- actual_return: `-0.008689`
- forecast_error: `-0.014136`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### IWM 3d from 2026-06-12

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.010671`
- actual_return: `-0.01048`
- forecast_error: `-0.021151`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 出现实质偏差，需要检查当时支持/冲突证据的权重是否合理。

### IWM 3d from 2026-06-12

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.010671`
- actual_return: `-0.01048`
- forecast_error: `-0.021151`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 出现实质偏差，需要检查当时支持/冲突证据的权重是否合理。

### QQQ 1d from 2026-06-12

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.001743`
- actual_return: `0.031414`
- forecast_error: `0.029671`
- severity: `extreme`
- primary_hit: `True`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, volatility_repair_underweighted, breadth_follow_through_underweighted, risk_on_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted, breadth_follow_through_underweighted, risk_on_flow_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势强于预测，复盘优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落或期货风险偏好改善。

### QQQ 1d from 2026-06-12

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.001743`
- actual_return: `0.031414`
- forecast_error: `0.029671`
- severity: `extreme`
- primary_hit: `True`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, volatility_repair_underweighted, breadth_follow_through_underweighted, risk_on_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted, breadth_follow_through_underweighted, risk_on_flow_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势强于预测，复盘优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落或期货风险偏好改善。

### SPY 1d from 2026-06-12

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.00313`
- actual_return: `0.017634`
- forecast_error: `0.020764`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, volatility_repair_underweighted, breadth_follow_through_underweighted, risk_on_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted, breadth_follow_through_underweighted, risk_on_flow_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势强于预测，复盘优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落或期货风险偏好改善。

### SPY 1d from 2026-06-12

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.00313`
- actual_return: `0.017634`
- forecast_error: `0.020764`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, volatility_repair_underweighted, breadth_follow_through_underweighted, risk_on_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted, breadth_follow_through_underweighted, risk_on_flow_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势强于预测，复盘优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落或期货风险偏好改善。


## Model Learning Summary

- status: `insufficient_forward_evidence`
- material_deviation_samples: `18`
- minimum_samples_before_weight_change: `20`
- recommended_challenger: `challenger_v2_error_learning`
- baseline_v1_policy: `frozen_do_not_rewrite`

### Lessons

- `news_data_gap_limited_attribution` count `18`: 新闻数据缺口会限制归因质量，需要标记而不是事后编故事。 Action: keep_observing_until_forward_sample_gate
- `intraday_snapshot_risk` count `18`: 该偏差主题需要继续积累样本后再判断是否稳定。 Action: keep_observing_until_forward_sample_gate
- `model_underestimated_downside_or_failed_bounce` count `11`: 模型低估了下跌延续或反抽失败风险，需要检查信用、宽度、波动率和新闻风险。 Action: keep_observing_until_forward_sample_gate
- `news_event_risk_underweighted` count `9`: 风险新闻如果被价格确认，应提高风险路径权重。 Action: shadow-test risk_event_confirmation：risk-off 新闻得到价格确认才提高风险路径。
- `model_underestimated_upside_or_repair` count `7`: 模型低估了修复/反抽强度，需要检查事件催化、波动率修复和价格确认。 Action: keep_observing_until_forward_sample_gate
- `news_event_driver_underweighted` count `7`: 重大新闻如果被价格确认，短周期影响可能大于历史相似样本。 Action: shadow-test event_reaction_overlay：新闻方向必须与 SPY/QQQ、VIX、HYG/LQD 价格反应一致。
- `volatility_repair_underweighted` count `7`: 波动率结构修复会放大短线反抽，需要进入 1d/3d/5d 权重。 Action: shadow-test vol_repair_boost：VIX term 修复提高短周期 bounce 权重。
- `risk_on_flow_underweighted` count `7`: risk-on flow 与成交量确认同向时，短线弹性可能被低估。 Action: shadow-test flow_confirmation_boost：risk-on flow 与成交量共振提高短线弹性。
- `breadth_follow_through_underweighted` count `5`: 宽度改善后的持续承接可能被低估。 Action: shadow-test breadth_follow_through：宽度改善持续两日以上才提高中期修复权重。
- `risk_off_news_overweighted_or_resolved` count `3`: risk-off 新闻若快速缓和或未被价格确认，不能继续压低主路径。 Action: shadow-test news_decay：未被价格确认或快速缓和的 risk-off 新闻权重衰减。

## Model Upgrade Plan

- 不改写旧预测；只允许回填 actual_return、best_matching_scenario、primary_hit、path_error。
- baseline_v1 保持冻结；经验先进入 challenger_v2_error_learning 的 shadow 评估。
- 在 challenger 中提高“重大新闻 + 价格反应确认”的短周期权重。
- 在 challenger 中要求 risk-off 新闻必须得到价格确认，否则降低风险路径权重。
- 在 challenger 中提高 VIX/VVIX/SKEW 修复对 1d/3d/5d 反抽路径的影响。
- 在 challenger 中提高 risk-on flow proxy 与成交量确认的共振权重。

## Guardrails

- This is forecast error attribution, not a trading or PnL report.
- Attribution is diagnostic and probabilistic; it is not proof of causality.
- Forecast fields are not rewritten. Only completed outcome fields are reviewed.
- Alpha v1 threshold remains frozen at 0.32534311.
- Baseline v1 is not changed by this review. Lessons must enter a challenger first.
