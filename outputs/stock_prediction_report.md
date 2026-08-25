# Stock Prediction Report

Generated at: `2026-08-25T20:54:58.982810+00:00`
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
- current_price: `213.05`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.0%`
- secondary: `stock_downside_continuation` / `17.1%`
- risk: `stock_event_risk` / `17.0%`
- stock_confluence_score: `48.63` / `mixed`
- stock_alpha_score_v1: `41.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.9%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.78`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `227.92`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `227.92`
- breakout_level: `227.92`
- breakdown_level: `190.01`
- nearest_support: `208.57`
- nearest_resistance: `219.77`
- bounce_target_zone: `{"conservative": 216.41, "base": 216.41, "extended": 232.4, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 210.53, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `350.25`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.2%`
- secondary: `stock_downside_continuation` / `19.7%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `43.09` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.2%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.41`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.53`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `366.50`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `366.50`
- breakout_level: `366.50`
- breakdown_level: `297.38`
- nearest_support: `340.63`
- nearest_resistance: `364.68`
- bounce_target_zone: `{"conservative": 357.46, "base": 357.46, "extended": 376.12, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 344.84, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.81`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `22.3%`
- secondary: `stock_trend_repair` / `19.6%`
- risk: `stock_downside_continuation` / `17.7%`
- stock_confluence_score: `49.86` / `mixed`
- stock_alpha_score_v1: `16.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.5%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `23.57`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.14`
- primary_invalidation_level: `7.54`
- risk_scenario_activation_level: `7.54`
- trend_repair_confirmation_level: `10.14`
- breakout_level: `10.14`
- breakdown_level: `7.54`
- nearest_support: `9.27`
- nearest_resistance: `10.14`
- bounce_target_zone: `{"conservative": 10.21, "base": 10.21, "extended": 10.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.49, "critical_warning": 7.54, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `278.42`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `20.3%`
- risk: `stock_event_risk` / `12.1%`
- stock_confluence_score: `44.76` / `weak`
- stock_alpha_score_v1: `37.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.8%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.3`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `256.16`
- risk_scenario_activation_level: `256.16`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `256.16`
- nearest_support: `270.96`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 284.01, "base": 284.01, "extended": 294.46, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 274.23, "critical_warning": 256.16, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
