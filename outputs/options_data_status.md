# Options / Volatility Structure Status

Generated at: `2026-10-23T17:11:34.400854+00:00`

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

- VIX: `19.959999084472656`
- VIX9D: `19.84000015258789`
- VIX3M: `20.739999771118164`
- VIX6M: `22.100000381469727`
- VVIX: `111.33000183105469`
- SKEW: `152.38999938964844`
- term_structure_state: `normal`
- volatility_reversal_score: `0.5431`
- panic_release_score: `0.4599`
- tail_risk_score: `0.7116`
- option_stress_score: `0.5201`
- failed_bounce_options_risk: `0.5159`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-22 | 152.38999938964844 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-23 | 19.959999084472656 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-23 | 20.739999771118164 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-23 | 22.100000381469727 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-23 | 19.84000015258789 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-23 | 111.33000183105469 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
