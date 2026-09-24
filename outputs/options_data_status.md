# Options / Volatility Structure Status

Generated at: `2026-09-24T17:16:48.717335+00:00`

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

- VIX: `15.399999618530273`
- VIX9D: `13.829999923706055`
- VIX3M: `18.239999771118164`
- VIX6M: `20.190000534057617`
- VVIX: `89.41000366210938`
- SKEW: `146.14999389648438`
- term_structure_state: `contango`
- volatility_reversal_score: `0.885`
- panic_release_score: `0.66`
- tail_risk_score: `0.3412`
- option_stress_score: `0.1392`
- failed_bounce_options_risk: `0.1948`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-23 | 146.14999389648438 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-24 | 15.399999618530273 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-24 | 18.239999771118164 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-24 | 20.190000534057617 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-24 | 13.829999923706055 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-24 | 89.41000366210938 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
