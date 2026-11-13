# Stock Prediction Report

Generated at: `2026-11-13T19:46:10.401661+00:00`
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
- current_price: `162.24`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.5%`
- secondary: `stock_failed_bounce` / `24.1%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `40.1` / `weak`
- stock_alpha_score_v1: `32.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `34.9%`
- 60d_expected_return: `-3.3%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `61.67`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `222.19`
- primary_invalidation_level: `148.80`
- risk_scenario_activation_level: `148.80`
- trend_repair_confirmation_level: `222.19`
- breakout_level: `222.19`
- breakdown_level: `148.80`
- nearest_support: `153.43`
- nearest_resistance: `175.44`
- bounce_target_zone: `{"conservative": 168.84, "base": 168.84, "extended": 230.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 157.28, "critical_warning": 148.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `391.13`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.3%`
- secondary: `stock_trend_repair` / `21.1%`
- risk: `stock_downside_continuation` / `16.7%`
- stock_confluence_score: `48.57` / `mixed`
- stock_alpha_score_v1: `17.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.7%`
- 60d_expected_return: `-0.2%`
- risk_reward_ratio: `0.68`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `56.15`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `376.60`
- nearest_resistance: `412.92`
- bounce_target_zone: `{"conservative": 402.03, "base": 402.03, "extended": 428.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 382.42, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `4.60`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.6%`
- secondary: `stock_failed_bounce` / `21.3%`
- risk: `stock_event_risk` / `12.2%`
- stock_confluence_score: `40.44` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `19.2%`
- 60d_expected_return: `-5.4%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `82.07`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `4.28`
- risk_scenario_activation_level: `4.05`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `4.05`
- nearest_support: `4.28`
- nearest_resistance: `5.20`
- bounce_target_zone: `{"conservative": 4.9, "base": 4.9, "extended": 6.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.38, "critical_warning": 4.28, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `278.00`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `18.4%`
- risk: `stock_event_risk` / `16.3%`
- stock_confluence_score: `43.44` / `weak`
- stock_alpha_score_v1: `33.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.5%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.09`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `231.30`
- nearest_support: `267.12`
- nearest_resistance: `284.97`
- bounce_target_zone: `{"conservative": 286.16, "base": 286.16, "extended": 295.85, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 271.88, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
