# Stock Prediction Report

Generated at: `2026-09-16T16:59:37.206619+00:00`
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
- current_price: `216.01`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.9%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `48.04` / `mixed`
- stock_alpha_score_v1: `39.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.3%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.82`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `209.97`
- nearest_resistance: `225.07`
- bounce_target_zone: `{"conservative": 220.54, "base": 220.54, "extended": 240.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 212.61, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `362.35`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `47.45` / `mixed`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.1%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.23`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `335.70`
- risk_scenario_activation_level: `335.70`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `335.70`
- nearest_support: `351.12`
- nearest_resistance: `379.20`
- bounce_target_zone: `{"conservative": 370.77, "base": 370.77, "extended": 395.27, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 356.03, "critical_warning": 335.7, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.22`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `31.4%`
- secondary: `stock_downside_continuation` / `22.1%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `37.44` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.7%`
- 60d_expected_return: `-3.2%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.45`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.77`
- risk_scenario_activation_level: `7.47`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.47`
- nearest_support: `8.10`
- nearest_resistance: `9.03`
- bounce_target_zone: `{"conservative": 8.62, "base": 8.62, "extended": 11.91, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.91, "critical_warning": 7.77, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `259.68`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `30.3%`
- secondary: `stock_downside_continuation` / `21.6%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `36.52` / `weak`
- stock_alpha_score_v1: `25.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.7%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.34`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `252.92`
- risk_scenario_activation_level: `248.25`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `248.25`
- nearest_support: `254.71`
- nearest_resistance: `272.15`
- bounce_target_zone: `{"conservative": 265.92, "base": 265.92, "extended": 314.11, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 255.0, "critical_warning": 252.92, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
