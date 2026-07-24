# Stock Prediction Report

Generated at: `2026-07-24T14:15:41.492074+00:00`
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
- current_price: `207.41`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `45.45` / `mixed`
- stock_alpha_score_v1: `50.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `66.3%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.82`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `189.80`
- nearest_support: `201.56`
- nearest_resistance: `214.39`
- bounce_target_zone: `{"conservative": 211.8, "base": 211.8, "extended": 220.24, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 204.12, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `315.64`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.7%`
- secondary: `stock_failed_bounce` / `27.6%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `34.16` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `28.7%`
- 60d_expected_return: `-2.5%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `62.9`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `305.09`
- risk_scenario_activation_level: `297.79`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `297.79`
- nearest_support: `314.27`
- nearest_resistance: `335.11`
- bounce_target_zone: `{"conservative": 325.38, "base": 325.38, "extended": 445.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 308.34, "critical_warning": 305.09, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.36`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.1%`
- secondary: `stock_failed_bounce` / `19.7%`
- risk: `stock_event_risk` / `12.3%`
- stock_confluence_score: `32.93` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `26.5%`
- 60d_expected_return: `-2.9%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `51.94`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `7.87`
- nearest_resistance: `9.11`
- bounce_target_zone: `{"conservative": 8.74, "base": 8.74, "extended": 11.37, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.08, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `276.27`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `20.8%`
- risk: `stock_event_risk` / `11.9%`
- stock_confluence_score: `41.91` / `weak`
- stock_alpha_score_v1: `31.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.4%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.38`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.02`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.84`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `278.98`
- breakout_level: `279.84`
- breakdown_level: `228.63`
- nearest_support: `269.91`
- nearest_resistance: `278.98`
- bounce_target_zone: `{"conservative": 281.03, "base": 281.03, "extended": 285.34, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 272.69, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
