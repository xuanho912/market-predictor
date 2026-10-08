# Stock Prediction Report

Generated at: `2026-10-08T18:54:27.243133+00:00`
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
- current_price: `230.38`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.5%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `46.01` / `mixed`
- stock_alpha_score_v1: `44.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.9%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.15`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `208.93`
- nearest_support: `226.10`
- nearest_resistance: `236.80`
- bounce_target_zone: `{"conservative": 233.59, "base": 233.59, "extended": 247.65, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 227.97, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `371.92`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.8%`
- secondary: `stock_downside_continuation` / `21.6%`
- risk: `stock_event_risk` / `14.1%`
- stock_confluence_score: `41.02` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.5%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.83`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.88`
- nearest_support: `363.07`
- nearest_resistance: `385.20`
- bounce_target_zone: `{"conservative": 378.56, "base": 378.56, "extended": 395.68, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 366.94, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.24`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.2%`
- secondary: `stock_failed_bounce` / `21.3%`
- risk: `stock_event_risk` / `10.5%`
- stock_confluence_score: `40.83` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `17.8%`
- 60d_expected_return: `-3.1%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `55.17`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.77`
- primary_invalidation_level: `6.95`
- risk_scenario_activation_level: `6.74`
- trend_repair_confirmation_level: `9.77`
- breakout_level: `9.77`
- breakdown_level: `6.74`
- nearest_support: `7.17`
- nearest_resistance: `7.80`
- bounce_target_zone: `{"conservative": 7.52, "base": 7.52, "extended": 10.14, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.04, "critical_warning": 6.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `282.34`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `16.3%`
- stock_confluence_score: `44.41` / `weak`
- stock_alpha_score_v1: `32.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.2%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.03`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `270.76`
- nearest_resistance: `299.71`
- bounce_target_zone: `{"conservative": 291.03, "base": 291.03, "extended": 321.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 275.82, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
