# Options / Volatility Structure Status

Generated at: `2026-06-16T00:16:04.697049+00:00`

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

- VIX: `16.200000762939453`
- VIX9D: `15.579999923706055`
- VIX3M: `19.360000610351562`
- VIX6M: `21.770000457763672`
- VVIX: `87.58000183105469`
- SKEW: `144.32000732421875`
- term_structure_state: `contango`
- volatility_reversal_score: `1.0`
- panic_release_score: `0.78`
- tail_risk_score: `0.2178`
- option_stress_score: `0.1308`
- failed_bounce_options_risk: `0.1655`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-15 | 144.32000732421875 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-15 | 16.200000762939453 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-15 | 19.360000610351562 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-15 | 21.770000457763672 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-15 | 15.579999923706055 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-15 | 87.58000183105469 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
