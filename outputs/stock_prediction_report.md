# Stock Prediction Report

Generated at: `2026-09-26T16:27:31.373556+00:00`
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
- current_price: `225.07`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `19.7%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `42.99` / `weak`
- stock_alpha_score_v1: `37.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.4%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.09`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `220.89`
- nearest_resistance: `231.34`
- bounce_target_zone: `{"conservative": 228.2, "base": 228.2, "extended": 238.94, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 222.72, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `372.11`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `20.7%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `44.1` / `weak`
- stock_alpha_score_v1: `13.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.5%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.49`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.20`
- risk_scenario_activation_level: `345.20`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.20`
- nearest_support: `363.14`
- nearest_resistance: `385.56`
- bounce_target_zone: `{"conservative": 378.84, "base": 378.84, "extended": 395.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 367.07, "critical_warning": 345.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.42`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `27.6%`
- secondary: `stock_failed_bounce` / `21.6%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `27.66` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `31.9%`
- 60d_expected_return: `-3.0%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `38.1`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.94`
- risk_scenario_activation_level: `7.61`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.61`
- nearest_support: `8.05`
- nearest_resistance: `9.30`
- bounce_target_zone: `{"conservative": 8.86, "base": 8.86, "extended": 11.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.09, "critical_warning": 7.94, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `263.27`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `24.3%`
- secondary: `stock_failed_bounce` / `23.6%`
- risk: `stock_event_risk` / `11.2%`
- stock_confluence_score: `36.71` / `weak`
- stock_alpha_score_v1: `26.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.0%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.34`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `250.55`
- risk_scenario_activation_level: `250.55`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `250.55`
- nearest_support: `256.09`
- nearest_resistance: `274.04`
- bounce_target_zone: `{"conservative": 268.66, "base": 268.66, "extended": 312.98, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 259.23, "critical_warning": 250.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
