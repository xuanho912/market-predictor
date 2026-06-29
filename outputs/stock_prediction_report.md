# Stock Prediction Report

Generated at: `2026-06-29T23:38:20.763970+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `CEG`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `194.97`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_downside_continuation` / `25.3%`
- risk: `stock_event_risk` / `12.7%`
- stock_confluence_score: `35.02` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.4%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `35.2`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `187.49`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `187.49`
- nearest_support: `189.80`
- nearest_resistance: `203.13`
- bounce_target_zone: `{"conservative": 199.05, "base": 199.05, "extended": 237.72, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 191.91, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `411.84`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_downside_continuation` / `24.2%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `40.6` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.1%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `33.17`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `433.60`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `433.60`
- breakout_level: `433.60`
- breakdown_level: `368.60`
- nearest_support: `396.96`
- nearest_resistance: `433.60`
- bounce_target_zone: `{"conservative": 423.0, "base": 423.0, "extended": 448.48, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 403.47, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.26`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.5%`
- secondary: `stock_failed_bounce` / `22.8%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `29.22` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `20.4%`
- 60d_expected_return: `-3.4%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Breakdown Warning` / `NO_ALERT` / `36.83`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.12`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `9.12`
- nearest_support: `9.49`
- nearest_resistance: `11.41`
- bounce_target_zone: `{"conservative": 10.84, "base": 10.84, "extended": 15.07, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.83, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `259.32`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.8%`
- secondary: `stock_failed_bounce` / `27.3%`
- risk: `stock_event_risk` / `10.2%`
- stock_confluence_score: `27.07` / `weak`
- stock_alpha_score_v1: `18.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.1%`
- 60d_expected_return: `-1.8%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `51.79`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `240.51`
- nearest_support: `251.76`
- nearest_resistance: `270.66`
- bounce_target_zone: `{"conservative": 264.99, "base": 264.99, "extended": 290.33, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 255.07, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
