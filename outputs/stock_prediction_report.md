# Stock Prediction Report

Generated at: `2026-10-21T17:21:26.557786+00:00`
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
- current_price: `221.78`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `19.5%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `42.37` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.5%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.13`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `212.77`
- risk_scenario_activation_level: `212.77`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `212.77`
- nearest_support: `217.07`
- nearest_resistance: `228.85`
- bounce_target_zone: `{"conservative": 225.31, "base": 225.31, "extended": 248.08, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 219.13, "critical_warning": 212.77, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `387.07`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_event_risk` / `17.6%`
- risk: `stock_downside_continuation` / `17.2%`
- stock_confluence_score: `42.39` / `weak`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.1%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `26.76`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `392.66`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.84`
- breakout_level: `392.66`
- breakdown_level: `345.88`
- nearest_support: `377.14`
- nearest_resistance: `388.84`
- bounce_target_zone: `{"conservative": 394.52, "base": 394.52, "extended": 398.77, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 381.11, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.62`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `36.5%`
- secondary: `stock_failed_bounce` / `18.8%`
- risk: `stock_event_risk` / `13.2%`
- stock_confluence_score: `39.87` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `11.3%`
- 60d_expected_return: `-4.5%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `81.55`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.68`
- primary_invalidation_level: `5.31`
- risk_scenario_activation_level: `5.10`
- trend_repair_confirmation_level: `8.68`
- breakout_level: `8.68`
- breakdown_level: `5.10`
- nearest_support: `5.33`
- nearest_resistance: `6.20`
- bounce_target_zone: `{"conservative": 5.91, "base": 5.91, "extended": 9.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.41, "critical_warning": 5.31, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `270.55`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `19.2%`
- risk: `stock_event_risk` / `13.2%`
- stock_confluence_score: `32.32` / `weak`
- stock_alpha_score_v1: `26.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.8%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.57`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `257.78`
- nearest_resistance: `289.71`
- bounce_target_zone: `{"conservative": 280.13, "base": 280.13, "extended": 322.57, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 263.37, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
