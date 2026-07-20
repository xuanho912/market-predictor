# Options / Volatility Structure Status

Generated at: `2026-07-20T22:35:08.202489+00:00`

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

- VIX: `18.649999618530273`
- VIX9D: `17.780000686645508`
- VIX3M: `20.399999618530273`
- VIX6M: `22.200000762939453`
- VVIX: `102.81999969482422`
- SKEW: `146.0500030517578`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5248`
- panic_release_score: `0.3723`
- tail_risk_score: `0.5072`
- option_stress_score: `0.513`
- failed_bounce_options_risk: `0.4708`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-20 | 146.0500030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-20 | 18.649999618530273 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-20 | 20.399999618530273 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-20 | 22.200000762939453 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-20 | 17.780000686645508 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-20 | 102.81999969482422 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
