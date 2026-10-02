# Breadth Data Status

Generated at: 2026-10-02T17:54:31.924479+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 18.85
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 18.0
- equal_weight_vs_cap_weight_20d: -0.041838
- small_cap_vs_large_cap_20d: -0.040493

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-09-29
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2664 / 0.2445 / 0.4271
- advancers / decliners / A-D ratio: 180 / 318 / 0.566
- new highs/lows 20d: 23 / 130
- new highs/lows 52w: 6 / 25
- improvement / deterioration / confirmation / conflict / quality: 23.39 / 88.73 / 37.74 / 67.44 / 100.0
- internal_resonance: surface_only / score 16.68 / SPY 指数表面强但内部没充分跟上：confirmation 38，conflict 67，RSP/SPY -4.18%，IWM/SPY -4.05%。

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
- internal_resonance: surface_only / score 1.9 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -4.18%，IWM/SPY -4.05%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-09-29
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3667 / 0.3333 / 0.6667
- advancers / decliners / A-D ratio: 8 / 22 / 0.3636
- new highs/lows 20d: 1 / 8
- new highs/lows 52w: 0 / 2
- improvement / deterioration / confirmation / conflict / quality: 31.22 / 85.73 / 43.62 / 65.16 / 100.0
- internal_resonance: surface_only / score 21.31 / DIA 指数表面强但内部没充分跟上：confirmation 44，conflict 65，RSP/SPY -4.18%，IWM/SPY -4.05%。

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
- improvement / deterioration / confirmation / conflict / quality: 28.14 / 77.55 / 37.1 / 67.16 / 64
- internal_resonance: surface_only / score 18.57 / IWM 指数表面强但内部没充分跟上：confirmation 37，conflict 67，RSP/SPY -4.18%，IWM/SPY -4.05%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
