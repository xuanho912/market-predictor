# Stock Prediction Report

Generated at: `2026-10-13T23:50:34.685952+00:00`
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
- current_price: `228.52`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.9%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `13.8%`
- stock_confluence_score: `48.73` / `mixed`
- stock_alpha_score_v1: `46.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.3%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.91`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `212.50`
- risk_scenario_activation_level: `212.50`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `212.50`
- nearest_support: `224.27`
- nearest_resistance: `234.89`
- bounce_target_zone: `{"conservative": 231.71, "base": 231.71, "extended": 247.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 226.13, "critical_warning": 212.5, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `375.23`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.5%`
- secondary: `stock_event_risk` / `18.1%`
- risk: `stock_downside_continuation` / `18.0%`
- stock_confluence_score: `45.35` / `mixed`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.8%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.43`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.88`
- nearest_support: `366.68`
- nearest_resistance: `388.05`
- bounce_target_zone: `{"conservative": 381.64, "base": 381.64, "extended": 397.11, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 370.1, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `6.49`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.6%`
- secondary: `stock_failed_bounce` / `26.2%`
- risk: `stock_event_risk` / `9.5%`
- stock_confluence_score: `27.43` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.0%`
- 60d_expected_return: `-3.5%`
- risk_reward_ratio: `0.28`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `76.66`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.26`
- primary_invalidation_level: `6.20`
- risk_scenario_activation_level: `6.01`
- trend_repair_confirmation_level: `9.26`
- breakout_level: `9.26`
- breakdown_level: `6.01`
- nearest_support: `6.41`
- nearest_resistance: `7.02`
- bounce_target_zone: `{"conservative": 6.75, "base": 6.75, "extended": 9.61, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 6.29, "critical_warning": 6.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `295.79`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.7%`
- secondary: `stock_trend_repair` / `21.1%`
- risk: `stock_downside_continuation` / `18.0%`
- stock_confluence_score: `48.57` / `mixed`
- stock_alpha_score_v1: `55.0` / `wait_for_confirmation`
- 20d_outperformance_probability: `68.9%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.67`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `38.43`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `283.55`
- nearest_resistance: `309.80`
- bounce_target_zone: `{"conservative": 304.97, "base": 304.97, "extended": 322.04, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 288.45, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
