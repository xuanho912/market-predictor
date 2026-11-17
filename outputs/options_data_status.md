# Options / Volatility Structure Status

Generated at: `2026-11-17T04:10:21.251989+00:00`

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

- VIX: `22.90999984741211`
- VIX9D: `23.149999618530273`
- VIX3M: `23.020000457763672`
- VIX6M: `23.790000915527344`
- VVIX: `114.2300033569336`
- SKEW: `146.3300018310547`
- term_structure_state: `normal`
- volatility_reversal_score: `0.5462`
- panic_release_score: `0.5062`
- tail_risk_score: `0.6301`
- option_stress_score: `0.6341`
- failed_bounce_options_risk: `0.6385`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-16 | 146.3300018310547 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-16 | 22.90999984741211 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-16 | 23.020000457763672 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-16 | 23.790000915527344 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-16 | 23.149999618530273 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-16 | 114.2300033569336 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
