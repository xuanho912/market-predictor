# Stock Prediction Report

Generated at: `2026-08-27T14:48:41.882652+00:00`
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
- current_price: `224.59`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.8%`
- secondary: `stock_trend_repair` / `19.3%`
- risk: `stock_downside_continuation` / `17.8%`
- stock_confluence_score: `55.5` / `mixed`
- stock_alpha_score_v1: `55.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `68.3%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.62`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `26.19`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `227.92`
- primary_invalidation_level: `194.95`
- risk_scenario_activation_level: `194.95`
- trend_repair_confirmation_level: `227.92`
- breakout_level: `227.92`
- breakdown_level: `194.95`
- nearest_support: `219.61`
- nearest_resistance: `227.92`
- bounce_target_zone: `{"conservative": 228.32, "base": 228.32, "extended": 232.9, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 221.6, "critical_warning": 194.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `350.86`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.4%`
- secondary: `stock_downside_continuation` / `20.7%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `39.73` / `weak`
- stock_alpha_score_v1: `12.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.9%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.76`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `366.50`
- primary_invalidation_level: `301.97`
- risk_scenario_activation_level: `301.97`
- trend_repair_confirmation_level: `366.50`
- breakout_level: `366.50`
- breakdown_level: `301.97`
- nearest_support: `341.40`
- nearest_resistance: `365.05`
- bounce_target_zone: `{"conservative": 357.95, "base": 357.95, "extended": 375.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 345.54, "critical_warning": 301.97, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.68`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `21.8%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `38.37` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `50.1%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.27`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.29`
- risk_scenario_activation_level: `8.29`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.29`
- nearest_support: `9.12`
- nearest_resistance: `10.26`
- bounce_target_zone: `{"conservative": 10.1, "base": 10.1, "extended": 10.81, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.37, "critical_warning": 8.29, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `281.32`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `20.3%`
- risk: `stock_event_risk` / `11.6%`
- stock_confluence_score: `41.68` / `weak`
- stock_alpha_score_v1: `37.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.2%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.52`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `260.67`
- risk_scenario_activation_level: `260.67`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `260.67`
- nearest_support: `274.87`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 286.16, "base": 286.16, "extended": 293.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 277.69, "critical_warning": 260.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
