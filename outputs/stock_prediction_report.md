# Stock Prediction Report

Generated at: `2026-11-19T03:55:06.592485+00:00`
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
- current_price: `150.96`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.4%`
- secondary: `stock_failed_bounce` / `22.7%`
- risk: `stock_event_risk` / `12.7%`
- stock_confluence_score: `43.6` / `weak`
- stock_alpha_score_v1: `28.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `30.9%`
- 60d_expected_return: `-4.2%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `70.86`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `219.99`
- primary_invalidation_level: `143.21`
- risk_scenario_activation_level: `137.84`
- trend_repair_confirmation_level: `219.99`
- breakout_level: `219.99`
- breakdown_level: `137.84`
- nearest_support: `148.80`
- nearest_resistance: `165.27`
- bounce_target_zone: `{"conservative": 158.11, "base": 158.11, "extended": 229.53, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 145.59, "critical_warning": 143.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `383.72`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.5%`
- secondary: `stock_downside_continuation` / `17.2%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `38.73` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.7%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `37.66`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `369.35`
- nearest_resistance: `405.28`
- bounce_target_zone: `{"conservative": 394.5, "base": 394.5, "extended": 428.6, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 375.64, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `3.91`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.4%`
- secondary: `stock_failed_bounce` / `25.1%`
- risk: `stock_event_risk` / `10.7%`
- stock_confluence_score: `45.88` / `mixed`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `16.7%`
- 60d_expected_return: `-7.4%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `94.37`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `3.59`
- risk_scenario_activation_level: `3.36`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `3.36`
- nearest_support: `3.90`
- nearest_resistance: `4.51`
- bounce_target_zone: `{"conservative": 4.21, "base": 4.21, "extended": 6.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 3.69, "critical_warning": 3.59, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `262.74`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `21.2%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `33.72` / `weak`
- stock_alpha_score_v1: `33.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.5%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.67`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `231.30`
- nearest_support: `252.02`
- nearest_resistance: `278.82`
- bounce_target_zone: `{"conservative": 270.78, "base": 270.78, "extended": 295.69, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 256.71, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
