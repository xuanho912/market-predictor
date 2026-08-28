# Breadth Data Status

Generated at: 2026-08-28T22:23:09.415579+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 31.3
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 38.0
- equal_weight_vs_cap_weight_20d: -0.003461
- small_cap_vs_large_cap_20d: -0.014253

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-08-26
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5308 / 0.5896 / 0.7186
- advancers / decliners / A-D ratio: 303 / 197 / 1.5381
- new highs/lows 20d: 73 / 28
- new highs/lows 52w: 17 / 4
- improvement / deterioration / confirmation / conflict / quality: 36.13 / 70.07 / 48.41 / 62.26 / 100.0
- internal_resonance: surface_only / score 35.73 / SPY 指数表面强但内部没充分跟上：confirmation 48，conflict 62，RSP/SPY -0.35%，IWM/SPY -1.43%。

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
- internal_resonance: surface_only / score 6.77 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -0.35%，IWM/SPY -1.43%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-08-24
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4333 / 0.5667 / 0.7
- advancers / decliners / A-D ratio: 19 / 11 / 1.7273
- new highs/lows 20d: 5 / 2
- new highs/lows 52w: 3 / 0
- improvement / deterioration / confirmation / conflict / quality: 31.43 / 100.0 / 42.63 / 85.0 / 100.0
- internal_resonance: surface_only / score 28.94 / DIA 指数表面强但内部没充分跟上：confirmation 43，conflict 85，RSP/SPY -0.35%，IWM/SPY -1.43%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-28
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
- improvement / deterioration / confirmation / conflict / quality: 40.88 / 51.8 / 46.66 / 47.85 / 64
- internal_resonance: surface_only / score 29.22 / IWM 指数表面强但内部没充分跟上：confirmation 47，conflict 48，RSP/SPY -0.35%，IWM/SPY -1.43%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
