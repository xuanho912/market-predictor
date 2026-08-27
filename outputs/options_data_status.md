# Options / Volatility Structure Status

Generated at: `2026-08-27T01:03:26.849683+00:00`

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

- VIX: `15.210000038146973`
- VIX9D: `13.329999923706055`
- VIX3M: `17.989999771118164`
- VIX6M: `20.639999389648438`
- VVIX: `85.23999786376953`
- SKEW: `142.9600067138672`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8`
- panic_release_score: `0.6706`
- tail_risk_score: `0.1871`
- option_stress_score: `0.2004`
- failed_bounce_options_risk: `0.2057`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-26 | 142.9600067138672 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-26 | 15.210000038146973 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-26 | 17.989999771118164 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-26 | 20.639999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-26 | 13.329999923706055 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-26 | 85.23999786376953 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
