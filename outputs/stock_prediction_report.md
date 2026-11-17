# Stock Prediction Report

Generated at: `2026-11-17T20:58:42.852038+00:00`
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
- current_price: `154.93`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.7%`
- secondary: `stock_failed_bounce` / `21.8%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `43.08` / `weak`
- stock_alpha_score_v1: `30.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `34.4%`
- 60d_expected_return: `-3.7%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `67.34`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `222.19`
- primary_invalidation_level: `147.46`
- risk_scenario_activation_level: `142.29`
- trend_repair_confirmation_level: `222.19`
- breakout_level: `222.19`
- breakdown_level: `142.29`
- nearest_support: `148.80`
- nearest_resistance: `168.73`
- bounce_target_zone: `{"conservative": 161.83, "base": 161.83, "extended": 231.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 149.76, "critical_warning": 147.46, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `379.51`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.6%`
- secondary: `stock_downside_continuation` / `17.0%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `41.96` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.8%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `41.53`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `365.39`
- nearest_resistance: `400.69`
- bounce_target_zone: `{"conservative": 390.1, "base": 390.1, "extended": 428.35, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 371.57, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `4.09`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.0%`
- secondary: `stock_failed_bounce` / `24.3%`
- risk: `stock_event_risk` / `11.0%`
- stock_confluence_score: `44.23` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.7%`
- 60d_expected_return: `-6.7%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `91.41`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `3.77`
- risk_scenario_activation_level: `3.55`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `3.55`
- nearest_support: `4.03`
- nearest_resistance: `4.69`
- bounce_target_zone: `{"conservative": 4.39, "base": 4.39, "extended": 6.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 3.87, "critical_warning": 3.77, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `268.11`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.0%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `43.49` / `weak`
- stock_alpha_score_v1: `41.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.4%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.5`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `231.30`
- nearest_support: `257.26`
- nearest_resistance: `284.38`
- bounce_target_zone: `{"conservative": 276.24, "base": 276.24, "extended": 295.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 262.01, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
