# Stock Prediction Report

Generated at: `2026-09-30T06:49:14.388756+00:00`
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
- current_price: `227.21`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `14.3%`
- stock_confluence_score: `48.01` / `mixed`
- stock_alpha_score_v1: `48.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.4%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.88`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `222.90`
- nearest_resistance: `233.68`
- bounce_target_zone: `{"conservative": 230.44, "base": 230.44, "extended": 239.07, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 224.78, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `352.84`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `30.0%`
- secondary: `stock_downside_continuation` / `22.5%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `31.29` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `33.8%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `46.3`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.69`
- risk_scenario_activation_level: `340.74`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `340.74`
- nearest_support: `349.92`
- nearest_resistance: `366.03`
- bounce_target_zone: `{"conservative": 359.44, "base": 359.44, "extended": 395.63, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 347.89, "critical_warning": 345.69, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.76`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `28.5%`
- secondary: `stock_failed_bounce` / `25.6%`
- risk: `stock_event_risk` / `11.3%`
- stock_confluence_score: `30.74` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `29.0%`
- 60d_expected_return: `-3.6%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `50.43`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.34`
- risk_scenario_activation_level: `7.05`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.05`
- nearest_support: `7.75`
- nearest_resistance: `8.53`
- bounce_target_zone: `{"conservative": 8.15, "base": 8.15, "extended": 11.89, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.47, "critical_warning": 7.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `264.58`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.1%`
- secondary: `stock_downside_continuation` / `22.7%`
- risk: `stock_event_risk` / `11.4%`
- stock_confluence_score: `39.09` / `weak`
- stock_alpha_score_v1: `30.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.3%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.41`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `250.55`
- risk_scenario_activation_level: `250.55`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `250.55`
- nearest_support: `257.39`
- nearest_resistance: `275.36`
- bounce_target_zone: `{"conservative": 269.97, "base": 269.97, "extended": 312.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 260.54, "critical_warning": 250.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
