# Stock Prediction Report

Generated at: `2026-09-30T18:04:14.961058+00:00`
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
- current_price: `230.33`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `49.26` / `mixed`
- stock_alpha_score_v1: `50.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.9%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.14`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `226.09`
- nearest_resistance: `234.76`
- bounce_target_zone: `{"conservative": 233.51, "base": 233.51, "extended": 239.0, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 227.95, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `353.52`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `29.8%`
- secondary: `stock_downside_continuation` / `20.4%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `38.14` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `34.8%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.38`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `41.25`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `341.65`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `341.65`
- nearest_support: `345.88`
- nearest_resistance: `366.45`
- bounce_target_zone: `{"conservative": 359.98, "base": 359.98, "extended": 395.46, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 348.66, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.95`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `27.8%`
- secondary: `stock_failed_bounce` / `24.6%`
- risk: `stock_event_risk` / `11.6%`
- stock_confluence_score: `25.04` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `30.2%`
- 60d_expected_return: `-3.1%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `38.45`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.55`
- risk_scenario_activation_level: `7.27`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.27`
- nearest_support: `7.75`
- nearest_resistance: `8.71`
- bounce_target_zone: `{"conservative": 8.33, "base": 8.33, "extended": 11.87, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.67, "critical_warning": 7.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `255.02`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.3%`
- secondary: `stock_failed_bounce` / `25.5%`
- risk: `stock_event_risk` / `10.1%`
- stock_confluence_score: `33.17` / `weak`
- stock_alpha_score_v1: `22.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.0%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.83`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `247.24`
- risk_scenario_activation_level: `244.49`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `244.49`
- nearest_support: `247.36`
- nearest_resistance: `266.52`
- bounce_target_zone: `{"conservative": 260.77, "base": 260.77, "extended": 313.46, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 250.71, "critical_warning": 247.24, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
