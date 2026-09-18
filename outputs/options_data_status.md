# Options / Volatility Structure Status

Generated at: `2026-09-18T16:27:26.998908+00:00`

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

- VIX: `15.390000343322754`
- VIX9D: `12.84000015258789`
- VIX3M: `18.600000381469727`
- VIX6M: `20.420000076293945`
- VVIX: `88.83000183105469`
- SKEW: `145.6999969482422`
- term_structure_state: `contango`
- volatility_reversal_score: `0.575`
- panic_release_score: `0.3943`
- tail_risk_score: `0.3131`
- option_stress_score: `0.1522`
- failed_bounce_options_risk: `0.1963`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-17 | 145.6999969482422 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-18 | 15.390000343322754 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-18 | 18.600000381469727 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-18 | 20.420000076293945 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-18 | 12.84000015258789 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-18 | 88.83000183105469 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
