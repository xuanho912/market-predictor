# Breadth Data Status

Generated at: 2026-08-17T20:51:26.091070+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 59.42
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: QQQ
- sector_score: 58.0
- equal_weight_vs_cap_weight_20d: -0.001805
- small_cap_vs_large_cap_20d: -0.001011

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-08-14
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.662 / 0.6972 / 0.7226
- advancers / decliners / A-D ratio: 250 / 245 / 1.0204
- new highs/lows 20d: 68 / 7
- new highs/lows 52w: 17 / 1
- improvement / deterioration / confirmation / conflict / quality: 74.41 / 37.0 / 78.61 / 28.12 / 100.0
- internal_resonance: mixed / score 65.51 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

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
- internal_resonance: surface_only / score 9.52 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -0.18%，IWM/SPY -0.10%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-08-14
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7 / 0.7 / 0.7667
- advancers / decliners / A-D ratio: 12 / 17 / 0.7059
- new highs/lows 20d: 4 / 0
- new highs/lows 52w: 1 / 0
- improvement / deterioration / confirmation / conflict / quality: 76.02 / 46.38 / 79.03 / 35.25 / 100.0
- internal_resonance: mixed / score 65.11 / DIA 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-17
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
- improvement / deterioration / confirmation / conflict / quality: 52.72 / 40.36 / 55.54 / 39.27 / 64
- internal_resonance: weak / score 47.64 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
