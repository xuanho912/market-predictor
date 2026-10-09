# Stock Prediction Report

Generated at: `2026-10-09T18:24:20.890184+00:00`
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
- current_price: `229.79`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `49.81` / `mixed`
- stock_alpha_score_v1: `46.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.7%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.88`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `208.93`
- nearest_support: `225.63`
- nearest_resistance: `236.03`
- bounce_target_zone: `{"conservative": 232.91, "base": 232.91, "extended": 247.53, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 227.45, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `383.34`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.3%`
- secondary: `stock_downside_continuation` / `22.0%`
- risk: `stock_event_risk` / `14.3%`
- stock_confluence_score: `43.68` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.0%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.66`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.88`
- nearest_support: `374.52`
- nearest_resistance: `388.56`
- bounce_target_zone: `{"conservative": 389.96, "base": 389.96, "extended": 397.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 378.38, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.20`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.6%`
- secondary: `stock_failed_bounce` / `23.9%`
- risk: `stock_event_risk` / `10.3%`
- stock_confluence_score: `33.13` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.5%`
- 60d_expected_return: `-2.9%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `54.17`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.26`
- primary_invalidation_level: `6.91`
- risk_scenario_activation_level: `6.72`
- trend_repair_confirmation_level: `9.26`
- breakout_level: `9.26`
- breakdown_level: `6.72`
- nearest_support: `7.07`
- nearest_resistance: `7.72`
- bounce_target_zone: `{"conservative": 7.46, "base": 7.46, "extended": 9.6, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.0, "critical_warning": 6.91, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `300.88`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.2%`
- secondary: `stock_downside_continuation` / `18.1%`
- risk: `stock_event_risk` / `16.0%`
- stock_confluence_score: `52.41` / `mixed`
- stock_alpha_score_v1: `50.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.0%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.18`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `289.26`
- nearest_resistance: `309.80`
- bounce_target_zone: `{"conservative": 309.59, "base": 309.59, "extended": 321.42, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 294.35, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
