# Options / Volatility Structure Status

Generated at: `2026-09-11T00:39:31.659170+00:00`

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

- VIX: `17.84000015258789`
- VIX9D: `17.700000762939453`
- VIX3M: `19.729999542236328`
- VIX6M: `21.170000076293945`
- VVIX: `102.66000366210938`
- SKEW: `147.02000427246094`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5119`
- panic_release_score: `0.2919`
- tail_risk_score: `0.5504`
- option_stress_score: `0.4997`
- failed_bounce_options_risk: `0.5229`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-10 | 147.02000427246094 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-10 | 17.84000015258789 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-10 | 19.729999542236328 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-10 | 21.170000076293945 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-10 | 17.700000762939453 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-10 | 102.66000366210938 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
