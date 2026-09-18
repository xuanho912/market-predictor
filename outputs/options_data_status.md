# Options / Volatility Structure Status

Generated at: `2026-09-18T01:16:18.546277+00:00`

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

- VIX: `15.4399995803833`
- VIX9D: `13.390000343322754`
- VIX3M: `18.549999237060547`
- VIX6M: `20.299999237060547`
- VVIX: `87.72000122070312`
- SKEW: `145.6999969482422`
- term_structure_state: `contango`
- volatility_reversal_score: `0.957`
- panic_release_score: `0.7085`
- tail_risk_score: `0.2965`
- option_stress_score: `0.1184`
- failed_bounce_options_risk: `0.1744`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-17 | 145.6999969482422 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-17 | 15.4399995803833 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-17 | 18.549999237060547 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-17 | 20.299999237060547 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-17 | 13.390000343322754 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-17 | 87.72000122070312 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
