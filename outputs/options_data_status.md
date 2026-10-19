# Options / Volatility Structure Status

Generated at: `2026-10-19T18:46:29.905223+00:00`

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

- VIX: `18.43000030517578`
- VIX9D: `17.950000762939453`
- VIX3M: `19.6299991607666`
- VIX6M: `21.170000076293945`
- VVIX: `105.0199966430664`
- SKEW: `168.58999633789062`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5224`
- panic_release_score: `0.3574`
- tail_risk_score: `0.6786`
- option_stress_score: `0.5595`
- failed_bounce_options_risk: `0.5739`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-16 | 168.58999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-19 | 18.43000030517578 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-19 | 19.6299991607666 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-19 | 21.170000076293945 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-19 | 17.950000762939453 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-19 | 105.0199966430664 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
