# Breadth Data Status

Generated at: 2026-11-11T01:28:48.544659+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 56.97
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: DIA
- sector_score: 76.0
- equal_weight_vs_cap_weight_20d: 0.071642
- small_cap_vs_large_cap_20d: 0.050127

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-11-09
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6083 / 0.6215 / 0.562
- advancers / decliners / A-D ratio: 209 / 293 / 0.7133
- new highs/lows 20d: 32 / 43
- new highs/lows 52w: 9 / 3
- improvement / deterioration / confirmation / conflict / quality: 54.7 / 63.4 / 62.31 / 48.18 / 100.0
- internal_resonance: mixed / score 61.01 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

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
- internal_resonance: weak / score 27.93 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-11-09
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7 / 0.7333 / 0.6333
- advancers / decliners / A-D ratio: 14 / 16 / 0.875
- new highs/lows 20d: 3 / 4
- new highs/lows 52w: 1 / 0
- improvement / deterioration / confirmation / conflict / quality: 48.66 / 56.74 / 58.49 / 52.12 / 100.0
- internal_resonance: surface_only / score 49.97 / DIA 指数表面强但内部没充分跟上：confirmation 58，conflict 52，RSP/SPY 7.16%，IWM/SPY 5.01%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-11-10
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
- improvement / deterioration / confirmation / conflict / quality: 81.15 / 26.44 / 76.86 / 28.83 / 64
- internal_resonance: mixed / score 59.93 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
