# Options / Volatility Structure Status

Generated at: `2026-08-10T13:47:58.343174+00:00`

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
- VIX9D: `13.1899995803833`
- VIX3M: `18.969999313354492`
- VIX6M: `21.149999618530273`
- VVIX: `92.13999938964844`
- SKEW: `132.57000732421875`
- term_structure_state: `contango`
- volatility_reversal_score: `0.7553`
- panic_release_score: `0.5078`
- tail_risk_score: `0.1452`
- option_stress_score: `0.0943`
- failed_bounce_options_risk: `0.1309`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-07 | 132.57000732421875 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-10 | 15.390000343322754 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-10 | 18.969999313354492 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-10 | 21.149999618530273 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-10 | 13.1899995803833 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-10 | 92.13999938964844 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
