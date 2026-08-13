# Options / Volatility Structure Status

Generated at: `2026-08-13T21:12:21.520144+00:00`

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

- VIX: `14.630000114440918`
- VIX9D: `11.369999885559082`
- VIX3M: `18.610000610351562`
- VIX6M: `20.93000030517578`
- VVIX: `89.41999816894531`
- SKEW: `136.5399932861328`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8397`
- panic_release_score: `0.5624`
- tail_risk_score: `0.1162`
- option_stress_score: `0.0484`
- failed_bounce_options_risk: `0.0999`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-12 | 136.5399932861328 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-13 | 14.630000114440918 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-13 | 18.610000610351562 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-13 | 20.93000030517578 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-13 | 11.369999885559082 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-13 | 89.41999816894531 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
