# Options / Volatility Structure Status

Generated at: `2026-09-15T23:01:47.545041+00:00`

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

- VIX: `17.200000762939453`
- VIX9D: `17.209999084472656`
- VIX3M: `19.360000610351562`
- VIX6M: `20.760000228881836`
- VVIX: `94.91000366210938`
- SKEW: `146.61000061035156`
- term_structure_state: `contango`
- volatility_reversal_score: `0.501`
- panic_release_score: `0.33`
- tail_risk_score: `0.4263`
- option_stress_score: `0.4295`
- failed_bounce_options_risk: `0.4085`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-15 | 146.61000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-15 | 17.200000762939453 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-15 | 19.360000610351562 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-15 | 20.760000228881836 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-15 | 17.209999084472656 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-15 | 94.91000366210938 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
