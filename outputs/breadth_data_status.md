# Breadth Data Status

Generated at: 2026-10-28T06:55:10.048194+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 63.57
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: DIA
- surface_only_symbols: QQQ
- sector_score: 76.0
- equal_weight_vs_cap_weight_20d: 0.031137
- small_cap_vs_large_cap_20d: -0.002951

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-10-26
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7072 / 0.5797 / 0.558
- advancers / decliners / A-D ratio: 153 / 349 / 0.4384
- new highs/lows 20d: 59 / 51
- new highs/lows 52w: 16 / 11
- improvement / deterioration / confirmation / conflict / quality: 93.98 / 47.74 / 91.84 / 36.28 / 100.0
- internal_resonance: mixed / score 69.05 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

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
- internal_resonance: surface_only / score 12.92 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 3.11%，IWM/SPY -0.30%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-10-26
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7667 / 0.6333 / 0.7
- advancers / decliners / A-D ratio: 11 / 19 / 0.5789
- new highs/lows 20d: 3 / 2
- new highs/lows 52w: 1 / 0
- improvement / deterioration / confirmation / conflict / quality: 98.6 / 57.02 / 94.43 / 43.33 / 100.0
- internal_resonance: aligned / score 70.9 / DIA 内部共振：成分股 20d 上方比例 77%，行业参与 80%，confirmation 94 高于 conflict 43。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-10-27
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
- improvement / deterioration / confirmation / conflict / quality: 58.56 / 50.13 / 59.92 / 46.6 / 64
- internal_resonance: mixed / score 50.77 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
