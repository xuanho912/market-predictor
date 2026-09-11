# Stock Prediction Report

Generated at: `2026-09-11T00:39:57.905534+00:00`
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
- current_price: `218.36`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `19.5%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `42.85` / `weak`
- stock_alpha_score_v1: `39.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.4%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.81`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `212.18`
- nearest_resistance: `227.62`
- bounce_target_zone: `{"conservative": 222.99, "base": 222.99, "extended": 240.94, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.89, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `363.56`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `24.7%`
- secondary: `stock_downside_continuation` / `17.8%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `43.89` / `weak`
- stock_alpha_score_v1: `14.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.3%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.6`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.78`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `325.24`
- risk_scenario_activation_level: `325.24`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `325.24`
- nearest_support: `351.32`
- nearest_resistance: `381.91`
- bounce_target_zone: `{"conservative": 372.74, "base": 372.74, "extended": 396.28, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 356.68, "critical_warning": 325.24, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.21`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.0%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `13.8%`
- stock_confluence_score: `40.54` / `weak`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.3%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.65`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.1`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.53`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `8.53`
- nearest_support: `9.66`
- nearest_resistance: `11.04`
- bounce_target_zone: `{"conservative": 10.62, "base": 10.62, "extended": 11.92, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.9, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `285.97`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `39.54` / `weak`
- stock_alpha_score_v1: `38.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.8%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.62`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `264.82`
- risk_scenario_activation_level: `264.82`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `264.82`
- nearest_support: `278.59`
- nearest_resistance: `297.04`
- bounce_target_zone: `{"conservative": 291.51, "base": 291.51, "extended": 313.18, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 281.82, "critical_warning": 264.82, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
