# Options / Volatility Structure Status

Generated at: `2026-10-30T18:09:17.088468+00:00`

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

- VIX: `21.600000381469727`
- VIX9D: `21.690000534057617`
- VIX3M: `21.850000381469727`
- VIX6M: `22.860000610351562`
- VVIX: `116.81999969482422`
- SKEW: `151.02999877929688`
- term_structure_state: `normal`
- volatility_reversal_score: `0.5452`
- panic_release_score: `0.5002`
- tail_risk_score: `0.7189`
- option_stress_score: `0.6579`
- failed_bounce_options_risk: `0.6474`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-29 | 151.02999877929688 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-30 | 21.600000381469727 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-30 | 21.850000381469727 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-30 | 22.860000610351562 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-30 | 21.690000534057617 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-30 | 116.81999969482422 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
