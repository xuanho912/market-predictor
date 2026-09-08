# Breadth Data Status

Generated at: 2026-09-08T16:41:09.685453+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 49.7
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: QQQ
- sector_score: 34.0
- equal_weight_vs_cap_weight_20d: -0.00531
- small_cap_vs_large_cap_20d: -0.007554

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-09-04
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3539 / 0.4692 / 0.6367
- advancers / decliners / A-D ratio: 175 / 327 / 0.5352
- new highs/lows 20d: 21 / 55
- new highs/lows 52w: 7 / 6
- improvement / deterioration / confirmation / conflict / quality: 35.72 / 80.92 / 47.24 / 61.5 / 100.0
- internal_resonance: weak / score 40.97 / SPY 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### QQQ

- status: missing
- source: wikipedia-nasdaq100
- latest_date: None
- true_breadth: False
- proxy: False
- constituents used / expected: 0 / 6
- coverage_ratio: 0.0
- stale_constituents: False
- stale_price_data: True
- percent_above_20d / 50d / 200d: None / None / None
- advancers / decliners / A-D ratio: 0 / 0 / 0.0
- new highs/lows 20d: 0 / 0
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 8.67 / 70.67 / 9.39 / 69.07 / 4.0
- internal_resonance: surface_only / score 6.49 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -0.53%，IWM/SPY -0.76%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-09-04
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5333 / 0.5 / 0.6667
- advancers / decliners / A-D ratio: 10 / 20 / 0.5
- new highs/lows 20d: 1 / 1
- new highs/lows 52w: 0 / 1
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 45.8 / 96.34 / 34.8 / 100.0
- internal_resonance: mixed / score 66.68 / DIA 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-08
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
- improvement / deterioration / confirmation / conflict / quality: 47.63 / 56.86 / 51.72 / 51.65 / 64
- internal_resonance: weak / score 41.46 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
