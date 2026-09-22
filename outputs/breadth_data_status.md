# Breadth Data Status

Generated at: 2026-09-22T00:19:04.045510+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 16.41
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 18.0
- equal_weight_vs_cap_weight_20d: -0.050716
- small_cap_vs_large_cap_20d: -0.0581

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-09-21
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.1968 / 0.2843 / 0.495
- advancers / decliners / A-D ratio: 158 / 344 / 0.4593
- new highs/lows 20d: 12 / 146
- new highs/lows 52w: 2 / 29
- improvement / deterioration / confirmation / conflict / quality: 23.4 / 100.0 / 36.85 / 85.0 / 100.0
- internal_resonance: surface_only / score 11.85 / SPY 指数表面强但内部没充分跟上：confirmation 37，conflict 85，RSP/SPY -5.07%，IWM/SPY -5.81%。

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
- internal_resonance: surface_only / score 0.96 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -5.07%，IWM/SPY -5.81%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-09-18
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2667 / 0.4 / 0.6
- advancers / decliners / A-D ratio: 10 / 20 / 0.5
- new highs/lows 20d: 0 / 6
- new highs/lows 52w: 0 / 2
- improvement / deterioration / confirmation / conflict / quality: 52.82 / 90.44 / 58.79 / 68.73 / 100.0
- internal_resonance: surface_only / score 22.53 / DIA 指数表面强但内部没充分跟上：confirmation 59，conflict 69，RSP/SPY -5.07%，IWM/SPY -5.81%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-21
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
- improvement / deterioration / confirmation / conflict / quality: 18.51 / 85.22 / 29.88 / 72.92 / 64
- internal_resonance: surface_only / score 14.86 / IWM 指数表面强但内部没充分跟上：confirmation 30，conflict 73，RSP/SPY -5.07%，IWM/SPY -5.81%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
