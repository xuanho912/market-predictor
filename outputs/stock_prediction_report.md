# Stock Prediction Report

Generated at: `2026-07-09T00:21:49.395486+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `SMR`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `204.12`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.0%`
- secondary: `stock_downside_continuation` / `23.3%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `40.44` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.2%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.4`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.95`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `198.79`
- nearest_resistance: `212.12`
- bounce_target_zone: `{"conservative": 208.12, "base": 208.12, "extended": 219.32, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 201.12, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `394.06`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.9%`
- secondary: `stock_downside_continuation` / `22.9%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `32.25` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.6%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.27`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `377.77`
- nearest_resistance: `418.50`
- bounce_target_zone: `{"conservative": 406.28, "base": 406.28, "extended": 449.15, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 384.9, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.76`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.3%`
- secondary: `stock_failed_bounce` / `23.4%`
- risk: `stock_event_risk` / `12.4%`
- stock_confluence_score: `33.86` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `20.5%`
- 60d_expected_return: `-4.1%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `56.84`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `8.21`
- risk_scenario_activation_level: `7.83`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `7.83`
- nearest_support: `8.55`
- nearest_resistance: `9.78`
- bounce_target_zone: `{"conservative": 9.27, "base": 9.27, "extended": 12.53, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.38, "critical_warning": 8.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `244.52`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `24.9%`
- risk: `stock_event_risk` / `13.5%`
- stock_confluence_score: `27.16` / `weak`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.6%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `44.54`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `236.54`
- nearest_resistance: `256.48`
- bounce_target_zone: `{"conservative": 250.5, "base": 250.5, "extended": 290.75, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 240.03, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
