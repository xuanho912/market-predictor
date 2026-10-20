# Stock Prediction Report

Generated at: `2026-10-20T17:10:56.990338+00:00`
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
- current_price: `216.75`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.4%`
- secondary: `stock_downside_continuation` / `21.6%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `39.97` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.3%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.22`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `212.77`
- risk_scenario_activation_level: `210.39`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `210.39`
- nearest_support: `212.77`
- nearest_resistance: `223.68`
- bounce_target_zone: `{"conservative": 220.22, "base": 220.22, "extended": 247.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.15, "critical_warning": 212.77, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `374.17`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `17.7%`
- risk: `stock_event_risk` / `17.4%`
- stock_confluence_score: `34.1` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.1%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.78`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.88`
- nearest_support: `364.76`
- nearest_resistance: `388.28`
- bounce_target_zone: `{"conservative": 381.22, "base": 381.22, "extended": 397.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 368.87, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.66`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.5%`
- secondary: `stock_failed_bounce` / `21.8%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `40.31` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `12.2%`
- 60d_expected_return: `-4.9%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `81.51`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.90`
- primary_invalidation_level: `5.33`
- risk_scenario_activation_level: `5.12`
- trend_repair_confirmation_level: `8.90`
- breakout_level: `8.90`
- breakdown_level: `5.12`
- nearest_support: `5.33`
- nearest_resistance: `6.24`
- bounce_target_zone: `{"conservative": 5.95, "base": 5.95, "extended": 9.29, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.44, "critical_warning": 5.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `259.38`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `29.7%`
- secondary: `stock_downside_continuation` / `20.9%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `31.48` / `weak`
- stock_alpha_score_v1: `19.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.9%`
- 60d_expected_return: `-2.5%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.76`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `241.46`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `241.46`
- nearest_support: `247.20`
- nearest_resistance: `278.93`
- bounce_target_zone: `{"conservative": 269.16, "base": 269.16, "extended": 322.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 252.05, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
