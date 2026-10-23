# Options / Volatility Structure Status

Generated at: `2026-10-23T23:59:29.559253+00:00`

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

- VIX: `19.450000762939453`
- VIX9D: `18.700000762939453`
- VIX3M: `20.479999542236328`
- VIX6M: `21.959999084472656`
- VVIX: `109.69999694824219`
- SKEW: `151.8000030517578`
- term_structure_state: `contango`
- volatility_reversal_score: `0.6238`
- panic_release_score: `0.506`
- tail_risk_score: `0.6565`
- option_stress_score: `0.4485`
- failed_bounce_options_risk: `0.428`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-23 | 151.8000030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-23 | 19.450000762939453 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-23 | 20.479999542236328 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-23 | 21.959999084472656 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-23 | 18.700000762939453 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-23 | 109.69999694824219 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
