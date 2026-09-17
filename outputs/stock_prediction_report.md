# Stock Prediction Report

Generated at: `2026-09-17T17:03:16.560992+00:00`
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
- current_price: `218.95`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `43.48` / `weak`
- stock_alpha_score_v1: `41.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.0%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.7`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `213.76`
- nearest_resistance: `226.74`
- bounce_target_zone: `{"conservative": 222.84, "base": 222.84, "extended": 239.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 216.03, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `366.73`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `15.9%`
- stock_confluence_score: `43.21` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.7%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.06`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `338.96`
- risk_scenario_activation_level: `338.96`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `338.96`
- nearest_support: `355.17`
- nearest_resistance: `384.04`
- bounce_target_zone: `{"conservative": 375.41, "base": 375.41, "extended": 395.6, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 360.23, "critical_warning": 338.96, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.18`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_bounce` / `17.5%`
- risk: `stock_downside_continuation` / `17.5%`
- stock_confluence_score: `35.57` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.9%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.25`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.05`
- risk_scenario_activation_level: `8.05`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `8.05`
- nearest_support: `8.61`
- nearest_resistance: `10.02`
- bounce_target_zone: `{"conservative": 9.6, "base": 9.6, "extended": 11.94, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.84, "critical_warning": 8.05, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `267.14`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.3%`
- secondary: `stock_downside_continuation` / `20.5%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `34.14` / `weak`
- stock_alpha_score_v1: `30.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.6%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.79`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `254.71`
- risk_scenario_activation_level: `254.71`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `254.71`
- nearest_support: `258.53`
- nearest_resistance: `280.05`
- bounce_target_zone: `{"conservative": 273.6, "base": 273.6, "extended": 314.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 262.3, "critical_warning": 254.71, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
