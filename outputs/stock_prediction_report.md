# Stock Prediction Report

Generated at: `2026-07-16T23:46:29.931662+00:00`
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
- current_price: `207.40`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `46.0` / `mixed`
- stock_alpha_score_v1: `44.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.4%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.45`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `201.80`
- nearest_resistance: `213.99`
- bounce_target_zone: `{"conservative": 211.6, "base": 211.6, "extended": 219.59, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 204.25, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `391.06`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_downside_continuation` / `22.3%`
- risk: `stock_event_risk` / `17.1%`
- stock_confluence_score: `34.62` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.9%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.62`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `375.84`
- nearest_resistance: `413.90`
- bounce_target_zone: `{"conservative": 402.48, "base": 402.48, "extended": 448.08, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 382.5, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.64`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.0%`
- secondary: `stock_failed_bounce` / `23.5%`
- risk: `stock_event_risk` / `11.3%`
- stock_confluence_score: `38.96` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.8%`
- 60d_expected_return: `-4.3%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `71.52`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `7.20`
- risk_scenario_activation_level: `6.89`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `6.89`
- nearest_support: `7.52`
- nearest_resistance: `8.45`
- bounce_target_zone: `{"conservative": 8.05, "base": 8.05, "extended": 12.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.33, "critical_warning": 7.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `251.77`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.9%`
- secondary: `stock_failed_bounce` / `25.8%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `27.73` / `weak`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.3%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `44.05`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `244.24`
- nearest_resistance: `263.06`
- bounce_target_zone: `{"conservative": 257.41, "base": 257.41, "extended": 290.3, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 247.54, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
