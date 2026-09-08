# Options / Volatility Structure Status

Generated at: `2026-09-08T16:41:16.789215+00:00`

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

- VIX: `15.319999694824219`
- VIX9D: `14.149999618530273`
- VIX3M: `18.149999618530273`
- VIX6M: `20.139999389648438`
- VVIX: `88.20999908447266`
- SKEW: `151.5800018310547`
- term_structure_state: `contango`
- volatility_reversal_score: `0.67`
- panic_release_score: `0.4757`
- tail_risk_score: `0.3859`
- option_stress_score: `0.1672`
- failed_bounce_options_risk: `0.2191`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-04 | 151.5800018310547 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-08 | 15.319999694824219 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-08 | 18.149999618530273 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-08 | 20.139999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-08 | 14.149999618530273 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-08 | 88.20999908447266 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
