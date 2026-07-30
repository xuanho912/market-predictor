# Forecast Deviation Review

Generated at: `2026-07-30T04:26:16.925915+00:00`

This report reviews forecast-vs-actual deviations after horizons complete. It is not a trading, PnL or execution report.

## Summary

- total_forecast_records: `132`
- raw_forecast_rows: `132`
- deduped_legacy_rows: `0`
- completed_outcomes_reviewed: `504`
- material_deviation_count: `236`
- latest_forecast_date: `2026-07-29`
- latest_reviewed_forecast_date: `2026-07-28`
- latest_market_date: `2026-07-29`
- data_freshness_status: `market_open_unconfirmed`
- largest_absolute_error: `0.13694`
- dominant_error_theme: `news_data_gap_limited_attribution`
- evidence_level: `stronger_evidence`
- validation_status: `early_evidence`
- update_blockers: `[{'reason': 'market_open_unconfirmed', 'detail': '当前仍处于美股盘中或收盘确认前，尚未形成完整收盘数据。 当前盘中快照日期为 2026-07-29，最近完整收盘交易日为 2026-07-29；正式 baseline_v1 预测记录应等美东 16:30 后重新生成。'}, {'reason': 'no_future_market_close_yet', 'detail': 'Latest market date 2026-07-29 is not after latest forecast date 2026-07-29, so no completed 1d/3d/5d outcome can be scored yet.'}]`
- correction_policy: `past_forecasts_are_not_rewritten_only_actuals_and_error_fields_are_backfilled`
- model_learning_status: `lessons_ready_for_shadow_challenger`

## Latest Material Deviations

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

### SPY 1d from 2026-07-27

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.019764`
- actual_return: `0.002395`
- forecast_error: `0.022159`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 1d from 2026-07-27

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.009834`
- actual_return: `0.010801`
- forecast_error: `0.020635`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, breadth_follow_through_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 1d from 2026-07-27

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.013327`
- actual_return: `0.00157`
- forecast_error: `0.014897`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 3d from 2026-07-24

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.03694`
- actual_return: `-0.012816`
- forecast_error: `0.024125`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: ``
- diagnostic_note: 出现实质偏差，需要复盘当时支持/冲突证据的权重是否合理；该归因是诊断，不是因果证明。

### QQQ 3d from 2026-07-24

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.020094`
- actual_return: `-0.032884`
- forecast_error: `-0.01279`
- severity: `moderate`
- primary_hit: `True`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, breadth_conflict_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, breadth_conflict_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### SPY 1d from 2026-07-24

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.012313`
- actual_return: `0.000217`
- forecast_error: `0.01253`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 1d from 2026-07-24

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.006171`
- actual_return: `0.005976`
- forecast_error: `0.012147`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 3d from 2026-07-23

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.030388`
- actual_return: `0.004382`
- forecast_error: `0.03477`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 3d from 2026-07-23

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.013219`
- actual_return: `0.02059`
- forecast_error: `0.033809`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, breadth_follow_through_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 3d from 2026-07-23

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.028438`
- actual_return: `0.003631`
- forecast_error: `0.032069`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 1d from 2026-07-23

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.017258`
- actual_return: `0.001016`
- forecast_error: `0.018274`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### DIA 1d from 2026-07-23

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.012211`
- actual_return: `0.004843`
- forecast_error: `0.017054`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, breadth_follow_through_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `breadth_follow_through_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 1d from 2026-07-23

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.017905`
- actual_return: `-0.00315`
- forecast_error: `0.014755`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: ``
- diagnostic_note: 出现实质偏差，需要复盘当时支持/冲突证据的权重是否合理；该归因是诊断，不是因果证明。

### QQQ 5d from 2026-07-22

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.024155`
- actual_return: `-0.061842`
- forecast_error: `-0.037687`
- severity: `large`
- primary_hit: `True`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, breadth_conflict_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, breadth_conflict_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### SPY 5d from 2026-07-22

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.041716`
- actual_return: `-0.024016`
- forecast_error: `0.0177`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, volatility_repair_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `volatility_repair_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势强于预测，可能低估了波动率回落和恐慌释放后的修复力度。

### SPY 3d from 2026-07-22

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.030278`
- actual_return: `-0.011132`
- forecast_error: `0.019147`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, volatility_repair_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `volatility_repair_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势强于预测，可能低估了波动率回落和恐慌释放后的修复力度。

### IWM 3d from 2026-07-22

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.015078`
- actual_return: `-0.002995`
- forecast_error: `0.012083`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, volatility_repair_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `volatility_repair_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势强于预测，可能低估了波动率回落和恐慌释放后的修复力度。

### QQQ 1d from 2026-07-22

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.008256`
- actual_return: `-0.018983`
- forecast_error: `-0.010728`
- severity: `moderate`
- primary_hit: `True`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, breadth_conflict_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, breadth_conflict_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。


## Model Learning Summary

- status: `lessons_ready_for_shadow_challenger`
- material_deviation_samples: `236`
- minimum_samples_before_weight_change: `20`
- recommended_challenger: `challenger_v2_error_learning`
- baseline_v1_policy: `frozen_do_not_rewrite`

### Lessons

- `news_data_gap_limited_attribution` count `236`: 新闻数据缺口会限制归因质量，需要标记而不是事后编故事。 Action: keep_observing_until_forward_sample_gate
- `intraday_snapshot_risk` count `236`: 盘中快照未确认时，不应冻结为正式收盘预测。 Action: keep_observing_until_forward_sample_gate
- `model_underestimated_downside_or_failed_bounce` count `131`: 模型低估了下跌延续或反抽失败风险，需要检查信用、宽度、波动率和新闻风险。 Action: keep_observing_until_forward_sample_gate
- `news_event_risk_underweighted` count `131`: 风险新闻如果被价格确认，应提高风险路径权重。 Action: shadow-test risk_event_confirmation：risk-off 新闻得到价格确认才提高风险路径。
- `model_underestimated_upside_or_repair` count `105`: 模型低估了修复/反抽强度，需要检查事件催化、波动率修复和价格确认。 Action: keep_observing_until_forward_sample_gate
- `risk_off_news_overweighted_or_resolved` count `73`: risk-off 新闻若快速缓和或未被价格确认，不应继续压低主路径。 Action: shadow-test news_decay：未被价格确认或快速缓和的 risk-off 新闻权重衰减。
- `breadth_conflict_underweighted` count `40`: 指数上涨但内部参与不足时，失败反抽风险可能被低估。 Action: shadow-test breadth_conflict_penalty：宽度冲突提高 failed_bounce 风险。
- `risk_on_flow_underweighted` count `25`: risk-on flow 与成交量确认同向时，短线弹性可能被低估。 Action: shadow-test flow_confirmation_boost：risk-on flow 与成交量共振提高短线弹性。
- `volatility_repair_underweighted` count `21`: 波动率结构修复会放大短线反抽，需要进入 1d/3d/5d 权重验证。 Action: shadow-test vol_repair_boost：VIX term 修复提高短周期 bounce 权重。
- `breadth_follow_through_underweighted` count `19`: 宽度改善后的持续承接可能被低估。 Action: shadow-test breadth_follow_through：宽度改善持续两日以上才提高中期修复权重。
- `risk_off_flow_underweighted` count `4`: risk-off flow 与价格走弱同向时，下跌延续风险可能被低估。 Action: shadow-test flow_conflict_penalty：risk-off flow 提高 downside continuation。

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
