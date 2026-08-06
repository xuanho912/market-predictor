# Options / Volatility Structure Status

Generated at: `2026-08-06T00:09:42.173603+00:00`

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

- VIX: `15.8100004196167`
- VIX9D: `13.789999961853027`
- VIX3M: `18.950000762939453`
- VIX6M: `21.059999465942383`
- VVIX: `90.43000030517578`
- SKEW: `133.32000732421875`
- term_structure_state: `contango`
- volatility_reversal_score: `1.0`
- panic_release_score: `0.78`
- tail_risk_score: `0.1121`
- option_stress_score: `0.0787`
- failed_bounce_options_risk: `0.1157`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-05 | 133.32000732421875 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-05 | 15.8100004196167 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-05 | 18.950000762939453 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-05 | 21.059999465942383 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-05 | 13.789999961853027 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-05 | 90.43000030517578 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
