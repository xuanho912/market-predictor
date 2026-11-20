# Forecast Deviation Review

Generated at: `2026-11-20T12:12:52.693922+00:00`

This report reviews forecast-vs-actual deviations after horizons complete. It is not a trading, PnL or execution report.

## Summary

- total_forecast_records: `452`
- raw_forecast_rows: `452`
- deduped_legacy_rows: `0`
- completed_outcomes_reviewed: `2316`
- material_deviation_count: `1311`
- latest_forecast_date: `2026-11-19`
- latest_reviewed_forecast_date: `2026-11-18`
- latest_market_date: `2026-11-19`
- data_freshness_status: `market_open_unconfirmed`
- largest_absolute_error: `0.264365`
- dominant_error_theme: `news_data_gap_limited_attribution`
- evidence_level: `stronger_evidence`
- validation_status: `early_evidence`
- update_blockers: `[{'reason': 'market_open_unconfirmed', 'detail': '当前仍处于美股盘中或收盘确认前，尚未形成完整收盘数据。 当前盘中快照日期为 2026-11-19，最近完整收盘交易日为 2026-11-19；正式 baseline_v1 预测记录应等美东 16:30 后重新生成。'}, {'reason': 'no_future_market_close_yet', 'detail': 'Latest market date 2026-11-19 is not after latest forecast date 2026-11-19, so no completed 1d/3d/5d outcome can be scored yet.'}]`
- correction_policy: `past_forecasts_are_not_rewritten_only_actuals_and_error_fields_are_backfilled`
- model_learning_status: `lessons_ready_for_shadow_challenger`

## Latest Material Deviations

### QQQ 1d from 2026-11-18

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.006169`
- actual_return: `-0.021941`
- forecast_error: `-0.015772`
- severity: `large`
- primary_hit: `True`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, volatility_or_tail_risk_underweighted, breadth_conflict_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, volatility_or_tail_risk_underweighted, breadth_conflict_underweighted, risk_off_flow_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### IWM 1d from 2026-11-18

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.010484`
- actual_return: `-0.021842`
- forecast_error: `-0.011358`
- severity: `moderate`
- primary_hit: `True`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, volatility_or_tail_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, volatility_or_tail_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### QQQ 1d from 2026-11-17

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.014222`
- actual_return: `0.003897`
- forecast_error: `0.018119`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### IWM 1d from 2026-11-17

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.008609`
- actual_return: `0.003977`
- forecast_error: `0.012586`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。

### SPY 1d from 2026-11-17

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.012828`
- actual_return: `-0.003058`
- forecast_error: `0.009769`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: ``
- overweighted_factors: ``
- diagnostic_note: 出现实质偏差，需要复盘当时支持/冲突证据的权重是否合理；该归因是诊断，不是因果证明。

### DIA 3d from 2026-11-16

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.013509`
- actual_return: `-0.048266`
- forecast_error: `-0.034758`
- severity: `large`
- primary_hit: `True`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, volatility_or_tail_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, volatility_or_tail_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### QQQ 3d from 2026-11-16

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.003072`
- actual_return: `-0.025251`
- forecast_error: `-0.022179`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, volatility_or_tail_risk_underweighted, breadth_conflict_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, volatility_or_tail_risk_underweighted, breadth_conflict_underweighted, risk_off_flow_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### IWM 3d from 2026-11-13

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.029198`
- actual_return: `-0.026735`
- forecast_error: `-0.055933`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### QQQ 3d from 2026-11-13

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `0.025375`
- actual_return: `-0.029975`
- forecast_error: `-0.05535`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, breadth_conflict_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, breadth_conflict_underweighted, risk_off_flow_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### DIA 3d from 2026-11-13

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.000912`
- actual_return: `-0.040944`
- forecast_error: `-0.041856`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### SPY 3d from 2026-11-13

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.003203`
- actual_return: `-0.03204`
- forecast_error: `-0.028837`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### QQQ 1d from 2026-11-13

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `0.000588`
- actual_return: `-0.026681`
- forecast_error: `-0.027269`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `expected_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, breadth_conflict_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, breadth_conflict_underweighted, risk_off_flow_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### IWM 1d from 2026-11-13

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.007337`
- actual_return: `-0.016574`
- forecast_error: `-0.023912`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### SPY 1d from 2026-11-13

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.003447`
- actual_return: `-0.019115`
- forecast_error: `-0.015668`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### DIA 1d from 2026-11-13

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.002077`
- actual_return: `-0.014279`
- forecast_error: `-0.012202`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### IWM 5d from 2026-11-12

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.034295`
- actual_return: `-0.05107`
- forecast_error: `-0.085365`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### DIA 5d from 2026-11-12

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.021648`
- actual_return: `-0.060635`
- forecast_error: `-0.082283`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### SPY 5d from 2026-11-12

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.026486`
- actual_return: `-0.054483`
- forecast_error: `-0.080969`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### QQQ 5d from 2026-11-12

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.008866`
- actual_return: `-0.062673`
- forecast_error: `-0.053807`
- severity: `extreme`
- primary_hit: `True`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, breadth_conflict_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, breadth_conflict_underweighted, risk_off_flow_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### IWM 3d from 2026-11-12

