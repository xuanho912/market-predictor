# Options / Volatility Structure Status

Generated at: `2026-07-24T00:10:16.651649+00:00`

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

- VIX: `18.700000762939453`
- VIX9D: `18.149999618530273`
- VIX3M: `20.600000381469727`
- VIX6M: `22.479999542236328`
- VVIX: `102.16999816894531`
- SKEW: `145.9499969482422`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5248`
- panic_release_score: `0.3723`
- tail_risk_score: `0.5002`
- option_stress_score: `0.5109`
- failed_bounce_options_risk: `0.4803`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-23 | 145.9499969482422 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-23 | 18.700000762939453 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-23 | 20.600000381469727 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-23 | 22.479999542236328 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-23 | 18.149999618530273 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-23 | 102.16999816894531 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
