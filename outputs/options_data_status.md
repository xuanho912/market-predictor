# Options / Volatility Structure Status

Generated at: `2026-10-13T02:10:05.634262+00:00`

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

- VIX: `15.210000038146973`
- VIX9D: `11.680000305175781`
- VIX3M: `17.93000030517578`
- VIX6M: `19.950000762939453`
- VVIX: `85.93000030517578`
- SKEW: `155.05999755859375`
- term_structure_state: `contango`
- volatility_reversal_score: `0.7407`
- panic_release_score: `0.4924`
- tail_risk_score: `0.3972`
- option_stress_score: `0.1714`
- failed_bounce_options_risk: `0.2237`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-12 | 155.05999755859375 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-12 | 15.210000038146973 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-12 | 17.93000030517578 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-12 | 19.950000762939453 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-12 | 11.680000305175781 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-12 | 85.93000030517578 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
