# Stock Prediction Report

Generated at: `2026-11-05T02:57:56.491736+00:00`
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
- current_price: `200.13`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.8%`
- secondary: `stock_failed_bounce` / `26.7%`
- risk: `stock_event_risk` / `11.9%`
- stock_confluence_score: `35.56` / `weak`
- stock_alpha_score_v1: `31.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.0%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Breakdown Warning` / `NO_ALERT` / `34.44`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `237.07`
- primary_invalidation_level: `195.90`
- risk_scenario_activation_level: `192.97`
- trend_repair_confirmation_level: `237.07`
- breakout_level: `237.07`
- breakdown_level: `192.97`
- nearest_support: `199.68`
- nearest_resistance: `207.94`
- bounce_target_zone: `{"conservative": 204.04, "base": 204.04, "extended": 242.28, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 197.2, "critical_warning": 195.9, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `385.19`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_trend_repair` / `17.1%`
- risk: `stock_downside_continuation` / `16.6%`
- stock_confluence_score: `48.48` / `mixed`
- stock_alpha_score_v1: `15.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.5%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `47.44`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `349.33`
- risk_scenario_activation_level: `349.33`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `349.33`
- nearest_support: `372.57`
- nearest_resistance: `404.12`
- bounce_target_zone: `{"conservative": 394.66, "base": 394.66, "extended": 426.85, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 377.61, "critical_warning": 349.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.13`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.4%`
- secondary: `stock_failed_bounce` / `20.7%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `41.61` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `9.7%`
- 60d_expected_return: `-4.1%`
- risk_reward_ratio: `0.25`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `80.35`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `7.55`
- primary_invalidation_level: `4.87`
- risk_scenario_activation_level: `4.69`
- trend_repair_confirmation_level: `7.55`
- breakout_level: `7.55`
- breakdown_level: `4.69`
- nearest_support: `5.01`
- nearest_resistance: `5.61`
- bounce_target_zone: `{"conservative": 5.37, "base": 5.37, "extended": 7.87, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.95, "critical_warning": 4.87, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `245.72`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.9%`
- secondary: `stock_failed_bounce` / `25.0%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `27.05` / `weak`
- stock_alpha_score_v1: `28.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.9%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `64.11`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `306.99`
- primary_invalidation_level: `237.81`
- risk_scenario_activation_level: `232.92`
- trend_repair_confirmation_level: `306.99`
- breakout_level: `306.99`
- breakdown_level: `232.92`
- nearest_support: `237.81`
- nearest_resistance: `259.68`
- bounce_target_zone: `{"conservative": 252.7, "base": 252.7, "extended": 316.3, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 240.48, "critical_warning": 237.81, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
