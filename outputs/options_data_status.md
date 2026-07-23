# Options / Volatility Structure Status

Generated at: `2026-07-23T14:41:56.746420+00:00`

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

- VIX: `19.040000915527344`
- VIX9D: `18.6200008392334`
- VIX3M: `20.889999389648438`
- VIX6M: `22.65999984741211`
- VVIX: `104.4000015258789`
- SKEW: `150.19000244140625`
- term_structure_state: `contango`
- volatility_reversal_score: `0.529`
- panic_release_score: `0.399`
- tail_risk_score: `0.5901`
- option_stress_score: `0.5466`
- failed_bounce_options_risk: `0.5264`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-22 | 150.19000244140625 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-23 | 19.040000915527344 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-23 | 20.889999389648438 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-23 | 22.65999984741211 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-23 | 18.6200008392334 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-23 | 104.4000015258789 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
