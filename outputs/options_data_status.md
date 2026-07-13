# Options / Volatility Structure Status

Generated at: `2026-07-13T15:14:37.884152+00:00`

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

- VIX: `16.270000457763672`
- VIX9D: `13.5600004196167`
- VIX3M: `19.25`
- VIX6M: `21.43000030517578`
- VVIX: `92.31999969482422`
- SKEW: `144.27000427246094`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8`
- panic_release_score: `0.5281`
- tail_risk_score: `0.2818`
- option_stress_score: `0.3015`
- failed_bounce_options_risk: `0.2897`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-10 | 144.27000427246094 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-13 | 16.270000457763672 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-13 | 19.25 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-13 | 21.43000030517578 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-13 | 13.5600004196167 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-13 | 92.31999969482422 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
