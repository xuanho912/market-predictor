# Stock Prediction Report

Generated at: `2026-09-15T17:03:04.068821+00:00`
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
- current_price: `211.66`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.1%`
- secondary: `stock_downside_continuation` / `21.1%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `40.73` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.8%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.84`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `206.77`
- risk_scenario_activation_level: `203.38`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `203.38`
- nearest_support: `207.25`
- nearest_resistance: `220.70`
- bounce_target_zone: `{"conservative": 216.18, "base": 216.18, "extended": 240.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 208.28, "critical_warning": 206.77, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `359.15`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `47.85` / `mixed`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `50.0%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.15`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `331.12`
- risk_scenario_activation_level: `331.12`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `331.12`
- nearest_support: `347.99`
- nearest_resistance: `375.88`
- bounce_target_zone: `{"conservative": 367.52, "base": 367.52, "extended": 395.2, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 352.87, "critical_warning": 331.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.65`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `31.5%`
- secondary: `stock_downside_continuation` / `21.6%`
- risk: `stock_event_risk` / `11.9%`
- stock_confluence_score: `37.46` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.2%`
- 60d_expected_return: `-3.2%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.32`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.18`
- risk_scenario_activation_level: `7.85`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.85`
- nearest_support: `8.23`
- nearest_resistance: `9.52`
- bounce_target_zone: `{"conservative": 9.09, "base": 9.09, "extended": 11.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.32, "critical_warning": 8.18, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `260.36`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `30.6%`
- secondary: `stock_downside_continuation` / `23.0%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `29.45` / `weak`
- stock_alpha_score_v1: `19.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.0%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.45`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `253.67`
- risk_scenario_activation_level: `249.04`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `249.04`
- nearest_support: `259.61`
- nearest_resistance: `272.71`
- bounce_target_zone: `{"conservative": 266.54, "base": 266.54, "extended": 314.03, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 255.73, "critical_warning": 253.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
