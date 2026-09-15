# Stock Prediction Report

Generated at: `2026-09-15T01:02:24.757856+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `CEG`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `210.96`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `28.9%`
- secondary: `stock_downside_continuation` / `21.1%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `36.82` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.1%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.16`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `205.91`
- risk_scenario_activation_level: `202.42`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `202.42`
- nearest_support: `207.25`
- nearest_resistance: `220.28`
- bounce_target_zone: `{"conservative": 215.62, "base": 215.62, "extended": 240.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 207.47, "critical_warning": 205.91, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `358.97`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `18.5%`
- risk: `stock_event_risk` / `15.5%`
- stock_confluence_score: `41.26` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.5%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.39`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `331.12`
- risk_scenario_activation_level: `331.12`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `331.12`
- nearest_support: `347.80`
- nearest_resistance: `375.73`
- bounce_target_zone: `{"conservative": 367.35, "base": 367.35, "extended": 395.21, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 352.69, "critical_warning": 331.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.51`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.5%`
- secondary: `stock_downside_continuation` / `23.1%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `26.56` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.0%`
- 60d_expected_return: `-3.4%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Liquidity / Gap Risk Alert` / `NO_ALERT` / `37.6`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.01`
- risk_scenario_activation_level: `7.67`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.67`
- nearest_support: `8.23`
- nearest_resistance: `9.43`
- bounce_target_zone: `{"conservative": 8.97, "base": 8.97, "extended": 11.98, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.17, "critical_warning": 8.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `264.57`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `30.5%`
- secondary: `stock_downside_continuation` / `22.8%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `28.91` / `weak`
- stock_alpha_score_v1: `19.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.1%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `42.38`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `257.88`
- risk_scenario_activation_level: `253.25`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `253.25`
- nearest_support: `264.32`
- nearest_resistance: `276.92`
- bounce_target_zone: `{"conservative": 270.75, "base": 270.75, "extended": 314.03, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 259.94, "critical_warning": 257.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
