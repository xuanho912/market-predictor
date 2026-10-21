# Stock Prediction Report

Generated at: `2026-10-21T06:06:05.779520+00:00`
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
- current_price: `216.47`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.4%`
- secondary: `stock_downside_continuation` / `21.7%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `41.28` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.3%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.43`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `212.71`
- risk_scenario_activation_level: `210.11`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `210.11`
- nearest_support: `212.77`
- nearest_resistance: `223.40`
- bounce_target_zone: `{"conservative": 219.94, "base": 219.94, "extended": 247.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 213.87, "critical_warning": 212.71, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `373.71`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `17.8%`
- risk: `stock_event_risk` / `17.4%`
- stock_confluence_score: `35.0` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.1%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.11`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.88`
- nearest_support: `364.30`
- nearest_resistance: `387.82`
- bounce_target_zone: `{"conservative": 380.77, "base": 380.77, "extended": 397.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 368.42, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.58`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.6%`
- secondary: `stock_failed_bounce` / `22.1%`
- risk: `stock_event_risk` / `12.5%`
- stock_confluence_score: `43.68` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `11.4%`
- 60d_expected_return: `-5.0%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `83.18`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.90`
- primary_invalidation_level: `5.27`
- risk_scenario_activation_level: `5.05`
- trend_repair_confirmation_level: `8.90`
- breakout_level: `8.90`
- breakdown_level: `5.05`
- nearest_support: `5.33`
- nearest_resistance: `6.16`
- bounce_target_zone: `{"conservative": 5.87, "base": 5.87, "extended": 9.29, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.36, "critical_warning": 5.27, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `258.84`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `29.7%`
- secondary: `stock_downside_continuation` / `21.1%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `31.33` / `weak`
- stock_alpha_score_v1: `19.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.6%`
- 60d_expected_return: `-2.5%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.25`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `240.91`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `240.91`
- nearest_support: `247.20`
- nearest_resistance: `278.40`
- bounce_target_zone: `{"conservative": 268.62, "base": 268.62, "extended": 322.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 251.51, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
