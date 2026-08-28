# Breadth Data Status

Generated at: 2026-08-28T06:25:06.779160+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 31.65
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 42.0
- equal_weight_vs_cap_weight_20d: -0.01147
- small_cap_vs_large_cap_20d: -0.014976

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
- internal_resonance: surface_only / score 35.78 / SPY 指数表面强但内部没充分跟上：confirmation 48，conflict 62，RSP/SPY -1.15%，IWM/SPY -1.50%。

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
- internal_resonance: surface_only / score 6.83 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -1.15%，IWM/SPY -1.50%。

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
- internal_resonance: surface_only / score 28.99 / DIA 指数表面强但内部没充分跟上：confirmation 43，conflict 85，RSP/SPY -1.15%，IWM/SPY -1.50%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-27
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
- improvement / deterioration / confirmation / conflict / quality: 44.49 / 49.82 / 49.37 / 46.37 / 64
- internal_resonance: surface_only / score 30.19 / IWM 指数表面强但内部没充分跟上：confirmation 49，conflict 46，RSP/SPY -1.15%，IWM/SPY -1.50%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
