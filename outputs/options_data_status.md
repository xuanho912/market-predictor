# Options / Volatility Structure Status

Generated at: `2026-08-13T13:50:40.131484+00:00`

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

- VIX: `14.430000305175781`
- VIX9D: `11.210000038146973`
- VIX3M: `18.5`
- VIX6M: `20.809999465942383`
- VVIX: `88.0999984741211`
- SKEW: `136.5399932861328`
- term_structure_state: `contango`
- volatility_reversal_score: `0.85`
- panic_release_score: `0.5766`
- tail_risk_score: `0.1011`
- option_stress_score: `0.0361`
- failed_bounce_options_risk: `0.0901`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-12 | 136.5399932861328 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-13 | 14.430000305175781 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-13 | 18.5 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-13 | 20.809999465942383 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-13 | 11.210000038146973 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-13 | 88.0999984741211 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
