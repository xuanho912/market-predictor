# Stock Prediction Report

Generated at: `2026-08-11T23:55:43.247746+00:00`
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
- current_price: `217.50`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `19.0%`
- risk: `stock_event_risk` / `15.6%`
- stock_confluence_score: `46.04` / `mixed`
- stock_alpha_score_v1: `43.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.7%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.81`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `224.76`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `224.76`
- breakout_level: `224.76`
- breakdown_level: `190.01`
- nearest_support: `211.32`
- nearest_resistance: `224.76`
- bounce_target_zone: `{"conservative": 222.13, "base": 222.13, "extended": 230.94, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.03, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `332.81`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.4%`
- secondary: `stock_failed_bounce` / `22.0%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `37.35` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `25.3%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `NO_ALERT` / `37.77`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `406.59`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `406.59`
- breakout_level: `406.59`
- breakdown_level: `297.38`
- nearest_support: `321.38`
- nearest_resistance: `349.95`
- bounce_target_zone: `{"conservative": 341.38, "base": 341.38, "extended": 418.02, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 326.38, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.89`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.3%`
- secondary: `stock_downside_continuation` / `19.2%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `43.03` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.0%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.41`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.21`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.02`
- breakout_level: `10.21`
- breakdown_level: `7.21`
- nearest_support: `9.32`
- nearest_resistance: `10.02`
- bounce_target_zone: `{"conservative": 10.32, "base": 10.32, "extended": 10.59, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.57, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `278.36`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.1%`
- secondary: `stock_downside_continuation` / `19.9%`
- risk: `stock_event_risk` / `12.3%`
- stock_confluence_score: `48.19` / `mixed`
- stock_alpha_score_v1: `39.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.5%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.54`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `283.11`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `280.36`
- breakout_level: `283.11`
- breakdown_level: `244.95`
- nearest_support: `269.92`
- nearest_resistance: `280.36`
- bounce_target_zone: `{"conservative": 284.69, "base": 284.69, "extended": 288.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 273.61, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
