# Stock Prediction Report

Generated at: `2026-09-14T18:07:37.857865+00:00`
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
- current_price: `212.30`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `28.9%`
- secondary: `stock_downside_continuation` / `20.7%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `43.7` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.3%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.02`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `203.76`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `203.76`
- nearest_support: `207.25`
- nearest_resistance: `221.62`
- bounce_target_zone: `{"conservative": 216.96, "base": 216.96, "extended": 240.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 208.81, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `361.55`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `18.5%`
- risk: `stock_event_risk` / `15.5%`
- stock_confluence_score: `43.3` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.8%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.13`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `331.12`
- risk_scenario_activation_level: `331.12`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `331.12`
- nearest_support: `350.38`
- nearest_resistance: `378.31`
- bounce_target_zone: `{"conservative": 369.93, "base": 369.93, "extended": 395.21, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 355.27, "critical_warning": 331.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.64`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.4%`
- secondary: `stock_downside_continuation` / `22.5%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `29.26` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.9%`
- 60d_expected_return: `-3.2%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Liquidity / Gap Risk Alert` / `NO_ALERT` / `36.76`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.14`
- risk_scenario_activation_level: `7.80`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.80`
- nearest_support: `8.23`
- nearest_resistance: `9.55`
- bounce_target_zone: `{"conservative": 9.1, "base": 9.1, "extended": 11.98, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.29, "critical_warning": 8.14, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `265.19`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `30.5%`
- secondary: `stock_downside_continuation` / `22.7%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `30.63` / `weak`
- stock_alpha_score_v1: `19.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.1%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.99`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `258.50`
- risk_scenario_activation_level: `253.87`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `253.87`
- nearest_support: `264.32`
- nearest_resistance: `277.54`
- bounce_target_zone: `{"conservative": 271.37, "base": 271.37, "extended": 314.03, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 260.56, "critical_warning": 258.5, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
