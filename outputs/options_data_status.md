# Options / Volatility Structure Status

Generated at: `2026-08-04T14:42:09.663217+00:00`

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

- VIX: `15.819999694824219`
- VIX9D: `13.649999618530273`
- VIX3M: `18.8700008392334`
- VIX6M: `21.190000534057617`
- VVIX: `88.77999877929688`
- SKEW: `139.9600067138672`
- term_structure_state: `contango`
- volatility_reversal_score: `0.9293`
- panic_release_score: `0.6908`
- tail_risk_score: `0.1414`
- option_stress_score: `0.0965`
- failed_bounce_options_risk: `0.1313`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-03 | 139.9600067138672 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-04 | 15.819999694824219 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-04 | 18.8700008392334 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-04 | 21.190000534057617 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-04 | 13.649999618530273 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-04 | 88.77999877929688 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
