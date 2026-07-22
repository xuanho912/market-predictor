# Stock Prediction Report

Generated at: `2026-07-22T23:50:33.255850+00:00`
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
- current_price: `212.06`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `15.4%`
- stock_confluence_score: `48.35` / `mixed`
- stock_alpha_score_v1: `49.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `63.5%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.85`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `215.42`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `215.42`
- breakdown_level: `189.80`
- nearest_support: `206.09`
- nearest_resistance: `214.39`
- bounce_target_zone: `{"conservative": 216.54, "base": 216.54, "extended": 220.36, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 208.7, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `374.01`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `20.0%`
- risk: `stock_event_risk` / `17.2%`
- stock_confluence_score: `33.31` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.3%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.0`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `363.20`
- risk_scenario_activation_level: `355.72`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `355.72`
- nearest_support: `368.60`
- nearest_resistance: `393.96`
- bounce_target_zone: `{"conservative": 383.98, "base": 383.98, "extended": 446.16, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 366.53, "critical_warning": 363.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.68`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `32.1%`
- secondary: `stock_failed_bounce` / `19.7%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `40.17` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.4%`
- 60d_expected_return: `-3.3%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `49.37`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `8.14`
- nearest_resistance: `9.50`
- bounce_target_zone: `{"conservative": 9.09, "base": 9.09, "extended": 11.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.37, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `274.90`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.3%`
- secondary: `stock_downside_continuation` / `23.2%`
- risk: `stock_event_risk` / `11.1%`
- stock_confluence_score: `43.42` / `weak`
- stock_alpha_score_v1: `29.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.7%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.46`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `278.66`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `275.81`
- breakout_level: `278.66`
- breakdown_level: `228.63`
- nearest_support: `268.21`
- nearest_resistance: `275.81`
- bounce_target_zone: `{"conservative": 279.91, "base": 279.91, "extended": 282.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 271.14, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
