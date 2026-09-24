# Stock Prediction Report

Generated at: `2026-09-24T17:17:16.524260+00:00`
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
- current_price: `224.43`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `18.4%`
- risk: `stock_event_risk` / `14.1%`
- stock_confluence_score: `49.22` / `mixed`
- stock_alpha_score_v1: `52.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.3%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.32`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `220.10`
- nearest_resistance: `230.91`
- bounce_target_zone: `{"conservative": 227.67, "base": 227.67, "extended": 239.08, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 221.99, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `382.15`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `45.02` / `mixed`
- stock_alpha_score_v1: `12.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.0%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.85`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `387.38`
- primary_invalidation_level: `345.20`
- risk_scenario_activation_level: `345.20`
- trend_repair_confirmation_level: `386.70`
- breakout_level: `387.38`
- breakdown_level: `345.20`
- nearest_support: `372.85`
- nearest_resistance: `386.70`
- bounce_target_zone: `{"conservative": 389.13, "base": 389.13, "extended": 396.0, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 376.92, "critical_warning": 345.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.57`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.7%`
- secondary: `stock_downside_continuation` / `24.3%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `30.27` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.6%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.2`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.05`
- risk_scenario_activation_level: `7.76`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.76`
- nearest_support: `8.05`
- nearest_resistance: `9.44`
- bounce_target_zone: `{"conservative": 9.0, "base": 9.0, "extended": 11.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.24, "critical_warning": 8.05, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `263.72`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `25.6%`
- secondary: `stock_failed_bounce` / `25.2%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `37.51` / `weak`
- stock_alpha_score_v1: `32.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.4%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.23`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `250.55`
- risk_scenario_activation_level: `250.55`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `250.55`
- nearest_support: `255.54`
- nearest_resistance: `275.99`
- bounce_target_zone: `{"conservative": 269.85, "base": 269.85, "extended": 313.98, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 259.12, "critical_warning": 250.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
