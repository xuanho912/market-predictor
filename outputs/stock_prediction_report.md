# Stock Prediction Report

Generated at: `2026-10-09T07:28:37.189079+00:00`
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
- current_price: `230.48`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.5%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `47.69` / `mixed`
- stock_alpha_score_v1: `48.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.5%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.97`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `208.93`
- nearest_support: `226.20`
- nearest_resistance: `236.90`
- bounce_target_zone: `{"conservative": 233.69, "base": 233.69, "extended": 247.65, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 228.07, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `375.00`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.0%`
- secondary: `stock_downside_continuation` / `21.8%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `42.79` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.1%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.09`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.88`
- nearest_support: `366.15`
- nearest_resistance: `386.83`
- bounce_target_zone: `{"conservative": 381.64, "base": 381.64, "extended": 395.68, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 370.02, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.32`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.1%`
- secondary: `stock_failed_bounce` / `21.2%`
- risk: `stock_event_risk` / `10.6%`
- stock_confluence_score: `35.86` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.2%`
- 60d_expected_return: `-3.0%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `53.62`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.77`
- primary_invalidation_level: `7.02`
- risk_scenario_activation_level: `6.82`
- trend_repair_confirmation_level: `9.77`
- breakout_level: `9.77`
- breakdown_level: `6.82`
- nearest_support: `7.17`
- nearest_resistance: `7.87`
- bounce_target_zone: `{"conservative": 7.6, "base": 7.6, "extended": 10.14, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.11, "critical_warning": 7.02, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `285.07`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.2%`
- secondary: `stock_downside_continuation` / `18.3%`
- risk: `stock_event_risk` / `16.2%`
- stock_confluence_score: `46.05` / `mixed`
- stock_alpha_score_v1: `33.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.5%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.03`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `273.49`
- nearest_resistance: `302.44`
- bounce_target_zone: `{"conservative": 293.76, "base": 293.76, "extended": 321.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 278.55, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
