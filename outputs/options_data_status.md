# Options / Volatility Structure Status

Generated at: `2026-10-29T18:31:16.904927+00:00`

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

- VIX: `16.860000610351562`
- VIX9D: `15.319999694824219`
- VIX3M: `19.139999389648438`
- VIX6M: `21.1200008392334`
- VVIX: `94.95999908447266`
- SKEW: `148.74000549316406`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8617`
- panic_release_score: `0.64`
- tail_risk_score: `0.4764`
- option_stress_score: `0.2732`
- failed_bounce_options_risk: `0.2955`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-28 | 148.74000549316406 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-29 | 16.860000610351562 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-29 | 19.139999389648438 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-29 | 21.1200008392334 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-29 | 15.319999694824219 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-29 | 94.95999908447266 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
