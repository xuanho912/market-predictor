# Options / Volatility Structure Status

Generated at: `2026-06-18T00:01:36.111603+00:00`

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

- VIX: `18.440000534057617`
- VIX9D: `18.6299991607666`
- VIX3M: `20.6200008392334`
- VIX6M: `22.6200008392334`
- VVIX: `94.52999877929688`
- SKEW: `142.6199951171875`
- term_structure_state: `contango`
- volatility_reversal_score: `0.9729`
- panic_release_score: `0.8104`
- tail_risk_score: `0.2771`
- option_stress_score: `0.2763`
- failed_bounce_options_risk: `0.2585`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-17 | 142.6199951171875 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-17 | 18.440000534057617 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-17 | 20.6200008392334 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-17 | 22.6200008392334 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-17 | 18.6299991607666 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-17 | 94.52999877929688 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
