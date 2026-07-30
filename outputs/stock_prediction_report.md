# Stock Prediction Report

Generated at: `2026-07-30T23:48:52.022127+00:00`
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
- current_price: `195.04`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.3%`
- secondary: `stock_downside_continuation` / `19.8%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `41.45` / `weak`
- stock_alpha_score_v1: `44.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.4%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.78`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `186.56`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `186.56`
- nearest_support: `190.01`
- nearest_resistance: `204.29`
- bounce_target_zone: `{"conservative": 199.66, "base": 199.66, "extended": 220.55, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 191.57, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `308.85`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `32.7%`
- secondary: `stock_failed_bounce` / `20.5%`
- risk: `stock_event_risk` / `12.3%`
- stock_confluence_score: `41.57` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `20.7%`
- 60d_expected_return: `-2.3%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `58.04`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.35`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `291.20`
- trend_repair_confirmation_level: `432.35`
- breakout_level: `432.35`
- breakdown_level: `291.20`
- nearest_support: `297.38`
- nearest_resistance: `328.11`
- bounce_target_zone: `{"conservative": 318.48, "base": 318.48, "extended": 445.19, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 301.63, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.60`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.3%`
- secondary: `stock_failed_bounce` / `22.1%`
- risk: `stock_event_risk` / `16.0%`
- stock_confluence_score: `34.02` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.6%`
- 60d_expected_return: `-3.5%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `42.16`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `8.05`
- nearest_resistance: `9.43`
- bounce_target_zone: `{"conservative": 9.02, "base": 9.02, "extended": 11.42, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.29, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `263.56`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `45.99` / `mixed`
- stock_alpha_score_v1: `33.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.0%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.4`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.04`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `236.56`
- risk_scenario_activation_level: `236.56`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `236.56`
- nearest_support: `256.12`
- nearest_resistance: `274.71`
- bounce_target_zone: `{"conservative": 269.14, "base": 269.14, "extended": 287.04, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 259.38, "critical_warning": 236.56, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
