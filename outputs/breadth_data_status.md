# Breadth Data Status

Generated at: 2026-07-08T04:36:07.773301+00:00

Provider available: True
True breadth available: True
True breadth symbols: SPY, QQQ, DIA
Proxy-only symbols: IWM
Average breadth quality score: 91.0
Stale data: False

## Market Internal Resonance

- resonance_score: 66.51
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: SPY, DIA
- surface_only_symbols: none
- sector_score: 72.0
- equal_weight_vs_cap_weight_20d: 0.019425
- small_cap_vs_large_cap_20d: 0.037849

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
- internal_resonance: aligned / score 70.96 / SPY 内部共振：成分股 20d 上方比例 67%，行业参与 80%，confirmation 85 高于 conflict 30。

### QQQ

- status: available
- source: wikipedia-nasdaq100
- latest_date: 2026-07-07
- true_breadth: True
- proxy: False
- constituents used / expected: 103 / 103
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5347 / 0.5248 / 0.6238
- advancers / decliners / A-D ratio: 48 / 54 / 0.8889
- new highs/lows 20d: 12 / 14
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 56.9 / 42.75 / 65.55 / 32.49 / 100.0
- internal_resonance: mixed / score 61.96 / QQQ 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

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
- internal_resonance: aligned / score 78.72 / DIA 内部共振：成分股 20d 上方比例 63%，行业参与 80%，confirmation 98 高于 conflict 21。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-07-07
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
- improvement / deterioration / confirmation / conflict / quality: 64.42 / 21.95 / 64.31 / 25.47 / 64
- internal_resonance: mixed / score 54.41 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
