# Options / Volatility Structure Status

Generated at: `2026-10-30T10:29:32.656083+00:00`

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

- VIX: `18.5`
- VIX9D: `15.869999885559082`
- VIX3M: `19.3700008392334`
- VIX6M: `21.239999771118164`
- VVIX: `98.01000213623047`
- SKEW: `151.02999877929688`
- term_structure_state: `normal`
- volatility_reversal_score: `0.6807`
- panic_release_score: `0.4931`
- tail_risk_score: `0.5856`
- option_stress_score: `0.437`
- failed_bounce_options_risk: `0.445`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-29 | 151.02999877929688 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-30 | 18.5 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-29 | 19.3700008392334 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-29 | 21.239999771118164 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-29 | 15.869999885559082 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-29 | 98.01000213623047 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
