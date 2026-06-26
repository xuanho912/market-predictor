# Stock Prediction Report

Generated at: `2026-06-26T23:46:26.735738+00:00`
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
- current_price: `192.53`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.9%`
- secondary: `stock_downside_continuation` / `26.2%`
- risk: `stock_event_risk` / `12.3%`
- stock_confluence_score: `34.76` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.1%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `35.1`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `188.16`
- risk_scenario_activation_level: `185.13`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `185.13`
- nearest_support: `191.22`
- nearest_resistance: `200.60`
- bounce_target_zone: `{"conservative": 196.57, "base": 196.57, "extended": 237.66, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 189.5, "critical_warning": 188.16, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `379.71`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.4%`
- secondary: `stock_failed_bounce` / `26.2%`
- risk: `stock_event_risk` / `13.2%`
- stock_confluence_score: `31.16` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `29.9%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `58.45`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `441.07`
- primary_invalidation_level: `368.18`
- risk_scenario_activation_level: `360.20`
- trend_repair_confirmation_level: `441.07`
- breakout_level: `441.07`
- breakdown_level: `360.20`
- nearest_support: `368.60`
- nearest_resistance: `401.00`
- bounce_target_zone: `{"conservative": 390.35, "base": 390.35, "extended": 455.26, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 371.73, "critical_warning": 368.18, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.10`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.6%`
- secondary: `stock_failed_bounce` / `24.9%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `25.57` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.1%`
- 60d_expected_return: `-3.6%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `39.04`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.06`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `9.06`
- nearest_support: `9.34`
- nearest_resistance: `11.24`
- bounce_target_zone: `{"conservative": 10.67, "base": 10.67, "extended": 15.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.67, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `264.02`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `26.1%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `27.98` / `weak`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.7%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `37.92`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `290.90`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `290.90`
- breakout_level: `290.90`
- breakdown_level: `240.51`
- nearest_support: `256.72`
- nearest_resistance: `274.97`
- bounce_target_zone: `{"conservative": 269.49, "base": 269.49, "extended": 298.2, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 259.92, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
