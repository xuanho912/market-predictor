# Options / Volatility Structure Status

Generated at: `2026-09-14T23:59:39.593699+00:00`

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

- VIX: `17.100000381469727`
- VIX9D: `16.90999984741211`
- VIX3M: `19.280000686645508`
- VIX6M: `20.709999084472656`
- VVIX: `94.88999938964844`
- SKEW: `152.08999633789062`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.4933`
- option_stress_score: `0.4444`
- failed_bounce_options_risk: `0.4381`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-14 | 152.08999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-14 | 17.100000381469727 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-14 | 19.280000686645508 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-14 | 20.709999084472656 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-14 | 16.90999984741211 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-14 | 94.88999938964844 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
