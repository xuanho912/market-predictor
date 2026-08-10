# Stock Prediction Report

Generated at: `2026-08-10T23:48:56.954060+00:00`
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
- current_price: `217.55`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `18.6%`
- risk: `stock_event_risk` / `15.4%`
- stock_confluence_score: `49.3` / `mixed`
- stock_alpha_score_v1: `52.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `63.5%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.83`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `224.76`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `224.76`
- breakout_level: `224.76`
- breakdown_level: `190.01`
- nearest_support: `211.17`
- nearest_resistance: `224.76`
- bounce_target_zone: `{"conservative": 222.33, "base": 222.33, "extended": 231.14, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 213.96, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `330.88`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.6%`
- secondary: `stock_failed_bounce` / `21.8%`
- risk: `stock_event_risk` / `13.5%`
- stock_confluence_score: `37.59` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `24.0%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `39.71`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `406.59`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `406.59`
- breakout_level: `406.59`
- breakdown_level: `297.38`
- nearest_support: `319.42`
- nearest_resistance: `348.07`
- bounce_target_zone: `{"conservative": 339.48, "base": 339.48, "extended": 418.05, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 324.43, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.18`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.8%`
- secondary: `stock_downside_continuation` / `23.2%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `36.79` / `weak`
- stock_alpha_score_v1: `6.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.8%`
- 60d_expected_return: `-2.3%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.97`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.02`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.02`
- breakout_level: `10.02`
- breakdown_level: `7.21`
- nearest_support: `8.63`
- nearest_resistance: `10.00`
- bounce_target_zone: `{"conservative": 9.59, "base": 9.59, "extended": 10.57, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.87, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `270.43`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `20.3%`
- risk: `stock_event_risk` / `12.7%`
- stock_confluence_score: `42.19` / `weak`
- stock_alpha_score_v1: `39.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.0%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.39`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `280.00`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `280.00`
- breakout_level: `280.00`
- breakdown_level: `244.95`
- nearest_support: `261.78`
- nearest_resistance: `280.00`
- bounce_target_zone: `{"conservative": 276.92, "base": 276.92, "extended": 288.65, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 265.56, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
