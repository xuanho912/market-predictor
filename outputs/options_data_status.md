# Options / Volatility Structure Status

Generated at: `2026-07-12T13:58:54.974278+00:00`

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

- VIX: `15.029999732971191`
- VIX9D: `11.149999618530273`
- VIX3M: `18.56999969482422`
- VIX6M: `21.09000015258789`
- VVIX: `87.27999877929688`
- SKEW: `144.27000427246094`
- term_structure_state: `contango`
- volatility_reversal_score: `0.9867`
- panic_release_score: `0.78`
- tail_risk_score: `0.2155`
- option_stress_score: `0.0729`
- failed_bounce_options_risk: `0.1332`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-10 | 144.27000427246094 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-10 | 15.029999732971191 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-10 | 18.56999969482422 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-10 | 21.09000015258789 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-10 | 11.149999618530273 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-10 | 87.27999877929688 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
