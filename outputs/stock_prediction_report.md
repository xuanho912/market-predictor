# Stock Prediction Report

Generated at: `2026-11-13T02:18:05.276383+00:00`
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
- current_price: `166.19`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.7%`
- secondary: `stock_failed_bounce` / `22.7%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `38.05` / `weak`
- stock_alpha_score_v1: `28.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.0%`
- 60d_expected_return: `-2.9%`
- risk_reward_ratio: `0.38`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `59.32`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `222.19`
- primary_invalidation_level: `148.80`
- risk_scenario_activation_level: `148.80`
- trend_repair_confirmation_level: `222.19`
- breakout_level: `222.19`
- breakdown_level: `148.80`
- nearest_support: `157.66`
- nearest_resistance: `178.98`
- bounce_target_zone: `{"conservative": 172.59, "base": 172.59, "extended": 230.72, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 161.39, "critical_warning": 148.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `397.45`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.5%`
- secondary: `stock_trend_repair` / `21.1%`
- risk: `stock_downside_continuation` / `16.9%`
- stock_confluence_score: `50.53` / `mixed`
- stock_alpha_score_v1: `17.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.1%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.67`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `56.43`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `382.55`
- nearest_resistance: `414.23`
- bounce_target_zone: `{"conservative": 408.63, "base": 408.63, "extended": 429.13, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 388.5, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `4.82`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.3%`
- secondary: `stock_failed_bounce` / `18.0%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `35.1` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `19.7%`
- 60d_expected_return: `-5.0%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `79.26`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.20`
- primary_invalidation_level: `4.28`
- risk_scenario_activation_level: `4.28`
- trend_repair_confirmation_level: `6.20`
- breakout_level: `6.20`
- breakdown_level: `4.28`
- nearest_support: `4.43`
- nearest_resistance: `5.41`
- bounce_target_zone: `{"conservative": 5.12, "base": 5.12, "extended": 6.59, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.6, "critical_warning": 4.28, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `282.40`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `18.5%`
- risk: `stock_event_risk` / `16.2%`
- stock_confluence_score: `46.84` / `mixed`
- stock_alpha_score_v1: `45.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.9%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.22`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `288.42`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `282.70`
- breakout_level: `288.42`
- breakdown_level: `231.30`
- nearest_support: `271.70`
- nearest_resistance: `282.70`
- bounce_target_zone: `{"conservative": 290.43, "base": 290.43, "extended": 293.4, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 276.38, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
