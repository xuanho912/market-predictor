# Options / Volatility Structure Status

Generated at: `2026-07-03T23:39:38.098528+00:00`

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
- VIX9D: `16.799999237060547`
- VIX3M: `20.1299991607666`
- VIX6M: `22.260000228881836`
- VVIX: `88.80000305175781`
- SKEW: `150.02000427246094`
- term_structure_state: `contango`
- volatility_reversal_score: `0.9333`
- panic_release_score: `0.7014`
- tail_risk_score: `0.3401`
- option_stress_score: `0.1652`
- failed_bounce_options_risk: `0.2151`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-02 | 150.02000427246094 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-03 | 15.8100004196167 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-26 | 20.1299991607666 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-26 | 22.260000228881836 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-26 | 16.799999237060547 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-02 | 88.80000305175781 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
