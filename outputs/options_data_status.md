# Options / Volatility Structure Status

Generated at: `2026-10-01T18:27:15.442598+00:00`

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

- VIX: `16.770000457763672`
- VIX9D: `14.5600004196167`
- VIX3M: `18.770000457763672`
- VIX6M: `20.6200008392334`
- VVIX: `93.41000366210938`
- SKEW: `141.9199981689453`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.2887`
- option_stress_score: `0.3627`
- failed_bounce_options_risk: `0.3347`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-30 | 141.9199981689453 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-01 | 16.770000457763672 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-01 | 18.770000457763672 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-01 | 20.6200008392334 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-01 | 14.5600004196167 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-01 | 93.41000366210938 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
