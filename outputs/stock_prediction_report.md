# Stock Prediction Report

Generated at: `2026-11-12T03:28:47.938021+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `NVDA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corporation`
- status: `available`
- current_price: `173.73`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.7%`
- secondary: `stock_failed_bounce` / `26.1%`
- risk: `stock_event_risk` / `13.9%`
- stock_confluence_score: `35.42` / `weak`
- stock_alpha_score_v1: `30.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.0%`
- 60d_expected_return: `-2.7%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `71.38`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `222.19`
- primary_invalidation_level: `165.89`
- risk_scenario_activation_level: `163.67`
- trend_repair_confirmation_level: `222.19`
- breakout_level: `222.19`
- breakdown_level: `163.67`
- nearest_support: `166.42`
- nearest_resistance: `184.70`
- bounce_target_zone: `{"conservative": 179.22, "base": 179.22, "extended": 229.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 169.62, "critical_warning": 165.89, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `390.84`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.7%`
- secondary: `stock_trend_repair` / `19.5%`
- risk: `stock_downside_continuation` / `17.0%`
- stock_confluence_score: `45.9` / `mixed`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.0%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.65`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `50.94`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `376.17`
- nearest_resistance: `412.85`
- bounce_target_zone: `{"conservative": 401.85, "base": 401.85, "extended": 428.9, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 382.04, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.23`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.6%`
- secondary: `stock_failed_bounce` / `20.6%`
- risk: `stock_event_risk` / `16.2%`
- stock_confluence_score: `38.8` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `26.3%`
- 60d_expected_return: `-4.0%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `67.18`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.20`
- primary_invalidation_level: `4.28`
- risk_scenario_activation_level: `4.28`
- trend_repair_confirmation_level: `6.20`
- breakout_level: `6.20`
- breakdown_level: `4.28`
- nearest_support: `4.85`
- nearest_resistance: `5.81`
- bounce_target_zone: `{"conservative": 5.52, "base": 5.52, "extended": 6.58, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.01, "critical_warning": 4.28, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `274.73`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `19.7%`
- risk: `stock_event_risk` / `16.4%`
- stock_confluence_score: `40.75` / `weak`
- stock_alpha_score_v1: `29.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.4%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.73`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `280.59`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `277.66`
- breakout_level: `280.59`
- breakdown_level: `231.30`
- nearest_support: `264.32`
- nearest_resistance: `277.66`
- bounce_target_zone: `{"conservative": 282.54, "base": 282.54, "extended": 288.07, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 268.87, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
