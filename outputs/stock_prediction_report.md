# Stock Prediction Report

Generated at: `2026-07-17T23:41:11.812090+00:00`
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
- current_price: `202.81`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `19.8%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `44.58` / `weak`
- stock_alpha_score_v1: `44.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.1%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.35`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `196.93`
- nearest_resistance: `211.63`
- bounce_target_zone: `{"conservative": 207.22, "base": 207.22, "extended": 219.87, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 199.5, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `380.84`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.3%`
- secondary: `stock_downside_continuation` / `22.8%`
- risk: `stock_event_risk` / `16.6%`
- stock_confluence_score: `30.91` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.9%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.62`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `360.33`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `360.33`
- nearest_support: `368.60`
- nearest_resistance: `403.22`
- bounce_target_zone: `{"conservative": 392.03, "base": 392.03, "extended": 447.78, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 372.45, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.72`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.5%`
- secondary: `stock_failed_bounce` / `23.1%`
- risk: `stock_event_risk` / `11.2%`
- stock_confluence_score: `38.73` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `16.6%`
- 60d_expected_return: `-4.3%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `69.53`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `6.96`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `6.96`
- nearest_support: `7.21`
- nearest_resistance: `8.55`
- bounce_target_zone: `{"conservative": 8.13, "base": 8.13, "extended": 12.4, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.41, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `252.39`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.0%`
- secondary: `stock_failed_bounce` / `25.3%`
- risk: `stock_event_risk` / `10.8%`
- stock_confluence_score: `27.26` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.5%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `37.98`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `244.85`
- nearest_resistance: `263.69`
- bounce_target_zone: `{"conservative": 258.04, "base": 258.04, "extended": 290.31, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 248.15, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
