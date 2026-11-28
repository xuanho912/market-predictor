# Stock Prediction Report

Generated at: `2026-11-28T04:22:36.465218+00:00`
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
- current_price: `150.49`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.8%`
- secondary: `stock_failed_bounce` / `18.2%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `38.28` / `weak`
- stock_alpha_score_v1: `25.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `31.7%`
- 60d_expected_return: `-4.8%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `66.34`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `209.98`
- primary_invalidation_level: `124.50`
- risk_scenario_activation_level: `124.50`
- trend_repair_confirmation_level: `209.98`
- breakout_level: `209.98`
- breakdown_level: `124.50`
- nearest_support: `138.21`
- nearest_resistance: `168.91`
- bounce_target_zone: `{"conservative": 159.7, "base": 159.7, "extended": 222.26, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 143.58, "critical_warning": 124.5, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `400.00`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.0%`
- secondary: `stock_downside_continuation` / `17.7%`
- risk: `stock_event_risk` / `15.4%`
- stock_confluence_score: `41.61` / `weak`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.1%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `41.93`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `383.91`
- nearest_resistance: `414.23`
- bounce_target_zone: `{"conservative": 412.07, "base": 412.07, "extended": 430.32, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 390.95, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `3.48`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `40.0%`
- secondary: `stock_failed_bounce` / `18.7%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `39.72` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `7.9%`
- 60d_expected_return: `-6.9%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `99.24`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `5.83`
- primary_invalidation_level: `2.97`
- risk_scenario_activation_level: `2.97`
- trend_repair_confirmation_level: `5.83`
- breakout_level: `5.83`
- breakdown_level: `2.97`
- nearest_support: `3.15`
- nearest_resistance: `3.97`
- bounce_target_zone: `{"conservative": 3.73, "base": 3.73, "extended": 6.16, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 3.3, "critical_warning": 2.97, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `238.10`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.4%`
- secondary: `stock_failed_bounce` / `26.0%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `29.61` / `weak`
- stock_alpha_score_v1: `22.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.3%`
- 60d_expected_return: `-2.5%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Breakdown Warning` / `NO_ALERT` / `33.92`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `229.17`
- risk_scenario_activation_level: `222.99`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `222.99`
- nearest_support: `230.53`
- nearest_resistance: `254.58`
- bounce_target_zone: `{"conservative": 246.34, "base": 246.34, "extended": 295.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 231.92, "critical_warning": 229.17, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
