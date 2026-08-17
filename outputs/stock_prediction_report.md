# Stock Prediction Report

Generated at: `2026-08-17T13:08:50.933914+00:00`
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
- current_price: `225.16`
- market_context: `market_tailwind`
- primary: `stock_bounce` / `23.1%`
- secondary: `stock_trend_repair` / `22.6%`
- risk: `stock_downside_continuation` / `14.2%`
- stock_confluence_score: `59.17` / `mixed`
- stock_alpha_score_v1: `68.5` / `watchlist_candidate`
- 20d_outperformance_probability: `70.1%`
- 60d_expected_return: `1.1%`
- risk_reward_ratio: `0.96`
- strongest_alert: `Stock Bounce Setup` / `NO_ALERT` / `27.07`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `228.24`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `233.72`
- breakout_level: `228.24`
- breakdown_level: `190.01`
- nearest_support: `219.69`
- nearest_resistance: `227.49`
- bounce_target_zone: `{"conservative": 229.81, "base": 233.72, "extended": 233.72, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 221.87, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `342.27`
- market_context: `market_tailwind`
- primary: `stock_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `24.8%`
- risk: `stock_failed_bounce` / `13.6%`
- stock_confluence_score: `36.24` / `weak`
- stock_alpha_score_v1: `6.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `28.4%`
- 60d_expected_return: `0.0%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `72.06`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.61`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `386.61`
- breakout_level: `386.61`
- breakdown_level: `297.38`
- nearest_support: `333.31`
- nearest_resistance: `355.70`
- bounce_target_zone: `{"conservative": 349.88, "base": 356.26, "extended": 395.57, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 337.23, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.39`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.3%`
- secondary: `stock_trend_repair` / `19.1%`
- risk: `stock_downside_continuation` / `17.4%`
- stock_confluence_score: `41.73` / `weak`
- stock_alpha_score_v1: `18.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.5%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.48`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.14`
- primary_invalidation_level: `7.54`
- risk_scenario_activation_level: `7.54`
- trend_repair_confirmation_level: `10.14`
- breakout_level: `10.14`
- breakdown_level: `7.54`
- nearest_support: `8.81`
- nearest_resistance: `10.14`
- bounce_target_zone: `{"conservative": 9.82, "base": 9.82, "extended": 10.71, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.04, "critical_warning": 7.54, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `282.50`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.4%`
- secondary: `stock_downside_continuation` / `19.4%`
- risk: `stock_event_risk` / `11.9%`
- stock_confluence_score: `47.54` / `mixed`
- stock_alpha_score_v1: `43.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.2%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.4`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.22`
- primary_invalidation_level: `251.33`
- risk_scenario_activation_level: `251.33`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.22`
- breakdown_level: `251.33`
- nearest_support: `274.12`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 288.79, "base": 288.79, "extended": 295.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 277.78, "critical_warning": 251.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
