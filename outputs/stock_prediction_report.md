# Stock Prediction Report

Generated at: `2026-11-16T22:06:20.505811+00:00`
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

- company_name: `NVIDIA Corporation`
- status: `available`
- current_price: `156.14`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.1%`
- secondary: `stock_failed_bounce` / `23.3%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `38.4` / `weak`
- stock_alpha_score_v1: `32.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `34.6%`
- 60d_expected_return: `-3.7%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `66.8`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `222.19`
- primary_invalidation_level: `148.79`
- risk_scenario_activation_level: `143.70`
- trend_repair_confirmation_level: `222.19`
- breakout_level: `222.19`
- breakdown_level: `143.70`
- nearest_support: `148.80`
- nearest_resistance: `169.72`
- bounce_target_zone: `{"conservative": 162.93, "base": 162.93, "extended": 231.24, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 151.05, "critical_warning": 148.79, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `379.74`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.9%`
- secondary: `stock_downside_continuation` / `17.2%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `42.58` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.4%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.62`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `38.4`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `365.34`
- nearest_resistance: `401.34`
- bounce_target_zone: `{"conservative": 390.54, "base": 390.54, "extended": 428.63, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 371.64, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `4.27`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.3%`
- secondary: `stock_failed_bounce` / `24.6%`
- risk: `stock_event_risk` / `11.2%`
- stock_confluence_score: `40.71` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `17.5%`
- 60d_expected_return: `-6.3%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `88.68`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `3.95`
- risk_scenario_activation_level: `3.73`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `3.73`
- nearest_support: `4.26`
- nearest_resistance: `4.86`
- bounce_target_zone: `{"conservative": 4.57, "base": 4.57, "extended": 6.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.05, "critical_warning": 3.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `277.82`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `24.2%`
- secondary: `stock_downside_continuation` / `19.2%`
- risk: `stock_event_risk` / `12.7%`
- stock_confluence_score: `47.81` / `mixed`
- stock_alpha_score_v1: `44.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `63.0%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.91`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `231.30`
- nearest_support: `267.28`
- nearest_resistance: `284.97`
- bounce_target_zone: `{"conservative": 285.72, "base": 285.72, "extended": 295.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 271.89, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
