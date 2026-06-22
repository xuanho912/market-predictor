# Stock Prediction Report

Generated at: `2026-06-22T23:54:33.072756+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `NVDA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `208.65`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `23.8%`
- risk: `stock_event_risk` / `14.3%`
- stock_confluence_score: `37.73` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.4%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `36.32`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `202.28`
- nearest_resistance: `218.20`
- bounce_target_zone: `{"conservative": 213.43, "base": 213.43, "extended": 238.65, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 205.07, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `405.05`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.7%`
- secondary: `stock_downside_continuation` / `22.3%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `35.06` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `32.9%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `47.92`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `390.34`
- nearest_resistance: `427.11`
- bounce_target_zone: `{"conservative": 416.08, "base": 416.08, "extended": 460.31, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 396.78, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `11.24`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.1%`
- secondary: `stock_downside_continuation` / `21.1%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `34.37` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `32.9%`
- 60d_expected_return: `-2.6%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `50.34`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.12`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `9.12`
- nearest_support: `10.31`
- nearest_resistance: `12.63`
- bounce_target_zone: `{"conservative": 11.93, "base": 11.93, "extended": 15.23, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 10.72, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `275.53`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `25.3%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `33.75` / `weak`
- stock_alpha_score_v1: `22.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.9%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `43.42`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `310.45`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `310.45`
- breakout_level: `310.45`
- breakdown_level: `240.51`
- nearest_support: `267.69`
- nearest_resistance: `287.30`
- bounce_target_zone: `{"conservative": 281.41, "base": 281.41, "extended": 318.29, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 271.12, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
