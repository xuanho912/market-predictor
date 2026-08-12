# Options / Volatility Structure Status

Generated at: `2026-08-12T13:49:54.362052+00:00`

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

- VIX: `14.899999618530273`
- VIX9D: `11.720000267028809`
- VIX3M: `18.809999465942383`
- VIX6M: `21.010000228881836`
- VVIX: `91.98999786376953`
- SKEW: `135.58999633789062`
- term_structure_state: `contango`
- volatility_reversal_score: `0.7287`
- panic_release_score: `0.5081`
- tail_risk_score: `0.1516`
- option_stress_score: `0.0746`
- failed_bounce_options_risk: `0.1213`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-11 | 135.58999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-12 | 14.899999618530273 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-12 | 18.809999465942383 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-12 | 21.010000228881836 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-12 | 11.720000267028809 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-12 | 91.98999786376953 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
