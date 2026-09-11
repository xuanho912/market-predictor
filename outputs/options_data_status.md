# Options / Volatility Structure Status

Generated at: `2026-09-11T16:31:37.697946+00:00`

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

- VIX: `15.710000038146973`
- VIX9D: `14.020000457763672`
- VIX3M: `18.65999984741211`
- VIX6M: `20.479999542236328`
- VVIX: `91.83999633789062`
- SKEW: `147.02000427246094`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.383`
- option_stress_score: `0.3136`
- failed_bounce_options_risk: `0.3286`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-10 | 147.02000427246094 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-11 | 15.710000038146973 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-11 | 18.65999984741211 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-11 | 20.479999542236328 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-11 | 14.020000457763672 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-11 | 91.83999633789062 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
