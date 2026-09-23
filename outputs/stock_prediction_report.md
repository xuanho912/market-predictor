# Stock Prediction Report

Generated at: `2026-09-23T23:03:34.870495+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `TSLA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `225.51`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `18.6%`
- risk: `stock_event_risk` / `14.3%`
- stock_confluence_score: `50.62` / `mixed`
- stock_alpha_score_v1: `50.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.5%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.29`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `221.10`
- nearest_resistance: `232.13`
- bounce_target_zone: `{"conservative": 228.82, "base": 228.82, "extended": 239.17, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 223.03, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `380.12`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `15.6%`
- stock_confluence_score: `45.53` / `mixed`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.4%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.09`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.70`
- primary_invalidation_level: `342.53`
- risk_scenario_activation_level: `342.53`
- trend_repair_confirmation_level: `386.70`
- breakout_level: `386.70`
- breakdown_level: `342.53`
- nearest_support: `369.71`
- nearest_resistance: `386.70`
- bounce_target_zone: `{"conservative": 387.93, "base": 387.93, "extended": 397.11, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 374.26, "critical_warning": 342.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.68`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.3%`
- secondary: `stock_failed_bounce` / `22.3%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `29.98` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `33.4%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `30.48`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.05`
- risk_scenario_activation_level: `7.87`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.87`
- nearest_support: `8.09`
- nearest_resistance: `9.57`
- bounce_target_zone: `{"conservative": 9.12, "base": 9.12, "extended": 11.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.35, "critical_warning": 8.05, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `263.88`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `24.7%`
- risk: `stock_event_risk` / `11.1%`
- stock_confluence_score: `37.94` / `weak`
- stock_alpha_score_v1: `32.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.8%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.03`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `250.55`
- risk_scenario_activation_level: `250.55`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `250.55`
- nearest_support: `255.27`
- nearest_resistance: `276.80`
- bounce_target_zone: `{"conservative": 270.34, "base": 270.34, "extended": 314.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 259.04, "critical_warning": 250.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
