# Forecast Deviation Review

Generated at: `2026-09-23T23:03:34.574712+00:00`

This report reviews forecast-vs-actual deviations after horizons complete. It is not a trading, PnL or execution report.

## Summary

- total_forecast_records: `288`
- raw_forecast_rows: `288`
- deduped_legacy_rows: `0`
- completed_outcomes_reviewed: `1325`
- material_deviation_count: `711`
- latest_forecast_date: `2026-09-23`
- latest_reviewed_forecast_date: `2026-09-22`
- latest_market_date: `2026-09-23`
- data_freshness_status: `fresh`
- largest_absolute_error: `0.264365`
- dominant_error_theme: `news_data_gap_limited_attribution`
- evidence_level: `stronger_evidence`
- validation_status: `early_evidence`
- update_blockers: `[{'reason': 'no_future_market_close_yet', 'detail': 'Latest market date 2026-09-23 is not after latest forecast date 2026-09-23, so no completed 1d/3d/5d outcome can be scored yet.'}]`
- correction_policy: `past_forecasts_are_not_rewritten_only_actuals_and_error_fields_are_backfilled`
- model_learning_status: `lessons_ready_for_shadow_challenger`

## Latest Material Deviations

### IWM 1d from 2026-09-22

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.003108`
- actual_return: `-0.018419`
- forecast_error: `-0.01531`
- severity: `large`
- primary_hit: `True`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, breadth_conflict_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_risk_underweighted, breadth_conflict_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### QQQ 1d from 2026-09-22

- primary_scenario: `bounce_path`
- secondary_scenario: `bearish_path`
- risk_scenario: `bearish_path`
- expected_return: `0.003061`
- actual_return: `-0.008362`
- forecast_error: `-0.011423`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_downside_or_failed_bounce, news_event_risk_underweighted, breadth_conflict_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_risk_underweighted, breadth_conflict_underweighted`
- overweighted_factors: `bounce_repair_assumption`
- diagnostic_note: 实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。

### IWM 1d from 2026-09-21

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.013568`
- actual_return: `0.005708`
- forecast_error: `0.019276`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### SPY 1d from 2026-09-21

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.016455`
- actual_return: `-0.000155`
- forecast_error: `0.016299`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, volatility_repair_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### QQQ 1d from 2026-09-21

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.004756`
- actual_return: `0.008079`
- forecast_error: `0.012834`
- severity: `moderate`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### SPY 3d from 2026-09-18

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.025287`
- actual_return: `0.008035`
- forecast_error: `0.033322`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### QQQ 3d from 2026-09-18

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.000648`
- actual_return: `0.027389`
- forecast_error: `0.028037`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### IWM 3d from 2026-09-18

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.028783`
- actual_return: `-0.007673`
- forecast_error: `0.021109`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `analog_average_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### QQQ 1d from 2026-09-18

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.000216`
- actual_return: `0.02775`
- forecast_error: `0.027965`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### SPY 1d from 2026-09-18

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.008429`
- actual_return: `0.015505`
- forecast_error: `0.023934`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### IWM 1d from 2026-09-18

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.009594`
- actual_return: `0.005209`
- forecast_error: `0.014804`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### SPY 3d from 2026-09-17

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.021725`
- actual_return: `0.014136`
- forecast_error: `0.035861`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### IWM 3d from 2026-09-17

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.028783`
- actual_return: `0.006236`
- forecast_error: `0.035019`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### QQQ 3d from 2026-09-17

