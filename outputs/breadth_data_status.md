# Breadth Data Status

Generated at: 2026-09-26T08:51:18.140979+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 17.67
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 24.0
- equal_weight_vs_cap_weight_20d: -0.047016
- small_cap_vs_large_cap_20d: -0.059829

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-09-23
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2545 / 0.3022 / 0.495
- advancers / decliners / A-D ratio: 270 / 230 / 1.1739
- new highs/lows 20d: 34 / 127
- new highs/lows 52w: 7 / 25
- improvement / deterioration / confirmation / conflict / quality: 43.93 / 82.13 / 53.06 / 62.42 / 100.0
- internal_resonance: surface_only / score 23.2 / SPY 指数表面强但内部没充分跟上：confirmation 53，conflict 62，RSP/SPY -4.70%，IWM/SPY -5.98%。

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
- internal_resonance: surface_only / score 1.79 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -4.70%，IWM/SPY -5.98%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-09-22
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2 / 0.4 / 0.6667
- advancers / decliners / A-D ratio: 15 / 14 / 1.0714
- new highs/lows 20d: 2 / 5
- new highs/lows 52w: 0 / 1
- improvement / deterioration / confirmation / conflict / quality: 13.66 / 100.0 / 29.84 / 85.0 / 100.0
- internal_resonance: surface_only / score 14.58 / DIA 指数表面强但内部没充分跟上：confirmation 30，conflict 85，RSP/SPY -4.70%，IWM/SPY -5.98%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-25
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
- improvement / deterioration / confirmation / conflict / quality: 18.72 / 88.81 / 30.04 / 75.61 / 64
- internal_resonance: surface_only / score 15.24 / IWM 指数表面强但内部没充分跟上：confirmation 30，conflict 76，RSP/SPY -4.70%，IWM/SPY -5.98%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
