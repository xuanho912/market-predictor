# Stock Prediction Report

Generated at: `2026-08-06T14:37:46.100452+00:00`
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
- current_price: `219.12`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `18.4%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `50.62` / `mixed`
- stock_alpha_score_v1: `58.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `68.5%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.58`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `223.63`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `223.63`
- breakout_level: `223.63`
- breakdown_level: `190.01`
- nearest_support: `212.99`
- nearest_resistance: `223.63`
- bounce_target_zone: `{"conservative": 223.71, "base": 223.71, "extended": 229.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 215.67, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `320.87`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `30.6%`
- secondary: `stock_failed_bounce` / `20.5%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `37.04` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `21.8%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `47.45`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `413.16`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `413.16`
- breakout_level: `413.16`
- breakdown_level: `297.38`
- nearest_support: `308.79`
- nearest_resistance: `338.98`
- bounce_target_zone: `{"conservative": 329.93, "base": 329.93, "extended": 425.24, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 314.08, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.49`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `23.7%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `36.76` / `weak`
- stock_alpha_score_v1: `6.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.7%`
- 60d_expected_return: `-2.7%`
- risk_reward_ratio: `0.38`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `38.02`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.86`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `9.86`
- breakout_level: `9.86`
- breakdown_level: `7.21`
- nearest_support: `8.95`
- nearest_resistance: `9.86`
- bounce_target_zone: `{"conservative": 9.9, "base": 9.9, "extended": 10.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.19, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `270.48`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_event_risk` / `18.9%`
- risk: `stock_downside_continuation` / `17.9%`
- stock_confluence_score: `41.81` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.3%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.14`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `280.00`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `280.00`
- breakout_level: `280.00`
- breakdown_level: `244.95`
- nearest_support: `261.96`
- nearest_resistance: `280.00`
- bounce_target_zone: `{"conservative": 276.88, "base": 276.88, "extended": 288.52, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 265.37, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
