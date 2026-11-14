# Stock Prediction Report

Generated at: `2026-11-14T03:07:05.190769+00:00`
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

- company_name: `NVIDIA Corporation`
- status: `available`
- current_price: `162.85`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.4%`
- secondary: `stock_failed_bounce` / `24.0%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `40.46` / `weak`
- stock_alpha_score_v1: `32.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.0%`
- 60d_expected_return: `-3.2%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `61.1`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `222.19`
- primary_invalidation_level: `148.80`
- risk_scenario_activation_level: `148.80`
- trend_repair_confirmation_level: `222.19`
- breakout_level: `222.19`
- breakdown_level: `148.80`
- nearest_support: `154.05`
- nearest_resistance: `176.06`
- bounce_target_zone: `{"conservative": 169.45, "base": 169.45, "extended": 230.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 157.9, "critical_warning": 148.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `390.22`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.3%`
- secondary: `stock_trend_repair` / `20.8%`
- risk: `stock_downside_continuation` / `16.8%`
- stock_confluence_score: `49.02` / `mixed`
- stock_alpha_score_v1: `19.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.2%`
- 60d_expected_return: `-0.2%`
- risk_reward_ratio: `0.68`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `54.44`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `375.69`
- nearest_resistance: `412.02`
- bounce_target_zone: `{"conservative": 401.12, "base": 401.12, "extended": 428.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 381.51, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `4.66`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.4%`
- secondary: `stock_failed_bounce` / `21.1%`
- risk: `stock_event_risk` / `12.4%`
- stock_confluence_score: `40.84` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `19.9%`
- 60d_expected_return: `-5.1%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `80.46`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `4.28`
- risk_scenario_activation_level: `4.11`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `4.11`
- nearest_support: `4.28`
- nearest_resistance: `5.26`
- bounce_target_zone: `{"conservative": 4.96, "base": 4.96, "extended": 6.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.44, "critical_warning": 4.28, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `280.20`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.9%`
- secondary: `stock_downside_continuation` / `19.8%`
- risk: `stock_event_risk` / `13.2%`
- stock_confluence_score: `49.2` / `mixed`
- stock_alpha_score_v1: `52.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `62.5%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.45`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `286.32`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `286.32`
- breakdown_level: `231.30`
- nearest_support: `269.32`
- nearest_resistance: `284.97`
- bounce_target_zone: `{"conservative": 288.36, "base": 288.36, "extended": 295.85, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 274.08, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