- primary_scenario: `bearish_path`
- secondary_scenario: `bounce_path`
- risk_scenario: `bearish_path`
- expected_return: `0.014282`
- actual_return: `0.042599`
- forecast_error: `0.028317`
- severity: `large`
- primary_hit: `True`
- best_matching_scenario: `bearish_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, volatility_repair_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted, volatility_repair_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### QQQ 5d from 2026-09-16

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.009428`
- actual_return: `0.05178`
- forecast_error: `0.061208`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### SPY 5d from 2026-09-16

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.026381`
- actual_return: `0.018248`
- forecast_error: `0.044629`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### IWM 5d from 2026-09-16

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.041148`
- actual_return: `-0.007044`
- forecast_error: `0.034104`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `expected_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: ``
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### QQQ 3d from 2026-09-16

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.016606`
- actual_return: `0.052148`
- forecast_error: `0.068755`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### SPY 3d from 2026-09-16

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.023405`
- actual_return: `0.025794`
- forecast_error: `0.049199`
- severity: `extreme`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。

### IWM 3d from 2026-09-16

- primary_scenario: `bearish_path`
- secondary_scenario: `analog_average_path`
- risk_scenario: `bearish_path`
- expected_return: `-0.026719`
- actual_return: `0.005847`
- forecast_error: `0.032566`
- severity: `large`
- primary_hit: `False`
- best_matching_scenario: `bounce_path`
- likely_error_drivers: `model_underestimated_upside_or_repair, news_event_driver_underweighted, risk_off_news_overweighted_or_resolved, news_data_gap_limited_attribution`
- underweighted_factors: `news_event_driver_underweighted`
- overweighted_factors: `risk_off_news_or_macro_risk`
- diagnostic_note: 实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。


## Model Learning Summary

- status: `lessons_ready_for_shadow_challenger`
- material_deviation_samples: `711`
- minimum_samples_before_weight_change: `20`
- recommended_challenger: `challenger_v2_error_learning`
- baseline_v1_policy: `frozen_do_not_rewrite`

### Lessons

- `news_data_gap_limited_attribution` count `711`: 新闻数据缺口会限制归因质量，需要标记而不是事后编故事。 Action: keep_observing_until_forward_sample_gate
- `model_underestimated_upside_or_repair` count `395`: 模型低估了修复/反抽强度，需要检查事件催化、波动率修复和价格确认。 Action: keep_observing_until_forward_sample_gate
- `news_event_driver_underweighted` count `395`: 重大新闻如果被价格确认，短周期影响可能大于历史相似样本。 Action: shadow-test event_reaction_overlay：新闻方向必须与 SPY/QQQ、VIX、HYG/LQD 价格反应一致。
- `risk_off_news_overweighted_or_resolved` count `324`: risk-off 新闻若快速缓和或未被价格确认，不应继续压低主路径。 Action: shadow-test news_decay：未被价格确认或快速缓和的 risk-off 新闻权重衰减。
- `model_underestimated_downside_or_failed_bounce` count `316`: 模型低估了下跌延续或反抽失败风险，需要检查信用、宽度、波动率和新闻风险。 Action: keep_observing_until_forward_sample_gate
- `news_event_risk_underweighted` count `299`: 风险新闻如果被价格确认，应提高风险路径权重。 Action: shadow-test risk_event_confirmation：risk-off 新闻得到价格确认才提高风险路径。
- `volatility_repair_underweighted` count `129`: 波动率结构修复会放大短线反抽，需要进入 1d/3d/5d 权重验证。 Action: shadow-test vol_repair_boost：VIX term 修复提高短周期 bounce 权重。
- `breadth_conflict_underweighted` count `94`: 指数上涨但内部参与不足时，失败反抽风险可能被低估。 Action: shadow-test breadth_conflict_penalty：宽度冲突提高 failed_bounce 风险。
- `breadth_follow_through_underweighted` count `74`: 宽度改善后的持续承接可能被低估。 Action: shadow-test breadth_follow_through：宽度改善持续两日以上才提高中期修复权重。
- `risk_on_flow_underweighted` count `60`: risk-on flow 与成交量确认同向时，短线弹性可能被低估。 Action: shadow-test flow_confirmation_boost：risk-on flow 与成交量共振提高短线弹性。
- `risk_off_flow_underweighted` count `7`: risk-off flow 与价格走弱同向时，下跌延续风险可能被低估。 Action: shadow-test flow_conflict_penalty：risk-off flow 提高 downside continuation。

## Model Upgrade Plan

- 不改写旧预测；只允许回填 actual_return、best_matching_scenario、primary_hit、path_error。
- baseline_v1 保持冻结；经验先进入 challenger_v2_error_learning 的 shadow 评估。
- 在 challenger 中提高“重大新闻 + 价格反应确认”的短周期权重。
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
