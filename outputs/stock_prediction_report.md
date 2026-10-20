# Stock Prediction Report

Generated at: `2026-10-20T08:54:22.309268+00:00`
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
- current_price: `217.09`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `21.5%`
- risk: `stock_event_risk` / `13.8%`
- stock_confluence_score: `41.65` / `weak`
- stock_alpha_score_v1: `36.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.5%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.04`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `212.85`
- risk_scenario_activation_level: `210.78`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `210.78`
- nearest_support: `212.85`
- nearest_resistance: `223.98`
- bounce_target_zone: `{"conservative": 220.53, "base": 220.53, "extended": 247.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.51, "critical_warning": 212.85, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `368.06`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `17.2%`
- stock_confluence_score: `38.77` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.1%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.14`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.88`
- nearest_support: `358.91`
- nearest_resistance: `381.78`
- bounce_target_zone: `{"conservative": 374.92, "base": 374.92, "extended": 397.71, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 362.92, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.69`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `36.4%`
- secondary: `stock_failed_bounce` / `22.0%`
- risk: `stock_event_risk` / `10.4%`
- stock_confluence_score: `39.47` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `13.8%`
- 60d_expected_return: `-4.8%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `82.32`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.02`
- primary_invalidation_level: `5.37`
- risk_scenario_activation_level: `5.16`
- trend_repair_confirmation_level: `9.02`
- breakout_level: `9.02`
- breakdown_level: `5.16`
- nearest_support: `5.44`
- nearest_resistance: `6.27`
- bounce_target_zone: `{"conservative": 5.98, "base": 5.98, "extended": 9.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.47, "critical_warning": 5.37, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `263.19`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `28.2%`
- secondary: `stock_downside_continuation` / `17.8%`
- risk: `stock_event_risk` / `15.5%`
- stock_confluence_score: `38.32` / `weak`
- stock_alpha_score_v1: `23.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.3%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.56`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `244.38`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `244.38`
- nearest_support: `249.51`
- nearest_resistance: `283.71`
- bounce_target_zone: `{"conservative": 273.45, "base": 273.45, "extended": 323.48, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 255.5, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
