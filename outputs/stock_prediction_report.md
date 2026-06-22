# Stock Prediction Report

Generated at: `2026-06-22T17:05:23.147300+00:00`
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
- current_price: `209.51`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.9%`
- secondary: `stock_downside_continuation` / `23.6%`
- risk: `stock_event_risk` / `14.3%`
- stock_confluence_score: `37.35` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.7%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `36.92`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `203.19`
- nearest_resistance: `218.99`
- bounce_target_zone: `{"conservative": 214.25, "base": 214.25, "extended": 238.6, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 205.96, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `408.15`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `22.0%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `33.96` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `33.7%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `43.66`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `393.45`
- nearest_resistance: `430.22`
- bounce_target_zone: `{"conservative": 419.19, "base": 419.19, "extended": 460.31, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 399.88, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `11.55`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.7%`
- secondary: `stock_downside_continuation` / `20.3%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `36.15` / `weak`
- stock_alpha_score_v1: `6.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.8%`
- 60d_expected_return: `-2.4%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Liquidity / Gap Risk Alert` / `WATCH` / `45.93`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.12`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `9.12`
- nearest_support: `10.62`
- nearest_resistance: `12.93`
- bounce_target_zone: `{"conservative": 12.24, "base": 12.24, "extended": 15.23, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 11.02, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `274.83`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `25.5%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `30.1` / `weak`
- stock_alpha_score_v1: `22.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.7%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `44.69`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `310.45`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `310.45`
- breakout_level: `310.45`
- breakdown_level: `240.51`
- nearest_support: `266.98`
- nearest_resistance: `286.59`
- bounce_target_zone: `{"conservative": 280.71, "base": 280.71, "extended": 318.29, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 270.41, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
