# Forecast Deviation Review

Generated at: `2026-08-04T06:18:41.540355+00:00`

This report reviews forecast-vs-actual deviations after horizons complete. It is not a trading, PnL or execution report.

## Summary

- total_forecast_records: `144`
- raw_forecast_rows: `144`
- deduped_legacy_rows: `0`
- completed_outcomes_reviewed: `564`
- material_deviation_count: `281`
- latest_forecast_date: `2026-08-03`
- latest_reviewed_forecast_date: `2026-07-31`
- latest_market_date: `2026-08-03`
- data_freshness_status: `market_open_unconfirmed`
- largest_absolute_error: `0.13694`
- dominant_error_theme: `news_data_gap_limited_attribution`
- evidence_level: `stronger_evidence`
- validation_status: `early_evidence`
- update_blockers: `[{'reason': 'market_open_unconfirmed', 'detail': '当前仍处于美股盘中或收盘确认前，尚未形成完整收盘数据。 当前盘中快照日期为 2026-08-03，最近完整收盘交易日为 2026-08-03；正式 baseline_v1 预测记录应等美东 16:30 后重新生成。'}, {'reason': 'no_future_market_close_yet', 'detail': 'Latest market date 2026-08-03 is not after latest forecast date 2026-08-03, so no completed 1d/3d/5d outcome can be scored yet.'}]`
- correction_policy: `past_forecasts_are_not_rewritten_only_actuals_and_error_fields_are_backfilled`
- model_learning_status: `lessons_ready_for_shadow_challenger`

## Latest Material Deviations

### IWM 1d from 2026-07-31

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.005026`
- actual_return: `0.017239`
- forecast_error: `0.022265`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `volatility_repair_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 1d from 2026-07-31

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.002916`
- actual_return: `0.017558`
- forecast_error: `0.020474`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `volatility_repair_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 1d from 2026-07-31

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.005027`
- actual_return: `0.01316`
- forecast_error: `0.018186`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, breadth_follow_through_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `volatility_repair_underweighted, breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 1d from 2026-07-31

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.00094`
- actual_return: `0.014243`
- forecast_error: `0.015183`
- severity: `large`
- primary_hit: `True`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, breadth_follow_through_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `volatility_repair_underweighted, breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 1d from 2026-07-30

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.003361`
- actual_return: `0.006496`
- forecast_error: `0.009856`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `expected_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `volatility_repair_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 3d from 2026-07-29

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.018111`
- actual_return: `0.057939`
- forecast_error: `0.07605`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 3d from 2026-07-29

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.028518`
- actual_return: `0.038672`
- forecast_error: `0.06719`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, breadth_follow_through_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 3d from 2026-07-29

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.005938`
- actual_return: `0.030675`
- forecast_error: `0.036612`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, breadth_follow_through_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 3d from 2026-07-29

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.00654`
- actual_return: `0.02651`
- forecast_error: `0.03305`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 1d from 2026-07-29

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.006037`
- actual_return: `0.032974`
- forecast_error: `0.039011`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 1d from 2026-07-29

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.009506`
- actual_return: `0.016766`
- forecast_error: `0.026272`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, breadth_follow_through_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 1d from 2026-07-29

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.00218`
- actual_return: `0.013931`
- forecast_error: `0.016111`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 1d from 2026-07-29

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.001979`
- actual_return: `0.011835`
- forecast_error: `0.013815`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, breadth_follow_through_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 3d from 2026-07-28

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.031987`
- actual_return: `0.008328`
- forecast_error: `0.040315`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, breadth_follow_through_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### QQQ 3d from 2026-07-28

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.004988`
- actual_return: `0.018505`
- forecast_error: `0.023493`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 3d from 2026-07-28

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.02644`
- actual_return: `-0.007397`
- forecast_error: `0.019044`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: ``
- diagnostic_note: 出现实质偏差，需要复盘当时支持/冲突证据的权重是否合理；该归因是诊断，不是因果证明。

### DIA 1d from 2026-07-28

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.000706`
- actual_return: `-0.021788`
- forecast_error: `-0.021082`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### QQQ 1d from 2026-07-28

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.001663`
- actual_return: `-0.02037`
- forecast_error: `-0.018708`
- severity: `large`
- primary_hit: `True`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, breadth_conflict_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, breadth_conflict_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### SPY 5d from 2026-07-27

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.048937`
- actual_return: `0.025139`
- forecast_error: `0.074076`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 5d from 2026-07-27

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.034726`
- actual_return: `0.0113`
- forecast_error: `0.046026`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。


## Model Learning Summary

- status: `lessons_ready_for_shadow_challenger`
- material_deviation_samples: `281`
- minimum_samples_before_weight_change: `20`
- recommended_challenger: `challenger_v2_error_learning`
- baseline_v1_policy: `frozen_do_not_rewrite`

### Lessons

- `news_data_gap_limited_attribution` count `281`: 新闻数据缺口会限制归因质量，需要标记而不是事后编故事。 Action: keep_observing_until_forward_sample_gate
- `intraday_snapshot_risk` count `281`: 盘中快照未确认时，不应冻结为正式收盘预测。 Action: keep_observing_until_forward_sample_gate
- `model_underestimated_upside_or_repair` count `141`: 模型低估了修复/反抽强度，需要检查事件催化、波动率修复和价格确认。 Action: keep_observing_until_forward_sample_gate
- `model_underestimated_downside_or_failed_bounce` count `140`: 模型低估了下跌延续或反抽失败风险，需要检查信用、宽度、波动率和新闻风险。 Action: keep_observing_until_forward_sample_gate
- `news_event_risk_underweighted` count `140`: 风险新闻如果被价格确认，应提高风险路径权重。 Action: shadow-test risk_event_confirmation：risk-off 新闻得到价格确认才提高风险路径。
- `risk_off_news_overweighted_or_resolved` count `105`: risk-off 新闻若快速缓和或未被价格确认，不应继续压低主路径。 Action: shadow-test news_decay：未被价格确认或快速缓和的 risk-off 新闻权重衰减。
- `breadth_conflict_underweighted` count `41`: 指数上涨但内部参与不足时，失败反抽风险可能被低估。 Action: shadow-test breadth_conflict_penalty：宽度冲突提高 failed_bounce 风险。
- `breadth_follow_through_underweighted` count `29`: 宽度改善后的持续承接可能被低估。 Action: shadow-test breadth_follow_through：宽度改善持续两日以上才提高中期修复权重。
- `volatility_repair_underweighted` count `27`: 波动率结构修复会放大短线反抽，需要进入 1d/3d/5d 权重验证。 Action: shadow-test vol_repair_boost：VIX term 修复提高短周期 bounce 权重。
- `risk_on_flow_underweighted` count `25`: risk-on flow 与成交量确认同向时，短线弹性可能被低估。 Action: shadow-test flow_confirmation_boost：risk-on flow 与成交量共振提高短线弹性。
- `risk_off_flow_underweighted` count `7`: risk-off flow 与价格走弱同向时，下跌延续风险可能被低估。 Action: shadow-test flow_conflict_penalty：risk-off flow 提高 downside continuation。

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
