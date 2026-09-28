# Stock Prediction Report

Generated at: `2026-09-28T19:43:27.137908+00:00`
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
- current_price: `228.66`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.0%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `51.09` / `mixed`
- stock_alpha_score_v1: `50.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `60.1%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.68`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `224.53`
- nearest_resistance: `234.76`
- bounce_target_zone: `{"conservative": 231.77, "base": 231.77, "extended": 238.9, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 226.34, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `358.12`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `29.3%`
- secondary: `stock_downside_continuation` / `20.7%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `44.33` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.3%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.86`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `347.15`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.88`
- nearest_support: `349.22`
- nearest_resistance: `371.48`
- bounce_target_zone: `{"conservative": 364.8, "base": 364.8, "extended": 395.73, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 353.11, "critical_warning": 347.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.95`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `27.9%`
- secondary: `stock_failed_bounce` / `24.9%`
- risk: `stock_event_risk` / `11.6%`
- stock_confluence_score: `23.04` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `30.6%`
- 60d_expected_return: `-3.3%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `44.82`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.53`
- risk_scenario_activation_level: `7.24`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.24`
- nearest_support: `7.95`
- nearest_resistance: `8.73`
- bounce_target_zone: `{"conservative": 8.34, "base": 8.34, "extended": 11.89, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.66, "critical_warning": 7.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `260.82`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `24.0%`
- secondary: `stock_failed_bounce` / `23.8%`
- risk: `stock_event_risk` / `11.1%`
- stock_confluence_score: `38.3` / `weak`
- stock_alpha_score_v1: `32.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.6%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.96`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `250.55`
- risk_scenario_activation_level: `250.55`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `250.55`
- nearest_support: `253.83`
- nearest_resistance: `271.31`
- bounce_target_zone: `{"conservative": 266.07, "base": 266.07, "extended": 312.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 256.89, "critical_warning": 250.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
