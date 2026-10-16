# Options / Volatility Structure Status

Generated at: `2026-10-16T16:42:23.761776+00:00`

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

- VIX: `17.190000534057617`
- VIX9D: `14.850000381469727`
- VIX3M: `18.93000030517578`
- VIX6M: `20.579999923706055`
- VVIX: `95.37000274658203`
- SKEW: `160.4499969482422`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5033`
- panic_release_score: `0.33`
- tail_risk_score: `0.5571`
- option_stress_score: `0.475`
- failed_bounce_options_risk: `0.4814`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-15 | 160.4499969482422 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-16 | 17.190000534057617 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-16 | 18.93000030517578 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-16 | 20.579999923706055 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-16 | 14.850000381469727 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-16 | 95.37000274658203 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
