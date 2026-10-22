# Stock Prediction Report

Generated at: `2026-10-22T17:14:17.524900+00:00`
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
- current_price: `212.44`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `40.67` / `weak`
- stock_alpha_score_v1: `36.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.1%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.31`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `208.49`
- risk_scenario_activation_level: `205.75`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `205.75`
- nearest_support: `212.25`
- nearest_resistance: `219.74`
- bounce_target_zone: `{"conservative": 216.09, "base": 216.09, "extended": 248.24, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 209.7, "critical_warning": 208.49, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `377.82`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.5%`
- secondary: `stock_downside_continuation` / `17.6%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `37.57` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.2%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `32.3`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.86`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.86`
- breakout_level: `388.86`
- breakdown_level: `345.88`
- nearest_support: `368.19`
- nearest_resistance: `388.86`
- bounce_target_zone: `{"conservative": 385.04, "base": 385.04, "extended": 398.49, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 372.41, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.37`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.9%`
- secondary: `stock_failed_bounce` / `21.6%`
- risk: `stock_event_risk` / `12.7%`
- stock_confluence_score: `39.49` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `10.4%`
- 60d_expected_return: `-5.0%`
- risk_reward_ratio: `0.28`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `85.4`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.68`
- primary_invalidation_level: `5.06`
- risk_scenario_activation_level: `4.85`
- trend_repair_confirmation_level: `8.68`
- breakout_level: `8.68`
- breakdown_level: `4.85`
- nearest_support: `5.23`
- nearest_resistance: `5.94`
- bounce_target_zone: `{"conservative": 5.65, "base": 5.65, "extended": 9.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.16, "critical_warning": 5.06, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `256.40`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `19.9%`
- risk: `stock_event_risk` / `15.4%`
- stock_confluence_score: `29.36` / `weak`
- stock_alpha_score_v1: `19.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.5%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.54`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `245.96`
- risk_scenario_activation_level: `238.73`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `238.73`
- nearest_support: `247.20`
- nearest_resistance: `275.68`
- bounce_target_zone: `{"conservative": 266.04, "base": 266.04, "extended": 322.65, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 249.17, "critical_warning": 245.96, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
