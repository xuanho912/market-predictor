# Stock Prediction Report

Generated at: `2026-07-30T06:14:34.926152+00:00`
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
- current_price: `190.01`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.2%`
- secondary: `stock_downside_continuation` / `21.9%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `42.49` / `weak`
- stock_alpha_score_v1: `40.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.1%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.4`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.7`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `184.92`
- risk_scenario_activation_level: `181.39`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `181.39`
- nearest_support: `190.01`
- nearest_resistance: `199.41`
- bounce_target_zone: `{"conservative": 194.71, "base": 194.71, "extended": 220.66, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 186.48, "critical_warning": 184.92, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `298.32`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.4%`
- secondary: `stock_failed_bounce` / `26.0%`
- risk: `stock_event_risk` / `11.2%`
- stock_confluence_score: `36.68` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.9%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.28`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `62.77`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `287.99`
- risk_scenario_activation_level: `280.84`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `280.84`
- nearest_support: `297.38`
- nearest_resistance: `317.39`
- bounce_target_zone: `{"conservative": 307.86, "base": 307.86, "extended": 445.57, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 291.17, "critical_warning": 287.99, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.59`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.6%`
- secondary: `stock_failed_bounce` / `23.0%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `33.22` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `21.7%`
- 60d_expected_return: `-4.0%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `62.29`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.17`
- risk_scenario_activation_level: `6.88`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `6.88`
- nearest_support: `7.21`
- nearest_resistance: `8.37`
- bounce_target_zone: `{"conservative": 7.98, "base": 7.98, "extended": 11.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.3, "critical_warning": 7.17, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `257.95`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.2%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `42.93` / `weak`
- stock_alpha_score_v1: `27.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.9%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.83`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `228.63`
- nearest_support: `251.01`
- nearest_resistance: `268.36`
- bounce_target_zone: `{"conservative": 263.16, "base": 263.16, "extended": 286.54, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 254.05, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
