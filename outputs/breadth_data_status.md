# Breadth Data Status

Generated at: 2026-07-15T14:12:24.743878+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 72.53
Stale data: False

## Market Internal Resonance

- resonance_score: 37.97
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 52.0
- equal_weight_vs_cap_weight_20d: -0.007604
- small_cap_vs_large_cap_20d: -0.00655

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-07-13
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6195 / 0.6607 / 0.662
- advancers / decliners / A-D ratio: 284 / 219 / 1.2968
- new highs/lows 20d: 74 / 17
- new highs/lows 52w: 20 / 1
- improvement / deterioration / confirmation / conflict / quality: 42.3 / 69.07 / 52.93 / 61.49 / 100.0
- internal_resonance: surface_only / score 39.96 / SPY 指数表面强但内部没充分跟上：confirmation 53，conflict 61，RSP/SPY -0.76%，IWM/SPY -0.66%。

### QQQ

- status: missing
- source: wikipedia-nasdaq100
- latest_date: 2026-07-13
- true_breadth: False
- proxy: False
- constituents used / expected: 1 / 19
- coverage_ratio: 0.0526
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.0 / 0.0 / 0.0
- advancers / decliners / A-D ratio: 0 / 1 / 0.0
- new highs/lows 20d: 0 / 1
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 100.0 / 77.22 / 87.82 / 26.11
- internal_resonance: surface_only / score 11.6 / QQQ 指数表面强但内部没充分跟上：confirmation 77，conflict 88，RSP/SPY -0.76%，IWM/SPY -0.66%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-07-13
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6 / 0.6333 / 0.6
- advancers / decliners / A-D ratio: 16 / 14 / 1.1429
- new highs/lows 20d: 3 / 0
- new highs/lows 52w: 1 / 0
- improvement / deterioration / confirmation / conflict / quality: 59.75 / 80.73 / 64.56 / 61.35 / 100.0
- internal_resonance: surface_only / score 41.82 / DIA 指数表面强但内部没充分跟上：confirmation 65，conflict 61，RSP/SPY -0.76%，IWM/SPY -0.66%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-07-15
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
- improvement / deterioration / confirmation / conflict / quality: 46.42 / 49.77 / 50.82 / 46.33 / 64
- internal_resonance: surface_only / score 32.12 / IWM 指数表面强但内部没充分跟上：confirmation 51，conflict 46，RSP/SPY -0.76%，IWM/SPY -0.66%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
