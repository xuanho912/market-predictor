# Options / Volatility Structure Status

Generated at: `2026-10-16T22:56:28.938436+00:00`

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

- VIX: `19.989999771118164`
- VIX9D: `20.1200008392334`
- VIX3M: `20.5`
- VIX6M: `21.670000076293945`
- VVIX: `109.91000366210938`
- SKEW: `168.58999633789062`
- term_structure_state: `normal`
- volatility_reversal_score: `0.5386`
- panic_release_score: `0.4586`
- tail_risk_score: `0.7441`
- option_stress_score: `0.6521`
- failed_bounce_options_risk: `0.7245`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-16 | 168.58999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-16 | 19.989999771118164 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-16 | 20.5 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-16 | 21.670000076293945 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-16 | 20.1200008392334 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-16 | 109.91000366210938 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
