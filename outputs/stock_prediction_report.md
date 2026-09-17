# Stock Prediction Report

Generated at: `2026-09-17T00:58:54.388983+00:00`
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
- current_price: `213.90`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.4%`
- secondary: `stock_downside_continuation` / `19.3%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `46.49` / `mixed`
- stock_alpha_score_v1: `37.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.3%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `36.24`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `205.60`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `205.60`
- nearest_support: `207.86`
- nearest_resistance: `222.96`
- bounce_target_zone: `{"conservative": 218.43, "base": 218.43, "extended": 240.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 210.5, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `358.08`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `18.1%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `45.43` / `mixed`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.7%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.81`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `335.70`
- risk_scenario_activation_level: `335.70`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `335.70`
- nearest_support: `346.84`
- nearest_resistance: `374.93`
- bounce_target_zone: `{"conservative": 366.51, "base": 366.51, "extended": 395.28, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 351.76, "critical_warning": 335.7, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.30`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `31.4%`
- secondary: `stock_downside_continuation` / `21.6%`
- risk: `stock_event_risk` / `11.6%`
- stock_confluence_score: `34.52` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.8%`
- 60d_expected_return: `-3.0%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.74`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.86`
- risk_scenario_activation_level: `7.55`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.55`
- nearest_support: `8.04`
- nearest_resistance: `9.12`
- bounce_target_zone: `{"conservative": 8.71, "base": 8.71, "extended": 11.92, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.99, "critical_warning": 7.86, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `259.53`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `30.3%`
- secondary: `stock_downside_continuation` / `21.6%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `35.71` / `weak`
- stock_alpha_score_v1: `25.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.2%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `41.66`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `252.77`
- risk_scenario_activation_level: `248.10`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `248.10`
- nearest_support: `254.71`
- nearest_resistance: `272.00`
- bounce_target_zone: `{"conservative": 265.77, "base": 265.77, "extended": 314.11, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 254.85, "critical_warning": 252.77, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
