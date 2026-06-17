# Stock Prediction Report

Generated at: `2026-06-17T00:01:37.396455+00:00`
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
- current_price: `207.41`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `24.3%`
- risk: `stock_failed_bounce` / `26.6%`
- stock_confluence_score: `37.26` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.7%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `36.72`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `198.21`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `198.21`
- nearest_support: `200.72`
- nearest_resistance: `217.45`
- bounce_target_zone: `{"conservative": 212.43, "base": 212.43, "extended": 238.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 203.65, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `404.66`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `21.3%`
- risk: `stock_failed_bounce` / `26.4%`
- stock_confluence_score: `33.03` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `34.2%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `35.73`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `390.43`
- nearest_resistance: `426.00`
- bounce_target_zone: `{"conservative": 415.33, "base": 415.33, "extended": 459.83, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 396.66, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.89`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `24.2%`
- secondary: `stock_failed_bounce` / `20.8%`
- risk: `stock_downside_continuation` / `24.2%`
- stock_confluence_score: `28.21` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `28.8%`
- 60d_expected_return: `-3.0%`
- risk_reward_ratio: `0.59`
- strongest_alert: `Liquidity / Gap Risk Alert` / `WATCH` / `51.77`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.11`
- risk_scenario_activation_level: `8.57`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `8.57`
- nearest_support: `9.12`
- nearest_resistance: `11.33`
- bounce_target_zone: `{"conservative": 10.61, "base": 10.61, "extended": 15.26, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.31, "critical_warning": 8.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `268.00`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.1%`
- secondary: `stock_downside_continuation` / `23.8%`
- risk: `stock_failed_bounce` / `25.1%`
- stock_confluence_score: `37.48` / `weak`
- stock_alpha_score_v1: `24.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.4%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `27.7`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `310.45`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `310.45`
- breakout_level: `310.45`
- breakdown_level: `240.51`
- nearest_support: `259.71`
- nearest_resistance: `280.44`
- bounce_target_zone: `{"conservative": 274.22, "base": 274.22, "extended": 318.74, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 263.34, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
