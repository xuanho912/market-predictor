# Options / Volatility Structure Status

Generated at: `2026-07-15T00:04:16.959835+00:00`

## Summary

- options_available: `True`
- options_partial: `False`
- options_missing: `False`
- options_stale: `False`
- options_source: `market_data_cache/yahoo/stooq`
- vix_term_available: `True`
- vvix_available: `True`
- skew_available: `True`
- put_call_available: `False`
- gamma_available: `False`
- options_quality_score: `92`

## Market Snapshot

- VIX: `16.5`
- VIX9D: `13.460000038146973`
- VIX3M: `19.299999237060547`
- VIX6M: `21.520000457763672`
- VVIX: `93.52999877929688`
- SKEW: `145.1300048828125`
- term_structure_state: `contango`
- volatility_reversal_score: `0.618`
- panic_release_score: `0.4038`
- tail_risk_score: `0.322`
- option_stress_score: `0.3527`
- failed_bounce_options_risk: `0.3176`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-14 | 145.1300048828125 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-14 | 16.5 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-14 | 19.299999237060547 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-14 | 21.520000457763672 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-14 | 13.460000038146973 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-14 | 93.52999877929688 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
