# Breadth Data Status

Generated at: 2026-06-14T16:43:15.699532+00:00

Provider available: True
True breadth available: True
True breadth symbols: SPY, QQQ, DIA
Proxy-only symbols: IWM
Average breadth quality score: 91.0
Stale data: False

## Market Internal Resonance

- resonance_score: 73.05
- resonance_state: aligned
- label: market_internal_resonance
- aligned_symbols: SPY, DIA
- surface_only_symbols: none
- sector_score: 84.0
- equal_weight_vs_cap_weight_20d: 0.047813
- small_cap_vs_large_cap_20d: 0.038463

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-06-12
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7112 / 0.6036 / 0.6088
- advancers / decliners / A-D ratio: 397 / 106 / 3.7453
- new highs/lows 20d: 126 / 14
- new highs/lows 52w: 38 / 6
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 21.41 / 98.29 / 16.27 / 100.0
- internal_resonance: aligned / score 83.12 / SPY 内部共振：成分股 20d 上方比例 71%，行业参与 80%，confirmation 98 高于 conflict 16。

### QQQ

- status: available
- source: wikipedia-nasdaq100
- latest_date: 2026-06-12
- true_breadth: True
- proxy: False
- constituents used / expected: 101 / 101
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5446 / 0.5149 / 0.5842
- advancers / decliners / A-D ratio: 70 / 31 / 2.2581
- new highs/lows 20d: 13 / 9
- new highs/lows 52w: 9 / 5
- improvement / deterioration / confirmation / conflict / quality: 75.38 / 40.08 / 79.07 / 30.46 / 100.0
- internal_resonance: mixed / score 70.77 / QQQ 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-06-12
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6333 / 0.6667 / 0.6667
- advancers / decliners / A-D ratio: 21 / 9 / 2.3333
- new highs/lows 20d: 9 / 1
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 89.83 / 24.42 / 90.72 / 18.56 / 100.0
- internal_resonance: aligned / score 78.09 / DIA 内部共振：成分股 20d 上方比例 63%，行业参与 80%，confirmation 91 高于 conflict 19。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-06-12
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
- improvement / deterioration / confirmation / conflict / quality: 82.1 / 27.14 / 77.57 / 29.36 / 64
- internal_resonance: mixed / score 60.21 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
