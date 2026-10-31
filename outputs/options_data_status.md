# Options / Volatility Structure Status

Generated at: `2026-10-31T07:02:47.814855+00:00`

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

- VIX: `19.420000076293945`
- VIX9D: `19.25`
- VIX3M: `20.780000686645508`
- VIX6M: `22.200000762939453`
- VVIX: `106.43000030517578`
- SKEW: `149.75999450683594`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5379`
- panic_release_score: `0.4271`
- tail_risk_score: `0.6115`
- option_stress_score: `0.4404`
- failed_bounce_options_risk: `0.4145`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-30 | 149.75999450683594 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-30 | 19.420000076293945 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-30 | 20.780000686645508 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-30 | 22.200000762939453 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-30 | 19.25 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-30 | 106.43000030517578 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
