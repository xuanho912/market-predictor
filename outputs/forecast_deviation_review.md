# Forecast Deviation Review

Generated at: `2026-07-01T23:55:40.941596+00:00`

This report reviews forecast-vs-actual deviations after horizons complete. It is not a trading, PnL or execution report.

## Summary

- total_forecast_records: `56`
- raw_forecast_rows: `56`
- deduped_legacy_rows: `0`
- completed_outcomes_reviewed: `148`
- material_deviation_count: `69`
- latest_forecast_date: `2026-07-01`
- latest_reviewed_forecast_date: `2026-06-30`
- latest_market_date: `2026-07-01`
- data_freshness_status: `fresh`
- largest_absolute_error: `0.067343`
- dominant_error_theme: `news_data_gap_limited_attribution`
- evidence_level: `stronger_evidence`
- validation_status: `early_evidence`
- update_blockers: `[{'reason': 'no_future_market_close_yet', 'detail': 'Latest market date 2026-07-01 is not after latest forecast date 2026-07-01, so no completed 1d/3d/5d outcome can be scored yet.'}]`
- correction_policy: `past_forecasts_are_not_rewritten_only_actuals_and_error_fields_are_backfilled`
- model_learning_status: `lessons_ready_for_shadow_challenger`

## Latest Material Deviations

### QQQ 1d from 2026-06-30

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.005603`
- actual_return: `-0.01525`
- forecast_error: `-0.020853`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_risk_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### QQQ 1d from 2026-06-29

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.003357`
- actual_return: `0.017015`
- forecast_error: `0.013658`
- severity: `moderate`
- primary_hit: `True`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, breadth_follow_through_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 1d from 2026-06-29

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.002042`
- actual_return: `0.007787`
- forecast_error: `0.009828`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, breadth_follow_through_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 3d from 2026-06-26

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.012431`
- actual_return: `0.008981`
- forecast_error: `0.021413`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 3d from 2026-06-26

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.008507`
- actual_return: `0.026397`
- forecast_error: `0.01789`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 1d from 2026-06-26

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.002836`
- actual_return: `0.024854`
- forecast_error: `0.022018`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 1d from 2026-06-26

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.004144`
- actual_return: `0.007591`
- forecast_error: `0.011734`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 1d from 2026-06-26

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.005544`
- actual_return: `0.016475`
- forecast_error: `0.010931`
- severity: `moderate`
- primary_hit: `True`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 3d from 2026-06-25

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.002536`
- actual_return: `0.027946`
- forecast_error: `0.02541`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 3d from 2026-06-25

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.014546`
- actual_return: `0.006028`
- forecast_error: `0.020574`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 1d from 2026-06-25

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.000845`
- actual_return: `-0.013764`
- forecast_error: `-0.014609`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, breadth_conflict_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_risk_underweighted, breadth_conflict_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### SPY 1d from 2026-06-25

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.005544`
- actual_return: `-0.007231`
- forecast_error: `-0.012776`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, breadth_conflict_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_risk_underweighted, breadth_conflict_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。

### SPY 5d from 2026-06-24

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.016413`
- actual_return: `0.017075`
- forecast_error: `0.033488`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 5d from 2026-06-24

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.023779`
- actual_return: `0.007483`
- forecast_error: `0.031262`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 5d from 2026-06-24

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.003619`
- actual_return: `0.020475`
- forecast_error: `0.024094`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 3d from 2026-06-24

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.014546`
- actual_return: `0.006094`
- forecast_error: `0.02064`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 3d from 2026-06-24

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.006648`
- actual_return: `0.010583`
- forecast_error: `0.017231`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `expected_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 3d from 2026-06-24

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.002536`
- actual_return: `0.018941`
- forecast_error: `0.016405`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 5d from 2026-06-23

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.018003`
- actual_return: `0.031878`
- forecast_error: `0.049881`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 5d from 2026-06-23

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.019128`
- actual_return: `0.01798`
- forecast_error: `0.037108`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。


## Model Learning Summary

- status: `lessons_ready_for_shadow_challenger`
- material_deviation_samples: `69`
- minimum_samples_before_weight_change: `20`
- recommended_challenger: `challenger_v2_error_learning`
- baseline_v1_policy: `frozen_do_not_rewrite`

### Lessons

- `news_data_gap_limited_attribution` count `69`: 新闻数据缺口会限制归因质量，需要标记而不是事后编故事。 Action: keep_observing_until_forward_sample_gate
- `model_underestimated_downside_or_failed_bounce` count `38`: 模型低估了下跌延续或反抽失败风险，需要检查信用、宽度、波动率和新闻风险。 Action: keep_observing_until_forward_sample_gate
- `news_event_risk_underweighted` count `38`: 风险新闻如果被价格确认，应提高风险路径权重。 Action: shadow-test risk_event_confirmation：risk-off 新闻得到价格确认才提高风险路径。
- `model_underestimated_upside_or_repair` count `31`: 模型低估了修复/反抽强度，需要检查事件催化、波动率修复和价格确认。 Action: keep_observing_until_forward_sample_gate
- `risk_off_news_overweighted_or_resolved` count `24`: risk-off 新闻若快速缓和或未被价格确认，不能继续压低主路径。 Action: shadow-test news_decay：未被价格确认或快速缓和的 risk-off 新闻权重衰减。
- `risk_on_flow_underweighted` count `17`: risk-on flow 与成交量确认同向时，短线弹性可能被低估。 Action: shadow-test flow_confirmation_boost：risk-on flow 与成交量共振提高短线弹性。
- `breadth_conflict_underweighted` count `9`: 指数上涨但内部参与不足时，失败反抽风险可能被低估。 Action: shadow-test breadth_conflict_penalty：宽度冲突提高 failed_bounce 风险。
- `breadth_follow_through_underweighted` count `8`: 宽度改善后的持续承接可能被低估。 Action: shadow-test breadth_follow_through：宽度改善持续两日以上才提高中期修复权重。
- `volatility_repair_underweighted` count `8`: 波动率结构修复会放大短线反抽，需要进入 1d/3d/5d 权重。 Action: shadow-test vol_repair_boost：VIX term 修复提高短周期 bounce 权重。

## Model Upgrade Plan

- 不改写旧预测；只允许回填 actual_return、best_matching_scenario、primary_hit、path_error。
- baseline_v1 保持冻结；经验先进入 challenger_v2_error_learning 的 shadow 评估。
- 在 challenger 中要求 risk-off 新闻必须得到价格确认，否则降低风险路径权重。
- 在 challenger 中提高 VIX/VVIX/SKEW 修复对 1d/3d/5d 反抽路径的影响。
- 在 challenger 中提高 breadth 冲突对失败反抽风险的惩罚。
- 在 challenger 中提高 risk-on flow proxy 与成交量确认的共振权重。

## Guardrails

- This is forecast error attribution, not a trading or PnL report.
- Attribution is diagnostic and probabilistic; it is not proof of causality.
- Forecast fields are not rewritten. Only completed outcome fields are reviewed.
- Alpha v1 threshold remains frozen at 0.32534311.
- Baseline v1 is not changed by this review. Lessons must enter a challenger first.
