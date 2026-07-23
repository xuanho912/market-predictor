# Stock Prediction Report

Generated at: `2026-07-23T23:45:55.446277+00:00`
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
- current_price: `208.76`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `19.0%`
- risk: `stock_event_risk` / `15.5%`
- stock_confluence_score: `46.37` / `mixed`
- stock_alpha_score_v1: `44.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.8%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.38`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `189.80`
- nearest_support: `202.88`
- nearest_resistance: `214.39`
- bounce_target_zone: `{"conservative": 213.17, "base": 213.17, "extended": 220.27, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 205.45, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `319.69`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `28.1%`
- secondary: `stock_failed_bounce` / `28.0%`
- risk: `stock_event_risk` / `11.7%`
- stock_confluence_score: `40.81` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `28.2%`
- 60d_expected_return: `-2.7%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `63.7`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `308.18`
- risk_scenario_activation_level: `300.21`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `300.21`
- nearest_support: `315.73`
- nearest_resistance: `340.94`
- bounce_target_zone: `{"conservative": 330.32, "base": 330.32, "extended": 447.03, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 311.72, "critical_warning": 308.18, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.81`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.6%`
- secondary: `stock_failed_bounce` / `20.7%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `38.87` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `28.3%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `44.31`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `8.31`
- nearest_resistance: `9.56`
- bounce_target_zone: `{"conservative": 9.19, "base": 9.19, "extended": 11.37, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.53, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `275.60`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.5%`
- secondary: `stock_downside_continuation` / `23.4%`
- risk: `stock_event_risk` / `11.1%`
- stock_confluence_score: `44.26` / `weak`
- stock_alpha_score_v1: `31.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.3%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.61`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.33`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `278.19`
- breakout_level: `279.33`
- breakdown_level: `228.63`
- nearest_support: `268.97`
- nearest_resistance: `278.19`
- bounce_target_zone: `{"conservative": 280.57, "base": 280.57, "extended": 284.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 271.87, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
