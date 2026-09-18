# Stock Prediction Report

Generated at: `2026-09-18T01:16:41.510366+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `CEG`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `219.34`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `42.93` / `weak`
- stock_alpha_score_v1: `43.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.0%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.14`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `214.15`
- nearest_resistance: `227.13`
- bounce_target_zone: `{"conservative": 223.23, "base": 223.23, "extended": 239.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 216.42, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `366.20`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `15.9%`
- stock_confluence_score: `41.32` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.5%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.9`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `338.96`
- risk_scenario_activation_level: `338.96`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `338.96`
- nearest_support: `354.64`
- nearest_resistance: `383.55`
- bounce_target_zone: `{"conservative": 374.87, "base": 374.87, "extended": 395.6, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 359.7, "critical_warning": 338.96, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.04`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.6%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `13.5%`
- stock_confluence_score: `33.34` / `weak`
- stock_alpha_score_v1: `4.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.0%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.12`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.05`
- risk_scenario_activation_level: `8.05`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `8.05`
- nearest_support: `8.47`
- nearest_resistance: `9.89`
- bounce_target_zone: `{"conservative": 9.47, "base": 9.47, "extended": 11.94, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.72, "critical_warning": 8.05, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `262.80`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `28.8%`
- secondary: `stock_downside_continuation` / `23.9%`
- risk: `stock_event_risk` / `10.6%`
- stock_confluence_score: `29.55` / `weak`
- stock_alpha_score_v1: `24.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.0%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `42.25`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `254.71`
- risk_scenario_activation_level: `250.95`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `250.95`
- nearest_support: `254.71`
- nearest_resistance: `275.73`
- bounce_target_zone: `{"conservative": 269.27, "base": 269.27, "extended": 314.42, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 257.95, "critical_warning": 254.71, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
