# Stock Prediction Report

Generated at: `2026-10-03T00:51:28.151250+00:00`
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
- current_price: `233.95`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `44.24` / `weak`
- stock_alpha_score_v1: `40.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.6%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.57`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `237.88`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `237.88`
- breakout_level: `237.88`
- breakdown_level: `208.93`
- nearest_support: `229.83`
- nearest_resistance: `237.88`
- bounce_target_zone: `{"conservative": 237.04, "base": 237.04, "extended": 242.0, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 231.63, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `370.59`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_downside_continuation` / `22.2%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `36.4` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.2%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `39.06`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.88`
- nearest_support: `361.42`
- nearest_resistance: `384.35`
- bounce_target_zone: `{"conservative": 377.47, "base": 377.47, "extended": 396.0, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 365.43, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.75`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.8%`
- secondary: `stock_failed_bounce` / `23.7%`
- risk: `stock_event_risk` / `10.5%`
- stock_confluence_score: `22.12` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `25.3%`
- 60d_expected_return: `-3.0%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `58.54`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.41`
- risk_scenario_activation_level: `7.18`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.18`
- nearest_support: `7.61`
- nearest_resistance: `8.38`
- bounce_target_zone: `{"conservative": 8.06, "base": 8.06, "extended": 11.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.52, "critical_warning": 7.41, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `257.49`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.0%`
- secondary: `stock_failed_bounce` / `25.8%`
- risk: `stock_event_risk` / `13.2%`
- stock_confluence_score: `32.06` / `weak`
- stock_alpha_score_v1: `17.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.4%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.13`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `246.48`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `246.48`
- nearest_support: `249.48`
- nearest_resistance: `269.50`
- bounce_target_zone: `{"conservative": 263.5, "base": 263.5, "extended": 313.81, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 252.99, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
