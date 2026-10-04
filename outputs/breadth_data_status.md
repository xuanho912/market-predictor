# Breadth Data Status

Generated at: 2026-10-04T16:52:56.660230+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 22.48
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 18.0
- equal_weight_vs_cap_weight_20d: -0.042333
- small_cap_vs_large_cap_20d: -0.041744

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-10-02
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2704 / 0.2525 / 0.4232
- advancers / decliners / A-D ratio: 206 / 290 / 0.7103
- new highs/lows 20d: 37 / 123
- new highs/lows 52w: 9 / 26
- improvement / deterioration / confirmation / conflict / quality: 24.99 / 82.94 / 39.36 / 63.03 / 100.0
- internal_resonance: surface_only / score 18.38 / SPY 指数表面强但内部没充分跟上：confirmation 39，conflict 63，RSP/SPY -4.23%，IWM/SPY -4.17%。

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
- internal_resonance: surface_only / score 1.83 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -4.23%，IWM/SPY -4.17%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-10-02
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3667 / 0.3667 / 0.6333
- advancers / decliners / A-D ratio: 11 / 18 / 0.6111
- new highs/lows 20d: 4 / 6
- new highs/lows 52w: 0 / 2
- improvement / deterioration / confirmation / conflict / quality: 50.23 / 64.03 / 59.05 / 48.66 / 100.0
- internal_resonance: surface_only / score 30.78 / DIA 指数表面强但内部没充分跟上：confirmation 59，conflict 49，RSP/SPY -4.23%，IWM/SPY -4.17%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-10-02
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
- improvement / deterioration / confirmation / conflict / quality: 27.37 / 78.27 / 36.53 / 67.71 / 64
- internal_resonance: surface_only / score 18.27 / IWM 指数表面强但内部没充分跟上：confirmation 37，conflict 68，RSP/SPY -4.23%，IWM/SPY -4.17%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
