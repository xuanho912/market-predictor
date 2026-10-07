# Stock Prediction Report

Generated at: `2026-10-07T18:59:46.863249+00:00`
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
- current_price: `236.83`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `49.0` / `mixed`
- stock_alpha_score_v1: `46.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.7%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.65`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `208.93`
- nearest_support: `232.73`
- nearest_resistance: `242.98`
- bounce_target_zone: `{"conservative": 239.9, "base": 239.9, "extended": 247.47, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 234.52, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `377.26`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.0%`
- secondary: `stock_downside_continuation` / `21.8%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `41.9` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.5%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.97`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.88`
- nearest_support: `368.38`
- nearest_resistance: `386.83`
- bounce_target_zone: `{"conservative": 383.91, "base": 383.91, "extended": 395.7, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 372.26, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.51`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.6%`
- secondary: `stock_failed_bounce` / `20.2%`
- risk: `stock_event_risk` / `10.5%`
- stock_confluence_score: `32.17` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `17.0%`
- 60d_expected_return: `-2.9%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `49.69`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.69`
- primary_invalidation_level: `7.18`
- risk_scenario_activation_level: `6.96`
- trend_repair_confirmation_level: `10.69`
- breakout_level: `10.69`
- breakdown_level: `6.96`
- nearest_support: `7.39`
- nearest_resistance: `8.10`
- bounce_target_zone: `{"conservative": 7.8, "base": 7.8, "extended": 11.08, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.28, "critical_warning": 7.18, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `298.48`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.3%`
- secondary: `stock_downside_continuation` / `17.5%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `53.31` / `mixed`
- stock_alpha_score_v1: `53.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.1%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.52`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `287.96`
- nearest_resistance: `309.80`
- bounce_target_zone: `{"conservative": 306.38, "base": 306.38, "extended": 320.32, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 292.57, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
