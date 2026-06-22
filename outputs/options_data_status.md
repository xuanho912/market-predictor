# Options / Volatility Structure Status

Generated at: `2026-06-22T17:42:32.562712+00:00`

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

- VIX: `17.25`
- VIX9D: `16.239999771118164`
- VIX3M: `19.780000686645508`
- VIX6M: `22.239999771118164`
- VVIX: `91.94999694824219`
- SKEW: `146.72000122070312`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5769`
- panic_release_score: `0.3914`
- tail_risk_score: `0.3246`
- option_stress_score: `0.2842`
- failed_bounce_options_risk: `0.2712`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-18 | 146.72000122070312 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-22 | 17.25 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-22 | 19.780000686645508 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-22 | 22.239999771118164 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-22 | 16.239999771118164 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-22 | 91.94999694824219 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
