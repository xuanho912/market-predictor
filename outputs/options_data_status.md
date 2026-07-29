# Options / Volatility Structure Status

Generated at: `2026-07-29T14:33:47.643306+00:00`

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

- VIX: `19.690000534057617`
- VIX9D: `19.290000915527344`
- VIX3M: `20.670000076293945`
- VIX6M: `22.420000076293945`
- VVIX: `102.37999725341797`
- SKEW: `142.97999572753906`
- term_structure_state: `normal`
- volatility_reversal_score: `0.5348`
- panic_release_score: `0.4348`
- tail_risk_score: `0.469`
- option_stress_score: `0.5609`
- failed_bounce_options_risk: `0.566`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-28 | 142.97999572753906 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-29 | 19.690000534057617 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-29 | 20.670000076293945 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-29 | 22.420000076293945 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-29 | 19.290000915527344 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-29 | 102.37999725341797 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
