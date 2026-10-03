# Options / Volatility Structure Status

Generated at: `2026-10-03T00:44:26.978155+00:00`

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

- VIX: `15.3100004196167`
- VIX9D: `12.0600004196167`
- VIX3M: `18.010000228881836`
- VIX6M: `20.149999618530273`
- VVIX: `87.0199966430664`
- SKEW: `144.8800048828125`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.2674`
- option_stress_score: `0.2675`
- failed_bounce_options_risk: `0.2616`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-02 | 144.8800048828125 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-02 | 15.3100004196167 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-02 | 18.010000228881836 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-02 | 20.149999618530273 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-02 | 12.0600004196167 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-02 | 87.0199966430664 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
