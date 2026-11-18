# Options / Volatility Structure Status

Generated at: `2026-11-18T20:34:44.390252+00:00`

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

- VIX: `24.510000228881836`
- VIX9D: `24.18000030517578`
- VIX3M: `24.309999465942383`
- VIX6M: `24.729999542236328`
- VVIX: `117.30999755859375`
- SKEW: `145.11000061035156`
- term_structure_state: `backwardation`
- volatility_reversal_score: `0.1905`
- panic_release_score: `0.373`
- tail_risk_score: `0.7284`
- option_stress_score: `0.7846`
- failed_bounce_options_risk: `0.9342`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-17 | 145.11000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-18 | 24.510000228881836 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-18 | 24.309999465942383 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-18 | 24.729999542236328 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-18 | 24.18000030517578 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-18 | 117.30999755859375 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
