# Options / Volatility Structure Status

Generated at: `2026-10-06T18:25:29.468852+00:00`

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

- VIX: `15.039999961853027`
- VIX9D: `12.229999542236328`
- VIX3M: `17.6299991607666`
- VIX6M: `19.84000015258789`
- VVIX: `82.0199966430664`
- SKEW: `143.0399932861328`
- term_structure_state: `contango`
- volatility_reversal_score: `0.7347`
- panic_release_score: `0.5154`
- tail_risk_score: `0.19`
- option_stress_score: `0.0943`
- failed_bounce_options_risk: `0.1399`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-05 | 143.0399932861328 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-06 | 15.039999961853027 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-06 | 17.6299991607666 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-06 | 19.84000015258789 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-06 | 12.229999542236328 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-06 | 82.0199966430664 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
