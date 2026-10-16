# Stock Prediction Report

Generated at: `2026-10-16T16:42:44.920026+00:00`
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

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `216.80`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_downside_continuation` / `20.1%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `39.62` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `50.4%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.94`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `212.85`
- risk_scenario_activation_level: `210.60`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `210.60`
- nearest_support: `212.85`
- nearest_resistance: `223.56`
- bounce_target_zone: `{"conservative": 220.18, "base": 220.18, "extended": 247.88, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.26, "critical_warning": 212.85, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `356.68`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.5%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `16.8%`
- stock_confluence_score: `39.79` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.9%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.19`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.28`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.28`
- nearest_support: `348.39`
- nearest_resistance: `369.12`
- bounce_target_zone: `{"conservative": 362.9, "base": 362.9, "extended": 396.85, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 352.01, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.88`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.0%`
- secondary: `stock_failed_bounce` / `23.8%`
- risk: `stock_event_risk` / `10.3%`
- stock_confluence_score: `38.82` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.4%`
- 60d_expected_return: `-4.3%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `78.19`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.02`
- primary_invalidation_level: `5.44`
- risk_scenario_activation_level: `5.35`
- trend_repair_confirmation_level: `9.02`
- breakout_level: `9.02`
- breakdown_level: `5.35`
- nearest_support: `5.49`
- nearest_resistance: `6.45`
- bounce_target_zone: `{"conservative": 6.16, "base": 6.16, "extended": 9.4, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.66, "critical_warning": 5.44, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `271.97`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.3%`
- secondary: `stock_downside_continuation` / `17.2%`
- risk: `stock_event_risk` / `15.7%`
- stock_confluence_score: `42.5` / `weak`
- stock_alpha_score_v1: `29.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.5%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.19`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `258.70`
- nearest_resistance: `291.88`
- bounce_target_zone: `{"conservative": 281.93, "base": 281.93, "extended": 323.07, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 264.5, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
