# Breadth Data Status

Generated at: 2026-09-04T05:59:36.016764+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 24.52
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 44.0
- equal_weight_vs_cap_weight_20d: 0.000727
- small_cap_vs_large_cap_20d: -0.016258

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-09-02
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3161 / 0.4533 / 0.6208
- advancers / decliners / A-D ratio: 157 / 343 / 0.4577
- new highs/lows 20d: 32 / 157
- new highs/lows 52w: 7 / 13
- improvement / deterioration / confirmation / conflict / quality: 14.3 / 100.0 / 30.3 / 85.0 / 100.0
- internal_resonance: surface_only / score 20.59 / SPY 指数表面强但内部没充分跟上：confirmation 30，conflict 85，RSP/SPY 0.07%，IWM/SPY -1.63%。

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
- internal_resonance: surface_only / score 7.55 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 0.07%，IWM/SPY -1.63%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-09-01
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3667 / 0.5 / 0.6667
- advancers / decliners / A-D ratio: 10 / 20 / 0.5
- new highs/lows 20d: 4 / 9
- new highs/lows 52w: 0 / 1
- improvement / deterioration / confirmation / conflict / quality: 23.4 / 100.0 / 36.85 / 85.0 / 100.0
- internal_resonance: surface_only / score 24.01 / DIA 指数表面强但内部没充分跟上：confirmation 37，conflict 85，RSP/SPY 0.07%，IWM/SPY -1.63%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-03
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
- improvement / deterioration / confirmation / conflict / quality: 40.59 / 59.07 / 46.44 / 53.3 / 64
- internal_resonance: surface_only / score 28.96 / IWM 指数表面强但内部没充分跟上：confirmation 46，conflict 53，RSP/SPY 0.07%，IWM/SPY -1.63%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
