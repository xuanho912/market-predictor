# Breadth Impact Audit

Generated at: `2026-06-24T05:13:59.198695Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `90`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `1`
- breadth_conflicts_primary_count: `3`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | False | True | STRONG_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1154 | -4 | -1 | SPY breadth conflicts with bounce_path: conflict score 76%, internal resonance is weak. | SPY breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| QQQ | False | True | STRONG_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1198 | -8 | -1 | QQQ breadth conflicts with bounce_path: conflict score 76%, internal resonance is weak. | QQQ breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| IWM | True | False | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0353 | 0 | 6 | IWM breadth supports bounce_path: internal resonance is mixed, support score 71%. | IWM breadth improves confidence in the primary path, but forward validation is still required. |
| DIA | False | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0812 | 4 | 9 | DIA breadth conflicts with bounce_path: conflict score 59%, internal resonance is mixed. | DIA breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
