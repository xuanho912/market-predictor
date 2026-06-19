# Stock Prediction Report

Generated at: `2026-06-19T23:43:33.562592+00:00`
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
- current_price: `210.69`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `24.0%`
- risk: `stock_failed_bounce` / `26.8%`
- stock_confluence_score: `41.6` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.7%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `37.02`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `203.89`
- nearest_resistance: `220.88`
- bounce_target_zone: `{"conservative": 215.79, "base": 215.79, "extended": 239.08, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 206.87, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `400.49`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.5%`
- secondary: `stock_downside_continuation` / `23.0%`
- risk: `stock_failed_bounce` / `26.5%`
- stock_confluence_score: `34.94` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `31.7%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `54.74`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `385.78`
- nearest_resistance: `422.55`
- bounce_target_zone: `{"conservative": 411.52, "base": 411.52, "extended": 460.31, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 392.22, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `11.74`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `21.1%`
- secondary: `stock_bounce` / `19.1%`
- risk: `stock_failed_bounce` / `21.1%`
- stock_confluence_score: `45.67` / `mixed`
- stock_alpha_score_v1: `18.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.3%`
- 60d_expected_return: `-0.2%`
- risk_reward_ratio: `0.71`
- strongest_alert: `Liquidity / Gap Risk Alert` / `WATCH` / `42.18`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.12`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `9.12`
- nearest_support: `10.78`
- nearest_resistance: `13.18`
- bounce_target_zone: `{"conservative": 12.46, "base": 12.46, "extended": 15.26, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 11.2, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `274.06`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `24.6%`
- risk: `stock_failed_bounce` / `25.5%`
- stock_confluence_score: `33.41` / `weak`
- stock_alpha_score_v1: `24.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.0%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `40.29`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `310.45`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `310.45`
- breakout_level: `310.45`
- breakdown_level: `240.51`
- nearest_support: `265.31`
- nearest_resistance: `287.19`
- bounce_target_zone: `{"conservative": 280.63, "base": 280.63, "extended": 319.2, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 269.14, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
