# Stock Prediction Report

Generated at: `2026-08-10T13:48:28.491509+00:00`
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
- current_price: `223.28`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `18.4%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `50.46` / `mixed`
- stock_alpha_score_v1: `58.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `68.0%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `40.38`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `226.69`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `224.76`
- breakout_level: `226.69`
- breakdown_level: `190.01`
- nearest_support: `217.22`
- nearest_resistance: `224.76`
- bounce_target_zone: `{"conservative": 227.82, "base": 227.82, "extended": 230.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 219.87, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `329.25`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.8%`
- secondary: `stock_failed_bounce` / `21.7%`
- risk: `stock_event_risk` / `13.4%`
- stock_confluence_score: `36.15` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `23.5%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `40.6`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `406.59`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `406.59`
- breakout_level: `406.59`
- breakdown_level: `297.38`
- nearest_support: `317.92`
- nearest_resistance: `346.25`
- bounce_target_zone: `{"conservative": 337.75, "base": 337.75, "extended": 417.92, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 322.87, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.36`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.0%`
- secondary: `stock_downside_continuation` / `22.8%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `35.45` / `weak`
- stock_alpha_score_v1: `6.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.3%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.11`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.02`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.02`
- breakout_level: `10.02`
- breakdown_level: `7.21`
- nearest_support: `8.81`
- nearest_resistance: `10.02`
- bounce_target_zone: `{"conservative": 9.76, "base": 9.76, "extended": 10.57, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.05, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `270.27`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `20.3%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `37.29` / `weak`
- stock_alpha_score_v1: `39.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.0%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.78`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `280.00`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `280.00`
- breakout_level: `280.00`
- breakdown_level: `244.95`
- nearest_support: `261.70`
- nearest_resistance: `280.00`
- bounce_target_zone: `{"conservative": 276.7, "base": 276.7, "extended": 288.57, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 265.45, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