- primary_scenario: `bounce_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `0.025942`
- actual_return: `-0.033724`
- forecast_error: `-0.059665`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, risk_off_flow_underweighted, news_data_gap_limited_attribution, intraday_snapshot_risk`
- underweighted_factors: `news_event_risk_underweighted, risk_off_flow_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。


## Model Learning Summary

- status: `lessons_ready_for_shadow_challenger`
- material_deviation_samples: `1311`
- minimum_samples_before_weight_change: `20`
- recommended_challenger: `challenger_v2_error_learning`
- baseline_v1_policy: `frozen_do_not_rewrite`

### Lessons

- `news_data_gap_limited_attribution` count `1311`: 新闻数据缺口会限制归因质量，需要标记而不是事后编故事。 Action: keep_observing_until_forward_sample_gate
- `intraday_snapshot_risk` count `1311`: 盘中快照未确认时，不应冻结为正式收盘预测。 Action: keep_observing_until_forward_sample_gate
- `model_underestimated_upside_or_repair` count `740`: 模型低估了修复/反抽强度，需要检查事件催化、波动率修复和价格确认。 Action: keep_observing_until_forward_sample_gate
- `model_underestimated_downside_or_failed_bounce` count `571`: 模型低估了下跌延续或反抽失败风险，需要检查信用、宽度、波动率和新闻风险。 Action: keep_observing_until_forward_sample_gate
- `news_event_risk_underweighted` count `571`: 风险新闻如果被价格确认，应提高风险路径权重。 Action: shadow-test risk_event_confirmation：risk-off 新闻得到价格确认才提高风险路径。
- `risk_off_news_overweighted_or_resolved` count `551`: risk-off 新闻若快速缓和或未被价格确认，不应继续压低主路径。 Action: shadow-test news_decay：未被价格确认或快速缓和的 risk-off 新闻权重衰减。
- `breadth_conflict_underweighted` count `198`: 指数上涨但内部参与不足时，失败反抽风险可能被低估。 Action: shadow-test breadth_conflict_penalty：宽度冲突提高 failed_bounce 风险。
- `volatility_repair_underweighted` count `187`: 波动率结构修复会放大短线反抽，需要进入 1d/3d/5d 权重验证。 Action: shadow-test vol_repair_boost：VIX term 修复提高短周期 bounce 权重。
- `breadth_follow_through_underweighted` count `151`: 宽度改善后的持续承接可能被低估。 Action: shadow-test breadth_follow_through：宽度改善持续两日以上才提高中期修复权重。
- `risk_on_flow_underweighted` count `138`: risk-on flow 与成交量确认同向时，短线弹性可能被低估。 Action: shadow-test flow_confirmation_boost：risk-on flow 与成交量共振提高短线弹性。
- `risk_off_flow_underweighted` count `134`: risk-off flow 与价格走弱同向时，下跌延续风险可能被低估。 Action: shadow-test flow_conflict_penalty：risk-off flow 提高 downside continuation。
- `volatility_or_tail_risk_underweighted` count `41`: 尾部风险或波动率重新上升时，失败反抽/风险扩散可能被低估。 Action: shadow-test tail_risk_penalty：VVIX/SKEW/VIX term 恶化时提高风险路径。

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
