# Stock Prediction Report

Generated at: `2026-10-28T18:24:02.223708+00:00`
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
- current_price: `216.79`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `21.9%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `39.93` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.7%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `36.99`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `210.18`
- risk_scenario_activation_level: `210.18`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `210.18`
- nearest_support: `212.06`
- nearest_resistance: `223.89`
- bounce_target_zone: `{"conservative": 220.34, "base": 220.34, "extended": 248.1, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.13, "critical_warning": 210.18, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `402.24`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `23.4%`
- secondary: `stock_failed_bounce` / `23.2%`
- risk: `stock_downside_continuation` / `16.7%`
- stock_confluence_score: `48.98` / `mixed`
- stock_alpha_score_v1: `19.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.5%`
- 60d_expected_return: `-0.1%`
- risk_reward_ratio: `0.7`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `66.57`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `410.85`
- primary_invalidation_level: `349.33`
- risk_scenario_activation_level: `349.33`
- trend_repair_confirmation_level: `419.14`
- breakout_level: `410.85`
- breakdown_level: `349.33`
- nearest_support: `390.99`
- nearest_resistance: `410.85`
- bounce_target_zone: `{"conservative": 410.68, "base": 419.14, "extended": 422.1, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 395.48, "critical_warning": 349.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.62`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `36.7%`
- secondary: `stock_failed_bounce` / `17.4%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `33.72` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `14.5%`
- 60d_expected_return: `-3.5%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `75.82`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `5.20`
- risk_scenario_activation_level: `5.17`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `5.17`
- nearest_support: `5.29`
- nearest_resistance: `6.12`
- bounce_target_zone: `{"conservative": 5.87, "base": 5.87, "extended": 8.7, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.44, "critical_warning": 5.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `257.93`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `19.0%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `33.3` / `weak`
- stock_alpha_score_v1: `23.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.6%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.26`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `244.86`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `244.86`
- nearest_support: `248.43`
- nearest_resistance: `272.19`
- bounce_target_zone: `{"conservative": 265.06, "base": 265.06, "extended": 319.3, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 252.58, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
