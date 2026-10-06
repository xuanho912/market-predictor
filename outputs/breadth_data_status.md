# Breadth Data Status

Generated at: 2026-10-06T02:35:39.973034+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 25.56
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 42.0
- equal_weight_vs_cap_weight_20d: -0.042006
- small_cap_vs_large_cap_20d: -0.048692

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
- internal_resonance: surface_only / score 33.06 / SPY 指数表面强但内部没充分跟上：confirmation 54，conflict 43，RSP/SPY -4.20%，IWM/SPY -4.87%。

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
- internal_resonance: surface_only / score 4.24 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -4.20%，IWM/SPY -4.87%。

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
- improvement / deterioration / confirmation / conflict / quality: 34.09 / 100.0 / 44.55 / 76.0 / 100.0
- internal_resonance: surface_only / score 23.01 / DIA 指数表面强但内部没充分跟上：confirmation 45，conflict 76，RSP/SPY -4.20%，IWM/SPY -4.87%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-10-05
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
- improvement / deterioration / confirmation / conflict / quality: 28.4 / 80.14 / 37.3 / 69.11 / 64
- internal_resonance: surface_only / score 20.61 / IWM 指数表面强但内部没充分跟上：confirmation 37，conflict 69，RSP/SPY -4.20%，IWM/SPY -4.87%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
