# Options / Volatility Structure Status

Generated at: `2026-10-27T18:03:49.662781+00:00`

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

- VIX: `17.709999084472656`
- VIX9D: `16.959999084472656`
- VIX3M: `19.579999923706055`
- VIX6M: `21.43000030517578`
- VVIX: `98.80000305175781`
- SKEW: `150.97000122070312`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5119`
- panic_release_score: `0.2919`
- tail_risk_score: `0.5574`
- option_stress_score: `0.5018`
- failed_bounce_options_risk: `0.4474`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-26 | 150.97000122070312 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-27 | 17.709999084472656 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-27 | 19.579999923706055 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-27 | 21.43000030517578 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-27 | 16.959999084472656 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-27 | 98.80000305175781 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
