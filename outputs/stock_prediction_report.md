# Stock Prediction Report

Generated at: `2026-08-11T13:48:34.641257+00:00`
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
- current_price: `220.44`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.7%`
- secondary: `stock_downside_continuation` / `19.2%`
- risk: `stock_event_risk` / `15.7%`
- stock_confluence_score: `46.24` / `mixed`
- stock_alpha_score_v1: `54.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `63.1%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `40.46`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `224.76`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `224.76`
- breakout_level: `224.76`
- breakdown_level: `190.01`
- nearest_support: `214.34`
- nearest_resistance: `224.76`
- bounce_target_zone: `{"conservative": 225.02, "base": 225.02, "extended": 230.86, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 217.01, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `331.95`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.5%`
- secondary: `stock_failed_bounce` / `21.9%`
- risk: `stock_event_risk` / `13.5%`
- stock_confluence_score: `36.81` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `25.1%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `38.26`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `406.59`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `406.59`
- breakout_level: `406.59`
- breakdown_level: `297.38`
- nearest_support: `320.66`
- nearest_resistance: `348.89`
- bounce_target_zone: `{"conservative": 340.42, "base": 340.42, "extended": 417.88, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 325.6, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.28`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `22.7%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `33.01` / `weak`
- stock_alpha_score_v1: `6.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.1%`
- 60d_expected_return: `-2.5%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.61`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.02`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.02`
- breakout_level: `10.02`
- breakdown_level: `7.21`
- nearest_support: `8.73`
- nearest_resistance: `10.02`
- bounce_target_zone: `{"conservative": 9.69, "base": 9.69, "extended": 10.57, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.97, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `275.41`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `20.2%`
- risk: `stock_event_risk` / `12.4%`
- stock_confluence_score: `40.63` / `weak`
- stock_alpha_score_v1: `39.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.3%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.57`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `280.08`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `280.00`
- breakout_level: `280.08`
- breakdown_level: `244.95`
- nearest_support: `267.11`
- nearest_resistance: `280.00`
- bounce_target_zone: `{"conservative": 281.64, "base": 281.64, "extended": 288.3, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 270.74, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
