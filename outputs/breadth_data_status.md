# Breadth Data Status

Generated at: 2026-10-23T08:52:22.488463+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 55.12
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, IWM
- sector_score: 80.0
- equal_weight_vs_cap_weight_20d: 0.042055
- small_cap_vs_large_cap_20d: -0.013519

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-10-21
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6534 / 0.4462 / 0.5
- advancers / decliners / A-D ratio: 198 / 304 / 0.6513
- new highs/lows 20d: 78 / 37
- new highs/lows 52w: 12 / 4
- improvement / deterioration / confirmation / conflict / quality: 98.83 / 53.66 / 94.86 / 40.78 / 100.0
- internal_resonance: surface_only / score 58.52 / SPY 指数表面强但内部没充分跟上：confirmation 95，conflict 41，RSP/SPY 4.21%，IWM/SPY -1.35%。

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
- internal_resonance: surface_only / score 13.47 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 4.21%，IWM/SPY -1.35%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-10-20
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7333 / 0.5 / 0.6
- advancers / decliners / A-D ratio: 13 / 17 / 0.7647
- new highs/lows 20d: 8 / 2
- new highs/lows 52w: 2 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 32.39 / 97.41 / 24.61 / 100.0
- internal_resonance: mixed / score 69.59 / DIA 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-10-22
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
- improvement / deterioration / confirmation / conflict / quality: 54.28 / 59.84 / 56.71 / 53.88 / 64
- internal_resonance: surface_only / score 37.24 / IWM 指数表面强但内部没充分跟上：confirmation 57，conflict 54，RSP/SPY 4.21%，IWM/SPY -1.35%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
