# Stock Prediction Report

Generated at: `2026-09-12T08:10:03.427809+00:00`
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
- current_price: `218.29`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_downside_continuation` / `19.7%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `42.37` / `weak`
- stock_alpha_score_v1: `37.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.4%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.97`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `212.14`
- nearest_resistance: `227.52`
- bounce_target_zone: `{"conservative": 222.91, "base": 222.91, "extended": 240.91, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.83, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `365.44`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.9%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `49.14` / `mixed`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `50.5%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.27`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `331.12`
- risk_scenario_activation_level: `331.12`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `331.12`
- nearest_support: `354.02`
- nearest_resistance: `382.57`
- bounce_target_zone: `{"conservative": 374.0, "base": 374.0, "extended": 395.46, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 359.02, "critical_warning": 331.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.61`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_downside_continuation` / `24.1%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `32.17` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `31.8%`
- 60d_expected_return: `-3.5%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Liquidity / Gap Risk Alert` / `WATCH` / `41.32`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.11`
- risk_scenario_activation_level: `7.77`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.77`
- nearest_support: `8.53`
- nearest_resistance: `9.53`
- bounce_target_zone: `{"conservative": 9.07, "base": 9.07, "extended": 11.98, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.26, "critical_warning": 8.11, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `284.75`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.7%`
- secondary: `stock_downside_continuation` / `19.5%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `41.2` / `weak`
- stock_alpha_score_v1: `43.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.4%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.02`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `264.82`
- risk_scenario_activation_level: `264.82`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `264.82`
- nearest_support: `277.34`
- nearest_resistance: `295.87`
- bounce_target_zone: `{"conservative": 290.31, "base": 290.31, "extended": 313.21, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 280.58, "critical_warning": 264.82, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
