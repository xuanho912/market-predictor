# Options / Volatility Structure Status

Generated at: `2026-10-06T23:57:12.935390+00:00`

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

- VIX: `15.010000228881836`
- VIX9D: `12.029999732971191`
- VIX3M: `17.639999389648438`
- VIX6M: `19.84000015258789`
- VVIX: `82.58999633789062`
- SKEW: `141.2100067138672`
- term_structure_state: `contango`
- volatility_reversal_score: `0.7427`
- panic_release_score: `0.5215`
- tail_risk_score: `0.1379`
- option_stress_score: `0.0768`
- failed_bounce_options_risk: `0.1198`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-06 | 141.2100067138672 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-06 | 15.010000228881836 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-06 | 17.639999389648438 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-06 | 19.84000015258789 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-06 | 12.029999732971191 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-06 | 82.58999633789062 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
