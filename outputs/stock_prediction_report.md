# Stock Prediction Report

Generated at: `2026-08-03T15:24:05.218799+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `TSLA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['company_news', 'single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `207.08`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `24.0%`
- secondary: `stock_downside_continuation` / `19.0%`
- risk: `stock_event_risk` / `14.1%`
- stock_confluence_score: `36.87` / `weak`
- stock_alpha_score_v1: `54.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `67.3%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.59`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.63`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `190.01`
- nearest_support: `200.88`
- nearest_resistance: `214.39`
- bounce_target_zone: `{"conservative": 211.73, "base": 211.73, "extended": 220.59, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 203.59, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `323.81`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `32.4%`
- secondary: `stock_failed_bounce` / `19.0%`
- risk: `stock_event_risk` / `12.2%`
- stock_confluence_score: `29.15` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.6%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `49.55`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `419.56`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `419.56`
- breakout_level: `419.56`
- breakdown_level: `297.38`
- nearest_support: `310.77`
- nearest_resistance: `343.37`
- bounce_target_zone: `{"conservative": 333.59, "base": 333.59, "extended": 432.6, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 316.48, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.90`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.1%`
- secondary: `stock_failed_bounce` / `24.1%`
- risk: `stock_event_risk` / `18.5%`
- stock_confluence_score: `23.26` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `32.9%`
- 60d_expected_return: `-4.2%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `72.03`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.46`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `9.46`
- breakout_level: `9.46`
- breakdown_level: `7.21`
- nearest_support: `8.32`
- nearest_resistance: `9.46`
- bounce_target_zone: `{"conservative": 9.33, "base": 9.33, "extended": 10.03, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.58, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `270.66`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.0%`
- secondary: `stock_downside_continuation` / `18.6%`
- risk: `stock_event_risk` / `17.6%`
- stock_confluence_score: `33.31` / `weak`
- stock_alpha_score_v1: `27.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.4%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.32`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `236.56`
- risk_scenario_activation_level: `236.56`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `236.56`
- nearest_support: `263.18`
- nearest_resistance: `279.60`
- bounce_target_zone: `{"conservative": 276.27, "base": 276.27, "extended": 287.08, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 266.45, "critical_warning": 236.56, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
