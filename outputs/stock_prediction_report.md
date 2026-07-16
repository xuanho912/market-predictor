# Stock Prediction Report

Generated at: `2026-07-16T06:07:05.040954+00:00`
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
- current_price: `212.50`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `49.91` / `mixed`
- stock_alpha_score_v1: `49.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `60.6%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.17`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `215.71`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `215.71`
- breakdown_level: `189.80`
- nearest_support: `206.79`
- nearest_resistance: `213.99`
- bounce_target_zone: `{"conservative": 216.78, "base": 216.78, "extended": 219.7, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 209.29, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `394.46`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `23.0%`
- risk: `stock_event_risk` / `17.6%`
- stock_confluence_score: `35.38` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.6%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.85`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `379.35`
- nearest_resistance: `417.12`
- bounce_target_zone: `{"conservative": 405.79, "base": 405.79, "extended": 447.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 385.96, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.36`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.0%`
- secondary: `stock_failed_bounce` / `20.2%`
- risk: `stock_event_risk` / `11.7%`
- stock_confluence_score: `38.66` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `20.5%`
- 60d_expected_return: `-3.4%`
- risk_reward_ratio: `0.4`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `60.7`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `7.92`
- risk_scenario_activation_level: `7.62`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `7.62`
- nearest_support: `8.07`
- nearest_resistance: `9.16`
- bounce_target_zone: `{"conservative": 8.76, "base": 8.76, "extended": 12.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.06, "critical_warning": 7.92, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `258.11`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `24.7%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `32.69` / `weak`
- stock_alpha_score_v1: `24.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.5%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.97`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `250.66`
- nearest_resistance: `269.30`
- bounce_target_zone: `{"conservative": 263.71, "base": 263.71, "extended": 290.22, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 253.92, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
