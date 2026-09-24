# Options / Volatility Structure Status

Generated at: `2026-09-24T23:17:50.258368+00:00`

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

- VIX: `15.670000076293945`
- VIX9D: `14.109999656677246`
- VIX3M: `18.43000030517578`
- VIX6M: `20.350000381469727`
- VVIX: `90.56999969482422`
- SKEW: `146.0399932861328`
- term_structure_state: `contango`
- volatility_reversal_score: `0.84`
- panic_release_score: `0.6214`
- tail_risk_score: `0.354`
- option_stress_score: `0.157`
- failed_bounce_options_risk: `0.2071`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-24 | 146.0399932861328 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-24 | 15.670000076293945 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-24 | 18.43000030517578 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-24 | 20.350000381469727 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-24 | 14.109999656677246 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-24 | 90.56999969482422 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
