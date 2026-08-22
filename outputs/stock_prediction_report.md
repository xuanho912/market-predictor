# Stock Prediction Report

Generated at: `2026-08-22T04:18:41.998299+00:00`
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
- current_price: `214.72`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.6%`
- secondary: `stock_downside_continuation` / `17.4%`
- risk: `stock_event_risk` / `17.4%`
- stock_confluence_score: `47.06` / `mixed`
- stock_alpha_score_v1: `41.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.2%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.21`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `227.92`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `227.92`
- breakout_level: `227.92`
- breakdown_level: `190.01`
- nearest_support: `210.12`
- nearest_resistance: `221.62`
- bounce_target_zone: `{"conservative": 218.17, "base": 218.17, "extended": 232.52, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 212.13, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `362.86`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.2%`
- secondary: `stock_trend_repair` / `17.9%`
- risk: `stock_downside_continuation` / `17.7%`
- stock_confluence_score: `49.81` / `mixed`
- stock_alpha_score_v1: `12.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.3%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.54`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `368.04`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `366.50`
- breakout_level: `368.04`
- breakdown_level: `297.38`
- nearest_support: `353.65`
- nearest_resistance: `366.50`
- bounce_target_zone: `{"conservative": 369.77, "base": 369.77, "extended": 375.71, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 357.34, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.40`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `22.5%`
- secondary: `stock_downside_continuation` / `17.8%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `42.04` / `weak`
- stock_alpha_score_v1: `15.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.5%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `23.69`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.14`
- primary_invalidation_level: `7.54`
- risk_scenario_activation_level: `7.54`
- trend_repair_confirmation_level: `10.14`
- breakout_level: `10.14`
- breakdown_level: `7.54`
- nearest_support: `8.89`
- nearest_resistance: `10.14`
- bounce_target_zone: `{"conservative": 9.79, "base": 9.79, "extended": 10.65, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.11, "critical_warning": 7.54, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `272.88`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.0%`
- secondary: `stock_downside_continuation` / `22.3%`
- risk: `stock_event_risk` / `11.1%`
- stock_confluence_score: `35.4` / `weak`
- stock_alpha_score_v1: `35.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.7%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.42`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `256.16`
- risk_scenario_activation_level: `256.16`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `256.16`
- nearest_support: `264.78`
- nearest_resistance: `285.02`
- bounce_target_zone: `{"conservative": 278.95, "base": 278.95, "extended": 295.1, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 268.33, "critical_warning": 256.16, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
