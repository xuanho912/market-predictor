# Stock Prediction Report

Generated at: `2026-09-22T17:00:33.218254+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `CEG`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `229.43`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `14.1%`
- stock_confluence_score: `51.8` / `mixed`
- stock_alpha_score_v1: `50.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.8%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.59`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.12`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `224.72`
- nearest_resistance: `234.76`
- bounce_target_zone: `{"conservative": 232.96, "base": 232.96, "extended": 239.47, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 226.78, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `378.68`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `15.6%`
- stock_confluence_score: `44.42` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.4%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.19`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.55`
- primary_invalidation_level: `342.53`
- risk_scenario_activation_level: `342.53`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.55`
- breakdown_level: `342.53`
- nearest_support: `368.25`
- nearest_resistance: `384.04`
- bounce_target_zone: `{"conservative": 386.51, "base": 386.51, "extended": 394.48, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 372.82, "critical_warning": 342.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.90`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `22.0%`
- secondary: `stock_bounce` / `19.3%`
- risk: `stock_downside_continuation` / `19.1%`
- stock_confluence_score: `32.22` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.2%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.6`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.38`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.05`
- risk_scenario_activation_level: `8.05`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `8.05`
- nearest_support: `8.30`
- nearest_resistance: `9.80`
- bounce_target_zone: `{"conservative": 9.35, "base": 9.35, "extended": 11.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.54, "critical_warning": 8.05, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `265.94`
- market_context: `market_tailwind`
- primary: `stock_bounce` / `27.8%`
- secondary: `stock_downside_continuation` / `19.0%`
- risk: `stock_failed_bounce` / `14.1%`
- stock_confluence_score: `50.7` / `mixed`
- stock_alpha_score_v1: `41.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.1%`
- 60d_expected_return: `0.6%`
- risk_reward_ratio: `0.85`
- strongest_alert: `Stock Bounce Setup` / `NO_ALERT` / `25.83`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `250.55`
- risk_scenario_activation_level: `250.55`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `250.55`
- nearest_support: `257.30`
- nearest_resistance: `278.90`
- bounce_target_zone: `{"conservative": 273.28, "base": 279.44, "extended": 314.44, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 261.08, "critical_warning": 250.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
