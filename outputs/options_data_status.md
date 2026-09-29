# Options / Volatility Structure Status

Generated at: `2026-09-29T01:21:43.191370+00:00`

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

- VIX: `16.06999969482422`
- VIX9D: `14.390000343322754`
- VIX3M: `18.229999542236328`
- VIX6M: `20.25`
- VVIX: `91.0199966430664`
- SKEW: `146.25`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.3694`
- option_stress_score: `0.3387`
- failed_bounce_options_risk: `0.3402`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-28 | 146.25 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-28 | 16.06999969482422 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-28 | 18.229999542236328 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-28 | 20.25 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-28 | 14.390000343322754 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-28 | 91.0199966430664 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
