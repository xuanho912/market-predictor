# Breadth Data Status

Generated at: 2026-07-24T06:14:43.452797+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 39.91
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 52.0
- equal_weight_vs_cap_weight_20d: 0.000583
- small_cap_vs_large_cap_20d: -0.022242

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-07-22
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4573 / 0.6208 / 0.64
- advancers / decliners / A-D ratio: 246 / 253 / 0.9723
- new highs/lows 20d: 45 / 33
- new highs/lows 52w: 15 / 6
- improvement / deterioration / confirmation / conflict / quality: 47.15 / 54.66 / 57.57 / 41.54 / 100.0
- internal_resonance: surface_only / score 40.94 / SPY 指数表面强但内部没充分跟上：confirmation 58，conflict 42，RSP/SPY 0.06%，IWM/SPY -2.22%。

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
- internal_resonance: surface_only / score 8.21 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 0.06%，IWM/SPY -2.22%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-07-22
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5667 / 0.6 / 0.6333
- advancers / decliners / A-D ratio: 14 / 15 / 0.9333
- new highs/lows 20d: 4 / 3
- new highs/lows 52w: 2 / 2
- improvement / deterioration / confirmation / conflict / quality: 77.04 / 40.95 / 80.19 / 31.12 / 100.0
- internal_resonance: surface_only / score 49.9 / DIA 指数表面强但内部没充分跟上：confirmation 80，conflict 31，RSP/SPY 0.06%，IWM/SPY -2.22%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-07-23
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
- improvement / deterioration / confirmation / conflict / quality: 39.36 / 62.77 / 45.52 / 56.08 / 64
- internal_resonance: surface_only / score 28.9 / IWM 指数表面强但内部没充分跟上：confirmation 46，conflict 56，RSP/SPY 0.06%，IWM/SPY -2.22%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
