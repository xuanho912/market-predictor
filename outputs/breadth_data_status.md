# Breadth Data Status

Generated at: 2026-10-08T02:42:02.326510+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 31.03
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 66.0
- equal_weight_vs_cap_weight_20d: -0.038261
- small_cap_vs_large_cap_20d: -0.063961

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-10-06
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3479 / 0.2744 / 0.4371
- advancers / decliners / A-D ratio: 324 / 178 / 1.8202
- new highs/lows 20d: 58 / 54
- new highs/lows 52w: 17 / 12
- improvement / deterioration / confirmation / conflict / quality: 47.65 / 52.44 / 58.11 / 39.85 / 100.0
- internal_resonance: surface_only / score 37.96 / SPY 指数表面强但内部没充分跟上：confirmation 58，conflict 40，RSP/SPY -3.83%，IWM/SPY -6.40%。

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
- internal_resonance: surface_only / score 6.8 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -3.83%，IWM/SPY -6.40%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-10-06
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3667 / 0.3 / 0.5667
- advancers / decliners / A-D ratio: 18 / 12 / 1.5
- new highs/lows 20d: 5 / 4
- new highs/lows 52w: 1 / 1
- improvement / deterioration / confirmation / conflict / quality: 44.32 / 71.65 / 54.17 / 54.46 / 100.0
- internal_resonance: surface_only / score 34.27 / DIA 指数表面强但内部没充分跟上：confirmation 54，conflict 54，RSP/SPY -3.83%，IWM/SPY -6.40%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-10-07
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
- improvement / deterioration / confirmation / conflict / quality: 20.56 / 86.72 / 31.42 / 74.04 / 64
- internal_resonance: surface_only / score 20.87 / IWM 指数表面强但内部没充分跟上：confirmation 31，conflict 74，RSP/SPY -3.83%，IWM/SPY -6.40%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
