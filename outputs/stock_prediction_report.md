# Stock Prediction Report

Generated at: `2026-11-06T19:28:11.609151+00:00`
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
- current_price: `187.49`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.9%`
- secondary: `stock_failed_bounce` / `25.7%`
- risk: `stock_event_risk` / `11.9%`
- stock_confluence_score: `32.35` / `weak`
- stock_alpha_score_v1: `28.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.7%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `44.45`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `228.86`
- primary_invalidation_level: `181.46`
- risk_scenario_activation_level: `178.66`
- trend_repair_confirmation_level: `228.86`
- breakout_level: `228.86`
- breakdown_level: `178.66`
- nearest_support: `181.46`
- nearest_resistance: `197.11`
- bounce_target_zone: `{"conservative": 192.3, "base": 192.3, "extended": 235.28, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 183.88, "critical_warning": 181.46, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `360.11`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_downside_continuation` / `19.8%`
- risk: `stock_event_risk` / `13.9%`
- stock_confluence_score: `35.27` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.1%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.21`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `345.80`
- nearest_resistance: `381.57`
- bounce_target_zone: `{"conservative": 370.84, "base": 370.84, "extended": 428.54, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 352.06, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.06`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.4%`
- secondary: `stock_failed_bounce` / `20.8%`
- risk: `stock_event_risk` / `11.1%`
- stock_confluence_score: `41.66` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `15.7%`
- 60d_expected_return: `-4.5%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `78.97`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `7.07`
- primary_invalidation_level: `4.28`
- risk_scenario_activation_level: `4.28`
- trend_repair_confirmation_level: `7.07`
- breakout_level: `7.07`
- breakdown_level: `4.28`
- nearest_support: `4.70`
- nearest_resistance: `5.60`
- bounce_target_zone: `{"conservative": 5.33, "base": 5.33, "extended": 7.42, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.86, "critical_warning": 4.28, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `251.36`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.8%`
- secondary: `stock_failed_bounce` / `25.5%`
- risk: `stock_event_risk` / `15.6%`
- stock_confluence_score: `28.8` / `weak`
- stock_alpha_score_v1: `21.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.0%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `36.82`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `301.77`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `301.77`
- breakout_level: `301.77`
- breakdown_level: `231.30`
- nearest_support: `241.75`
- nearest_resistance: `265.78`
- bounce_target_zone: `{"conservative": 258.57, "base": 258.57, "extended": 311.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 245.95, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
