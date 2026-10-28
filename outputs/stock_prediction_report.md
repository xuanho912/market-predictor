# Stock Prediction Report

Generated at: `2026-10-28T01:51:43.197428+00:00`
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
- current_price: `217.94`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `21.6%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `42.91` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.9%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.67`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `210.18`
- risk_scenario_activation_level: `210.18`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `210.18`
- nearest_support: `212.98`
- nearest_resistance: `225.38`
- bounce_target_zone: `{"conservative": 221.66, "base": 221.66, "extended": 248.33, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 215.15, "critical_warning": 210.18, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `407.46`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `25.1%`
- secondary: `stock_failed_bounce` / `22.1%`
- risk: `stock_downside_continuation` / `15.9%`
- stock_confluence_score: `52.76` / `mixed`
- stock_alpha_score_v1: `25.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `62.2%`
- 60d_expected_return: `0.2%`
- risk_reward_ratio: `0.77`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `413.66`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `423.99`
- breakout_level: `413.66`
- breakdown_level: `345.88`
- nearest_support: `396.43`
- nearest_resistance: `408.45`
- bounce_target_zone: `{"conservative": 415.73, "base": 423.99, "extended": 423.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 400.85, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.70`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.9%`
- secondary: `stock_failed_bounce` / `17.6%`
- risk: `stock_event_risk` / `11.1%`
- stock_confluence_score: `35.55` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `16.4%`
- 60d_expected_return: `-3.3%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `74.61`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `5.20`
- risk_scenario_activation_level: `5.20`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `5.20`
- nearest_support: `5.36`
- nearest_resistance: `6.22`
- bounce_target_zone: `{"conservative": 5.96, "base": 5.96, "extended": 8.71, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.51, "critical_warning": 5.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `258.98`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.2%`
- secondary: `stock_downside_continuation` / `22.7%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `29.84` / `weak`
- stock_alpha_score_v1: `21.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.1%`
- 60d_expected_return: `-1.8%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.66`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `244.39`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `244.39`
- nearest_support: `248.37`
- nearest_resistance: `274.90`
- bounce_target_zone: `{"conservative": 266.94, "base": 266.94, "extended": 320.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 253.01, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
