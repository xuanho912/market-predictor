# Stock Prediction Report

Generated at: `2026-11-06T03:23:54.157273+00:00`
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
- current_price: `181.60`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.3%`
- secondary: `stock_failed_bounce` / `27.1%`
- risk: `stock_event_risk` / `11.0%`
- stock_confluence_score: `42.31` / `weak`
- stock_alpha_score_v1: `35.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.0%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `50.04`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `233.92`
- primary_invalidation_level: `176.75`
- risk_scenario_activation_level: `173.39`
- trend_repair_confirmation_level: `233.92`
- breakout_level: `233.92`
- breakdown_level: `173.39`
- nearest_support: `181.46`
- nearest_resistance: `190.55`
- bounce_target_zone: `{"conservative": 186.08, "base": 186.08, "extended": 239.89, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 178.24, "critical_warning": 176.75, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `343.69`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.8%`
- secondary: `stock_downside_continuation` / `21.3%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `33.92` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.5%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `27.24`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `332.23`
- risk_scenario_activation_level: `324.30`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `324.30`
- nearest_support: `338.15`
- nearest_resistance: `364.84`
- bounce_target_zone: `{"conservative": 354.27, "base": 354.27, "extended": 428.33, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 335.76, "critical_warning": 332.23, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `4.37`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.8%`
- secondary: `stock_failed_bounce` / `24.8%`
- risk: `stock_event_risk` / `12.1%`
- stock_confluence_score: `43.72` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `7.7%`
- 60d_expected_return: `-6.2%`
- risk_reward_ratio: `0.24`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `97.17`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `7.42`
- primary_invalidation_level: `4.09`
- risk_scenario_activation_level: `3.90`
- trend_repair_confirmation_level: `7.42`
- breakout_level: `7.42`
- breakdown_level: `3.90`
- nearest_support: `4.28`
- nearest_resistance: `4.88`
- bounce_target_zone: `{"conservative": 4.63, "base": 4.63, "extended": 7.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.18, "critical_warning": 4.09, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `239.65`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `26.8%`
- secondary: `stock_failed_bounce` / `26.4%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `28.95` / `weak`
- stock_alpha_score_v1: `28.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.7%`
- 60d_expected_return: `-2.4%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `43.46`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `301.77`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `226.26`
- trend_repair_confirmation_level: `301.77`
- breakout_level: `301.77`
- breakdown_level: `226.26`
- nearest_support: `231.30`
- nearest_resistance: `254.26`
- bounce_target_zone: `{"conservative": 246.95, "base": 246.95, "extended": 311.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 234.17, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
