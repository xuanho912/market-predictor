# Stock Prediction Report

Generated at: `2026-10-13T19:21:47.041977+00:00`
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
- current_price: `227.88`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.0%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `50.73` / `mixed`
- stock_alpha_score_v1: `44.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.4%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.36`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `212.50`
- risk_scenario_activation_level: `212.50`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `212.50`
- nearest_support: `223.68`
- nearest_resistance: `234.20`
- bounce_target_zone: `{"conservative": 231.04, "base": 231.04, "extended": 247.58, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 225.52, "critical_warning": 212.5, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `374.45`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.6%`
- secondary: `stock_event_risk` / `18.1%`
- risk: `stock_downside_continuation` / `18.0%`
- stock_confluence_score: `44.53` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.8%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.81`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.88`
- nearest_support: `365.91`
- nearest_resistance: `387.28`
- bounce_target_zone: `{"conservative": 380.87, "base": 380.87, "extended": 397.11, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 369.33, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `6.55`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.4%`
- secondary: `stock_failed_bounce` / `26.1%`
- risk: `stock_event_risk` / `9.5%`
- stock_confluence_score: `27.08` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.5%`
- 60d_expected_return: `-3.6%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `73.74`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.26`
- primary_invalidation_level: `6.27`
- risk_scenario_activation_level: `6.07`
- trend_repair_confirmation_level: `9.26`
- breakout_level: `9.26`
- breakdown_level: `6.07`
- nearest_support: `6.41`
- nearest_resistance: `7.08`
- bounce_target_zone: `{"conservative": 6.82, "base": 6.82, "extended": 9.61, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 6.36, "critical_warning": 6.27, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `296.90`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.4%`
- secondary: `stock_trend_repair` / `21.4%`
- risk: `stock_downside_continuation` / `18.0%`
- stock_confluence_score: `48.62` / `mixed`
- stock_alpha_score_v1: `55.0` / `wait_for_confirmation`
- 20d_outperformance_probability: `69.2%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.68`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `40.05`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `284.66`
- nearest_resistance: `309.80`
- bounce_target_zone: `{"conservative": 306.09, "base": 306.09, "extended": 322.04, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 289.57, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
