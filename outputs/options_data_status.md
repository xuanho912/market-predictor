# Options / Volatility Structure Status

Generated at: `2026-10-14T23:21:32.876815+00:00`

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

- VIX: `16.8700008392334`
- VIX9D: `14.59000015258789`
- VIX3M: `18.790000915527344`
- VIX6M: `20.489999771118164`
- VVIX: `94.44999694824219`
- SKEW: `157.3000030517578`
- term_structure_state: `contango`
- volatility_reversal_score: `0.584`
- panic_release_score: `0.3825`
- tail_risk_score: `0.5365`
- option_stress_score: `0.4395`
- failed_bounce_options_risk: `0.4438`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-14 | 157.3000030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-14 | 16.8700008392334 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-14 | 18.790000915527344 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-14 | 20.489999771118164 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-14 | 14.59000015258789 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-14 | 94.44999694824219 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
