# Breadth Data Status

Generated at: 2026-07-31T04:46:02.541610+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 52.49
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 60.0
- equal_weight_vs_cap_weight_20d: 0.014689
- small_cap_vs_large_cap_20d: -0.017027

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-07-27
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6322 / 0.6846 / 0.686
- advancers / decliners / A-D ratio: 328 / 175 / 1.8743
- new highs/lows 20d: 101 / 37
- new highs/lows 52w: 31 / 2
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 26.65 / 97.87 / 20.25 / 100.0
- internal_resonance: surface_only / score 62.93 / SPY 指数表面强但内部没充分跟上：confirmation 98，conflict 20，RSP/SPY 1.47%，IWM/SPY -1.70%。

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
- internal_resonance: surface_only / score 9.91 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 1.47%，IWM/SPY -1.70%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-07-27
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5667 / 0.6333 / 0.6
- advancers / decliners / A-D ratio: 23 / 7 / 3.2857
- new highs/lows 20d: 6 / 1
- new highs/lows 52w: 4 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 26.0 / 97.92 / 19.76 / 100.0
- internal_resonance: surface_only / score 62.5 / DIA 指数表面强但内部没充分跟上：confirmation 98，conflict 20，RSP/SPY 1.47%，IWM/SPY -1.70%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-07-30
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
- improvement / deterioration / confirmation / conflict / quality: 47.11 / 62.43 / 51.33 / 55.82 / 64
- internal_resonance: surface_only / score 32.04 / IWM 指数表面强但内部没充分跟上：confirmation 51，conflict 56，RSP/SPY 1.47%，IWM/SPY -1.70%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
