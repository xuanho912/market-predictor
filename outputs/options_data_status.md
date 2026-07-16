# Options / Volatility Structure Status

Generated at: `2026-07-16T22:35:14.674647+00:00`

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
- VIX9D: `13.979999542236328`
- VIX3M: `19.5`
- VIX6M: `21.68000030517578`
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
| ^VIX3M | available | 2026-07-16 | 19.5 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-16 | 21.68000030517578 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-16 | 13.979999542236328 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-16 | 97.30999755859375 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
