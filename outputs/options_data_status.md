# Options / Volatility Structure Status

Generated at: `2026-09-24T01:26:41.524307+00:00`

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

- VIX: `15.180000305175781`
- VIX9D: `13.449999809265137`
- VIX3M: `18.110000610351562`
- VIX6M: `20.110000610351562`
- VVIX: `88.5999984741211`
- SKEW: `146.14999389648438`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8637`
- panic_release_score: `0.6354`
- tail_risk_score: `0.3261`
- option_stress_score: `0.1244`
- failed_bounce_options_risk: `0.1836`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-23 | 146.14999389648438 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-23 | 15.180000305175781 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-23 | 18.110000610351562 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-23 | 20.110000610351562 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-23 | 13.449999809265137 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-23 | 88.5999984741211 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
