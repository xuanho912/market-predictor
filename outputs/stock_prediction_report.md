# Stock Prediction Report

Generated at: `2026-10-15T17:05:08.956401+00:00`
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
- current_price: `217.11`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `45.64` / `mixed`
- stock_alpha_score_v1: `39.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.2%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.64`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `212.85`
- risk_scenario_activation_level: `210.55`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `210.55`
- nearest_support: `212.85`
- nearest_resistance: `224.26`
- bounce_target_zone: `{"conservative": 220.69, "base": 220.69, "extended": 248.14, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.43, "critical_warning": 212.85, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `360.66`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.7%`
- secondary: `stock_downside_continuation` / `20.4%`
- risk: `stock_event_risk` / `16.2%`
- stock_confluence_score: `41.28` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.0%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.29`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.88`
- nearest_support: `352.31`
- nearest_resistance: `373.19`
- bounce_target_zone: `{"conservative": 366.92, "base": 366.92, "extended": 396.91, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 355.96, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.91`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.4%`
- secondary: `stock_failed_bounce` / `23.6%`
- risk: `stock_event_risk` / `10.1%`
- stock_confluence_score: `39.98` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `13.8%`
- 60d_expected_return: `-4.5%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `79.13`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.21`
- primary_invalidation_level: `5.44`
- risk_scenario_activation_level: `5.39`
- trend_repair_confirmation_level: `9.21`
- breakout_level: `9.21`
- breakdown_level: `5.39`
- nearest_support: `5.53`
- nearest_resistance: `6.49`
- bounce_target_zone: `{"conservative": 6.2, "base": 6.2, "extended": 9.6, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.7, "critical_warning": 5.44, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `274.20`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `17.8%`
- risk: `stock_event_risk` / `16.5%`
- stock_confluence_score: `44.01` / `weak`
- stock_alpha_score_v1: `31.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.1%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.07`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `260.91`
- nearest_resistance: `294.15`
- bounce_target_zone: `{"conservative": 284.18, "base": 284.18, "extended": 323.09, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 266.73, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
