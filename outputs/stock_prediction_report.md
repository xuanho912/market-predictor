# Stock Prediction Report

Generated at: `2026-06-16T09:59:04.358111+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `NVDA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['fundamentals', 'earnings', 'company_news', 'single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `212.45`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `25.1%`
- risk: `stock_failed_bounce` / `25.6%`
- stock_confluence_score: `18.25` / `weak`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `41.88`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `205.71`
- nearest_resistance: `222.57`
- bounce_target_zone: `{"conservative": 217.51, "base": 217.51, "extended": 239.02, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 208.66, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `411.15`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `23.1%`
- risk: `stock_failed_bounce` / `25.5%`
- stock_confluence_score: `21.49` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `46.78`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `396.91`
- nearest_resistance: `432.51`
- bounce_target_zone: `{"conservative": 421.83, "base": 421.83, "extended": 459.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 403.14, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.64`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `23.8%`
- secondary: `stock_failed_bounce` / `22.4%`
- risk: `stock_downside_continuation` / `23.8%`
- stock_confluence_score: `13.84` / `weak`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `76.35`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.12`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `9.12`
- nearest_support: `9.69`
- nearest_resistance: `12.06`
- bounce_target_zone: `{"conservative": 11.35, "base": 11.35, "extended": 15.25, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 10.07, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `262.35`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `24.5%`
- secondary: `stock_failed_bounce` / `24.0%`
- risk: `stock_downside_continuation` / `24.5%`
- stock_confluence_score: `19.92` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `56.69`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `310.45`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `310.45`
- breakout_level: `310.45`
- breakdown_level: `240.51`
- nearest_support: `253.81`
- nearest_resistance: `275.16`
- bounce_target_zone: `{"conservative": 268.76, "base": 268.76, "extended": 318.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 257.22, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
