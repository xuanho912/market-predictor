# Stock Prediction Report

Generated at: `2026-06-15T17:17:05.098924+00:00`
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
- current_price: `28.91`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.5%`
- secondary: `stock_failed_bounce` / `24.2%`
- risk: `stock_downside_continuation` / `27.5%`
- stock_confluence_score: `13.73` / `weak`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `74.22`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `32.83`
- primary_invalidation_level: `27.48`
- risk_scenario_activation_level: `27.48`
- trend_repair_confirmation_level: `32.83`
- breakout_level: `32.83`
- breakdown_level: `27.48`
- nearest_support: `28.28`
- nearest_resistance: `29.84`
- bounce_target_zone: `{"conservative": 29.37, "base": 29.37, "extended": 33.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 28.53, "critical_warning": 27.48, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### KC

- company_name: `Kingsoft Cloud Holdings Ltd`
- status: `available`
- current_price: `11.34`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.1%`
- secondary: `stock_failed_bounce` / `18.1%`
- risk: `stock_downside_continuation` / `34.1%`
- stock_confluence_score: `22.88` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `61.56`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `15.25`
- primary_invalidation_level: `10.47`
- risk_scenario_activation_level: `10.47`
- trend_repair_confirmation_level: `15.25`
- breakout_level: `15.25`
- breakdown_level: `10.47`
- nearest_support: `10.80`
- nearest_resistance: `12.14`
- bounce_target_zone: `{"conservative": 11.74, "base": 11.74, "extended": 15.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 11.01, "critical_warning": 10.47, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `212.34`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `25.1%`
- risk: `stock_failed_bounce` / `25.6%`
- stock_confluence_score: `20.18` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `40.18`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `205.60`
- nearest_resistance: `222.46`
- bounce_target_zone: `{"conservative": 217.4, "base": 217.4, "extended": 239.02, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 208.55, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `410.15`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `23.2%`
- risk: `stock_failed_bounce` / `25.4%`
- stock_confluence_score: `16.56` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `47.78`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `395.91`
- nearest_resistance: `431.51`
- bounce_target_zone: `{"conservative": 420.83, "base": 420.83, "extended": 459.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 402.14, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### AMD

- company_name: `Advanced Micro Devices Inc`
- status: `available`
- current_price: `548.80`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `27.5%`
- secondary: `stock_failed_bounce` / `20.4%`
- risk: `stock_failed_bounce` / `20.4%`
- stock_confluence_score: `44.03` / `weak`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `564.81`
- primary_invalidation_level: `393.36`
- risk_scenario_activation_level: `393.36`
- trend_repair_confirmation_level: `591.47`
- breakout_level: `564.81`
- breakdown_level: `393.36`
- nearest_support: `520.33`
- nearest_resistance: `558.37`
- bounce_target_zone: `{"conservative": 570.15, "base": 591.47, "extended": 591.47, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 532.79, "critical_warning": 393.36, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### AAPL

- company_name: `Apple Inc`
- status: `available`
- current_price: `296.82`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_failed_bounce` / `26.6%`
- stock_confluence_score: `17.54` / `weak`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `36.69`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `317.40`
- primary_invalidation_level: `287.38`
- risk_scenario_activation_level: `287.38`
- trend_repair_confirmation_level: `317.40`
- breakout_level: `317.40`
- breakdown_level: `287.38`
- nearest_support: `290.60`
- nearest_resistance: `306.14`
- bounce_target_zone: `{"conservative": 301.48, "base": 301.48, "extended": 323.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 293.32, "critical_warning": 287.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### MSFT

- company_name: `Microsoft Corp`
- status: `available`
- current_price: `399.52`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `24.6%`
- risk: `stock_failed_bounce` / `25.9%`
- stock_confluence_score: `13.65` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `62.24`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `466.32`
- primary_invalidation_level: `382.27`
- risk_scenario_activation_level: `382.27`
- trend_repair_confirmation_level: `466.32`
- breakout_level: `466.32`
- breakdown_level: `382.27`
- nearest_support: `388.75`
- nearest_resistance: `415.67`
- bounce_target_zone: `{"conservative": 407.6, "base": 407.6, "extended": 477.09, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 393.46, "critical_warning": 382.27, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### META

- company_name: `Meta Platforms Inc`
- status: `available`
- current_price: `596.05`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `24.9%`
- risk: `stock_failed_bounce` / `25.3%`
- stock_confluence_score: `18.3` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `61.89`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `643.00`
- primary_invalidation_level: `557.01`
- risk_scenario_activation_level: `557.01`
- trend_repair_confirmation_level: `643.00`
- breakout_level: `643.00`
- breakdown_level: `557.01`
- nearest_support: `578.23`
- nearest_resistance: `622.80`
- bounce_target_zone: `{"conservative": 609.43, "base": 609.43, "extended": 660.83, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 586.03, "critical_warning": 557.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### BABA

- company_name: `Alibaba Group Holding Ltd`
- status: `available`
- current_price: `113.05`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.5%`
- secondary: `stock_failed_bounce` / `23.3%`
- risk: `stock_downside_continuation` / `28.5%`
- stock_confluence_score: `15.68` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `40.75`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `136.78`
- primary_invalidation_level: `109.66`
- risk_scenario_activation_level: `108.86`
- trend_repair_confirmation_level: `136.78`
- breakout_level: `136.78`
- breakdown_level: `108.86`
- nearest_support: `110.01`
- nearest_resistance: `117.62`
- bounce_target_zone: `{"conservative": 115.33, "base": 115.33, "extended": 139.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 111.22, "critical_warning": 109.05, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### PLTR

- company_name: `Palantir Technologies Inc`
- status: `available`
- current_price: `133.97`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.3%`
- secondary: `stock_downside_continuation` / `21.2%`
- risk: `stock_failed_bounce` / `24.3%`
- stock_confluence_score: `14.08` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `70.96`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `163.70`
- primary_invalidation_level: `126.65`
- risk_scenario_activation_level: `125.50`
- trend_repair_confirmation_level: `163.70`
- breakout_level: `163.70`
- breakdown_level: `125.50`
- nearest_support: `127.81`
- nearest_resistance: `143.21`
- bounce_target_zone: `{"conservative": 138.59, "base": 138.59, "extended": 169.86, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 130.5, "critical_warning": 126.65, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMCI

- company_name: `Super Micro Computer Inc`
- status: `available`
- current_price: `31.21`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `32.5%`
- secondary: `stock_downside_continuation` / `17.4%`
- risk: `stock_failed_bounce` / `32.5%`
- stock_confluence_score: `25.38` / `weak`
- strongest_alert: `Liquidity / Gap Risk Alert` / `HIGH_CONVICTION` / `73.07`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `51.40`
- primary_invalidation_level: `28.24`
- risk_scenario_activation_level: `26.18`
- trend_repair_confirmation_level: `51.40`
- breakout_level: `51.40`
- breakdown_level: `26.18`
- nearest_support: `28.61`
- nearest_resistance: `36.70`
- bounce_target_zone: `{"conservative": 33.96, "base": 33.96, "extended": 55.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 29.15, "critical_warning": 27.09, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
