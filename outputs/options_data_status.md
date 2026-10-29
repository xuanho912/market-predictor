# Options / Volatility Structure Status

Generated at: `2026-10-29T01:15:41.528908+00:00`

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

- VIX: `16.90999984741211`
- VIX9D: `15.600000381469727`
- VIX3M: `19.219999313354492`
- VIX6M: `21.239999771118164`
- VVIX: `96.61000061035156`
- SKEW: `148.74000549316406`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.4975`
- option_stress_score: `0.4394`
- failed_bounce_options_risk: `0.3969`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-28 | 148.74000549316406 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-28 | 16.90999984741211 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-28 | 19.219999313354492 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-28 | 21.239999771118164 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-28 | 15.600000381469727 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-28 | 96.61000061035156 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
