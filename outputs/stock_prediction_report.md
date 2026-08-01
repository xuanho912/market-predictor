# Stock Prediction Report

Generated at: `2026-08-01T04:39:17.237045+00:00`
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
- current_price: `200.75`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `51.55` / `mixed`
- stock_alpha_score_v1: `61.0` / `wait_for_confirmation`
- 20d_outperformance_probability: `67.6%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.84`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `190.01`
- nearest_support: `194.64`
- nearest_resistance: `209.92`
- bounce_target_zone: `{"conservative": 205.33, "base": 205.33, "extended": 220.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 197.31, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `311.21`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `30.9%`
- secondary: `stock_failed_bounce` / `20.1%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `35.13` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `24.0%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `55.21`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `420.00`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `293.78`
- trend_repair_confirmation_level: `420.00`
- breakout_level: `420.00`
- breakdown_level: `293.78`
- nearest_support: `298.53`
- nearest_resistance: `330.22`
- bounce_target_zone: `{"conservative": 320.72, "base": 320.72, "extended": 432.68, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 304.08, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.42`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.0%`
- secondary: `stock_failed_bounce` / `22.4%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `29.79` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `28.7%`
- 60d_expected_return: `-3.9%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `79.62`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.12`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.12`
- breakout_level: `10.12`
- breakdown_level: `7.21`
- nearest_support: `7.87`
- nearest_resistance: `9.24`
- bounce_target_zone: `{"conservative": 8.83, "base": 8.83, "extended": 10.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.11, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `262.75`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `18.3%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `43.25` / `weak`
- stock_alpha_score_v1: `30.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.8%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.36`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `236.56`
- risk_scenario_activation_level: `236.56`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `236.56`
- nearest_support: `255.20`
- nearest_resistance: `274.07`
- bounce_target_zone: `{"conservative": 268.41, "base": 268.41, "extended": 287.15, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 258.5, "critical_warning": 236.56, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
