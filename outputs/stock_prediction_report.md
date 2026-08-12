# Stock Prediction Report

Generated at: `2026-08-12T13:50:13.770618+00:00`
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
- current_price: `223.08`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `15.6%`
- stock_confluence_score: `43.46` / `weak`
- stock_alpha_score_v1: `45.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.2%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `39.11`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `226.55`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `224.76`
- breakout_level: `226.55`
- breakdown_level: `190.01`
- nearest_support: `216.92`
- nearest_resistance: `224.76`
- bounce_target_zone: `{"conservative": 227.7, "base": 227.7, "extended": 230.92, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 219.61, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `329.38`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.9%`
- secondary: `stock_failed_bounce` / `22.1%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `34.02` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `23.8%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.24`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `39.01`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `395.31`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `395.31`
- breakout_level: `395.31`
- breakdown_level: `297.38`
- nearest_support: `320.91`
- nearest_resistance: `342.09`
- bounce_target_zone: `{"conservative": 335.73, "base": 335.73, "extended": 403.78, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 324.62, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.59`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.9%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `37.53` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.8%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.87`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.02`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.02`
- breakout_level: `10.02`
- breakdown_level: `7.21`
- nearest_support: `9.02`
- nearest_resistance: `10.02`
- bounce_target_zone: `{"conservative": 10.02, "base": 10.02, "extended": 10.59, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.27, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `281.83`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.8%`
- secondary: `stock_downside_continuation` / `19.7%`
- risk: `stock_event_risk` / `12.1%`
- stock_confluence_score: `43.04` / `weak`
- stock_alpha_score_v1: `45.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.4%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.59`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.32`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `286.61`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `285.50`
- breakout_level: `286.61`
- breakdown_level: `244.95`
- nearest_support: `273.34`
- nearest_resistance: `285.50`
- bounce_target_zone: `{"conservative": 288.2, "base": 288.2, "extended": 293.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 277.05, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
