# Stock Prediction Report

Generated at: `2026-10-16T08:31:40.697953+00:00`
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
- current_price: `217.23`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `45.81` / `mixed`
- stock_alpha_score_v1: `41.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.4%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.15`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `212.85`
- risk_scenario_activation_level: `210.67`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `210.67`
- nearest_support: `212.85`
- nearest_resistance: `224.38`
- bounce_target_zone: `{"conservative": 220.81, "base": 220.81, "extended": 248.14, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.55, "critical_warning": 212.85, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `362.44`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.6%`
- secondary: `stock_downside_continuation` / `20.2%`
- risk: `stock_event_risk` / `16.3%`
- stock_confluence_score: `42.42` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.9%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.66`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.88`
- nearest_support: `354.09`
- nearest_resistance: `374.97`
- bounce_target_zone: `{"conservative": 368.7, "base": 368.7, "extended": 396.91, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 357.74, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `6.15`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.7%`
- secondary: `stock_failed_bounce` / `22.9%`
- risk: `stock_event_risk` / `10.3%`
- stock_confluence_score: `41.03` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `15.3%`
- 60d_expected_return: `-4.2%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `73.95`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.21`
- primary_invalidation_level: `5.44`
- risk_scenario_activation_level: `5.44`
- trend_repair_confirmation_level: `9.21`
- breakout_level: `9.21`
- breakdown_level: `5.44`
- nearest_support: `5.76`
- nearest_resistance: `6.74`
- bounce_target_zone: `{"conservative": 6.45, "base": 6.45, "extended": 9.6, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.93, "critical_warning": 5.44, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `275.00`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.7%`
- secondary: `stock_downside_continuation` / `17.7%`
- risk: `stock_event_risk` / `16.6%`
- stock_confluence_score: `44.91` / `weak`
- stock_alpha_score_v1: `31.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.1%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.75`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `261.70`
- nearest_resistance: `294.96`
- bounce_target_zone: `{"conservative": 284.98, "base": 284.98, "extended": 323.1, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 267.52, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
