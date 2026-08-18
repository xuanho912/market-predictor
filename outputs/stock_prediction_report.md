# Stock Prediction Report

Generated at: `2026-08-18T21:53:57.836441+00:00`
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
- current_price: `219.74`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `48.68` / `mixed`
- stock_alpha_score_v1: `51.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `62.4%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.31`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `227.92`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `227.92`
- breakout_level: `227.92`
- breakdown_level: `190.01`
- nearest_support: `214.47`
- nearest_resistance: `227.64`
- bounce_target_zone: `{"conservative": 223.69, "base": 223.69, "extended": 233.19, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 216.78, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `336.87`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.4%`
- secondary: `stock_failed_bounce` / `24.9%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `34.55` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `28.2%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.23`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `63.95`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `380.17`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `380.17`
- breakout_level: `380.17`
- breakdown_level: `297.38`
- nearest_support: `328.19`
- nearest_resistance: `349.90`
- bounce_target_zone: `{"conservative": 343.38, "base": 343.38, "extended": 388.85, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 331.99, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.64`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.9%`
- secondary: `stock_downside_continuation` / `22.0%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `30.58` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.4%`
- 60d_expected_return: `-3.1%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `49.14`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.14`
- primary_invalidation_level: `7.54`
- risk_scenario_activation_level: `7.54`
- trend_repair_confirmation_level: `10.14`
- breakout_level: `10.14`
- breakdown_level: `7.54`
- nearest_support: `8.09`
- nearest_resistance: `9.47`
- bounce_target_zone: `{"conservative": 9.05, "base": 9.05, "extended": 10.69, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.33, "critical_warning": 7.54, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `266.83`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.2%`
- secondary: `stock_downside_continuation` / `21.8%`
- risk: `stock_event_risk` / `11.3%`
- stock_confluence_score: `38.08` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.8%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.56`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `256.16`
- risk_scenario_activation_level: `254.72`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `254.72`
- nearest_support: `258.02`
- nearest_resistance: `280.04`
- bounce_target_zone: `{"conservative": 273.44, "base": 273.44, "extended": 295.81, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 261.87, "critical_warning": 256.16, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
