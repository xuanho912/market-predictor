# Options / Volatility Structure Status

Generated at: `2026-08-05T14:35:49.894027+00:00`

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

- VIX: `16.920000076293945`
- VIX9D: `16.15999984741211`
- VIX3M: `19.440000534057617`
- VIX6M: `21.360000610351562`
- VVIX: `92.61000061035156`
- SKEW: `126.41000366210938`
- term_structure_state: `contango`
- volatility_reversal_score: `0.95`
- panic_release_score: `0.78`
- tail_risk_score: `0.1487`
- option_stress_score: `0.1685`
- failed_bounce_options_risk: `0.1724`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-04 | 126.41000366210938 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-05 | 16.920000076293945 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-05 | 19.440000534057617 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-05 | 21.360000610351562 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-05 | 16.15999984741211 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-05 | 92.61000061035156 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
