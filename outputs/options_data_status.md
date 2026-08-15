# Options / Volatility Structure Status

Generated at: `2026-08-15T13:02:44.299123+00:00`

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

- VIX: `14.25`
- VIX9D: `10.609999656677246`
- VIX3M: `18.459999084472656`
- VIX6M: `20.799999237060547`
- VVIX: `87.4800033569336`
- SKEW: `138.36000061035156`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8333`
- panic_release_score: `0.5635`
- tail_risk_score: `0.1103`
- option_stress_score: `0.0376`
- failed_bounce_options_risk: `0.0928`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-14 | 138.36000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-14 | 14.25 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-14 | 18.459999084472656 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-14 | 20.799999237060547 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-14 | 10.609999656677246 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-14 | 87.4800033569336 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
