# Breadth Data Status

Generated at: 2026-11-01T17:58:41.950024+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 68.53
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: SPY, DIA
- surface_only_symbols: none
- sector_score: 84.0
- equal_weight_vs_cap_weight_20d: 0.058996
- small_cap_vs_large_cap_20d: 0.010307

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-10-30
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7276 / 0.5857 / 0.576
- advancers / decliners / A-D ratio: 217 / 285 / 0.7614
- new highs/lows 20d: 73 / 35
- new highs/lows 52w: 12 / 5
- improvement / deterioration / confirmation / conflict / quality: 97.78 / 39.15 / 95.27 / 29.75 / 100.0
- internal_resonance: aligned / score 73.97 / SPY 内部共振：成分股 20d 上方比例 73%，行业参与 80%，confirmation 95 高于 conflict 30。

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
- internal_resonance: weak / score 27.37 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-10-30
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7333 / 0.6333 / 0.6333
- advancers / decliners / A-D ratio: 9 / 21 / 0.4286
- new highs/lows 20d: 6 / 3
- new highs/lows 52w: 1 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 31.6 / 97.47 / 24.02 / 100.0
- internal_resonance: aligned / score 76.49 / DIA 内部共振：成分股 20d 上方比例 73%，行业参与 80%，confirmation 97 高于 conflict 24。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-10-30
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
- improvement / deterioration / confirmation / conflict / quality: 67.47 / 47.82 / 66.6 / 44.87 / 64
- internal_resonance: mixed / score 55.14 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
