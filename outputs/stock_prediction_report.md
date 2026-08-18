# Stock Prediction Report

Generated at: `2026-08-18T13:12:10.466397+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `TSLA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `225.01`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `18.6%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `49.46` / `mixed`
- stock_alpha_score_v1: `52.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `63.7%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.7`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `228.00`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `227.92`
- breakout_level: `228.00`
- breakdown_level: `190.01`
- nearest_support: `219.70`
- nearest_resistance: `227.92`
- bounce_target_zone: `{"conservative": 228.99, "base": 228.99, "extended": 233.23, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 222.02, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `339.30`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.7%`
- secondary: `stock_failed_bounce` / `24.5%`
- risk: `stock_event_risk` / `10.1%`
- stock_confluence_score: `30.41` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.6%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.26`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `67.86`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.07`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `384.07`
- breakout_level: `384.07`
- breakdown_level: `297.38`
- nearest_support: `330.49`
- nearest_resistance: `352.52`
- bounce_target_zone: `{"conservative": 345.91, "base": 345.91, "extended": 392.88, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 334.34, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.19`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.0%`
- secondary: `stock_downside_continuation` / `19.2%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `30.3` / `weak`
- stock_alpha_score_v1: `6.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.7%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `39.24`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.14`
- primary_invalidation_level: `7.54`
- risk_scenario_activation_level: `7.54`
- trend_repair_confirmation_level: `10.14`
- breakout_level: `10.14`
- breakdown_level: `7.54`
- nearest_support: `8.63`
- nearest_resistance: `10.03`
- bounce_target_zone: `{"conservative": 9.61, "base": 9.61, "extended": 10.7, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.87, "critical_warning": 7.54, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `278.20`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.1%`
- secondary: `stock_downside_continuation` / `19.9%`
- risk: `stock_event_risk` / `12.2%`
- stock_confluence_score: `38.66` / `weak`
- stock_alpha_score_v1: `37.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.3%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.85`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `255.72`
- risk_scenario_activation_level: `255.72`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `255.72`
- nearest_support: `269.79`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 284.51, "base": 284.51, "extended": 295.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 273.47, "critical_warning": 255.72, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
