# Stock Prediction Report

Generated at: `2026-08-14T05:21:01.691579+00:00`
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
- current_price: `225.30`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `50.39` / `mixed`
- stock_alpha_score_v1: `46.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `60.5%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.74`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `228.71`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `227.23`
- breakout_level: `228.71`
- breakdown_level: `190.01`
- nearest_support: `219.24`
- nearest_resistance: `227.23`
- bounce_target_zone: `{"conservative": 229.85, "base": 229.85, "extended": 233.29, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 221.89, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `339.96`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.1%`
- secondary: `stock_failed_bounce` / `24.5%`
- risk: `stock_event_risk` / `12.7%`
- stock_confluence_score: `34.83` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `24.6%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.24`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `78.24`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.61`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `386.61`
- breakout_level: `386.61`
- breakdown_level: `297.38`
- nearest_support: `331.19`
- nearest_resistance: `353.12`
- bounce_target_zone: `{"conservative": 346.54, "base": 346.54, "extended": 395.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 335.03, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.85`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `26.0%`
- secondary: `stock_failed_bounce` / `20.5%`
- risk: `stock_downside_continuation` / `16.2%`
- stock_confluence_score: `47.78` / `mixed`
- stock_alpha_score_v1: `24.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `68.6%`
- 60d_expected_return: `0.8%`
- risk_reward_ratio: `0.74`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `41.79`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.17`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.70`
- breakout_level: `10.17`
- breakdown_level: `7.21`
- nearest_support: `9.28`
- nearest_resistance: `10.14`
- bounce_target_zone: `{"conservative": 10.28, "base": 10.7, "extended": 10.7, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.51, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `278.64`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.6%`
- secondary: `stock_downside_continuation` / `19.6%`
- risk: `stock_event_risk` / `12.0%`
- stock_confluence_score: `49.04` / `mixed`
- stock_alpha_score_v1: `45.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.6%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.6`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.83`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `285.50`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `285.50`
- breakout_level: `285.50`
- breakdown_level: `244.95`
- nearest_support: `270.19`
- nearest_resistance: `285.50`
- bounce_target_zone: `{"conservative": 284.97, "base": 284.97, "extended": 293.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 273.89, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
