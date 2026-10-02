# Stock Prediction Report

Generated at: `2026-10-02T17:54:57.341550+00:00`
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
- current_price: `234.79`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `47.96` / `mixed`
- stock_alpha_score_v1: `42.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.7%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.06`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `237.87`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `237.87`
- breakout_level: `237.87`
- breakdown_level: `208.93`
- nearest_support: `230.67`
- nearest_resistance: `237.87`
- bounce_target_zone: `{"conservative": 237.87, "base": 237.87, "extended": 241.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 232.47, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `373.04`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.5%`
- secondary: `stock_downside_continuation` / `21.9%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `39.92` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.8%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `32.27`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.88`
- nearest_support: `363.89`
- nearest_resistance: `386.78`
- bounce_target_zone: `{"conservative": 379.91, "base": 379.91, "extended": 395.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 367.89, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.86`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.3%`
- secondary: `stock_failed_bounce` / `23.4%`
- risk: `stock_event_risk` / `10.6%`
- stock_confluence_score: `23.7` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `26.1%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `53.92`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.52`
- risk_scenario_activation_level: `7.29`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.29`
- nearest_support: `7.61`
- nearest_resistance: `8.49`
- bounce_target_zone: `{"conservative": 8.17, "base": 8.17, "extended": 11.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.63, "critical_warning": 7.52, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `254.55`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.4%`
- secondary: `stock_failed_bounce` / `25.9%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `30.48` / `weak`
- stock_alpha_score_v1: `17.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.6%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.95`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `243.56`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `243.56`
- nearest_support: `247.20`
- nearest_resistance: `266.55`
- bounce_target_zone: `{"conservative": 260.55, "base": 260.55, "extended": 313.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 250.06, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
