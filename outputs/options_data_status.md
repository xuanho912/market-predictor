# Options / Volatility Structure Status

Generated at: `2026-09-30T18:03:54.236068+00:00`

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

- VIX: `15.829999923706055`
- VIX9D: `13.600000381469727`
- VIX3M: `18.079999923706055`
- VIX6M: `20.15999984741211`
- VVIX: `88.69999694824219`
- SKEW: `144.5800018310547`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.2879`
- option_stress_score: `0.299`
- failed_bounce_options_risk: `0.2883`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-29 | 144.5800018310547 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-30 | 15.829999923706055 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-30 | 18.079999923706055 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-30 | 20.15999984741211 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-30 | 13.600000381469727 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-30 | 88.69999694824219 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
