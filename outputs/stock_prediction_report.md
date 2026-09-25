# Stock Prediction Report

Generated at: `2026-09-25T17:15:47.163515+00:00`
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
- current_price: `225.27`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `19.6%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `42.47` / `weak`
- stock_alpha_score_v1: `39.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `50.2%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.13`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `221.09`
- nearest_resistance: `231.54`
- bounce_target_zone: `{"conservative": 228.4, "base": 228.4, "extended": 238.94, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 222.92, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `372.12`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `28.0%`
- secondary: `stock_downside_continuation` / `21.8%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `42.83` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.0%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.45`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.20`
- risk_scenario_activation_level: `345.20`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.20`
- nearest_support: `363.16`
- nearest_resistance: `385.58`
- bounce_target_zone: `{"conservative": 378.85, "base": 378.85, "extended": 395.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 367.08, "critical_warning": 345.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.51`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.1%`
- secondary: `stock_failed_bounce` / `21.9%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `27.6` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `32.5%`
- 60d_expected_return: `-2.9%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `34.9`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.03`
- risk_scenario_activation_level: `7.70`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.70`
- nearest_support: `8.05`
- nearest_resistance: `9.39`
- bounce_target_zone: `{"conservative": 8.95, "base": 8.95, "extended": 11.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.17, "critical_warning": 8.03, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `261.11`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `24.8%`
- secondary: `stock_failed_bounce` / `23.3%`
- risk: `stock_event_risk` / `11.1%`
- stock_confluence_score: `35.38` / `weak`
- stock_alpha_score_v1: `26.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.4%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.23`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `250.55`
- risk_scenario_activation_level: `250.55`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `250.55`
- nearest_support: `253.94`
- nearest_resistance: `271.88`
- bounce_target_zone: `{"conservative": 266.5, "base": 266.5, "extended": 312.98, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 257.08, "critical_warning": 250.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
