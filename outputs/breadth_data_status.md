# Breadth Data Status

Generated at: 2026-07-07T21:50:52.175783+00:00

Provider available: True
True breadth available: True
True breadth symbols: SPY, QQQ, DIA
Proxy-only symbols: IWM
Average breadth quality score: 91.0
Stale data: False

## Market Internal Resonance

- resonance_score: 73.14
- resonance_state: aligned
- label: market_internal_resonance
- aligned_symbols: SPY, DIA
- surface_only_symbols: none
- sector_score: 72.0
- equal_weight_vs_cap_weight_20d: 0.019425
- small_cap_vs_large_cap_20d: 0.037849

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-07-02
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6753 / 0.6687 / 0.656
- advancers / decliners / A-D ratio: 357 / 145 / 2.4621
- new highs/lows 20d: 165 / 37
- new highs/lows 52w: 53 / 0
- improvement / deterioration / confirmation / conflict / quality: 99.77 / 25.89 / 97.76 / 19.68 / 100.0
- internal_resonance: aligned / score 77.81 / SPY 内部共振：成分股 20d 上方比例 68%，行业参与 80%，confirmation 98 高于 conflict 20。

### QQQ

- status: available
- source: wikipedia-nasdaq100
- latest_date: 2026-07-02
- true_breadth: True
- proxy: False
- constituents used / expected: 101 / 101
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5644 / 0.5545 / 0.6238
- advancers / decliners / A-D ratio: 56 / 45 / 1.2444
- new highs/lows 20d: 23 / 12
- new highs/lows 52w: 4 / 0
- improvement / deterioration / confirmation / conflict / quality: 96.87 / 34.96 / 94.95 / 26.57 / 100.0
- internal_resonance: mixed / score 74.78 / QQQ 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-07-02
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7333 / 0.6667 / 0.7333
- advancers / decliners / A-D ratio: 26 / 4 / 6.5
- new highs/lows 20d: 9 / 1
- new highs/lows 52w: 5 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 18.93 / 98.49 / 14.39 / 100.0
- internal_resonance: aligned / score 85.57 / DIA 内部共振：成分股 20d 上方比例 73%，行业参与 80%，confirmation 98 高于 conflict 14。

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
