# Stock Prediction Report

Generated at: `2026-11-22T19:44:10.894373+00:00`
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
- current_price: `125.53`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.8%`
- secondary: `stock_failed_bounce` / `24.0%`
- risk: `stock_event_risk` / `12.4%`
- stock_confluence_score: `47.96` / `mixed`
- stock_alpha_score_v1: `28.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.9%`
- 60d_expected_return: `-6.3%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `92.32`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `219.99`
- primary_invalidation_level: `117.18`
- risk_scenario_activation_level: `111.40`
- trend_repair_confirmation_level: `219.99`
- breakout_level: `219.99`
- breakdown_level: `111.40`
- nearest_support: `124.50`
- nearest_resistance: `140.94`
- bounce_target_zone: `{"conservative": 133.23, "base": 133.23, "extended": 230.26, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 119.75, "critical_warning": 117.18, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `345.82`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.7%`
- secondary: `stock_downside_continuation` / `21.2%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `33.35` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.2%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.12`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `333.24`
- risk_scenario_activation_level: `324.52`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `324.52`
- nearest_support: `338.15`
- nearest_resistance: `369.05`
- bounce_target_zone: `{"conservative": 357.44, "base": 357.44, "extended": 429.72, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 337.11, "critical_warning": 333.24, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `3.36`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `37.2%`
- secondary: `stock_failed_bounce` / `24.7%`
- risk: `stock_event_risk` / `10.1%`
- stock_confluence_score: `43.69` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `13.5%`
- 60d_expected_return: `-9.2%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `100`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `3.04`
- risk_scenario_activation_level: `2.82`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `2.82`
- nearest_support: `3.30`
- nearest_resistance: `3.95`
- bounce_target_zone: `{"conservative": 3.66, "base": 3.66, "extended": 6.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 3.14, "critical_warning": 3.04, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `237.41`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.5%`
- secondary: `stock_downside_continuation` / `23.3%`
- risk: `stock_event_risk` / `11.6%`
- stock_confluence_score: `30.35` / `weak`
- stock_alpha_score_v1: `33.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.5%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Breakdown Warning` / `NO_ALERT` / `33.47`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `227.99`
- risk_scenario_activation_level: `221.47`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `221.47`
- nearest_support: `231.30`
- nearest_resistance: `254.80`
- bounce_target_zone: `{"conservative": 246.1, "base": 246.1, "extended": 296.56, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 230.89, "critical_warning": 227.99, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
