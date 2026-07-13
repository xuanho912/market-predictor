# Stock Prediction Report

Generated at: `2026-07-13T15:14:56.905268+00:00`
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
- current_price: `207.36`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `19.2%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `44.24` / `weak`
- stock_alpha_score_v1: `40.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.2%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.86`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `202.03`
- nearest_resistance: `213.99`
- bounce_target_zone: `{"conservative": 211.36, "base": 211.36, "extended": 219.32, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 204.36, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `397.21`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `28.4%`
- secondary: `stock_downside_continuation` / `21.1%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `35.19` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.6%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.25`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `381.38`
- nearest_resistance: `420.97`
- bounce_target_zone: `{"conservative": 409.09, "base": 409.09, "extended": 448.69, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 388.31, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.68`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.8%`
- secondary: `stock_failed_bounce` / `23.6%`
- risk: `stock_event_risk` / `12.2%`
- stock_confluence_score: `35.78` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `29.5%`
- 60d_expected_return: `-2.9%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `54.31`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `8.22`
- risk_scenario_activation_level: `7.90`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `7.90`
- nearest_support: `8.55`
- nearest_resistance: `9.54`
- bounce_target_zone: `{"conservative": 9.11, "base": 9.11, "extended": 12.42, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.36, "critical_warning": 8.22, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `254.97`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `24.6%`
- risk: `stock_event_risk` / `10.8%`
- stock_confluence_score: `35.33` / `weak`
- stock_alpha_score_v1: `26.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.7%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.48`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `247.77`
- nearest_resistance: `265.77`
- bounce_target_zone: `{"conservative": 260.37, "base": 260.37, "extended": 289.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 250.92, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
