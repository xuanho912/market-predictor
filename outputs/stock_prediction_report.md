# Stock Prediction Report

Generated at: `2026-07-09T15:37:36.074282+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `TSLA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `201.36`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `24.2%`
- risk: `stock_event_risk` / `13.9%`
- stock_confluence_score: `36.58` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.9%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.38`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.5`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `196.06`
- nearest_resistance: `209.31`
- bounce_target_zone: `{"conservative": 205.33, "base": 205.33, "extended": 219.29, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 198.38, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `396.61`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.8%`
- secondary: `stock_downside_continuation` / `18.3%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `41.6` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.5%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.04`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `380.59`
- nearest_resistance: `420.66`
- bounce_target_zone: `{"conservative": 408.64, "base": 408.64, "extended": 448.89, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 387.6, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.05`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.7%`
- secondary: `stock_failed_bounce` / `25.4%`
- risk: `stock_event_risk` / `12.1%`
- stock_confluence_score: `29.98` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.1%`
- 60d_expected_return: `-3.8%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `64.5`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.17`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `8.17`
- nearest_support: `8.55`
- nearest_resistance: `10.01`
- bounce_target_zone: `{"conservative": 9.53, "base": 9.53, "extended": 12.49, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.69, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `247.77`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `24.3%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `29.26` / `weak`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.6%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `44.42`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `239.91`
- nearest_resistance: `259.56`
- bounce_target_zone: `{"conservative": 253.66, "base": 253.66, "extended": 290.63, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 243.35, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
