# Stock Prediction Report

Generated at: `2026-08-19T21:56:35.365575+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `NVDA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `217.56`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_event_risk` / `17.7%`
- risk: `stock_downside_continuation` / `17.5%`
- stock_confluence_score: `50.1` / `mixed`
- stock_alpha_score_v1: `45.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.1%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.37`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `227.92`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `227.92`
- breakout_level: `227.92`
- breakdown_level: `190.01`
- nearest_support: `212.36`
- nearest_resistance: `225.36`
- bounce_target_zone: `{"conservative": 221.46, "base": 221.46, "extended": 233.12, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.44, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `351.12`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `26.4%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `33.77` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `31.9%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.23`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `47.02`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `356.11`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `351.62`
- breakout_level: `356.11`
- breakdown_level: `297.38`
- nearest_support: `342.24`
- nearest_resistance: `351.62`
- bounce_target_zone: `{"conservative": 357.78, "base": 357.78, "extended": 360.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 346.13, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.29`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_downside_continuation` / `21.5%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `38.46` / `weak`
- stock_alpha_score_v1: `12.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.3%`
- 60d_expected_return: `-2.3%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.9`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.14`
- primary_invalidation_level: `7.54`
- risk_scenario_activation_level: `7.54`
- trend_repair_confirmation_level: `10.14`
- breakout_level: `10.14`
- breakdown_level: `7.54`
- nearest_support: `8.75`
- nearest_resistance: `10.09`
- bounce_target_zone: `{"conservative": 9.69, "base": 9.69, "extended": 10.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.99, "critical_warning": 7.54, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `274.17`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_event_risk` / `11.3%`
- stock_confluence_score: `35.61` / `weak`
- stock_alpha_score_v1: `35.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.5%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.85`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `256.16`
- risk_scenario_activation_level: `256.16`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `256.16`
- nearest_support: `265.60`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 280.6, "base": 280.6, "extended": 295.57, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 269.35, "critical_warning": 256.16, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
