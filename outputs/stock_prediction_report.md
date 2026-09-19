# Stock Prediction Report

Generated at: `2026-09-19T00:45:46.482276+00:00`
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
- current_price: `222.27`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `18.5%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `44.38` / `weak`
- stock_alpha_score_v1: `49.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.6%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.4`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `217.52`
- nearest_resistance: `229.39`
- bounce_target_zone: `{"conservative": 225.83, "base": 225.83, "extended": 239.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 219.6, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `364.27`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `15.7%`
- stock_confluence_score: `41.02` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.3%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.89`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `342.53`
- risk_scenario_activation_level: `342.53`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `342.53`
- nearest_support: `352.90`
- nearest_resistance: `381.32`
- bounce_target_zone: `{"conservative": 372.8, "base": 372.8, "extended": 395.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 357.88, "critical_warning": 342.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.27`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.6%`
- secondary: `stock_failed_bounce` / `23.6%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `26.66` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `34.6%`
- 60d_expected_return: `-2.9%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.98`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.79`
- risk_scenario_activation_level: `7.46`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.46`
- nearest_support: `8.05`
- nearest_resistance: `9.15`
- bounce_target_zone: `{"conservative": 8.71, "base": 8.71, "extended": 11.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.94, "critical_warning": 7.79, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `254.71`
- market_context: `market_tailwind`
- primary: `stock_bounce` / `27.0%`
- secondary: `stock_downside_continuation` / `20.5%`
- risk: `stock_failed_bounce` / `18.5%`
- stock_confluence_score: `37.36` / `weak`
- stock_alpha_score_v1: `35.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.8%`
- 60d_expected_return: `0.1%`
- risk_reward_ratio: `0.8`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `31.58`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `247.70`
- risk_scenario_activation_level: `242.85`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `242.85`
- nearest_support: `254.56`
- nearest_resistance: `267.64`
- bounce_target_zone: `{"conservative": 262.04, "base": 268.18, "extended": 314.42, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 249.86, "critical_warning": 245.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
