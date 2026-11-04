# Options / Volatility Structure Status

Generated at: `2026-11-04T03:01:39.626076+00:00`

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

- VIX: `20.829999923706055`
- VIX9D: `21.959999084472656`
- VIX3M: `21.270000457763672`
- VIX6M: `22.309999465942383`
- VVIX: `107.4000015258789`
- SKEW: `150.00999450683594`
- term_structure_state: `stress`
- volatility_reversal_score: `0.1824`
- panic_release_score: `0.3224`
- tail_risk_score: `0.837`
- option_stress_score: `0.8532`
- failed_bounce_options_risk: `0.9515`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-03 | 150.00999450683594 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-03 | 20.829999923706055 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-03 | 21.270000457763672 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-03 | 22.309999465942383 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-03 | 21.959999084472656 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-03 | 107.4000015258789 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
