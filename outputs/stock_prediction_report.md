# Stock Prediction Report

Generated at: `2026-09-03T23:35:53.740165+00:00`
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
- current_price: `228.45`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `50.96` / `mixed`
- stock_alpha_score_v1: `55.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `63.3%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.73`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `231.77`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `230.47`
- breakout_level: `231.77`
- breakdown_level: `207.25`
- nearest_support: `222.54`
- nearest_resistance: `230.47`
- bounce_target_zone: `{"conservative": 232.88, "base": 232.88, "extended": 236.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 225.13, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla`
- status: `available`
- current_price: `376.36`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `23.1%`
- secondary: `stock_trend_repair` / `21.6%`
- risk: `stock_downside_continuation` / `16.6%`
- stock_confluence_score: `48.59` / `mixed`
- stock_alpha_score_v1: `23.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.3%`
- 60d_expected_return: `-0.1%`
- risk_reward_ratio: `0.71`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `30.6`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `321.25`
- risk_scenario_activation_level: `321.25`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `321.25`
- nearest_support: `365.07`
- nearest_resistance: `384.04`
- bounce_target_zone: `{"conservative": 384.84, "base": 384.84, "extended": 395.33, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 369.59, "critical_warning": 321.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.75`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.0%`
- secondary: `stock_downside_continuation` / `19.8%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `35.79` / `weak`
- stock_alpha_score_v1: `6.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.6%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.46`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.53`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.53`
- nearest_support: `9.24`
- nearest_resistance: `10.26`
- bounce_target_zone: `{"conservative": 10.13, "base": 10.13, "extended": 10.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.47, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `285.05`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `22.9%`
- secondary: `stock_trend_repair` / `20.2%`
- risk: `stock_downside_continuation` / `18.1%`
- stock_confluence_score: `47.8` / `mixed`
- stock_alpha_score_v1: `53.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `66.3%`
- 60d_expected_return: `-0.1%`
- risk_reward_ratio: `0.72`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `26.95`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `296.62`
- primary_invalidation_level: `261.37`
- risk_scenario_activation_level: `261.37`
- trend_repair_confirmation_level: `296.62`
- breakout_level: `296.62`
- breakdown_level: `261.37`
- nearest_support: `277.53`
- nearest_resistance: `296.33`
- bounce_target_zone: `{"conservative": 290.69, "base": 290.69, "extended": 304.14, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 280.53, "critical_warning": 261.37, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
