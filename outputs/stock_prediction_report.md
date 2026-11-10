# Stock Prediction Report

Generated at: `2026-11-10T04:36:57.129413+00:00`
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

- company_name: `NVIDIA Corporation`
- status: `available`
- current_price: `178.67`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.5%`
- secondary: `stock_failed_bounce` / `25.8%`
- risk: `stock_event_risk` / `13.9%`
- stock_confluence_score: `39.57` / `weak`
- stock_alpha_score_v1: `33.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.7%`
- 60d_expected_return: `-2.5%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `54.43`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `228.64`
- primary_invalidation_level: `170.24`
- risk_scenario_activation_level: `169.01`
- trend_repair_confirmation_level: `228.64`
- breakout_level: `228.64`
- breakdown_level: `169.01`
- nearest_support: `171.64`
- nearest_resistance: `189.21`
- bounce_target_zone: `{"conservative": 183.94, "base": 183.94, "extended": 235.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 174.72, "critical_warning": 170.24, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `378.05`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `16.2%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `47.69` / `mixed`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.1%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `40.32`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `363.09`
- nearest_resistance: `400.49`
- bounce_target_zone: `{"conservative": 389.27, "base": 389.27, "extended": 429.19, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 369.63, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.44`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.7%`
- secondary: `stock_failed_bounce` / `19.0%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `39.76` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `21.6%`
- 60d_expected_return: `-4.0%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `67.38`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.61`
- primary_invalidation_level: `4.28`
- risk_scenario_activation_level: `4.28`
- trend_repair_confirmation_level: `6.61`
- breakout_level: `6.61`
- breakdown_level: `4.28`
- nearest_support: `5.06`
- nearest_resistance: `6.00`
- bounce_target_zone: `{"conservative": 5.72, "base": 5.72, "extended": 6.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.23, "critical_warning": 4.28, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `276.09`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.9%`
- secondary: `stock_downside_continuation` / `20.6%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `40.92` / `weak`
- stock_alpha_score_v1: `31.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.2%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.12`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `298.50`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `298.50`
- breakout_level: `298.50`
- breakdown_level: `231.30`
- nearest_support: `265.08`
- nearest_resistance: `292.61`
- bounce_target_zone: `{"conservative": 284.35, "base": 284.35, "extended": 309.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 269.89, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
