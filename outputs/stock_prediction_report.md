# Stock Prediction Report

Generated at: `2026-07-07T15:18:00.821592+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `SMR`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `192.74`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.2%`
- secondary: `stock_failed_bounce` / `26.2%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `33.96` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.8%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `39.34`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `188.77`
- risk_scenario_activation_level: `186.02`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `186.02`
- nearest_support: `189.80`
- nearest_resistance: `200.08`
- bounce_target_zone: `{"conservative": 196.41, "base": 196.41, "extended": 218.88, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 189.99, "critical_warning": 188.77, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `407.39`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.0%`
- secondary: `stock_downside_continuation` / `18.3%`
- risk: `stock_event_risk` / `16.2%`
- stock_confluence_score: `37.8` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.8%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.66`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `391.42`
- nearest_resistance: `431.35`
- bounce_target_zone: `{"conservative": 419.37, "base": 419.37, "extended": 448.83, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 398.4, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.77`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.4%`
- secondary: `stock_failed_bounce` / `24.2%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `32.05` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `20.7%`
- 60d_expected_return: `-4.2%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `56.81`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `8.20`
- risk_scenario_activation_level: `7.81`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `7.81`
- nearest_support: `8.64`
- nearest_resistance: `9.83`
- bounce_target_zone: `{"conservative": 9.3, "base": 9.3, "extended": 12.56, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.38, "critical_warning": 8.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `240.88`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.4%`
- secondary: `stock_failed_bounce` / `27.0%`
- risk: `stock_event_risk` / `10.2%`
- stock_confluence_score: `25.22` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.9%`
- 60d_expected_return: `-1.8%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `53.25`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `232.89`
- nearest_resistance: `252.87`
- bounce_target_zone: `{"conservative": 246.88, "base": 246.88, "extended": 290.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 236.38, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
