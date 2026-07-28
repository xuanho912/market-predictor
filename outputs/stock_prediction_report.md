# Stock Prediction Report

Generated at: `2026-07-28T23:47:55.725524+00:00`
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
- current_price: `197.01`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `19.0%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `45.11` / `mixed`
- stock_alpha_score_v1: `50.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `64.4%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.96`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `191.14`
- risk_scenario_activation_level: `188.50`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `188.50`
- nearest_support: `191.14`
- nearest_resistance: `206.29`
- bounce_target_zone: `{"conservative": 201.65, "base": 201.65, "extended": 220.58, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 193.53, "critical_warning": 191.14, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `307.44`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `30.1%`
- secondary: `stock_failed_bounce` / `26.1%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `36.62` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `23.1%`
- 60d_expected_return: `-2.6%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `58.73`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `296.86`
- risk_scenario_activation_level: `289.54`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `289.54`
- nearest_support: `300.69`
- nearest_resistance: `326.97`
- bounce_target_zone: `{"conservative": 317.2, "base": 317.2, "extended": 445.88, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 300.12, "critical_warning": 296.86, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.22`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.1%`
- secondary: `stock_failed_bounce` / `21.6%`
- risk: `stock_event_risk` / `11.9%`
- stock_confluence_score: `33.13` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `23.6%`
- 60d_expected_return: `-3.3%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `52.35`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `7.72`
- nearest_resistance: `8.97`
- bounce_target_zone: `{"conservative": 8.6, "base": 8.6, "extended": 11.37, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.94, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `259.82`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.5%`
- secondary: `stock_downside_continuation` / `22.6%`
- risk: `stock_event_risk` / `10.7%`
- stock_confluence_score: `36.42` / `weak`
- stock_alpha_score_v1: `26.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.8%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `28.3`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `228.63`
- nearest_support: `252.91`
- nearest_resistance: `270.18`
- bounce_target_zone: `{"conservative": 265.0, "base": 265.0, "extended": 286.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 255.93, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
