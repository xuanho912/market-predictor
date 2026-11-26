# Stock Prediction Report

Generated at: `2026-11-26T03:46:39.052128+00:00`
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
- current_price: `149.30`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.1%`
- secondary: `stock_failed_bounce` / `18.5%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `47.59` / `mixed`
- stock_alpha_score_v1: `23.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `33.0%`
- 60d_expected_return: `-5.1%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `68.52`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `215.33`
- primary_invalidation_level: `124.50`
- risk_scenario_activation_level: `124.50`
- trend_repair_confirmation_level: `215.33`
- breakout_level: `215.33`
- breakdown_level: `124.50`
- nearest_support: `136.63`
- nearest_resistance: `168.30`
- bounce_target_zone: `{"conservative": 158.8, "base": 158.8, "extended": 228.0, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 142.18, "critical_warning": 124.5, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `380.14`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.1%`
- secondary: `stock_downside_continuation` / `20.2%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `35.33` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.9%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `33.7`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `364.10`
- nearest_resistance: `404.20`
- bounce_target_zone: `{"conservative": 392.17, "base": 392.17, "extended": 430.27, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 371.12, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `3.25`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `39.9%`
- secondary: `stock_failed_bounce` / `21.0%`
- risk: `stock_event_risk` / `10.4%`
- stock_confluence_score: `41.86` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `7.4%`
- 60d_expected_return: `-8.6%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `100`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `2.96`
- risk_scenario_activation_level: `2.77`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `2.77`
- nearest_support: `2.97`
- nearest_resistance: `3.78`
- bounce_target_zone: `{"conservative": 3.51, "base": 3.51, "extended": 6.46, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 3.05, "critical_warning": 2.96, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `235.28`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_downside_continuation` / `25.5%`
- risk: `stock_event_risk` / `13.5%`
- stock_confluence_score: `30.18` / `weak`
- stock_alpha_score_v1: `24.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.5%`
- 60d_expected_return: `-2.6%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Breakdown Warning` / `NO_ALERT` / `35.6`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `226.19`
- risk_scenario_activation_level: `219.89`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `219.89`
- nearest_support: `230.53`
- nearest_resistance: `252.07`
- bounce_target_zone: `{"conservative": 243.67, "base": 243.67, "extended": 296.16, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 228.99, "critical_warning": 226.19, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
