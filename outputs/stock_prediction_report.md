# Stock Prediction Report

Generated at: `2026-06-18T00:01:55.358777+00:00`
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
- current_price: `204.65`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.0%`
- secondary: `stock_downside_continuation` / `24.9%`
- risk: `stock_failed_bounce` / `26.0%`
- stock_confluence_score: `36.88` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.8%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `38.61`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.15`
- risk_scenario_activation_level: `195.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `195.34`
- nearest_support: `199.34`
- nearest_resistance: `214.81`
- bounce_target_zone: `{"conservative": 209.73, "base": 209.73, "extended": 239.05, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 200.84, "critical_warning": 197.02, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `396.38`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `21.8%`
- risk: `stock_failed_bounce` / `26.1%`
- stock_confluence_score: `34.89` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `34.1%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `41.18`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `376.46`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `376.46`
- nearest_support: `381.89`
- nearest_resistance: `418.11`
- bounce_target_zone: `{"conservative": 407.24, "base": 407.24, "extended": 460.09, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 388.23, "critical_warning": 380.08, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.34`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `21.6%`
- secondary: `stock_failed_bounce` / `21.3%`
- risk: `stock_downside_continuation` / `21.6%`
- stock_confluence_score: `33.19` / `weak`
- stock_alpha_score_v1: `10.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.3%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.65`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `51.22`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.02`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `9.02`
- nearest_support: `9.38`
- nearest_resistance: `11.78`
- bounce_target_zone: `{"conservative": 11.06, "base": 11.06, "extended": 15.26, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.76, "critical_warning": 9.08, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `267.17`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.1%`
- secondary: `stock_downside_continuation` / `23.9%`
- risk: `stock_failed_bounce` / `25.1%`
- stock_confluence_score: `39.12` / `weak`
- stock_alpha_score_v1: `30.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.4%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.53`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `310.45`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `310.45`
- breakout_level: `310.45`
- breakdown_level: `240.51`
- nearest_support: `258.95`
- nearest_resistance: `279.50`
- bounce_target_zone: `{"conservative": 273.33, "base": 273.33, "extended": 318.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 262.55, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
