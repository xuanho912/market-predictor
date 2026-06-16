# Stock Prediction Report

Generated at: `2026-06-16T08:19:36.388440+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `1`
- watchlist_size: `1`
- strongest_stock_symbol: `SPCX`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['fundamentals', 'earnings', 'company_news', 'single_stock_options']`

## Symbols

### SPCX

- company_name: `Space Exploration Technologies Corp`
- status: `available`
- current_price: `192.50`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.9%`
- secondary: `stock_downside_continuation` / `21.1%`
- risk: `stock_failed_bounce` / `24.9%`
- stock_confluence_score: `17.88` / `weak`
- strongest_alert: `Liquidity / Gap Risk Alert` / `EXTREME` / `90.64`
- historical_analog_support: `low sample` / samples `0`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `206.92`
- primary_invalidation_level: `149.34`
- risk_scenario_activation_level: `149.34`
- trend_repair_confirmation_level: `193.00`
- breakout_level: `206.92`
- breakdown_level: `149.34`
- nearest_support: `166.86`
- nearest_resistance: `193.00`
- bounce_target_zone: `{"conservative": 211.73, "base": 211.73, "extended": 218.64, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 178.08, "critical_warning": 149.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
