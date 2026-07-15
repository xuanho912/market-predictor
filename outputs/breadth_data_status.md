# Breadth Data Status

Generated at: 2026-07-15T22:35:26.556612+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 72.53
Stale data: False

## Market Internal Resonance

- resonance_score: 40.93
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA
- sector_score: 54.0
- equal_weight_vs_cap_weight_20d: 0.000449
- small_cap_vs_large_cap_20d: 0.003862

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-07-13
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6195 / 0.6607 / 0.662
- advancers / decliners / A-D ratio: 284 / 219 / 1.2968
- new highs/lows 20d: 74 / 17
- new highs/lows 52w: 20 / 1
- improvement / deterioration / confirmation / conflict / quality: 42.3 / 69.07 / 52.93 / 61.49 / 100.0
- internal_resonance: surface_only / score 40.92 / SPY 指数表面强但内部没充分跟上：confirmation 53，conflict 61，RSP/SPY 0.04%，IWM/SPY 0.39%。

### QQQ

- status: missing
- source: wikipedia-nasdaq100
- latest_date: 2026-07-13
- true_breadth: False
- proxy: False
- constituents used / expected: 1 / 19
- coverage_ratio: 0.0526
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.0 / 0.0 / 0.0
- advancers / decliners / A-D ratio: 0 / 1 / 0.0
- new highs/lows 20d: 0 / 1
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 100.0 / 77.22 / 87.82 / 26.11
- internal_resonance: surface_only / score 12.56 / QQQ 指数表面强但内部没充分跟上：confirmation 77，conflict 88，RSP/SPY 0.04%，IWM/SPY 0.39%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-07-13
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6 / 0.6333 / 0.6
- advancers / decliners / A-D ratio: 16 / 14 / 1.1429
- new highs/lows 20d: 3 / 0
- new highs/lows 52w: 1 / 0
- improvement / deterioration / confirmation / conflict / quality: 41.75 / 98.73 / 50.16 / 84.03 / 100.0
- internal_resonance: surface_only / score 35.24 / DIA 指数表面强但内部没充分跟上：confirmation 50，conflict 84，RSP/SPY 0.04%，IWM/SPY 0.39%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-07-15
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
- improvement / deterioration / confirmation / conflict / quality: 53.38 / 47.5 / 56.04 / 44.62 / 64
- internal_resonance: weak / score 46.64 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
