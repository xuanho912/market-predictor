# Stock Prediction Report

Generated at: `2026-06-16T15:33:57.700880+00:00`
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
- current_price: `209.36`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.5%`
- secondary: `stock_downside_continuation` / `24.5%`
- risk: `stock_failed_bounce` / `26.5%`
- stock_confluence_score: `35.36` / `weak`
- stock_alpha_score_v1: `37.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.9%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `46.05`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `202.69`
- nearest_resistance: `219.37`
- bounce_target_zone: `{"conservative": 214.37, "base": 214.37, "extended": 238.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 205.61, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `406.24`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.0%`
- secondary: `stock_downside_continuation` / `22.8%`
- risk: `stock_failed_bounce` / `27.0%`
- stock_confluence_score: `29.58` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `31.5%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `51.57`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `391.87`
- nearest_resistance: `427.79`
- bounce_target_zone: `{"conservative": 417.02, "base": 417.02, "extended": 459.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 398.16, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.14`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `24.6%`
- secondary: `stock_failed_bounce` / `22.0%`
- risk: `stock_downside_continuation` / `24.6%`
- stock_confluence_score: `22.45` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `30.2%`
- 60d_expected_return: `-3.3%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `74.93`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `8.83`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `8.83`
- nearest_support: `9.18`
- nearest_resistance: `11.57`
- bounce_target_zone: `{"conservative": 10.86, "base": 10.86, "extended": 15.26, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.57, "critical_warning": 8.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `268.97`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `23.8%`
- risk: `stock_failed_bounce` / `25.3%`
- stock_confluence_score: `34.87` / `weak`
- stock_alpha_score_v1: `24.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.4%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.35`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `310.45`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `310.45`
- breakout_level: `310.45`
- breakdown_level: `240.51`
- nearest_support: `260.68`
- nearest_resistance: `281.41`
- bounce_target_zone: `{"conservative": 275.19, "base": 275.19, "extended": 318.74, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 264.31, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
