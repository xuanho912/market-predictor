# Options / Volatility Structure Status

Generated at: `2026-06-22T16:01:34.396912+00:00`

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

- VIX: `17.219999313354492`
- VIX9D: `16.18000030517578`
- VIX3M: `19.75`
- VIX6M: `22.239999771118164`
- VVIX: `91.54000091552734`
- SKEW: `146.72000122070312`
- term_structure_state: `contango`
- volatility_reversal_score: `0.581`
- panic_release_score: `0.3957`
- tail_risk_score: `0.314`
- option_stress_score: `0.2781`
- failed_bounce_options_risk: `0.2657`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-18 | 146.72000122070312 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-22 | 17.219999313354492 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-22 | 19.75 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-22 | 22.239999771118164 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-22 | 16.18000030517578 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-22 | 91.54000091552734 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
