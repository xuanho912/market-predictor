# Options / Volatility Structure Status

Generated at: `2026-07-27T21:35:33.955379+00:00`

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

- VIX: `18.670000076293945`
- VIX9D: `18.1299991607666`
- VIX3M: `20.200000762939453`
- VIX6M: `22.110000610351562`
- VVIX: `100.91000366210938`
- SKEW: `146.60000610351562`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5243`
- panic_release_score: `0.3693`
- tail_risk_score: `0.493`
- option_stress_score: `0.5077`
- failed_bounce_options_risk: `0.4284`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-27 | 146.60000610351562 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-27 | 18.670000076293945 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-27 | 20.200000762939453 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-27 | 22.110000610351562 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-27 | 18.1299991607666 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-27 | 100.91000366210938 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
