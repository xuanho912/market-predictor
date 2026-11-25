# Stock Prediction Report

Generated at: `2026-11-25T04:34:29.438000+00:00`
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
- current_price: `155.38`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.3%`
- secondary: `stock_failed_bounce` / `19.7%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `35.93` / `weak`
- stock_alpha_score_v1: `23.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `33.7%`
- 60d_expected_return: `-5.2%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `76.32`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `219.99`
- primary_invalidation_level: `124.50`
- risk_scenario_activation_level: `124.50`
- trend_repair_confirmation_level: `219.99`
- breakout_level: `219.99`
- breakdown_level: `124.50`
- nearest_support: `142.46`
- nearest_resistance: `174.76`
- bounce_target_zone: `{"conservative": 165.07, "base": 165.07, "extended": 232.91, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 148.11, "critical_warning": 124.5, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `384.68`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.9%`
- secondary: `stock_downside_continuation` / `20.3%`
- risk: `stock_event_risk` / `15.8%`
- stock_confluence_score: `36.06` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.6%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.79`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `367.50`
- nearest_resistance: `410.45`
- bounce_target_zone: `{"conservative": 397.57, "base": 397.57, "extended": 431.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 375.01, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `3.30`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `39.4%`
- secondary: `stock_failed_bounce` / `21.8%`
- risk: `stock_event_risk` / `10.3%`
- stock_confluence_score: `42.26` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `8.0%`
- 60d_expected_return: `-9.1%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `100`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `2.99`
- risk_scenario_activation_level: `2.78`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `2.78`
- nearest_support: `3.27`
- nearest_resistance: `3.87`
- bounce_target_zone: `{"conservative": 3.59, "base": 3.59, "extended": 6.49, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 3.09, "critical_warning": 2.99, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `244.84`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.3%`
- secondary: `stock_downside_continuation` / `22.0%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `33.21` / `weak`
- stock_alpha_score_v1: `26.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.5%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.7`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `229.44`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `229.44`
- nearest_support: `233.64`
- nearest_resistance: `261.64`
- bounce_target_zone: `{"conservative": 253.24, "base": 253.24, "extended": 296.17, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 238.54, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
