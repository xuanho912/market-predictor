# Stock Prediction Report

Generated at: `2026-11-04T19:50:22.632420+00:00`
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
- current_price: `203.32`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.4%`
- secondary: `stock_failed_bounce` / `26.6%`
- risk: `stock_event_risk` / `12.1%`
- stock_confluence_score: `36.69` / `weak`
- stock_alpha_score_v1: `26.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.9%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.36`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `237.07`
- primary_invalidation_level: `199.14`
- risk_scenario_activation_level: `196.25`
- trend_repair_confirmation_level: `237.07`
- breakout_level: `237.07`
- breakdown_level: `196.25`
- nearest_support: `200.92`
- nearest_resistance: `211.02`
- bounce_target_zone: `{"conservative": 207.17, "base": 207.17, "extended": 242.21, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 200.43, "critical_warning": 199.14, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `389.83`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_trend_repair` / `18.4%`
- risk: `stock_downside_continuation` / `16.8%`
- stock_confluence_score: `41.8` / `weak`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.0%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.63`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `51.96`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `349.33`
- risk_scenario_activation_level: `349.33`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `349.33`
- nearest_support: `377.21`
- nearest_resistance: `408.76`
- bounce_target_zone: `{"conservative": 399.29, "base": 399.29, "extended": 426.85, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 382.25, "critical_warning": 349.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.15`
- market_context: `market_tailwind`
- primary: `stock_downside_continuation` / `31.4%`
- secondary: `stock_bounce` / `25.3%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `36.57` / `weak`
- stock_alpha_score_v1: `2.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `11.1%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `77.49`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `7.55`
- primary_invalidation_level: `4.89`
- risk_scenario_activation_level: `4.71`
- trend_repair_confirmation_level: `7.55`
- breakout_level: `7.55`
- breakdown_level: `4.71`
- nearest_support: `5.01`
- nearest_resistance: `5.63`
- bounce_target_zone: `{"conservative": 5.39, "base": 5.39, "extended": 7.87, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.97, "critical_warning": 4.89, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `247.79`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.7%`
- secondary: `stock_failed_bounce` / `24.9%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `26.81` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `33.3%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `61.63`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `306.99`
- primary_invalidation_level: `237.81`
- risk_scenario_activation_level: `234.99`
- trend_repair_confirmation_level: `306.99`
- breakout_level: `306.99`
- breakdown_level: `234.99`
- nearest_support: `238.48`
- nearest_resistance: `261.75`
- bounce_target_zone: `{"conservative": 254.77, "base": 254.77, "extended": 316.3, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 242.55, "critical_warning": 237.81, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
