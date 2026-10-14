# Options / Volatility Structure Status

Generated at: `2026-10-14T17:14:37.234545+00:00`

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

- VIX: `16.469999313354492`
- VIX9D: `13.670000076293945`
- VIX3M: `18.579999923706055`
- VIX6M: `20.360000610351562`
- VVIX: `94.2300033569336`
- SKEW: `154.74000549316406`
- term_structure_state: `contango`
- volatility_reversal_score: `0.624`
- panic_release_score: `0.4075`
- tail_risk_score: `0.5261`
- option_stress_score: `0.4161`
- failed_bounce_options_risk: `0.4188`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-13 | 154.74000549316406 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-14 | 16.469999313354492 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-14 | 18.579999923706055 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-14 | 20.360000610351562 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-14 | 13.670000076293945 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-14 | 94.2300033569336 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
