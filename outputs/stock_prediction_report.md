# Stock Prediction Report

Generated at: `2026-10-31T02:18:13.076863+00:00`
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
- current_price: `204.64`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `27.7%`
- secondary: `stock_failed_bounce` / `25.5%`
- risk: `stock_event_risk` / `12.3%`
- stock_confluence_score: `43.14` / `weak`
- stock_alpha_score_v1: `41.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `50.9%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.4`
- strongest_alert: `Stock Breakdown Warning` / `NO_ALERT` / `30.51`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `200.39`
- risk_scenario_activation_level: `197.45`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `197.45`
- nearest_support: `200.92`
- nearest_resistance: `212.49`
- bounce_target_zone: `{"conservative": 208.56, "base": 208.56, "extended": 248.6, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 201.7, "critical_warning": 200.39, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `399.81`
- market_context: `market_headwind`
- primary: `stock_trend_repair` / `23.3%`
- secondary: `stock_failed_bounce` / `22.4%`
- risk: `stock_downside_continuation` / `16.1%`
- stock_confluence_score: `52.3` / `mixed`
- stock_alpha_score_v1: `21.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.2%`
- 60d_expected_return: `0.1%`
- risk_reward_ratio: `0.75`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `410.85`
- primary_invalidation_level: `349.33`
- risk_scenario_activation_level: `349.33`
- trend_repair_confirmation_level: `417.08`
- breakout_level: `410.85`
- breakdown_level: `349.33`
- nearest_support: `388.30`
- nearest_resistance: `410.85`
- bounce_target_zone: `{"conservative": 408.44, "base": 417.08, "extended": 422.36, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 392.9, "critical_warning": 349.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.62`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.6%`
- secondary: `stock_failed_bounce` / `18.0%`
- risk: `stock_event_risk` / `13.5%`
- stock_confluence_score: `38.68` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `16.6%`
- 60d_expected_return: `-3.6%`
- risk_reward_ratio: `0.28`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `72.49`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `5.20`
- risk_scenario_activation_level: `5.16`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `5.16`
- nearest_support: `5.28`
- nearest_resistance: `6.13`
- bounce_target_zone: `{"conservative": 5.87, "base": 5.87, "extended": 8.71, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.43, "critical_warning": 5.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `262.38`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.1%`
- secondary: `stock_downside_continuation` / `20.0%`
- risk: `stock_event_risk` / `11.7%`
- stock_confluence_score: `35.24` / `weak`
- stock_alpha_score_v1: `28.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.2%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.56`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `253.39`
- nearest_resistance: `275.87`
- bounce_target_zone: `{"conservative": 269.12, "base": 269.12, "extended": 318.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 257.32, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
