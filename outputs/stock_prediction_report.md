# Stock Prediction Report

Generated at: `2026-10-30T02:34:37.445139+00:00`
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
- current_price: `213.66`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `25.6%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `40.96` / `weak`
- stock_alpha_score_v1: `36.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.5%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.63`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `209.80`
- risk_scenario_activation_level: `207.12`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `207.12`
- nearest_support: `210.18`
- nearest_resistance: `220.79`
- bounce_target_zone: `{"conservative": 217.23, "base": 217.23, "extended": 248.12, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 210.99, "critical_warning": 209.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `403.30`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `23.7%`
- secondary: `stock_failed_bounce` / `23.2%`
- risk: `stock_downside_continuation` / `16.7%`
- stock_confluence_score: `49.25` / `mixed`
- stock_alpha_score_v1: `17.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.0%`
- 60d_expected_return: `-0.0%`
- risk_reward_ratio: `0.71`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `410.85`
- primary_invalidation_level: `349.33`
- risk_scenario_activation_level: `349.33`
- trend_repair_confirmation_level: `419.56`
- breakout_level: `410.85`
- breakdown_level: `349.33`
- nearest_support: `392.46`
- nearest_resistance: `410.85`
- bounce_target_zone: `{"conservative": 411.43, "base": 419.56, "extended": 421.69, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 396.8, "critical_warning": 349.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.92`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.9%`
- secondary: `stock_failed_bounce` / `18.5%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `39.39` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `17.4%`
- 60d_expected_return: `-3.0%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `65.81`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `5.20`
- risk_scenario_activation_level: `5.20`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `5.20`
- nearest_support: `5.58`
- nearest_resistance: `6.43`
- bounce_target_zone: `{"conservative": 6.18, "base": 6.18, "extended": 8.71, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.73, "critical_warning": 5.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `264.58`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.5%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `36.27` / `weak`
- stock_alpha_score_v1: `23.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.4%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.0`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `255.42`
- nearest_resistance: `278.32`
- bounce_target_zone: `{"conservative": 271.45, "base": 271.45, "extended": 318.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 259.43, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
