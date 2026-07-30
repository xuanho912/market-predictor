# Stock Prediction Report

Generated at: `2026-07-30T14:35:12.540140+00:00`
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
- current_price: `197.18`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.9%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `45.34` / `mixed`
- stock_alpha_score_v1: `46.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.0%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.65`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `188.71`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `188.71`
- nearest_support: `191.02`
- nearest_resistance: `206.43`
- bounce_target_zone: `{"conservative": 201.8, "base": 201.8, "extended": 220.55, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 193.71, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `308.18`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `32.8%`
- secondary: `stock_failed_bounce` / `20.6%`
- risk: `stock_event_risk` / `12.2%`
- stock_confluence_score: `40.54` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `20.6%`
- 60d_expected_return: `-2.3%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `58.36`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.35`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `290.66`
- trend_repair_confirmation_level: `432.35`
- breakout_level: `432.35`
- breakdown_level: `290.66`
- nearest_support: `297.38`
- nearest_resistance: `327.29`
- bounce_target_zone: `{"conservative": 317.73, "base": 317.73, "extended": 445.09, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 301.01, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.35`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.0%`
- secondary: `stock_failed_bounce` / `22.5%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `25.88` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `26.1%`
- 60d_expected_return: `-3.6%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `46.95`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `7.82`
- nearest_resistance: `9.16`
- bounce_target_zone: `{"conservative": 8.76, "base": 8.76, "extended": 11.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.05, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `269.60`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `40.05` / `weak`
- stock_alpha_score_v1: `39.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `65.8%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.29`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `236.56`
- risk_scenario_activation_level: `236.56`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `236.56`
- nearest_support: `262.18`
- nearest_resistance: `279.60`
- bounce_target_zone: `{"conservative": 275.17, "base": 275.17, "extended": 287.02, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 265.43, "critical_warning": 236.56, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
