# Breadth Data Status

Generated at: 2026-08-18T04:22:14.951696+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 47.16
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 62.0
- equal_weight_vs_cap_weight_20d: -0.014564
- small_cap_vs_large_cap_20d: -0.001011

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-08-14
- true_breadth: True
- proxy: False
- constituents used / expected: 502 / 502
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6633 / 0.6986 / 0.722
- advancers / decliners / A-D ratio: 249 / 245 / 1.0163
- new highs/lows 20d: 68 / 7
- new highs/lows 52w: 17 / 1
- improvement / deterioration / confirmation / conflict / quality: 74.5 / 36.98 / 78.68 / 28.11 / 100.0
- internal_resonance: surface_only / score 53.41 / SPY 指数表面强但内部没充分跟上：confirmation 79，conflict 28，RSP/SPY -1.46%，IWM/SPY -0.10%。

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
- internal_resonance: surface_only / score 9.39 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -1.46%，IWM/SPY -0.10%。

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
- internal_resonance: surface_only / score 52.98 / DIA 指数表面强但内部没充分跟上：confirmation 79，conflict 35，RSP/SPY -1.46%，IWM/SPY -0.10%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-17
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
- improvement / deterioration / confirmation / conflict / quality: 50.42 / 40.36 / 53.82 / 39.27 / 64
- internal_resonance: surface_only / score 35.1 / IWM 指数表面强但内部没充分跟上：confirmation 54，conflict 39，RSP/SPY -1.46%，IWM/SPY -0.10%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
