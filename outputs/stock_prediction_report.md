# Stock Prediction Report

Generated at: `2026-10-06T01:53:32.949356+00:00`
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
- current_price: `238.90`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `18.3%`
- risk: `stock_event_risk` / `13.9%`
- stock_confluence_score: `46.33` / `mixed`
- stock_alpha_score_v1: `46.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.2%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.33`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `241.32`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `240.10`
- breakout_level: `241.32`
- breakdown_level: `208.93`
- nearest_support: `234.60`
- nearest_resistance: `240.10`
- bounce_target_zone: `{"conservative": 242.13, "base": 242.13, "extended": 244.4, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 236.48, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `378.73`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `45.61` / `mixed`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.0%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.24`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.88`
- nearest_support: `369.08`
- nearest_resistance: `386.83`
- bounce_target_zone: `{"conservative": 385.97, "base": 385.97, "extended": 396.48, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 373.3, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.68`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `31.8%`
- secondary: `stock_failed_bounce` / `21.7%`
- risk: `stock_event_risk` / `10.6%`
- stock_confluence_score: `28.1` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `24.8%`
- 60d_expected_return: `-2.7%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `63.22`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.35`
- risk_scenario_activation_level: `7.12`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.12`
- nearest_support: `7.61`
- nearest_resistance: `8.29`
- bounce_target_zone: `{"conservative": 7.98, "base": 7.98, "extended": 11.78, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.45, "critical_warning": 7.35, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `267.62`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.9%`
- secondary: `stock_failed_bounce` / `25.5%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `35.48` / `weak`
- stock_alpha_score_v1: `23.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.3%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.55`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `247.20`
- nearest_support: `259.25`
- nearest_resistance: `280.18`
- bounce_target_zone: `{"conservative": 273.9, "base": 273.9, "extended": 314.17, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 262.91, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
