# Stock Prediction Report

Generated at: `2026-07-22T14:25:10.108413+00:00`
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
- current_price: `206.77`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.6%`
- secondary: `stock_downside_continuation` / `19.2%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `48.04` / `mixed`
- stock_alpha_score_v1: `46.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `60.1%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.55`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.81`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.81`
- breakout_level: `213.81`
- breakdown_level: `189.80`
- nearest_support: `201.15`
- nearest_resistance: `213.81`
- bounce_target_zone: `{"conservative": 210.98, "base": 210.98, "extended": 219.43, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 203.61, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `377.58`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `19.4%`
- risk: `stock_event_risk` / `17.3%`
- stock_confluence_score: `32.47` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.9%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `36.06`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `366.87`
- risk_scenario_activation_level: `359.45`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `359.45`
- nearest_support: `368.60`
- nearest_resistance: `397.36`
- bounce_target_zone: `{"conservative": 387.47, "base": 387.47, "extended": 446.04, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 370.16, "critical_warning": 366.87, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.70`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.0%`
- secondary: `stock_failed_bounce` / `19.8%`
- risk: `stock_event_risk` / `12.6%`
- stock_confluence_score: `32.93` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.1%`
- 60d_expected_return: `-3.3%`
- risk_reward_ratio: `0.38`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `48.89`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `8.17`
- nearest_resistance: `9.51`
- bounce_target_zone: `{"conservative": 9.11, "base": 9.11, "extended": 11.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.4, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `271.86`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_downside_continuation` / `23.0%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `36.22` / `weak`
- stock_alpha_score_v1: `27.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.9%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.61`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `275.81`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `275.81`
- breakout_level: `275.81`
- breakdown_level: `228.63`
- nearest_support: `265.37`
- nearest_resistance: `275.81`
- bounce_target_zone: `{"conservative": 276.73, "base": 276.73, "extended": 282.31, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 268.21, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
