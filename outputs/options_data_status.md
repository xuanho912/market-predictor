# Options / Volatility Structure Status

Generated at: `2026-08-06T14:37:26.203573+00:00`

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

- VIX: `15.5600004196167`
- VIX9D: `13.510000228881836`
- VIX3M: `18.829999923706055`
- VIX6M: `20.969999313354492`
- VVIX: `89.33000183105469`
- SKEW: `133.32000732421875`
- term_structure_state: `contango`
- volatility_reversal_score: `0.783`
- panic_release_score: `0.5661`
- tail_risk_score: `0.103`
- option_stress_score: `0.0796`
- failed_bounce_options_risk: `0.1144`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-05 | 133.32000732421875 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-06 | 15.5600004196167 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-06 | 18.829999923706055 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-06 | 20.969999313354492 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-06 | 13.510000228881836 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-06 | 89.33000183105469 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
