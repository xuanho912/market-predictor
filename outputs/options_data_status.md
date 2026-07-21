# Options / Volatility Structure Status

Generated at: `2026-07-21T22:32:12.461645+00:00`

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

- VIX: `17.049999237060547`
- VIX9D: `15.479999542236328`
- VIX3M: `19.59000015258789`
- VIX6M: `21.65999984741211`
- VVIX: `96.33999633789062`
- SKEW: `151.66000366210938`
- term_structure_state: `contango`
- volatility_reversal_score: `0.523`
- panic_release_score: `0.3444`
- tail_risk_score: `0.4767`
- option_stress_score: `0.4393`
- failed_bounce_options_risk: `0.4007`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-21 | 151.66000366210938 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-21 | 17.049999237060547 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-21 | 19.59000015258789 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-21 | 21.65999984741211 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-21 | 15.479999542236328 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-21 | 96.33999633789062 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
