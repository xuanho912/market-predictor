# Stock Prediction Report

Generated at: `2026-11-20T20:25:34.693874+00:00`
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
- current_price: `128.13`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.5%`
- secondary: `stock_failed_bounce` / `23.7%`
- risk: `stock_event_risk` / `12.5%`
- stock_confluence_score: `46.82` / `mixed`
- stock_alpha_score_v1: `25.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.0%`
- 60d_expected_return: `-6.0%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `89.92`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `219.99`
- primary_invalidation_level: `119.87`
- risk_scenario_activation_level: `114.15`
- trend_repair_confirmation_level: `219.99`
- breakout_level: `219.99`
- breakdown_level: `114.15`
- nearest_support: `126.31`
- nearest_resistance: `143.39`
- bounce_target_zone: `{"conservative": 135.76, "base": 135.76, "extended": 230.16, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 122.41, "critical_warning": 119.87, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `346.31`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.7%`
- secondary: `stock_downside_continuation` / `21.2%`
- risk: `stock_event_risk` / `13.8%`
- stock_confluence_score: `33.38` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.8%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.84`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `333.79`
- risk_scenario_activation_level: `325.13`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `325.13`
- nearest_support: `338.15`
- nearest_resistance: `369.42`
- bounce_target_zone: `{"conservative": 357.86, "base": 357.86, "extended": 429.64, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 337.64, "critical_warning": 333.79, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `3.32`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `37.3%`
- secondary: `stock_failed_bounce` / `24.8%`
- risk: `stock_event_risk` / `10.0%`
- stock_confluence_score: `42.79` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `12.5%`
- 60d_expected_return: `-9.6%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `100`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `3.00`
- risk_scenario_activation_level: `2.78`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `2.78`
- nearest_support: `3.30`
- nearest_resistance: `3.91`
- bounce_target_zone: `{"conservative": 3.61, "base": 3.61, "extended": 6.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 3.1, "critical_warning": 3.0, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `240.24`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.5%`
- secondary: `stock_downside_continuation` / `22.8%`
- risk: `stock_event_risk` / `11.7%`
- stock_confluence_score: `28.69` / `weak`
- stock_alpha_score_v1: `31.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.4%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.21`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `230.93`
- risk_scenario_activation_level: `224.49`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `224.49`
- nearest_support: `231.30`
- nearest_resistance: `257.42`
- bounce_target_zone: `{"conservative": 248.83, "base": 248.83, "extended": 296.42, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 233.8, "critical_warning": 230.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
