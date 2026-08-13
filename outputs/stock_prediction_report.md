# Stock Prediction Report

Generated at: `2026-08-13T13:50:59.589146+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `TSLA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `225.89`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `47.11` / `mixed`
- stock_alpha_score_v1: `48.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.7%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.03`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `229.29`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `227.23`
- breakout_level: `229.29`
- breakdown_level: `190.01`
- nearest_support: `219.85`
- nearest_resistance: `227.23`
- bounce_target_zone: `{"conservative": 230.42, "base": 230.42, "extended": 233.27, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 222.49, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `331.41`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.6%`
- secondary: `stock_failed_bounce` / `22.6%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `36.38` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `23.0%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.23`
- strongest_alert: `Stock Breakdown Warning` / `NO_ALERT` / `37.01`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.61`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `386.61`
- breakout_level: `386.61`
- breakdown_level: `297.38`
- nearest_support: `323.21`
- nearest_resistance: `343.72`
- bounce_target_zone: `{"conservative": 337.56, "base": 337.56, "extended": 394.81, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 326.79, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.70`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `23.5%`
- secondary: `stock_failed_bounce` / `21.7%`
- risk: `stock_downside_continuation` / `17.2%`
- stock_confluence_score: `39.79` / `weak`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `63.5%`
- 60d_expected_return: `0.0%`
- risk_reward_ratio: `0.64`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.86`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.02`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.54`
- breakout_level: `10.02`
- breakdown_level: `7.21`
- nearest_support: `9.14`
- nearest_resistance: `10.02`
- bounce_target_zone: `{"conservative": 10.12, "base": 10.54, "extended": 10.58, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.37, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `279.20`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.6%`
- secondary: `stock_downside_continuation` / `19.5%`
- risk: `stock_event_risk` / `12.0%`
- stock_confluence_score: `43.1` / `weak`
- stock_alpha_score_v1: `45.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.9%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.6`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.28`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `285.50`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `285.50`
- breakout_level: `285.50`
- breakdown_level: `244.95`
- nearest_support: `270.87`
- nearest_resistance: `285.50`
- bounce_target_zone: `{"conservative": 285.45, "base": 285.45, "extended": 293.83, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 274.51, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
