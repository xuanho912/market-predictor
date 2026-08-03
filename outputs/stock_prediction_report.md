# Stock Prediction Report

Generated at: `2026-08-03T21:38:35.254087+00:00`
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
- current_price: `206.64`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `18.3%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `50.43` / `mixed`
- stock_alpha_score_v1: `60.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `69.3%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.32`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `190.01`
- nearest_support: `200.36`
- nearest_resistance: `214.39`
- bounce_target_zone: `{"conservative": 211.35, "base": 211.35, "extended": 220.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 203.11, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `322.08`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `31.5%`
- secondary: `stock_failed_bounce` / `20.2%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `37.6` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `21.9%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `49.82`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `419.56`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `419.56`
- breakout_level: `419.56`
- breakdown_level: `297.38`
- nearest_support: `309.02`
- nearest_resistance: `341.67`
- bounce_target_zone: `{"conservative": 331.88, "base": 331.88, "extended": 432.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 314.73, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.01`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.1%`
- secondary: `stock_failed_bounce` / `25.0%`
- risk: `stock_event_risk` / `17.0%`
- stock_confluence_score: `30.74` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `33.7%`
- 60d_expected_return: `-4.1%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `68.16`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.46`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `9.46`
- breakout_level: `9.46`
- breakdown_level: `7.21`
- nearest_support: `8.43`
- nearest_resistance: `9.46`
- bounce_target_zone: `{"conservative": 9.44, "base": 9.44, "extended": 10.03, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.69, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `273.71`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `15.5%`
- stock_confluence_score: `40.37` / `weak`
- stock_alpha_score_v1: `30.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.6%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.2`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `236.56`
- risk_scenario_activation_level: `236.56`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `236.56`
- nearest_support: `266.05`
- nearest_resistance: `279.60`
- bounce_target_zone: `{"conservative": 279.46, "base": 279.46, "extended": 287.26, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 269.4, "critical_warning": 236.56, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
