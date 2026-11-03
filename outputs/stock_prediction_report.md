# Stock Prediction Report

Generated at: `2026-11-03T07:59:24.177678+00:00`
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
- current_price: `202.06`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.3%`
- secondary: `stock_failed_bounce` / `26.3%`
- risk: `stock_event_risk` / `11.9%`
- stock_confluence_score: `36.94` / `weak`
- stock_alpha_score_v1: `28.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.8%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.38`
- strongest_alert: `Stock Breakdown Warning` / `NO_ALERT` / `32.78`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `197.68`
- risk_scenario_activation_level: `194.65`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `194.65`
- nearest_support: `200.92`
- nearest_resistance: `210.14`
- bounce_target_zone: `{"conservative": 206.1, "base": 206.1, "extended": 248.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 199.03, "critical_warning": 197.68, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `403.82`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `23.1%`
- secondary: `stock_failed_bounce` / `22.5%`
- risk: `stock_downside_continuation` / `16.2%`
- stock_confluence_score: `49.36` / `mixed`
- stock_alpha_score_v1: `17.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.1%`
- 60d_expected_return: `0.1%`
- risk_reward_ratio: `0.74`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `349.33`
- risk_scenario_activation_level: `349.33`
- trend_repair_confirmation_level: `421.94`
- breakout_level: `414.23`
- breakdown_level: `349.33`
- nearest_support: `391.75`
- nearest_resistance: `414.23`
- bounce_target_zone: `{"conservative": 412.87, "base": 421.94, "extended": 426.3, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 396.57, "critical_warning": 349.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.35`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.8%`
- secondary: `stock_failed_bounce` / `17.6%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `40.69` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `14.9%`
- 60d_expected_return: `-3.9%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `78.1`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `5.07`
- risk_scenario_activation_level: `4.87`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `4.87`
- nearest_support: `5.20`
- nearest_resistance: `5.88`
- bounce_target_zone: `{"conservative": 5.61, "base": 5.61, "extended": 8.72, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.15, "critical_warning": 5.07, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `257.25`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.5%`
- secondary: `stock_downside_continuation` / `22.0%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `29.58` / `weak`
- stock_alpha_score_v1: `21.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.6%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.33`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `244.93`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `244.93`
- nearest_support: `248.29`
- nearest_resistance: `270.69`
- bounce_target_zone: `{"conservative": 263.97, "base": 263.97, "extended": 318.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 252.21, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
