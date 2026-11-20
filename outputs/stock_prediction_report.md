# Stock Prediction Report

Generated at: `2026-11-20T03:58:26.250432+00:00`
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
- current_price: `145.98`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.7%`
- secondary: `stock_failed_bounce` / `22.3%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `43.01` / `weak`
- stock_alpha_score_v1: `23.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `29.2%`
- 60d_expected_return: `-4.3%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `74.39`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `219.99`
- primary_invalidation_level: `138.24`
- risk_scenario_activation_level: `132.89`
- trend_repair_confirmation_level: `219.99`
- breakout_level: `219.99`
- breakdown_level: `132.89`
- nearest_support: `145.71`
- nearest_resistance: `160.26`
- bounce_target_zone: `{"conservative": 153.12, "base": 153.12, "extended": 229.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 140.62, "critical_warning": 138.24, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `374.41`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `16.4%`
- risk: `stock_event_risk` / `14.3%`
- stock_confluence_score: `46.99` / `mixed`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.7%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `38.91`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `359.69`
- nearest_resistance: `396.49`
- bounce_target_zone: `{"conservative": 385.45, "base": 385.45, "extended": 428.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 366.13, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `3.81`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.1%`
- secondary: `stock_failed_bounce` / `23.8%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `41.15` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.3%`
- 60d_expected_return: `-7.3%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `95.51`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `3.49`
- risk_scenario_activation_level: `3.27`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `3.27`
- nearest_support: `3.71`
- nearest_resistance: `4.40`
- bounce_target_zone: `{"conservative": 4.11, "base": 4.11, "extended": 6.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 3.59, "critical_warning": 3.49, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `252.03`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.3%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `37.33` / `weak`
- stock_alpha_score_v1: `28.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.4%`
- 60d_expected_return: `-1.8%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.95`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `231.30`
- nearest_support: `240.64`
- nearest_resistance: `269.12`
- bounce_target_zone: `{"conservative": 260.58, "base": 260.58, "extended": 296.36, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 245.62, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
