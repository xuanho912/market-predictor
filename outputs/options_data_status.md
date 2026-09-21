# Options / Volatility Structure Status

Generated at: `2026-09-21T18:15:39.768237+00:00`

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

- VIX: `15.050000190734863`
- VIX9D: `13.420000076293945`
- VIX3M: `18.149999618530273`
- VIX6M: `20.139999389648438`
- VVIX: `86.18000030517578`
- SKEW: `148.10000610351562`
- term_structure_state: `contango`
- volatility_reversal_score: `0.9217`
- panic_release_score: `0.6729`
- tail_risk_score: `0.3213`
- option_stress_score: `0.1141`
- failed_bounce_options_risk: `0.177`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-18 | 148.10000610351562 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-21 | 15.050000190734863 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-21 | 18.149999618530273 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-21 | 20.139999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-21 | 13.420000076293945 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-21 | 86.18000030517578 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
