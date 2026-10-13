# Options / Volatility Structure Status

Generated at: `2026-10-13T23:49:58.691806+00:00`

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

- VIX: `15.270000457763672`
- VIX9D: `11.989999771118164`
- VIX3M: `17.959999084472656`
- VIX6M: `19.920000076293945`
- VVIX: `85.37999725341797`
- SKEW: `154.74000549316406`
- term_structure_state: `contango`
- volatility_reversal_score: `0.693`
- panic_release_score: `0.4506`
- tail_risk_score: `0.3859`
- option_stress_score: `0.2935`
- failed_bounce_options_risk: `0.2951`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-13 | 154.74000549316406 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-13 | 15.270000457763672 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-13 | 17.959999084472656 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-13 | 19.920000076293945 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-13 | 11.989999771118164 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-13 | 85.37999725341797 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
