# Breadth Data Status

Generated at: 2026-07-10T23:45:18.149638+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 72.53
Stale data: False

## Market Internal Resonance

- resonance_score: 63.64
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: DIA
- surface_only_symbols: QQQ
- sector_score: 58.0
- equal_weight_vs_cap_weight_20d: -0.003071
- small_cap_vs_large_cap_20d: 0.008731

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-07-07
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6673 / 0.6727 / 0.664
- advancers / decliners / A-D ratio: 284 / 218 / 1.3028
- new highs/lows 20d: 97 / 29
- new highs/lows 52w: 31 / 1
- improvement / deterioration / confirmation / conflict / quality: 83.82 / 39.13 / 85.22 / 29.74 / 100.0
- internal_resonance: mixed / score 67.36 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### QQQ

- status: missing
- source: wikipedia-nasdaq100
- latest_date: 2026-07-09
- true_breadth: False
- proxy: False
- constituents used / expected: 1 / 19
- coverage_ratio: 0.0526
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.0 / 0.0 / 0.0
- advancers / decliners / A-D ratio: 1 / 0 / 1.0
- new highs/lows 20d: 0 / 0
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 70.67 / 79.57 / 65.53 / 26.11
- internal_resonance: surface_only / score 19.51 / QQQ 指数表面强但内部没充分跟上：confirmation 80，conflict 66，RSP/SPY -0.31%，IWM/SPY 0.87%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-07-07
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6333 / 0.6333 / 0.7
- advancers / decliners / A-D ratio: 18 / 12 / 1.5
- new highs/lows 20d: 6 / 1
- new highs/lows 52w: 4 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 28.27 / 97.74 / 21.48 / 100.0
- internal_resonance: aligned / score 75.12 / DIA 内部共振：成分股 20d 上方比例 63%，行业参与 70%，confirmation 98 高于 conflict 21。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-07-10
- true_breadth: False
- proxy: True
- constituents used / expected: None / None
- coverage_ratio: None
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: None / None / None
- advancers / decliners / A-D ratio: None / None / None
- new highs/lows 20d: None / None
- new highs/lows 52w: None / None
- improvement / deterioration / confirmation / conflict / quality: 51.17 / 34.15 / 54.38 / 34.61 / 64
- internal_resonance: weak / score 48.43 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
