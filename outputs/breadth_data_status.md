# Breadth Data Status

Generated at: 2026-07-21T23:45:46.332026+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 37.67
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 40.0
- equal_weight_vs_cap_weight_20d: 0.009802
- small_cap_vs_large_cap_20d: -0.010726

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-07-17
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5805 / 0.6347 / 0.662
- advancers / decliners / A-D ratio: 147 / 356 / 0.4129
- new highs/lows 20d: 58 / 48
- new highs/lows 52w: 32 / 4
- improvement / deterioration / confirmation / conflict / quality: 50.9 / 50.91 / 60.58 / 38.69 / 100.0
- internal_resonance: surface_only / score 42.42 / SPY 指数表面强但内部没充分跟上：confirmation 61，conflict 39，RSP/SPY 0.98%，IWM/SPY -1.07%。

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
- internal_resonance: surface_only / score 7.72 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 0.98%，IWM/SPY -1.07%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-07-17
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6 / 0.5667 / 0.6333
- advancers / decliners / A-D ratio: 7 / 23 / 0.3043
- new highs/lows 20d: 3 / 1
- new highs/lows 52w: 2 / 0
- improvement / deterioration / confirmation / conflict / quality: 48.75 / 66.93 / 57.75 / 50.86 / 100.0
- internal_resonance: surface_only / score 39.35 / DIA 指数表面强但内部没充分跟上：confirmation 58，conflict 51，RSP/SPY 0.98%，IWM/SPY -1.07%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-07-21
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
- improvement / deterioration / confirmation / conflict / quality: 49.73 / 55.67 / 53.3 / 50.75 / 64
- internal_resonance: surface_only / score 31.23 / IWM 指数表面强但内部没充分跟上：confirmation 53，conflict 51，RSP/SPY 0.98%，IWM/SPY -1.07%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
