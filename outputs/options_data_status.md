# Options / Volatility Structure Status

Generated at: `2026-11-28T20:06:39.878919+00:00`

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

- VIX: `23.809999465942383`
- VIX9D: `24.100000381469727`
- VIX3M: `23.81999969482422`
- VIX6M: `25.020000457763672`
- VVIX: `107.83999633789062`
- SKEW: `145.89999389648438`
- term_structure_state: `normal`
- volatility_reversal_score: `0.9957`
- panic_release_score: `0.9532`
- tail_risk_score: `0.5914`
- option_stress_score: `0.4569`
- failed_bounce_options_risk: `0.4589`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-27 | 145.89999389648438 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-27 | 23.809999465942383 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-27 | 23.81999969482422 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-27 | 25.020000457763672 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-27 | 24.100000381469727 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-27 | 107.83999633789062 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
