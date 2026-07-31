# Stock Prediction Report

Generated at: `2026-07-31T14:38:38.578870+00:00`
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
- current_price: `197.78`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `14.3%`
- stock_confluence_score: `41.86` / `weak`
- stock_alpha_score_v1: `46.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `60.9%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.69`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `189.53`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `189.53`
- nearest_support: `191.78`
- nearest_resistance: `206.78`
- bounce_target_zone: `{"conservative": 202.28, "base": 202.28, "extended": 220.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 194.4, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `305.57`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `31.4%`
- secondary: `stock_failed_bounce` / `20.6%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `40.54` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `23.2%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `58.06`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `420.00`
- primary_invalidation_level: `295.27`
- risk_scenario_activation_level: `288.14`
- trend_repair_confirmation_level: `420.00`
- breakout_level: `420.00`
- breakdown_level: `288.14`
- nearest_support: `297.38`
- nearest_resistance: `324.58`
- bounce_target_zone: `{"conservative": 315.08, "base": 315.08, "extended": 432.68, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 298.44, "critical_warning": 295.27, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.51`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `29.6%`
- secondary: `stock_failed_bounce` / `22.7%`
- risk: `stock_event_risk` / `15.4%`
- stock_confluence_score: `24.84` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `29.8%`
- 60d_expected_return: `-3.8%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `74.26`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.12`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.12`
- breakout_level: `10.12`
- breakdown_level: `7.21`
- nearest_support: `7.96`
- nearest_resistance: `9.32`
- bounce_target_zone: `{"conservative": 8.91, "base": 8.91, "extended": 10.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.2, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `263.51`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `41.25` / `weak`
- stock_alpha_score_v1: `33.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.9%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `36.41`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `236.56`
- risk_scenario_activation_level: `236.56`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `236.56`
- nearest_support: `256.02`
- nearest_resistance: `274.73`
- bounce_target_zone: `{"conservative": 269.12, "base": 269.12, "extended": 287.08, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 259.3, "critical_warning": 236.56, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
