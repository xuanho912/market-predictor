# Options / Volatility Structure Status

Generated at: `2026-06-24T23:47:11.957109+00:00`

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
- VIX9D: `18.06999969482422`
- VIX3M: `20.3700008392334`
- VIX6M: `22.399999618530273`
- VVIX: `95.58000183105469`
- SKEW: `145.3000030517578`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5252`
- panic_release_score: `0.3752`
- tail_risk_score: `0.3671`
- option_stress_score: `0.4719`
- failed_bounce_options_risk: `0.4385`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-24 | 145.3000030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-24 | 18.6299991607666 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-24 | 20.3700008392334 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-24 | 22.399999618530273 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-24 | 18.06999969482422 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-24 | 95.58000183105469 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
