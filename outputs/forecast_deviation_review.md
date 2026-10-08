# Forecast Deviation Review

Generated at: `2026-10-08T01:23:48.417136+00:00`

This report reviews forecast-vs-actual deviations after horizons complete. It is not a trading, PnL or execution report.

## Summary

- total_forecast_records: `328`
- raw_forecast_rows: `328`
- deduped_legacy_rows: `0`
- completed_outcomes_reviewed: `1572`
- material_deviation_count: `845`
- latest_forecast_date: `2026-10-07`
- latest_reviewed_forecast_date: `2026-10-06`
- latest_market_date: `2026-10-07`
- data_freshness_status: `fresh`
- largest_absolute_error: `0.264365`
- dominant_error_theme: `news_data_gap_limited_attribution`
- evidence_level: `stronger_evidence`
- validation_status: `early_evidence`
- update_blockers: `[{'reason': 'no_future_market_close_yet', 'detail': 'Latest market date 2026-10-07 is not after latest forecast date 2026-10-07, so no completed 1d/3d/5d outcome can be scored yet.'}]`
- correction_policy: `past_forecasts_are_not_rewritten_only_actuals_and_error_fields_are_backfilled`
- model_learning_status: `lessons_ready_for_shadow_challenger`

## Latest Material Deviations

### SPY 1d from 2026-10-05

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.010056`
- actual_return: `0.005498`
- forecast_error: `0.015554`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 1d from 2026-10-05

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.004336`
- actual_return: `0.004784`
- forecast_error: `0.00912`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 3d from 2026-10-02

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.028438`
- actual_return: `0.009849`
- forecast_error: `0.038287`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 1d from 2026-10-02

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.009479`
- actual_return: `0.006743`
- forecast_error: `0.016223`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 1d from 2026-10-02

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.00777`
- actual_return: `0.006607`
- forecast_error: `0.014377`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 3d from 2026-10-01

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.021702`
- actual_return: `0.019765`
- forecast_error: `0.041466`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 3d from 2026-10-01

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.032975`
- actual_return: `0.008315`
- forecast_error: `0.04129`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 3d from 2026-10-01

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.001786`
- actual_return: `0.023759`
- forecast_error: `0.025545`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 3d from 2026-10-01

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.008145`
- actual_return: `0.011679`
- forecast_error: `0.019824`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 1d from 2026-10-01

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.018763`
- actual_return: `0.00896`
- forecast_error: `0.027723`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 1d from 2026-10-01

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.015024`
- actual_return: `0.007395`
- forecast_error: `0.02242`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 1d from 2026-10-01

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.008419`
- actual_return: `0.010175`
- forecast_error: `0.018594`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 1d from 2026-10-01

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.010528`
- actual_return: `0.004876`
- forecast_error: `0.015404`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, risk_on_flow_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `risk_on_flow_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 5d from 2026-09-30

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.003774`
- actual_return: `0.024278`
- forecast_error: `0.028052`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: ``
- diagnostic_note: 出现实质偏差，需要复盘当时支持/冲突证据的权重是否合理；该归因是诊断，不是因果证明。

### IWM 5d from 2026-09-30

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.02057`
- actual_return: `-0.000684`
- forecast_error: `0.019887`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: ``
- diagnostic_note: 出现实质偏差，需要复盘当时支持/冲突证据的权重是否合理；该归因是诊断，不是因果证明。

### IWM 3d from 2026-09-30

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.018671`
- actual_return: `0.019756`
- forecast_error: `0.038427`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: ``
- diagnostic_note: 出现实质偏差，需要复盘当时支持/冲突证据的权重是否合理；该归因是诊断，不是因果证明。

### QQQ 3d from 2026-09-30

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.013463`
- actual_return: `0.02221`
- forecast_error: `0.035673`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: ``
- diagnostic_note: 出现实质偏差，需要复盘当时支持/冲突证据的权重是否合理；该归因是诊断，不是因果证明。

### IWM 1d from 2026-09-30

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.006224`
- actual_return: `0.004066`
- forecast_error: `0.01029`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: ``
- diagnostic_note: 出现实质偏差，需要复盘当时支持/冲突证据的权重是否合理；该归因是诊断，不是因果证明。

### SPY 5d from 2026-09-29

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.03979`
- actual_return: `0.019484`
- forecast_error: `0.059274`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, breadth_follow_through_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 5d from 2026-09-29

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.029057`
- actual_return: `0.008351`
- forecast_error: `0.037408`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。


## Model Learning Summary

- status: `lessons_ready_for_shadow_challenger`
- material_deviation_samples: `845`
- minimum_samples_before_weight_change: `20`
- recommended_challenger: `challenger_v2_error_learning`
- baseline_v1_policy: `frozen_do_not_rewrite`

### Lessons

- `news_data_gap_limited_attribution` count `845`: 新闻数据缺口会限制归因质量，需要标记而不是事后编故事。 Action: keep_observing_until_forward_sample_gate
- `model_underestimated_upside_or_repair` count `493`: 模型低估了修复/反抽强度，需要检查事件催化、波动率修复和价格确认。 Action: keep_observing_until_forward_sample_gate
- `risk_off_news_overweighted_or_resolved` count `381`: risk-off 新闻若快速缓和或未被价格确认，不应继续压低主路径。 Action: shadow-test news_decay：未被价格确认或快速缓和的 risk-off 新闻权重衰减。
- `model_underestimated_downside_or_failed_bounce` count `352`: 模型低估了下跌延续或反抽失败风险，需要检查信用、宽度、波动率和新闻风险。 Action: keep_observing_until_forward_sample_gate
- `news_event_risk_underweighted` count `352`: 风险新闻如果被价格确认，应提高风险路径权重。 Action: shadow-test risk_event_confirmation：risk-off 新闻得到价格确认才提高风险路径。
- `volatility_repair_underweighted` count `157`: 波动率结构修复会放大短线反抽，需要进入 1d/3d/5d 权重验证。 Action: shadow-test vol_repair_boost：VIX term 修复提高短周期 bounce 权重。
- `breadth_conflict_underweighted` count `110`: 指数上涨但内部参与不足时，失败反抽风险可能被低估。 Action: shadow-test breadth_conflict_penalty：宽度冲突提高 failed_bounce 风险。
- `risk_on_flow_underweighted` count `83`: risk-on flow 与成交量确认同向时，短线弹性可能被低估。 Action: shadow-test flow_confirmation_boost：risk-on flow 与成交量共振提高短线弹性。
- `breadth_follow_through_underweighted` count `81`: 宽度改善后的持续承接可能被低估。 Action: shadow-test breadth_follow_through：宽度改善持续两日以上才提高中期修复权重。
- `risk_off_flow_underweighted` count `9`: risk-off flow 与价格走弱同向时，下跌延续风险可能被低估。 Action: shadow-test flow_conflict_penalty：risk-off flow 提高 downside continuation。

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
