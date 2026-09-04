# Options / Volatility Structure Status

Generated at: `2026-09-04T16:25:16.349787+00:00`

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

- VIX: `14.039999961853027`
- VIX9D: `11.34000015258789`
- VIX3M: `17.239999771118164`
- VIX6M: `19.610000610351562`
- VVIX: `82.27999877929688`
- SKEW: `150.6300048828125`
- term_structure_state: `contango`
- volatility_reversal_score: `0.651`
- panic_release_score: `0.4395`
- tail_risk_score: `0.3373`
- option_stress_score: `0.1143`
- failed_bounce_options_risk: `0.1803`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-03 | 150.6300048828125 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-04 | 14.039999961853027 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-04 | 17.239999771118164 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-04 | 19.610000610351562 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-04 | 11.34000015258789 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-04 | 82.27999877929688 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
