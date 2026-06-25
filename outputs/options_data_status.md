# Options / Volatility Structure Status

Generated at: `2026-06-25T05:18:30.988679+00:00`

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
- VIX9D: `13.930000305175781`
- VIX3M: `19.56999969482422`
- VIX6M: `21.989999771118164`
- VVIX: `95.58000183105469`
- SKEW: `145.3000030517578`
- term_structure_state: `normal`
- volatility_reversal_score: `0.5252`
- panic_release_score: `0.3752`
- tail_risk_score: `0.4121`
- option_stress_score: `0.5244`
- failed_bounce_options_risk: `0.5138`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-24 | 145.3000030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-24 | 18.6299991607666 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-18 | 19.56999969482422 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-18 | 21.989999771118164 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-18 | 13.930000305175781 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-24 | 95.58000183105469 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
