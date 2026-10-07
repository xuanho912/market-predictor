# Breadth Data Status

Generated at: 2026-10-07T18:59:17.810614+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 25.96
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 66.0
- equal_weight_vs_cap_weight_20d: -0.036574
- small_cap_vs_large_cap_20d: -0.062901

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-10-05
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.34 / 0.2624 / 0.4291
- advancers / decliners / A-D ratio: 322 / 178 / 1.809
- new highs/lows 20d: 56 / 59
- new highs/lows 52w: 16 / 15
- improvement / deterioration / confirmation / conflict / quality: 42.85 / 56.38 / 54.34 / 42.85 / 100.0
- internal_resonance: surface_only / score 35.69 / SPY 指数表面强但内部没充分跟上：confirmation 54，conflict 43，RSP/SPY -3.66%，IWM/SPY -6.29%。

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
- internal_resonance: surface_only / score 6.88 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -3.66%，IWM/SPY -6.29%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-10-05
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3 / 0.3 / 0.5667
- advancers / decliners / A-D ratio: 17 / 12 / 1.4167
- new highs/lows 20d: 5 / 5
- new highs/lows 52w: 0 / 2
- improvement / deterioration / confirmation / conflict / quality: 16.09 / 100.0 / 31.59 / 85.0 / 100.0
- internal_resonance: surface_only / score 20.92 / DIA 指数表面强但内部没充分跟上：confirmation 32，conflict 85，RSP/SPY -3.66%，IWM/SPY -6.29%。

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
- improvement / deterioration / confirmation / conflict / quality: 21.68 / 85.87 / 32.26 / 73.4 / 64
- internal_resonance: surface_only / score 21.26 / IWM 指数表面强但内部没充分跟上：confirmation 32，conflict 73，RSP/SPY -3.66%，IWM/SPY -6.29%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
