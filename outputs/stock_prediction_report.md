# Stock Prediction Report

Generated at: `2026-08-02T13:57:58.856916+00:00`
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
- current_price: `200.75`
- market_context: `market_tailwind`
- primary: `stock_bounce` / `26.3%`
- secondary: `stock_trend_repair` / `19.9%`
- risk: `stock_failed_bounce` / `13.9%`
- stock_confluence_score: `60.37` / `moderate`
- stock_alpha_score_v1: `68.0` / `watchlist_candidate`
- 20d_outperformance_probability: `70.4%`
- 60d_expected_return: `1.3%`
- risk_reward_ratio: `0.95`
- strongest_alert: `Stock Bounce Setup` / `NO_ALERT` / `29.37`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `190.01`
- nearest_support: `194.64`
- nearest_resistance: `209.92`
- bounce_target_zone: `{"conservative": 205.95, "base": 210.31, "extended": 220.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 197.31, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `311.21`
- market_context: `market_tailwind`
- primary: `stock_bounce` / `30.6%`
- secondary: `stock_downside_continuation` / `27.8%`
- risk: `stock_event_risk` / `10.1%`
- stock_confluence_score: `32.32` / `weak`
- stock_alpha_score_v1: `6.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `26.6%`
- 60d_expected_return: `0.2%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `53.33`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `420.00`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `293.78`
- trend_repair_confirmation_level: `420.00`
- breakout_level: `420.00`
- breakdown_level: `293.78`
- nearest_support: `298.53`
- nearest_resistance: `330.22`
- bounce_target_zone: `{"conservative": 321.98, "base": 331.01, "extended": 432.68, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 304.08, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.42`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.0%`
- secondary: `stock_failed_bounce` / `22.4%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `29.79` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `28.7%`
- 60d_expected_return: `-3.9%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `79.62`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.12`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.12`
- breakout_level: `10.12`
- breakdown_level: `7.21`
- nearest_support: `7.87`
- nearest_resistance: `9.24`
- bounce_target_zone: `{"conservative": 8.83, "base": 8.83, "extended": 10.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.11, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `262.75`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `18.3%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `42.88` / `weak`
- stock_alpha_score_v1: `30.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.8%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.36`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `236.56`
- risk_scenario_activation_level: `236.56`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `236.56`
- nearest_support: `255.20`
- nearest_resistance: `274.07`
- bounce_target_zone: `{"conservative": 268.41, "base": 268.41, "extended": 287.15, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 258.5, "critical_warning": 236.56, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
