# Options / Volatility Structure Status

Generated at: `2026-09-30T06:48:48.528507+00:00`

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

- VIX: `16.040000915527344`
- VIX9D: `14.210000038146973`
- VIX3M: `18.09000015258789`
- VIX6M: `20.200000762939453`
- VVIX: `89.70999908447266`
- SKEW: `144.5800018310547`
- term_structure_state: `contango`
- volatility_reversal_score: `0.53`
- panic_release_score: `0.3487`
- tail_risk_score: `0.3015`
- option_stress_score: `0.3139`
- failed_bounce_options_risk: `0.3287`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-29 | 144.5800018310547 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-29 | 16.040000915527344 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-29 | 18.09000015258789 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-29 | 20.200000762939453 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-29 | 14.210000038146973 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-29 | 89.70999908447266 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
