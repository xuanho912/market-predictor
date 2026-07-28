# Stock Prediction Report

Generated at: `2026-07-28T00:11:38.182838+00:00`
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
- current_price: `196.51`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `19.9%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `45.2` / `mixed`
- stock_alpha_score_v1: `50.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `62.4%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.15`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `187.68`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `187.68`
- nearest_support: `190.09`
- nearest_resistance: `206.15`
- bounce_target_zone: `{"conservative": 201.33, "base": 201.33, "extended": 220.81, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 192.9, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `309.22`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `29.8%`
- secondary: `stock_failed_bounce` / `26.9%`
- risk: `stock_event_risk` / `11.4%`
- stock_confluence_score: `31.46` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `25.9%`
- 60d_expected_return: `-2.6%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `72.54`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `298.55`
- risk_scenario_activation_level: `291.17`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `291.17`
- nearest_support: `304.28`
- nearest_resistance: `328.91`
- bounce_target_zone: `{"conservative": 319.07, "base": 319.07, "extended": 445.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 301.84, "critical_warning": 298.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.54`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `30.3%`
- secondary: `stock_failed_bounce` / `20.2%`
- risk: `stock_event_risk` / `12.5%`
- stock_confluence_score: `39.93` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.5%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `47.27`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `8.05`
- nearest_resistance: `9.28`
- bounce_target_zone: `{"conservative": 8.91, "base": 8.91, "extended": 11.36, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.26, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `270.00`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_downside_continuation` / `23.0%`
- risk: `stock_event_risk` / `11.0%`
- stock_confluence_score: `43.72` / `weak`
- stock_alpha_score_v1: `35.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.9%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.32`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `228.63`
- nearest_support: `263.33`
- nearest_resistance: `279.60`
- bounce_target_zone: `{"conservative": 275.0, "base": 275.0, "extended": 286.27, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 266.25, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
