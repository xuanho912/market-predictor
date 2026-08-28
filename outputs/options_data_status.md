# Options / Volatility Structure Status

Generated at: `2026-08-28T15:41:38.025758+00:00`

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

- VIX: `14.140000343322754`
- VIX9D: `11.069999694824219`
- VIX3M: `17.440000534057617`
- VIX6M: `20.309999465942383`
- VVIX: `85.80000305175781`
- SKEW: `144.0500030517578`
- term_structure_state: `contango`
- volatility_reversal_score: `0.85`
- panic_release_score: `0.5871`
- tail_risk_score: `0.2325`
- option_stress_score: `0.0694`
- failed_bounce_options_risk: `0.1347`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-27 | 144.0500030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-28 | 14.140000343322754 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-28 | 17.440000534057617 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-28 | 20.309999465942383 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-28 | 11.069999694824219 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-28 | 85.80000305175781 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
