# Stock Prediction Report

Generated at: `2026-08-21T13:13:40.761849+00:00`
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
- current_price: `216.85`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.1%`
- secondary: `stock_event_risk` / `17.6%`
- risk: `stock_downside_continuation` / `17.4%`
- stock_confluence_score: `49.52` / `mixed`
- stock_alpha_score_v1: `43.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.3%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.83`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `227.92`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `227.92`
- breakout_level: `227.92`
- breakdown_level: `190.01`
- nearest_support: `211.81`
- nearest_resistance: `224.41`
- bounce_target_zone: `{"conservative": 220.63, "base": 220.63, "extended": 232.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 213.83, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `345.13`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.0%`
- secondary: `stock_downside_continuation` / `22.6%`
- risk: `stock_event_risk` / `11.7%`
- stock_confluence_score: `36.71` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.8%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.15`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `351.62`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `351.62`
- breakout_level: `351.62`
- breakdown_level: `297.38`
- nearest_support: `336.33`
- nearest_resistance: `351.62`
- bounce_target_zone: `{"conservative": 351.73, "base": 351.73, "extended": 360.42, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 340.18, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.07`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.7%`
- secondary: `stock_downside_continuation` / `21.4%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `33.6` / `weak`
- stock_alpha_score_v1: `10.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.0%`
- 60d_expected_return: `-2.6%`
- risk_reward_ratio: `0.38`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `37.66`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.14`
- primary_invalidation_level: `7.54`
- risk_scenario_activation_level: `7.54`
- trend_repair_confirmation_level: `10.14`
- breakout_level: `10.14`
- breakdown_level: `7.54`
- nearest_support: `8.54`
- nearest_resistance: `9.86`
- bounce_target_zone: `{"conservative": 9.47, "base": 9.47, "extended": 10.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.77, "critical_warning": 7.54, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `272.92`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.4%`
- secondary: `stock_downside_continuation` / `22.8%`
- risk: `stock_event_risk` / `11.3%`
- stock_confluence_score: `35.04` / `weak`
- stock_alpha_score_v1: `35.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.6%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.87`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `256.16`
- risk_scenario_activation_level: `256.16`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `256.16`
- nearest_support: `264.47`
- nearest_resistance: `285.60`
- bounce_target_zone: `{"conservative": 279.26, "base": 279.26, "extended": 295.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 268.17, "critical_warning": 256.16, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
