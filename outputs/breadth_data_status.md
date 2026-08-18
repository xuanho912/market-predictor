# Breadth Data Status

Generated at: 2026-08-18T20:46:52.378198+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 47.3
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 66.0
- equal_weight_vs_cap_weight_20d: 0.00447
- small_cap_vs_large_cap_20d: -0.013175

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-08-17
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6653 / 0.7006 / 0.722
- advancers / decliners / A-D ratio: 250 / 245 / 1.0204
- new highs/lows 20d: 68 / 7
- new highs/lows 52w: 17 / 1
- improvement / deterioration / confirmation / conflict / quality: 75.39 / 36.67 / 79.34 / 27.87 / 100.0
- internal_resonance: surface_only / score 54.57 / SPY 指数表面强但内部没充分跟上：confirmation 79，conflict 28，RSP/SPY 0.45%，IWM/SPY -1.32%。

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
- internal_resonance: surface_only / score 10.25 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 0.45%，IWM/SPY -1.32%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-08-14
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7 / 0.7 / 0.7667
- advancers / decliners / A-D ratio: 12 / 17 / 0.7059
- new highs/lows 20d: 4 / 0
- new highs/lows 52w: 1 / 0
- improvement / deterioration / confirmation / conflict / quality: 76.02 / 46.38 / 79.03 / 35.25 / 100.0
- internal_resonance: surface_only / score 53.84 / DIA 指数表面强但内部没充分跟上：confirmation 79，conflict 35，RSP/SPY 0.45%，IWM/SPY -1.32%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-18
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
- improvement / deterioration / confirmation / conflict / quality: 45.56 / 52.16 / 50.17 / 48.12 / 64
- internal_resonance: surface_only / score 33.49 / IWM 指数表面强但内部没充分跟上：confirmation 50，conflict 48，RSP/SPY 0.45%，IWM/SPY -1.32%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
