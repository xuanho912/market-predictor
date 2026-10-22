# Stock Prediction Report

Generated at: `2026-10-22T01:22:29.797604+00:00`
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
- current_price: `221.97`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `19.3%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `40.7` / `weak`
- stock_alpha_score_v1: `40.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.7%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `40.7`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `212.77`
- risk_scenario_activation_level: `212.77`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `212.77`
- nearest_support: `217.26`
- nearest_resistance: `229.04`
- bounce_target_zone: `{"conservative": 225.5, "base": 225.5, "extended": 248.08, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 219.32, "critical_warning": 212.77, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `386.47`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.2%`
- secondary: `stock_downside_continuation` / `18.1%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `39.69` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.5%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.48`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `392.06`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.84`
- breakout_level: `392.06`
- breakdown_level: `345.88`
- nearest_support: `376.54`
- nearest_resistance: `388.84`
- bounce_target_zone: `{"conservative": 393.92, "base": 393.92, "extended": 398.77, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 380.88, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.50`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `36.8%`
- secondary: `stock_failed_bounce` / `19.3%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `37.38` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `10.2%`
- 60d_expected_return: `-4.9%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `84.33`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.68`
- primary_invalidation_level: `5.19`
- risk_scenario_activation_level: `4.97`
- trend_repair_confirmation_level: `8.68`
- breakout_level: `8.68`
- breakdown_level: `4.97`
- nearest_support: `5.33`
- nearest_resistance: `6.08`
- bounce_target_zone: `{"conservative": 5.79, "base": 5.79, "extended": 9.07, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.28, "critical_warning": 5.19, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `270.74`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `31.81` / `weak`
- stock_alpha_score_v1: `26.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.9%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.74`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `257.85`
- nearest_resistance: `290.07`
- bounce_target_zone: `{"conservative": 280.41, "base": 280.41, "extended": 322.69, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 263.49, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
