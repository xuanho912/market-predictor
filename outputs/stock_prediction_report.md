# Stock Prediction Report

Generated at: `2026-07-23T14:42:27.938781+00:00`
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
- current_price: `208.43`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `15.5%`
- stock_confluence_score: `44.45` / `weak`
- stock_alpha_score_v1: `44.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.5%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.08`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `189.80`
- nearest_support: `202.63`
- nearest_resistance: `214.39`
- bounce_target_zone: `{"conservative": 212.78, "base": 212.78, "extended": 220.19, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 205.17, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `324.42`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `28.0%`
- secondary: `stock_downside_continuation` / `27.8%`
- risk: `stock_event_risk` / `11.8%`
- stock_confluence_score: `35.72` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `29.0%`
- 60d_expected_return: `-2.5%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `59.47`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `313.23`
- risk_scenario_activation_level: `305.49`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `305.49`
- nearest_support: `322.71`
- nearest_resistance: `345.08`
- bounce_target_zone: `{"conservative": 334.75, "base": 334.75, "extended": 446.63, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 316.67, "critical_warning": 313.23, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.72`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.1%`
- secondary: `stock_failed_bounce` / `20.5%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `37.42` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.5%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `46.12`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `8.23`
- nearest_resistance: `9.46`
- bounce_target_zone: `{"conservative": 9.09, "base": 9.09, "extended": 11.36, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.44, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `274.04`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.4%`
- secondary: `stock_downside_continuation` / `23.2%`
- risk: `stock_event_risk` / `11.0%`
- stock_confluence_score: `41.14` / `weak`
- stock_alpha_score_v1: `31.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.7%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.84`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `277.68`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `275.81`
- breakout_level: `277.68`
- breakdown_level: `228.63`
- nearest_support: `267.57`
- nearest_resistance: `275.81`
- bounce_target_zone: `{"conservative": 278.89, "base": 278.89, "extended": 282.28, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 270.4, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
