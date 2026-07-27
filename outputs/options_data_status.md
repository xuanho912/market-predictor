# Options / Volatility Structure Status

Generated at: `2026-07-27T15:16:16.702555+00:00`

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

- VIX: `18.889999389648438`
- VIX9D: `18.68000030517578`
- VIX3M: `20.43000030517578`
- VIX6M: `22.3799991607666`
- VVIX: `101.25`
- SKEW: `145.9499969482422`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5271`
- panic_release_score: `0.3871`
- tail_risk_score: `0.4836`
- option_stress_score: `0.5107`
- failed_bounce_options_risk: `0.4306`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-23 | 145.9499969482422 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-27 | 18.889999389648438 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-27 | 20.43000030517578 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-27 | 22.3799991607666 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-27 | 18.68000030517578 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-27 | 101.25 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
