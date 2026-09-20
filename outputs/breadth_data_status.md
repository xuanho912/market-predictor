# Breadth Data Status

Generated at: 2026-09-20T16:09:34.072047+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 19.78
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 20.0
- equal_weight_vs_cap_weight_20d: -0.035079
- small_cap_vs_large_cap_20d: -0.044394

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-09-18
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.1909 / 0.2783 / 0.489
- advancers / decliners / A-D ratio: 156 / 346 / 0.4509
- new highs/lows 20d: 11 / 147
- new highs/lows 52w: 2 / 30
- improvement / deterioration / confirmation / conflict / quality: 39.95 / 100.0 / 48.76 / 76.0 / 100.0
- internal_resonance: surface_only / score 17.47 / SPY 指数表面强但内部没充分跟上：confirmation 49，conflict 76，RSP/SPY -3.51%，IWM/SPY -4.44%。

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
- internal_resonance: surface_only / score 2.28 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -3.51%，IWM/SPY -4.44%。

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
- internal_resonance: surface_only / score 23.86 / DIA 指数表面强但内部没充分跟上：confirmation 59，conflict 69，RSP/SPY -3.51%，IWM/SPY -4.44%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-18
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
- improvement / deterioration / confirmation / conflict / quality: 24.0 / 79.15 / 34.0 / 68.37 / 64
- internal_resonance: surface_only / score 18.0 / IWM 指数表面强但内部没充分跟上：confirmation 34，conflict 68，RSP/SPY -3.51%，IWM/SPY -4.44%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
