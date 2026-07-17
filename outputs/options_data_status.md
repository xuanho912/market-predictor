# Options / Volatility Structure Status

Generated at: `2026-07-17T06:06:23.471086+00:00`

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

- VIX: `16.729999542236328`
- VIX9D: `11.149999618530273`
- VIX3M: `18.56999969482422`
- VIX6M: `21.09000015258789`
- VVIX: `97.30999755859375`
- SKEW: `145.72000122070312`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.4068`
- option_stress_score: `0.4045`
- failed_bounce_options_risk: `0.3761`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-16 | 145.72000122070312 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-16 | 16.729999542236328 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-10 | 18.56999969482422 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-10 | 21.09000015258789 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-10 | 11.149999618530273 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-16 | 97.30999755859375 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
