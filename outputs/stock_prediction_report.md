# Stock Prediction Report

Generated at: `2026-08-07T23:23:18.394879+00:00`
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
- current_price: `223.96`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `15.4%`
- stock_confluence_score: `52.79` / `mixed`
- stock_alpha_score_v1: `60.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `67.4%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.75`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `227.48`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `224.76`
- breakout_level: `227.48`
- breakdown_level: `190.01`
- nearest_support: `217.70`
- nearest_resistance: `224.76`
- bounce_target_zone: `{"conservative": 228.66, "base": 228.66, "extended": 231.02, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 220.44, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `328.58`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `29.9%`
- secondary: `stock_failed_bounce` / `21.3%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `43.26` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.7%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `42.5`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `406.59`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `406.59`
- breakout_level: `406.59`
- breakdown_level: `297.38`
- nearest_support: `316.63`
- nearest_resistance: `346.51`
- bounce_target_zone: `{"conservative": 337.55, "base": 337.55, "extended": 418.54, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 321.86, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.82`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `44.12` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.2%`
- 60d_expected_return: `-2.4%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.76`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.13`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.02`
- breakout_level: `10.13`
- breakdown_level: `7.21`
- nearest_support: `9.27`
- nearest_resistance: `10.02`
- bounce_target_zone: `{"conservative": 10.23, "base": 10.23, "extended": 10.58, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.51, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `269.89`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `20.2%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `43.65` / `weak`
- stock_alpha_score_v1: `35.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.1%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.79`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `280.00`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `280.00`
- breakout_level: `280.00`
- breakdown_level: `244.95`
- nearest_support: `261.00`
- nearest_resistance: `280.00`
- bounce_target_zone: `{"conservative": 276.56, "base": 276.56, "extended": 288.89, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 264.89, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
