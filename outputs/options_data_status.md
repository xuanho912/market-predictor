# Options / Volatility Structure Status

Generated at: `2026-07-30T14:34:38.250240+00:00`

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

- VIX: `18.440000534057617`
- VIX9D: `16.90999984741211`
- VIX3M: `20.209999084472656`
- VIX6M: `22.18000030517578`
- VVIX: `100.31999969482422`
- SKEW: `139.5500030517578`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5633`
- panic_release_score: `0.3796`
- tail_risk_score: `0.3253`
- option_stress_score: `0.325`
- failed_bounce_options_risk: `0.2938`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-29 | 139.5500030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-30 | 18.440000534057617 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-30 | 20.209999084472656 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-30 | 22.18000030517578 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-30 | 16.90999984741211 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-30 | 100.31999969482422 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
