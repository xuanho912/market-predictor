# Options / Volatility Structure Status

Generated at: `2026-07-21T14:25:45.411323+00:00`

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

- VIX: `17.68000030517578`
- VIX9D: `16.75`
- VIX3M: `19.889999389648438`
- VIX6M: `21.8799991607666`
- VVIX: `98.62999725341797`
- SKEW: `146.0500030517578`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5119`
- panic_release_score: `0.2919`
- tail_risk_score: `0.4499`
- option_stress_score: `0.4695`
- failed_bounce_options_risk: `0.4277`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-20 | 146.0500030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-21 | 17.68000030517578 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-21 | 19.889999389648438 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-21 | 21.8799991607666 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-21 | 16.75 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-21 | 98.62999725341797 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
