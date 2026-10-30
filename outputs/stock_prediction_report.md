# Stock Prediction Report

Generated at: `2026-10-30T18:09:51.982124+00:00`
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
- current_price: `202.65`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.0%`
- secondary: `stock_failed_bounce` / `25.6%`
- risk: `stock_event_risk` / `12.1%`
- stock_confluence_score: `35.88` / `weak`
- stock_alpha_score_v1: `26.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.6%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.36`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `198.46`
- risk_scenario_activation_level: `195.56`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `195.56`
- nearest_support: `202.29`
- nearest_resistance: `210.38`
- bounce_target_zone: `{"conservative": 206.52, "base": 206.52, "extended": 248.52, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 199.75, "critical_warning": 198.46, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `394.68`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.4%`
- secondary: `stock_trend_repair` / `21.7%`
- risk: `stock_downside_continuation` / `16.8%`
- stock_confluence_score: `47.54` / `mixed`
- stock_alpha_score_v1: `13.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.3%`
- 60d_expected_return: `-0.1%`
- risk_reward_ratio: `0.69`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `410.85`
- primary_invalidation_level: `349.33`
- risk_scenario_activation_level: `349.33`
- trend_repair_confirmation_level: `410.85`
- breakout_level: `410.85`
- breakdown_level: `349.33`
- nearest_support: `383.18`
- nearest_resistance: `410.85`
- bounce_target_zone: `{"conservative": 403.31, "base": 403.31, "extended": 422.35, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 387.78, "critical_warning": 349.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.48`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.4%`
- secondary: `stock_failed_bounce` / `17.8%`
- risk: `stock_event_risk` / `13.5%`
- stock_confluence_score: `33.28` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `15.5%`
- 60d_expected_return: `-3.7%`
- risk_reward_ratio: `0.28`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `76.11`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `5.20`
- risk_scenario_activation_level: `5.02`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `5.02`
- nearest_support: `5.20`
- nearest_resistance: `5.99`
- bounce_target_zone: `{"conservative": 5.73, "base": 5.73, "extended": 8.71, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.29, "critical_warning": 5.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `261.43`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `23.0%`
- secondary: `stock_downside_continuation` / `20.1%`
- risk: `stock_event_risk` / `11.7%`
- stock_confluence_score: `36.41` / `weak`
- stock_alpha_score_v1: `28.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.0%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.6`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.51`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `252.44`
- nearest_resistance: `274.92`
- bounce_target_zone: `{"conservative": 268.17, "base": 268.17, "extended": 318.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 256.37, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
