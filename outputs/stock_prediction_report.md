# Stock Prediction Report

Generated at: `2026-06-24T23:47:29.377016+00:00`
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
- current_price: `199.00`
- market_context: `market_tailwind`
- primary: `stock_bounce` / `25.0%`
- secondary: `stock_downside_continuation` / `20.7%`
- risk: `stock_failed_bounce` / `17.0%`
- stock_confluence_score: `45.93` / `mixed`
- stock_alpha_score_v1: `43.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.6%`
- 60d_expected_return: `-0.0%`
- risk_reward_ratio: `0.71`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `24.34`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `194.08`
- risk_scenario_activation_level: `190.68`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `190.68`
- nearest_support: `196.58`
- nearest_resistance: `208.08`
- bounce_target_zone: `{"conservative": 204.14, "base": 208.45, "extended": 238.33, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 195.59, "critical_warning": 192.19, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `375.53`
- market_context: `market_tailwind`
- primary: `stock_bounce` / `25.0%`
- secondary: `stock_downside_continuation` / `22.6%`
- risk: `stock_failed_bounce` / `17.2%`
- stock_confluence_score: `36.37` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `29.4%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.74`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `63.25`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `363.15`
- risk_scenario_activation_level: `354.59`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `354.59`
- nearest_support: `373.05`
- nearest_resistance: `398.38`
- bounce_target_zone: `{"conservative": 388.48, "base": 399.33, "extended": 460.83, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 366.96, "critical_warning": 358.39, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.21`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.0%`
- secondary: `stock_failed_bounce` / `19.3%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `37.52` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `23.1%`
- 60d_expected_return: `-3.1%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Liquidity / Gap Risk Alert` / `WATCH` / `41.24`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.07`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `9.07`
- nearest_support: `9.38`
- nearest_resistance: `11.46`
- bounce_target_zone: `{"conservative": 10.83, "base": 10.83, "extended": 15.13, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.74, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `267.97`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.8%`
- secondary: `stock_failed_bounce` / `25.4%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `29.55` / `weak`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.1%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `63.95`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `300.81`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `300.81`
- breakout_level: `300.81`
- breakdown_level: `240.51`
- nearest_support: `260.60`
- nearest_resistance: `279.03`
- bounce_target_zone: `{"conservative": 273.5, "base": 273.5, "extended": 308.18, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 263.82, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
