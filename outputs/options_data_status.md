# Options / Volatility Structure Status

Generated at: `2026-09-23T01:03:43.867491+00:00`

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

- VIX: `14.210000038146973`
- VIX9D: `12.130000114440918`
- VIX3M: `17.610000610351562`
- VIX6M: `19.790000915527344`
- VVIX: `83.16999816894531`
- SKEW: `144.8000030517578`
- term_structure_state: `contango`
- volatility_reversal_score: `1.0`
- panic_release_score: `0.78`
- tail_risk_score: `0.236`
- option_stress_score: `0.0524`
- failed_bounce_options_risk: `0.126`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-22 | 144.8000030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-22 | 14.210000038146973 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-22 | 17.610000610351562 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-22 | 19.790000915527344 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-22 | 12.130000114440918 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-22 | 83.16999816894531 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
