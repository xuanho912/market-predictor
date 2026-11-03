# Options / Volatility Structure Status

Generated at: `2026-11-03T19:31:34.012113+00:00`

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

- VIX: `20.6200008392334`
- VIX9D: `21.559999465942383`
- VIX3M: `21.229999542236328`
- VIX6M: `22.389999389648438`
- VVIX: `107.33000183105469`
- SKEW: `152.77999877929688`
- term_structure_state: `normal`
- volatility_reversal_score: `0.5414`
- panic_release_score: `0.4764`
- tail_risk_score: `0.7024`
- option_stress_score: `0.6507`
- failed_bounce_options_risk: `0.6692`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-02 | 152.77999877929688 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-03 | 20.6200008392334 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-03 | 21.229999542236328 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-03 | 22.389999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-03 | 21.559999465942383 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-03 | 107.33000183105469 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
