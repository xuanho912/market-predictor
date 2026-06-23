# Options / Volatility Structure Status

Generated at: `2026-06-23T23:39:07.443238+00:00`

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

- VIX: `19.489999771118164`
- VIX9D: `19.469999313354492`
- VIX3M: `21.059999465942383`
- VIX6M: `22.969999313354492`
- VVIX: `99.5`
- SKEW: `143.13999938964844`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5329`
- panic_release_score: `0.4229`
- tail_risk_score: `0.3932`
- option_stress_score: `0.4953`
- failed_bounce_options_risk: `0.4833`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-23 | 143.13999938964844 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-23 | 19.489999771118164 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-23 | 21.059999465942383 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-23 | 22.969999313354492 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-23 | 19.469999313354492 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-23 | 99.5 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
