# Stock Prediction Report

Generated at: `2026-11-03T19:31:54.288643+00:00`
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

- company_name: `NVIDIA Corporation`
- status: `available`
- current_price: `206.69`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.9%`
- secondary: `stock_failed_bounce` / `25.4%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `38.83` / `weak`
- stock_alpha_score_v1: `36.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.5%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.07`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `239.08`
- primary_invalidation_level: `200.92`
- risk_scenario_activation_level: `199.42`
- trend_repair_confirmation_level: `239.08`
- breakout_level: `239.08`
- breakdown_level: `199.42`
- nearest_support: `201.40`
- nearest_resistance: `214.62`
- bounce_target_zone: `{"conservative": 210.65, "base": 210.65, "extended": 244.37, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 203.71, "critical_warning": 200.92, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `399.03`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.6%`
- secondary: `stock_trend_repair` / `21.0%`
- risk: `stock_downside_continuation` / `16.8%`
- stock_confluence_score: `45.38` / `mixed`
- stock_alpha_score_v1: `13.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.1%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.66`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `66.24`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `349.33`
- risk_scenario_activation_level: `349.33`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `349.33`
- nearest_support: `387.06`
- nearest_resistance: `414.23`
- bounce_target_zone: `{"conservative": 408.01, "base": 408.01, "extended": 426.2, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 391.84, "critical_warning": 349.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.30`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.7%`
- secondary: `stock_failed_bounce` / `19.9%`
- risk: `stock_event_risk` / `12.7%`
- stock_confluence_score: `39.82` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `11.1%`
- 60d_expected_return: `-4.0%`
- risk_reward_ratio: `0.25`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `77.91`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `7.82`
- primary_invalidation_level: `5.04`
- risk_scenario_activation_level: `4.86`
- trend_repair_confirmation_level: `7.82`
- breakout_level: `7.82`
- breakdown_level: `4.86`
- nearest_support: `5.20`
- nearest_resistance: `5.79`
- bounce_target_zone: `{"conservative": 5.55, "base": 5.55, "extended": 8.14, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.12, "critical_warning": 5.04, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `264.68`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.9%`
- secondary: `stock_failed_bounce` / `24.5%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `32.05` / `weak`
- stock_alpha_score_v1: `21.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.4%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.74`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `306.99`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `306.99`
- breakout_level: `306.99`
- breakdown_level: `247.20`
- nearest_support: `256.16`
- nearest_resistance: `277.48`
- bounce_target_zone: `{"conservative": 271.08, "base": 271.08, "extended": 315.52, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 259.89, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
