# Options / Volatility Structure Status

Generated at: `2026-06-17T00:01:18.119550+00:00`

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

- VIX: `16.40999984741211`
- VIX9D: `15.770000457763672`
- VIX3M: `19.530000686645508`
- VIX6M: `21.8700008392334`
- VVIX: `87.69000244140625`
- SKEW: `142.66000366210938`
- term_structure_state: `contango`
- volatility_reversal_score: `1.0`
- panic_release_score: `0.78`
- tail_risk_score: `0.1774`
- option_stress_score: `0.1415`
- failed_bounce_options_risk: `0.1633`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-16 | 142.66000366210938 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-16 | 16.40999984741211 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-16 | 19.530000686645508 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-16 | 21.8700008392334 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-16 | 15.770000457763672 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-16 | 87.69000244140625 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
