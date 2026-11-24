# Stock Prediction Report

Generated at: `2026-11-24T11:00:53.400785+00:00`
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

- company_name: `NVIDIA Corporation`
- status: `available`
- current_price: `165.05`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.0%`
- secondary: `stock_failed_bounce` / `19.7%`
- risk: `stock_event_risk` / `13.9%`
- stock_confluence_score: `39.29` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.0%`
- 60d_expected_return: `-3.7%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Liquidity / Gap Risk Alert` / `EXTREME` / `100`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `219.99`
- primary_invalidation_level: `124.50`
- risk_scenario_activation_level: `124.50`
- trend_repair_confirmation_level: `219.99`
- breakout_level: `219.99`
- breakdown_level: `124.50`
- nearest_support: `152.55`
- nearest_resistance: `183.79`
- bounce_target_zone: `{"conservative": 174.42, "base": 174.42, "extended": 232.49, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 158.02, "critical_warning": 124.5, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `385.46`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.6%`
- secondary: `stock_downside_continuation` / `17.8%`
- risk: `stock_event_risk` / `15.7%`
- stock_confluence_score: `38.14` / `weak`
- stock_alpha_score_v1: `11.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.0%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `37.98`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `367.80`
- nearest_resistance: `411.95`
- bounce_target_zone: `{"conservative": 398.71, "base": 398.71, "extended": 431.89, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 375.52, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `3.53`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `37.1%`
- secondary: `stock_failed_bounce` / `22.1%`
- risk: `stock_event_risk` / `10.8%`
- stock_confluence_score: `45.23` / `mixed`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `14.8%`
- 60d_expected_return: `-8.2%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `100`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `3.20`
- risk_scenario_activation_level: `2.98`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `2.98`
- nearest_support: `3.30`
- nearest_resistance: `4.13`
- bounce_target_zone: `{"conservative": 3.83, "base": 3.83, "extended": 6.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 3.3, "critical_warning": 3.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `251.72`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.0%`
- secondary: `stock_downside_continuation` / `19.3%`
- risk: `stock_event_risk` / `12.3%`
- stock_confluence_score: `35.5` / `weak`
- stock_alpha_score_v1: `33.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.5%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Liquidity / Gap Risk Alert` / `NO_ALERT` / `28.7`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `231.30`
- nearest_support: `239.58`
- nearest_resistance: `269.94`
- bounce_target_zone: `{"conservative": 260.83, "base": 260.83, "extended": 297.11, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 244.89, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
