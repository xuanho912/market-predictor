# Stock Prediction Report

Generated at: `2026-06-15T15:11:25.387290+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `11`
- watchlist_size: `11`
- strongest_stock_symbol: `KC`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['fundamentals', 'earnings', 'company_news', 'single_stock_options']`

## Symbols

### JD

- company_name: `JD.com Inc`
- status: `available`
- current_price: `28.75`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.8%`
- secondary: `stock_failed_bounce` / `24.1%`
- risk: `stock_downside_continuation` / `27.8%`
- stock_confluence_score: `14.34` / `weak`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `75.55`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `32.83`
- primary_invalidation_level: `27.48`
- risk_scenario_activation_level: `27.48`
- trend_repair_confirmation_level: `32.83`
- breakout_level: `32.83`
- breakdown_level: `27.48`
- nearest_support: `28.12`
- nearest_resistance: `29.68`
- bounce_target_zone: `{"conservative": 29.21, "base": 29.21, "extended": 33.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 28.37, "critical_warning": 27.48, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### KC

- company_name: `Kingsoft Cloud Holdings Ltd`
- status: `available`
- current_price: `11.28`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.2%`
- secondary: `stock_failed_bounce` / `18.2%`
- risk: `stock_downside_continuation` / `34.2%`
- stock_confluence_score: `22.21` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `62.26`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `15.25`
- primary_invalidation_level: `10.47`
- risk_scenario_activation_level: `10.47`
- trend_repair_confirmation_level: `15.25`
- breakout_level: `15.25`
- breakdown_level: `10.47`
- nearest_support: `10.74`
- nearest_resistance: `12.09`
- bounce_target_zone: `{"conservative": 11.68, "base": 11.68, "extended": 15.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 10.96, "critical_warning": 10.47, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `210.90`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `25.3%`
- risk: `stock_failed_bounce` / `25.4%`
- stock_confluence_score: `18.89` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `42.26`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `204.24`
- nearest_resistance: `220.89`
- bounce_target_zone: `{"conservative": 215.9, "base": 215.9, "extended": 238.94, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 207.15, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `408.74`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `23.4%`
- risk: `stock_failed_bounce` / `25.5%`
- stock_confluence_score: `14.94` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `48.35`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `394.50`
- nearest_resistance: `430.09`
- bounce_target_zone: `{"conservative": 419.41, "base": 419.41, "extended": 459.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 400.73, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### AMD

- company_name: `Advanced Micro Devices Inc`
- status: `available`
- current_price: `551.36`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `27.7%`
- secondary: `stock_failed_bounce` / `20.4%`
- risk: `stock_failed_bounce` / `20.4%`
- stock_confluence_score: `43.14` / `weak`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `567.38`
- primary_invalidation_level: `393.36`
- risk_scenario_activation_level: `393.36`
- trend_repair_confirmation_level: `594.04`
- breakout_level: `567.38`
- breakdown_level: `393.36`
- nearest_support: `522.90`
- nearest_resistance: `558.37`
- bounce_target_zone: `{"conservative": 572.72, "base": 594.04, "extended": 594.04, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 535.35, "critical_warning": 393.36, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### AAPL

- company_name: `Apple Inc`
- status: `available`
- current_price: `296.42`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_failed_bounce` / `26.6%`
- stock_confluence_score: `16.91` / `weak`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.16`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `317.40`
- primary_invalidation_level: `287.38`
- risk_scenario_activation_level: `287.38`
- trend_repair_confirmation_level: `317.40`
- breakout_level: `317.40`
- breakdown_level: `287.38`
- nearest_support: `290.25`
- nearest_resistance: `305.67`
- bounce_target_zone: `{"conservative": 301.04, "base": 301.04, "extended": 323.57, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 292.95, "critical_warning": 287.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### MSFT

- company_name: `Microsoft Corp`
- status: `available`
- current_price: `398.94`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `24.7%`
- risk: `stock_failed_bounce` / `25.9%`
- stock_confluence_score: `13.18` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `61.92`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `466.32`
- primary_invalidation_level: `382.27`
- risk_scenario_activation_level: `382.27`
- trend_repair_confirmation_level: `466.32`
- breakout_level: `466.32`
- breakdown_level: `382.27`
- nearest_support: `388.29`
- nearest_resistance: `414.91`
- bounce_target_zone: `{"conservative": 406.93, "base": 406.93, "extended": 476.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 392.95, "critical_warning": 382.27, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### META

- company_name: `Meta Platforms Inc`
- status: `available`
- current_price: `595.60`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `25.0%`
- risk: `stock_failed_bounce` / `25.3%`
- stock_confluence_score: `17.65` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `61.28`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `643.00`
- primary_invalidation_level: `557.01`
- risk_scenario_activation_level: `557.01`
- trend_repair_confirmation_level: `643.00`
- breakout_level: `643.00`
- breakdown_level: `557.01`
- nearest_support: `578.06`
- nearest_resistance: `621.93`
- bounce_target_zone: `{"conservative": 608.77, "base": 608.77, "extended": 660.55, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 585.73, "critical_warning": 557.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### BABA

- company_name: `Alibaba Group Holding Ltd`
- status: `available`
- current_price: `113.10`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.5%`
- secondary: `stock_failed_bounce` / `23.2%`
- risk: `stock_downside_continuation` / `28.5%`
- stock_confluence_score: `15.01` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `40.67`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `136.78`
- primary_invalidation_level: `109.66`
- risk_scenario_activation_level: `108.91`
- trend_repair_confirmation_level: `136.78`
- breakout_level: `136.78`
- breakdown_level: `108.91`
- nearest_support: `110.06`
- nearest_resistance: `117.67`
- bounce_target_zone: `{"conservative": 115.38, "base": 115.38, "extended": 139.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 111.27, "critical_warning": 109.1, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### PLTR

- company_name: `Palantir Technologies Inc`
- status: `available`
- current_price: `134.14`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.3%`
- secondary: `stock_downside_continuation` / `21.2%`
- risk: `stock_failed_bounce` / `24.3%`
- stock_confluence_score: `15.76` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `69.5`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `163.70`
- primary_invalidation_level: `126.65`
- risk_scenario_activation_level: `125.71`
- trend_repair_confirmation_level: `163.70`
- breakout_level: `163.70`
- breakdown_level: `125.71`
- nearest_support: `128.01`
- nearest_resistance: `143.33`
- bounce_target_zone: `{"conservative": 138.74, "base": 138.74, "extended": 169.83, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 130.69, "critical_warning": 126.65, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMCI

- company_name: `Super Micro Computer Inc`
- status: `available`
- current_price: `31.42`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `32.5%`
- secondary: `stock_downside_continuation` / `17.3%`
- risk: `stock_failed_bounce` / `32.5%`
- stock_confluence_score: `25.49` / `weak`
- strongest_alert: `Liquidity / Gap Risk Alert` / `HIGH_CONVICTION` / `72.47`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `51.40`
- primary_invalidation_level: `28.45`
- risk_scenario_activation_level: `26.39`
- trend_repair_confirmation_level: `51.40`
- breakout_level: `51.40`
- breakdown_level: `26.39`
- nearest_support: `28.61`
- nearest_resistance: `36.91`
- bounce_target_zone: `{"conservative": 34.17, "base": 34.17, "extended": 55.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 29.36, "critical_warning": 27.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
