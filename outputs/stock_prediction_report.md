# Stock Prediction Report

Generated at: `2026-08-27T01:03:52.011367+00:00`
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
- current_price: `209.66`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `17.9%`
- risk: `stock_event_risk` / `13.9%`
- stock_confluence_score: `49.13` / `mixed`
- stock_alpha_score_v1: `45.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.3%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.11`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `227.92`
- primary_invalidation_level: `191.52`
- risk_scenario_activation_level: `191.52`
- trend_repair_confirmation_level: `227.92`
- breakout_level: `227.92`
- breakdown_level: `191.52`
- nearest_support: `205.31`
- nearest_resistance: `216.19`
- bounce_target_zone: `{"conservative": 212.92, "base": 212.92, "extended": 232.27, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 207.21, "critical_warning": 191.52, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `345.82`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `19.5%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `40.57` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.7%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.41`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.79`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `366.50`
- primary_invalidation_level: `301.33`
- risk_scenario_activation_level: `301.33`
- trend_repair_confirmation_level: `366.50`
- breakout_level: `366.50`
- breakdown_level: `301.33`
- nearest_support: `336.09`
- nearest_resistance: `360.41`
- bounce_target_zone: `{"conservative": 353.12, "base": 353.12, "extended": 376.23, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 340.35, "critical_warning": 301.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.27`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `22.8%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `42.52` / `weak`
- stock_alpha_score_v1: `14.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.6%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `23.89`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `7.79`
- risk_scenario_activation_level: `7.79`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `7.79`
- nearest_support: `8.70`
- nearest_resistance: `10.12`
- bounce_target_zone: `{"conservative": 9.69, "base": 9.69, "extended": 10.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.95, "critical_warning": 7.79, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `279.52`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.1%`
- secondary: `stock_downside_continuation` / `20.0%`
- risk: `stock_event_risk` / `11.6%`
- stock_confluence_score: `43.3` / `weak`
- stock_alpha_score_v1: `37.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.5%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.62`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `260.67`
- risk_scenario_activation_level: `260.67`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `260.67`
- nearest_support: `272.76`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 284.59, "base": 284.59, "extended": 293.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 275.72, "critical_warning": 260.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
