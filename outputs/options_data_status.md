# Options / Volatility Structure Status

Generated at: `2026-06-29T23:38:04.097334+00:00`

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

- VIX: `17.649999618530273`
- VIX9D: `15.510000228881836`
- VIX3M: `19.530000686645508`
- VIX6M: `21.799999237060547`
- VVIX: `88.70999908447266`
- SKEW: `144.4600067138672`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5119`
- panic_release_score: `0.2919`
- tail_risk_score: `0.237`
- option_stress_score: `0.4057`
- failed_bounce_options_risk: `0.3298`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-29 | 144.4600067138672 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-29 | 17.649999618530273 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-29 | 19.530000686645508 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-29 | 21.799999237060547 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-29 | 15.510000228881836 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-29 | 88.70999908447266 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
