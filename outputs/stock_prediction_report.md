# Stock Prediction Report

Generated at: `2026-10-29T18:31:43.062184+00:00`
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
- current_price: `212.43`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.9%`
- secondary: `stock_failed_bounce` / `25.7%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `36.54` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.6%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.66`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `208.57`
- risk_scenario_activation_level: `205.89`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `205.89`
- nearest_support: `210.18`
- nearest_resistance: `219.56`
- bounce_target_zone: `{"conservative": 216.0, "base": 216.0, "extended": 248.12, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 209.76, "critical_warning": 208.57, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `404.77`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `23.8%`
- secondary: `stock_failed_bounce` / `23.2%`
- risk: `stock_downside_continuation` / `16.7%`
- stock_confluence_score: `49.14` / `mixed`
- stock_alpha_score_v1: `19.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `60.4%`
- 60d_expected_return: `-0.0%`
- risk_reward_ratio: `0.71`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `410.87`
- primary_invalidation_level: `349.33`
- risk_scenario_activation_level: `349.33`
- trend_repair_confirmation_level: `421.04`
- breakout_level: `410.87`
- breakdown_level: `349.33`
- nearest_support: `393.93`
- nearest_resistance: `410.85`
- bounce_target_zone: `{"conservative": 412.9, "base": 421.04, "extended": 421.69, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 398.26, "critical_warning": 349.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.91`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.0%`
- secondary: `stock_failed_bounce` / `18.5%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `34.29` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `17.5%`
- 60d_expected_return: `-3.1%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `66.22`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `5.20`
- risk_scenario_activation_level: `5.20`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `5.20`
- nearest_support: `5.56`
- nearest_resistance: `6.42`
- bounce_target_zone: `{"conservative": 6.16, "base": 6.16, "extended": 8.71, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.71, "critical_warning": 5.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `262.56`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.3%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `35.67` / `weak`
- stock_alpha_score_v1: `23.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.0%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.04`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `253.40`
- nearest_resistance: `276.30`
- bounce_target_zone: `{"conservative": 269.43, "base": 269.43, "extended": 318.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 257.41, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
