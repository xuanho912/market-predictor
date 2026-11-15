# Breadth Data Status

Generated at: 2026-11-15T18:53:36.054269+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 69.13
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: SPY, DIA
- surface_only_symbols: QQQ
- sector_score: 82.0
- equal_weight_vs_cap_weight_20d: 0.044658
- small_cap_vs_large_cap_20d: 0.037888

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-11-13
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7157 / 0.7191 / 0.63
- advancers / decliners / A-D ratio: 311 / 188 / 1.6543
- new highs/lows 20d: 67 / 5
- new highs/lows 52w: 25 / 3
- improvement / deterioration / confirmation / conflict / quality: 88.24 / 29.54 / 89.17 / 22.45 / 100.0
- internal_resonance: aligned / score 74.99 / SPY 内部共振：成分股 20d 上方比例 72%，行业参与 70%，confirmation 89 高于 conflict 22。

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
- internal_resonance: surface_only / score 15.65 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 4.47%，IWM/SPY 3.79%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-11-13
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7 / 0.8 / 0.6667
- advancers / decliners / A-D ratio: 16 / 14 / 1.1429
- new highs/lows 20d: 3 / 1
- new highs/lows 52w: 3 / 1
- improvement / deterioration / confirmation / conflict / quality: 86.58 / 25.72 / 88.28 / 19.55 / 100.0
- internal_resonance: aligned / score 73.87 / DIA 内部共振：成分股 20d 上方比例 70%，行业参与 70%，confirmation 88 高于 conflict 20。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-11-13
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
- improvement / deterioration / confirmation / conflict / quality: 74.83 / 28.28 / 72.13 / 30.21 / 64
- internal_resonance: mixed / score 58.52 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
