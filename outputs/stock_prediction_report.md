# Stock Prediction Report

Generated at: `2026-08-31T19:11:11.403088+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `CEG`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `218.79`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.2%`
- secondary: `stock_downside_continuation` / `18.1%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `48.78` / `mixed`
- stock_alpha_score_v1: `55.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `64.3%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.59`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.2`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `230.47`
- primary_invalidation_level: `196.85`
- risk_scenario_activation_level: `196.85`
- trend_repair_confirmation_level: `230.47`
- breakout_level: `230.47`
- breakdown_level: `196.85`
- nearest_support: `213.33`
- nearest_resistance: `226.98`
- bounce_target_zone: `{"conservative": 222.89, "base": 222.89, "extended": 235.93, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 215.72, "critical_warning": 196.85, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `366.02`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.6%`
- secondary: `stock_trend_repair` / `20.0%`
- risk: `stock_downside_continuation` / `17.0%`
- stock_confluence_score: `47.06` / `mixed`
- stock_alpha_score_v1: `22.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.8%`
- 60d_expected_return: `-0.2%`
- risk_reward_ratio: `0.66`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.05`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `371.87`
- primary_invalidation_level: `310.43`
- risk_scenario_activation_level: `310.43`
- trend_repair_confirmation_level: `368.54`
- breakout_level: `371.87`
- breakdown_level: `310.43`
- nearest_support: `355.64`
- nearest_resistance: `368.54`
- bounce_target_zone: `{"conservative": 373.82, "base": 373.82, "extended": 378.93, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 359.79, "critical_warning": 310.43, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.29`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.5%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `36.06` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.7%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Liquidity / Gap Risk Alert` / `NO_ALERT` / `33.81`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.29`
- risk_scenario_activation_level: `8.29`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.29`
- nearest_support: `8.73`
- nearest_resistance: `10.12`
- bounce_target_zone: `{"conservative": 9.71, "base": 9.71, "extended": 10.81, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.98, "critical_warning": 8.29, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `276.36`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `20.2%`
- risk: `stock_event_risk` / `11.7%`
- stock_confluence_score: `41.66` / `weak`
- stock_alpha_score_v1: `37.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.9%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.74`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `260.67`
- risk_scenario_activation_level: `260.67`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `260.67`
- nearest_support: `269.81`
- nearest_resistance: `286.19`
- bounce_target_zone: `{"conservative": 281.28, "base": 281.28, "extended": 293.55, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 272.67, "critical_warning": 260.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
