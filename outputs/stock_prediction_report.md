# Stock Prediction Report

Generated at: `2026-11-18T08:37:27.879651+00:00`
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
- current_price: `155.46`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.9%`
- secondary: `stock_failed_bounce` / `21.5%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `44.13` / `weak`
- stock_alpha_score_v1: `30.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `34.2%`
- 60d_expected_return: `-3.6%`
- risk_reward_ratio: `0.38`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `67.61`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `222.19`
- primary_invalidation_level: `147.99`
- risk_scenario_activation_level: `142.81`
- trend_repair_confirmation_level: `222.19`
- breakout_level: `222.19`
- breakdown_level: `142.81`
- nearest_support: `148.80`
- nearest_resistance: `169.25`
- bounce_target_zone: `{"conservative": 162.36, "base": 162.36, "extended": 231.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 150.29, "critical_warning": 147.99, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `380.11`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.6%`
- secondary: `stock_downside_continuation` / `17.0%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `42.44` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.5%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `41.44`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `365.99`
- nearest_resistance: `401.29`
- bounce_target_zone: `{"conservative": 390.7, "base": 390.7, "extended": 428.35, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 372.17, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `4.09`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.0%`
- secondary: `stock_failed_bounce` / `24.3%`
- risk: `stock_event_risk` / `11.0%`
- stock_confluence_score: `45.01` / `mixed`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.6%`
- 60d_expected_return: `-6.9%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `91.57`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `3.77`
- risk_scenario_activation_level: `3.54`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `3.54`
- nearest_support: `4.03`
- nearest_resistance: `4.69`
- bounce_target_zone: `{"conservative": 4.39, "base": 4.39, "extended": 6.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 3.87, "critical_warning": 3.77, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `268.07`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.0%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `41.95` / `weak`
- stock_alpha_score_v1: `41.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.3%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.6`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.78`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `231.30`
- nearest_support: `257.22`
- nearest_resistance: `284.34`
- bounce_target_zone: `{"conservative": 276.2, "base": 276.2, "extended": 295.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 261.97, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
