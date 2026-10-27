# Stock Prediction Report

Generated at: `2026-10-27T18:04:16.118118+00:00`
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

- company_name: `NVIDIA Corporation`
- status: `available`
- current_price: `217.80`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `21.6%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `41.38` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.0%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.79`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `210.18`
- risk_scenario_activation_level: `210.18`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `210.18`
- nearest_support: `212.84`
- nearest_resistance: `225.24`
- bounce_target_zone: `{"conservative": 221.52, "base": 221.52, "extended": 248.33, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 215.01, "critical_warning": 210.18, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `406.10`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `24.1%`
- secondary: `stock_failed_bounce` / `23.2%`
- risk: `stock_downside_continuation` / `16.7%`
- stock_confluence_score: `51.06` / `mixed`
- stock_alpha_score_v1: `19.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.8%`
- 60d_expected_return: `-0.0%`
- risk_reward_ratio: `0.71`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `412.27`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `422.57`
- breakout_level: `412.27`
- breakdown_level: `345.88`
- nearest_support: `395.13`
- nearest_resistance: `407.50`
- bounce_target_zone: `{"conservative": 414.33, "base": 422.57, "extended": 422.57, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 399.51, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.64`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `36.2%`
- secondary: `stock_failed_bounce` / `17.5%`
- risk: `stock_event_risk` / `11.1%`
- stock_confluence_score: `40.12` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `16.0%`
- 60d_expected_return: `-3.5%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `76.01`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `5.20`
- risk_scenario_activation_level: `5.17`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `5.17`
- nearest_support: `5.30`
- nearest_resistance: `6.16`
- bounce_target_zone: `{"conservative": 5.9, "base": 5.9, "extended": 8.71, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.45, "critical_warning": 5.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `256.99`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.7%`
- secondary: `stock_downside_continuation` / `24.6%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `30.53` / `weak`
- stock_alpha_score_v1: `28.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.4%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.28`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `242.40`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `242.40`
- nearest_support: `247.20`
- nearest_resistance: `272.91`
- bounce_target_zone: `{"conservative": 264.95, "base": 264.95, "extended": 320.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 251.02, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
