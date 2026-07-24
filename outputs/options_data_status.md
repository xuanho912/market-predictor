# Options / Volatility Structure Status

Generated at: `2026-07-24T14:15:19.852483+00:00`

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

- VIX: `18.6299991607666`
- VIX9D: `17.809999465942383`
- VIX3M: `20.559999465942383`
- VIX6M: `22.489999771118164`
- VVIX: `100.69000244140625`
- SKEW: `145.9499969482422`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5727`
- panic_release_score: `0.3996`
- tail_risk_score: `0.4745`
- option_stress_score: `0.3766`
- failed_bounce_options_risk: `0.352`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-23 | 145.9499969482422 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-24 | 18.6299991607666 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-24 | 20.559999465942383 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-24 | 22.489999771118164 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-24 | 17.809999465942383 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-24 | 100.69000244140625 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
