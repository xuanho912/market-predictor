# Options / Volatility Structure Status

Generated at: `2026-10-26T18:44:00.264259+00:00`

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

- VIX: `18.3700008392334`
- VIX9D: `17.84000015258789`
- VIX3M: `19.93000030517578`
- VIX6M: `21.6200008392334`
- VVIX: `102.41999816894531`
- SKEW: `151.8000030517578`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5317`
- panic_release_score: `0.3525`
- tail_risk_score: `0.6083`
- option_stress_score: `0.4126`
- failed_bounce_options_risk: `0.3986`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-23 | 151.8000030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-26 | 18.3700008392334 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-26 | 19.93000030517578 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-26 | 21.6200008392334 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-26 | 17.84000015258789 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-26 | 102.41999816894531 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
