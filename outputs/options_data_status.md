# Options / Volatility Structure Status

Generated at: `2026-09-17T17:02:53.603827+00:00`

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

- VIX: `15.5600004196167`
- VIX9D: `13.850000381469727`
- VIX3M: `18.56999969482422`
- VIX6M: `20.309999465942383`
- VVIX: `88.05999755859375`
- SKEW: `145.9499969482422`
- term_structure_state: `contango`
- volatility_reversal_score: `0.925`
- panic_release_score: `0.6838`
- tail_risk_score: `0.3094`
- option_stress_score: `0.1298`
- failed_bounce_options_risk: `0.1833`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-16 | 145.9499969482422 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-17 | 15.5600004196167 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-17 | 18.56999969482422 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-17 | 20.309999465942383 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-17 | 13.850000381469727 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-17 | 88.05999755859375 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
