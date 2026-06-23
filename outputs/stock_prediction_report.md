# Stock Prediction Report

Generated at: `2026-06-23T23:39:21.568551+00:00`
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
- current_price: `200.04`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.0%`
- secondary: `stock_downside_continuation` / `24.7%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `36.16` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.8%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.55`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `194.97`
- risk_scenario_activation_level: `191.46`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `191.46`
- nearest_support: `199.34`
- nearest_resistance: `209.40`
- bounce_target_zone: `{"conservative": 204.72, "base": 204.72, "extended": 238.52, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 196.53, "critical_warning": 194.97, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `381.61`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.4%`
- secondary: `stock_downside_continuation` / `25.5%`
- risk: `stock_event_risk` / `13.5%`
- stock_confluence_score: `30.41` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `30.1%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `59.87`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `368.95`
- risk_scenario_activation_level: `360.19`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `360.19`
- nearest_support: `379.06`
- nearest_resistance: `404.98`
- bounce_target_zone: `{"conservative": 393.29, "base": 393.29, "extended": 461.18, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 372.85, "critical_warning": 368.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.86`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `24.1%`
- secondary: `stock_failed_bounce` / `22.7%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `28.21` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `31.4%`
- 60d_expected_return: `-2.9%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `53.52`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.12`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `9.12`
- nearest_support: `9.97`
- nearest_resistance: `12.20`
- bounce_target_zone: `{"conservative": 11.53, "base": 11.53, "extended": 15.19, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 10.36, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `270.26`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.1%`
- secondary: `stock_failed_bounce` / `25.6%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `32.2` / `weak`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.0%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.38`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `50.58`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `310.45`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `310.45`
- breakout_level: `310.45`
- breakdown_level: `240.51`
- nearest_support: `262.80`
- nearest_resistance: `281.46`
- bounce_target_zone: `{"conservative": 275.86, "base": 275.86, "extended": 317.91, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 266.06, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
