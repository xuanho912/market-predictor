# Stock Prediction Report

Generated at: `2026-11-10T19:47:16.224977+00:00`
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
- current_price: `167.34`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.7%`
- secondary: `stock_failed_bounce` / `26.9%`
- risk: `stock_event_risk` / `13.2%`
- stock_confluence_score: `36.03` / `weak`
- stock_alpha_score_v1: `33.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.6%`
- 60d_expected_return: `-3.0%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `75.1`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `226.00`
- primary_invalidation_level: `161.32`
- risk_scenario_activation_level: `157.15`
- trend_repair_confirmation_level: `226.00`
- breakout_level: `226.00`
- breakdown_level: `157.15`
- nearest_support: `166.24`
- nearest_resistance: `178.46`
- bounce_target_zone: `{"conservative": 172.9, "base": 172.9, "extended": 233.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 163.17, "critical_warning": 161.32, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `378.52`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_trend_repair` / `16.4%`
- risk: `stock_downside_continuation` / `16.2%`
- stock_confluence_score: `47.22` / `mixed`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.4%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.6`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `46.95`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `363.95`
- nearest_resistance: `400.37`
- bounce_target_zone: `{"conservative": 389.44, "base": 389.44, "extended": 428.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 369.78, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.16`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.1%`
- secondary: `stock_failed_bounce` / `20.2%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `37.49` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `20.6%`
- 60d_expected_return: `-4.6%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `73.17`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.32`
- primary_invalidation_level: `4.28`
- risk_scenario_activation_level: `4.28`
- trend_repair_confirmation_level: `6.32`
- breakout_level: `6.32`
- breakdown_level: `4.28`
- nearest_support: `4.78`
- nearest_resistance: `5.72`
- bounce_target_zone: `{"conservative": 5.44, "base": 5.44, "extended": 6.7, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.94, "critical_warning": 4.28, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `265.33`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.3%`
- secondary: `stock_failed_bounce` / `25.8%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `34.87` / `weak`
- stock_alpha_score_v1: `21.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.1%`
- 60d_expected_return: `-2.4%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.14`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `294.50`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `294.50`
- breakout_level: `294.50`
- breakdown_level: `231.30`
- nearest_support: `254.43`
- nearest_resistance: `281.67`
- bounce_target_zone: `{"conservative": 273.5, "base": 273.5, "extended": 305.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 259.2, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
