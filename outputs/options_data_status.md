# Options / Volatility Structure Status

Generated at: `2026-08-04T22:40:41.322785+00:00`

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
- VIX9D: `15.039999961853027`
- VIX3M: `19.34000015258789`
- VIX6M: `21.350000381469727`
- VVIX: `92.56999969482422`
- SKEW: `126.41000366210938`
- term_structure_state: `contango`
- volatility_reversal_score: `0.785`
- panic_release_score: `0.5743`
- tail_risk_score: `0.1457`
- option_stress_score: `0.1577`
- failed_bounce_options_risk: `0.1659`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-04 | 126.41000366210938 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-04 | 16.5 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-04 | 19.34000015258789 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-04 | 21.350000381469727 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-04 | 15.039999961853027 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-04 | 92.56999969482422 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
