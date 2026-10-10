# Options / Volatility Structure Status

Generated at: `2026-10-10T01:58:28.369079+00:00`

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

- VIX: `14.84000015258789`
- VIX9D: `11.260000228881836`
- VIX3M: `17.770000457763672`
- VIX6M: `19.860000610351562`
- VVIX: `84.87999725341797`
- SKEW: `154.33999633789062`
- term_structure_state: `contango`
- volatility_reversal_score: `0.6783`
- panic_release_score: `0.4596`
- tail_risk_score: `0.3786`
- option_stress_score: `0.1437`
- failed_bounce_options_risk: `0.2048`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-09 | 154.33999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-09 | 14.84000015258789 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-09 | 17.770000457763672 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-09 | 19.860000610351562 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-09 | 11.260000228881836 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-09 | 84.87999725341797 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
