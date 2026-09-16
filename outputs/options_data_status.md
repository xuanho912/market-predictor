# Options / Volatility Structure Status

Generated at: `2026-09-16T16:59:16.860233+00:00`

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

- VIX: `16.790000915527344`
- VIX9D: `16.440000534057617`
- VIX3M: `19.219999313354492`
- VIX6M: `20.670000076293945`
- VVIX: `94.81999969482422`
- SKEW: `146.61000061035156`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.4247`
- option_stress_score: `0.4048`
- failed_bounce_options_risk: `0.3658`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-15 | 146.61000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-16 | 16.790000915527344 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-16 | 19.219999313354492 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-16 | 20.670000076293945 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-16 | 16.440000534057617 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-16 | 94.81999969482422 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
