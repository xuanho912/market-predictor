# Options / Volatility Structure Status

Generated at: `2026-07-06T14:44:14.711567+00:00`

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

- VIX: `16.040000915527344`
- VIX9D: `13.479999542236328`
- VIX3M: `18.940000534057617`
- VIX6M: `21.299999237060547`
- VVIX: `90.33000183105469`
- SKEW: `150.02000427246094`
- term_structure_state: `contango`
- volatility_reversal_score: `0.895`
- panic_release_score: `0.6686`
- tail_risk_score: `0.3478`
- option_stress_score: `0.1707`
- failed_bounce_options_risk: `0.2135`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-02 | 150.02000427246094 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-06 | 16.040000915527344 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-06 | 18.940000534057617 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-06 | 21.299999237060547 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-06 | 13.479999542236328 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-06 | 90.33000183105469 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
