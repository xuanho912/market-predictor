# Stock Prediction Report

Generated at: `2026-10-15T05:58:26.988372+00:00`
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
- current_price: `221.30`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `28.9%`
- secondary: `stock_downside_continuation` / `18.1%`
- risk: `stock_event_risk` / `13.8%`
- stock_confluence_score: `50.48` / `mixed`
- stock_alpha_score_v1: `43.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.4%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.0`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `217.15`
- risk_scenario_activation_level: `215.11`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `215.11`
- nearest_support: `217.15`
- nearest_resistance: `228.05`
- bounce_target_zone: `{"conservative": 224.68, "base": 224.68, "extended": 247.87, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 218.77, "critical_warning": 217.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `367.16`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_event_risk` / `17.8%`
- risk: `stock_downside_continuation` / `17.6%`
- stock_confluence_score: `47.02` / `mixed`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.3%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.26`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.88`
- nearest_support: `358.40`
- nearest_resistance: `380.31`
- bounce_target_zone: `{"conservative": 373.73, "base": 373.73, "extended": 397.32, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 361.91, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.83`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.8%`
- secondary: `stock_failed_bounce` / `25.5%`
- risk: `stock_event_risk` / `10.0%`
- stock_confluence_score: `39.5` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `17.7%`
- 60d_expected_return: `-4.5%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `80.86`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.26`
- primary_invalidation_level: `5.52`
- risk_scenario_activation_level: `5.31`
- trend_repair_confirmation_level: `9.26`
- breakout_level: `9.26`
- breakdown_level: `5.31`
- nearest_support: `5.72`
- nearest_resistance: `6.39`
- bounce_target_zone: `{"conservative": 6.11, "base": 6.11, "extended": 9.63, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.62, "critical_warning": 5.52, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `279.54`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.4%`
- secondary: `stock_downside_continuation` / `16.9%`
- risk: `stock_event_risk` / `15.7%`
- stock_confluence_score: `47.24` / `mixed`
- stock_alpha_score_v1: `42.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.3%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.94`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `266.58`
- nearest_resistance: `298.98`
- bounce_target_zone: `{"conservative": 289.26, "base": 289.26, "extended": 322.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 272.25, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
