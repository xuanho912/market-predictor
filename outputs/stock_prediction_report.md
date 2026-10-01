# Stock Prediction Report

Generated at: `2026-10-01T00:11:12.045432+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `TSLA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `228.38`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `46.89` / `mixed`
- stock_alpha_score_v1: `50.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.6%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.99`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `224.14`
- nearest_resistance: `234.74`
- bounce_target_zone: `{"conservative": 231.56, "base": 231.56, "extended": 239.0, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 226.0, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `354.81`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `29.7%`
- secondary: `stock_downside_continuation` / `20.3%`
- risk: `stock_event_risk` / `13.2%`
- stock_confluence_score: `36.52` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.5%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `39.64`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `342.89`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `342.89`
- nearest_support: `346.14`
- nearest_resistance: `367.82`
- bounce_target_zone: `{"conservative": 361.31, "base": 361.31, "extended": 395.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 349.93, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.90`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.0%`
- secondary: `stock_failed_bounce` / `24.7%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `23.5` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `30.1%`
- 60d_expected_return: `-3.2%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `39.68`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.49`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.21`
- nearest_support: `7.75`
- nearest_resistance: `8.65`
- bounce_target_zone: `{"conservative": 8.28, "base": 8.28, "extended": 11.87, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.62, "critical_warning": 7.49, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `254.02`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `26.0%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `32.13` / `weak`
- stock_alpha_score_v1: `19.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.0%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.45`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `243.48`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `243.48`
- nearest_support: `247.20`
- nearest_resistance: `265.52`
- bounce_target_zone: `{"conservative": 259.77, "base": 259.77, "extended": 313.47, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 249.71, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
