# Stock Prediction Report

Generated at: `2026-10-01T18:27:34.817952+00:00`
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

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `231.06`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `19.3%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `45.45` / `mixed`
- stock_alpha_score_v1: `40.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.8%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.01`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `226.83`
- nearest_resistance: `234.76`
- bounce_target_zone: `{"conservative": 234.23, "base": 234.23, "extended": 238.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 228.68, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `357.40`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `29.2%`
- secondary: `stock_downside_continuation` / `20.3%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `41.04` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.6%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.4`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `32.75`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.56`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.56`
- nearest_support: `348.79`
- nearest_resistance: `370.32`
- bounce_target_zone: `{"conservative": 363.86, "base": 363.86, "extended": 395.44, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 352.56, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.90`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `29.6%`
- secondary: `stock_failed_bounce` / `23.7%`
- risk: `stock_event_risk` / `10.7%`
- stock_confluence_score: `25.1` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `28.1%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `42.77`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.56`
- risk_scenario_activation_level: `7.32`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.32`
- nearest_support: `7.75`
- nearest_resistance: `8.54`
- bounce_target_zone: `{"conservative": 8.22, "base": 8.22, "extended": 11.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.66, "critical_warning": 7.56, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `258.83`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `26.5%`
- secondary: `stock_failed_bounce` / `25.2%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `34.37` / `weak`
- stock_alpha_score_v1: `19.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.1%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.99`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `247.20`
- nearest_support: `250.61`
- nearest_resistance: `271.17`
- bounce_target_zone: `{"conservative": 265.0, "base": 265.0, "extended": 314.02, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 254.21, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
