# Stock Prediction Report

Generated at: `2026-08-12T21:12:12.885310+00:00`
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
- current_price: `224.09`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.5%`
- secondary: `stock_downside_continuation` / `19.0%`
- risk: `stock_event_risk` / `15.6%`
- stock_confluence_score: `48.65` / `mixed`
- stock_alpha_score_v1: `43.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.1%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.08`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `227.62`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `225.10`
- breakout_level: `227.62`
- breakdown_level: `190.01`
- nearest_support: `217.82`
- nearest_resistance: `225.10`
- bounce_target_zone: `{"conservative": 228.79, "base": 228.79, "extended": 231.37, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 220.56, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `327.51`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.1%`
- secondary: `stock_failed_bounce` / `21.9%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `36.43` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `23.8%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.25`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `40.03`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `395.31`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `395.31`
- breakout_level: `395.31`
- breakdown_level: `297.38`
- nearest_support: `318.73`
- nearest_resistance: `340.67`
- bounce_target_zone: `{"conservative": 334.09, "base": 334.09, "extended": 404.09, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 322.57, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.59`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.9%`
- secondary: `stock_downside_continuation` / `19.0%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `40.03` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.7%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.69`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.02`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.02`
- breakout_level: `10.02`
- breakdown_level: `7.21`
- nearest_support: `9.02`
- nearest_resistance: `10.02`
- bounce_target_zone: `{"conservative": 10.02, "base": 10.02, "extended": 10.59, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.27, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `278.68`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.1%`
- secondary: `stock_downside_continuation` / `19.9%`
- risk: `stock_event_risk` / `12.3%`
- stock_confluence_score: `46.0` / `mixed`
- stock_alpha_score_v1: `39.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.1%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.55`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `285.50`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `285.50`
- breakout_level: `285.50`
- breakdown_level: `244.95`
- nearest_support: `270.19`
- nearest_resistance: `285.50`
- bounce_target_zone: `{"conservative": 285.05, "base": 285.05, "extended": 293.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 273.9, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
