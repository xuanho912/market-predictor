# Stock Prediction Report

Generated at: `2026-07-27T15:16:36.921021+00:00`
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
- current_price: `196.95`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.0%`
- secondary: `stock_downside_continuation` / `19.9%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `42.67` / `weak`
- stock_alpha_score_v1: `46.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.2%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.34`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `188.22`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `188.22`
- nearest_support: `190.60`
- nearest_resistance: `206.47`
- bounce_target_zone: `{"conservative": 201.71, "base": 201.71, "extended": 220.74, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 193.38, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `309.23`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.3%`
- secondary: `stock_failed_bounce` / `27.7%`
- risk: `stock_event_risk` / `11.4%`
- stock_confluence_score: `34.21` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `28.0%`
- 60d_expected_return: `-2.7%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `66.35`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `298.38`
- risk_scenario_activation_level: `290.86`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `290.86`
- nearest_support: `304.28`
- nearest_resistance: `329.28`
- bounce_target_zone: `{"conservative": 319.26, "base": 319.26, "extended": 446.22, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 301.72, "critical_warning": 298.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.19`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.9%`
- secondary: `stock_failed_bounce` / `19.2%`
- risk: `stock_event_risk` / `12.3%`
- stock_confluence_score: `32.61` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `24.8%`
- 60d_expected_return: `-3.1%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `55.5`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `7.67`
- nearest_resistance: `8.95`
- bounce_target_zone: `{"conservative": 8.57, "base": 8.57, "extended": 11.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.9, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `269.14`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.7%`
- secondary: `stock_downside_continuation` / `22.7%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `36.65` / `weak`
- stock_alpha_score_v1: `27.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.6%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.61`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `278.19`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `278.19`
- breakout_level: `278.19`
- breakdown_level: `228.63`
- nearest_support: `262.48`
- nearest_resistance: `278.19`
- bounce_target_zone: `{"conservative": 274.15, "base": 274.15, "extended": 284.86, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 265.39, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
