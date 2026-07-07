# Stock Prediction Report

Generated at: `2026-07-07T05:10:56.591337+00:00`
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
- current_price: `195.55`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.9%`
- secondary: `stock_failed_bounce` / `25.4%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `35.9` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.5%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `40.61`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.87`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `188.58`
- trend_repair_confirmation_level: `214.87`
- breakout_level: `214.87`
- breakdown_level: `188.58`
- nearest_support: `190.48`
- nearest_resistance: `203.15`
- bounce_target_zone: `{"conservative": 199.35, "base": 199.35, "extended": 219.94, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 192.7, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `419.77`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.2%`
- secondary: `stock_downside_continuation` / `17.4%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `45.56` / `mixed`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.8%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.44`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `403.98`
- nearest_resistance: `432.86`
- bounce_target_zone: `{"conservative": 431.61, "base": 431.61, "extended": 448.65, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 410.89, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.61`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.1%`
- secondary: `stock_failed_bounce` / `21.4%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `36.19` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `20.2%`
- 60d_expected_return: `-4.0%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `45.59`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `12.24`
- primary_invalidation_level: `9.02`
- risk_scenario_activation_level: `8.61`
- trend_repair_confirmation_level: `12.24`
- breakout_level: `12.24`
- breakdown_level: `8.61`
- nearest_support: `9.12`
- nearest_resistance: `10.70`
- bounce_target_zone: `{"conservative": 10.16, "base": 10.16, "extended": 12.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.2, "critical_warning": 9.02, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `245.87`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.9%`
- secondary: `stock_failed_bounce` / `27.0%`
- risk: `stock_event_risk` / `10.3%`
- stock_confluence_score: `27.37` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.1%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `53.65`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `237.55`
- nearest_resistance: `258.35`
- bounce_target_zone: `{"conservative": 252.11, "base": 252.11, "extended": 291.09, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 241.19, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
