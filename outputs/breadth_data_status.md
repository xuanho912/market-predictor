# Breadth Data Status

Generated at: 2026-06-14T09:33:48.171094+00:00

Provider available: True
True breadth available: True
True breadth symbols: SPY, QQQ, DIA
Proxy-only symbols: IWM
Average breadth quality score: 91.0
Stale data: False

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-06-12
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7112 / 0.6036 / 0.6088
- advancers / decliners / A-D ratio: 397 / 106 / 3.7453
- new highs/lows 20d: 126 / 14
- new highs/lows 52w: 38 / 6
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 21.41 / 98.29 / 16.27 / 100.0

### QQQ

- status: available
- source: wikipedia-nasdaq100
- latest_date: 2026-06-12
- true_breadth: True
- proxy: False
- constituents used / expected: 101 / 101
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5446 / 0.5149 / 0.5842
- advancers / decliners / A-D ratio: 70 / 31 / 2.2581
- new highs/lows 20d: 13 / 9
- new highs/lows 52w: 9 / 5
- improvement / deterioration / confirmation / conflict / quality: 75.38 / 40.08 / 79.07 / 30.46 / 100.0

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-06-12
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6333 / 0.6667 / 0.6667
- advancers / decliners / A-D ratio: 21 / 9 / 2.3333
- new highs/lows 20d: 9 / 1
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 89.83 / 24.42 / 90.72 / 18.56 / 100.0

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-06-12
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
- improvement / deterioration / confirmation / conflict / quality: 82.1 / 27.14 / 77.57 / 29.36 / 64

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
