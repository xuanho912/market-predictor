# Options / Volatility Structure Status

Generated at: `2026-07-29T21:26:10.742550+00:00`

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

- VIX: `20.65999984741211`
- VIX9D: `20.3799991607666`
- VIX3M: `21.5`
- VIX6M: `23.059999465942383`
- VVIX: `109.47000122070312`
- SKEW: `139.5500030517578`
- term_structure_state: `normal`
- volatility_reversal_score: `0.5405`
- panic_release_score: `0.4705`
- tail_risk_score: `0.4578`
- option_stress_score: `0.5692`
- failed_bounce_options_risk: `0.5926`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-29 | 139.5500030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-29 | 20.65999984741211 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-29 | 21.5 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-29 | 23.059999465942383 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-29 | 20.3799991607666 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-29 | 109.47000122070312 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
