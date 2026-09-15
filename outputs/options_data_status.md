# Options / Volatility Structure Status

Generated at: `2026-09-15T17:02:43.392658+00:00`

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

- VIX: `17.510000228881836`
- VIX9D: `17.450000762939453`
- VIX3M: `19.510000228881836`
- VIX6M: `20.799999237060547`
- VVIX: `96.30999755859375`
- SKEW: `152.08999633789062`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5076`
- panic_release_score: `0.2651`
- tail_risk_score: `0.5174`
- option_stress_score: `0.481`
- failed_bounce_options_risk: `0.4628`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-14 | 152.08999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-15 | 17.510000228881836 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-15 | 19.510000228881836 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-15 | 20.799999237060547 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-15 | 17.450000762939453 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-15 | 96.30999755859375 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
