# Options / Volatility Structure Status

Generated at: `2026-09-26T00:14:45.208697+00:00`

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

- VIX: `14.869999885559082`
- VIX9D: `12.760000228881836`
- VIX3M: `17.93000030517578`
- VIX6M: `20.010000228881836`
- VVIX: `87.83999633789062`
- SKEW: `144.91000366210938`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.2822`
- option_stress_score: `0.2503`
- failed_bounce_options_risk: `0.2456`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-25 | 144.91000366210938 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-25 | 14.869999885559082 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-25 | 17.93000030517578 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-25 | 20.010000228881836 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-25 | 12.760000228881836 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-25 | 87.83999633789062 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
