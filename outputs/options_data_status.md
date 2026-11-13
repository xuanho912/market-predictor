# Options / Volatility Structure Status

Generated at: `2026-11-13T08:03:41.347729+00:00`

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

- VIX: `18.700000762939453`
- VIX9D: `17.510000228881836`
- VIX3M: `20.059999465942383`
- VIX6M: `21.709999084472656`
- VVIX: `96.70999908447266`
- SKEW: `150.16000366210938`
- term_structure_state: `contango`
- volatility_reversal_score: `0.9748`
- panic_release_score: `0.8223`
- tail_risk_score: `0.5137`
- option_stress_score: `0.3499`
- failed_bounce_options_risk: `0.3452`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-12 | 150.16000366210938 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-12 | 18.700000762939453 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-12 | 20.059999465942383 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-12 | 21.709999084472656 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-12 | 17.510000228881836 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-12 | 96.70999908447266 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
