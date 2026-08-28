# Stock Prediction Report

Generated at: `2026-08-28T05:38:58.056177+00:00`
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
- current_price: `227.98`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.3%`
- secondary: `stock_trend_repair` / `21.6%`
- risk: `stock_downside_continuation` / `16.7%`
- stock_confluence_score: `61.5` / `moderate`
- stock_alpha_score_v1: `60.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `71.3%`
- 60d_expected_return: `-0.0%`
- risk_reward_ratio: `0.71`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `30.91`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `230.91`
- primary_invalidation_level: `194.95`
- risk_scenario_activation_level: `194.95`
- trend_repair_confirmation_level: `230.47`
- breakout_level: `230.91`
- breakdown_level: `194.95`
- nearest_support: `222.77`
- nearest_resistance: `230.47`
- bounce_target_zone: `{"conservative": 231.89, "base": 231.89, "extended": 235.68, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 224.85, "critical_warning": 194.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `354.81`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.2%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `41.97` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.7%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.36`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `366.50`
- primary_invalidation_level: `301.97`
- risk_scenario_activation_level: `301.97`
- trend_repair_confirmation_level: `366.50`
- breakout_level: `366.50`
- breakdown_level: `301.97`
- nearest_support: `345.31`
- nearest_resistance: `366.50`
- bounce_target_zone: `{"conservative": 361.94, "base": 361.94, "extended": 376.0, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 349.46, "critical_warning": 301.97, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.74`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.5%`
- secondary: `stock_downside_continuation` / `20.8%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `41.94` / `weak`
- stock_alpha_score_v1: `13.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.0%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.59`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.43`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.29`
- risk_scenario_activation_level: `8.29`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.29`
- nearest_support: `9.18`
- nearest_resistance: `10.26`
- bounce_target_zone: `{"conservative": 10.16, "base": 10.16, "extended": 10.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.42, "critical_warning": 8.29, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `282.41`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `20.3%`
- risk: `stock_event_risk` / `11.6%`
- stock_confluence_score: `44.98` / `weak`
- stock_alpha_score_v1: `37.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.4%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.23`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `260.67`
- risk_scenario_activation_level: `260.67`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `260.67`
- nearest_support: `275.94`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 287.26, "base": 287.26, "extended": 293.47, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 278.77, "critical_warning": 260.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
