# Breadth Impact Audit

Generated at: `2026-07-03T23:39:58.197479Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `90`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `3`
- breadth_conflicts_primary_count: `1`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0358 | 0 | 10 | SPY breadth supports bounce_path: internal resonance is mixed, support score 97%, above 20d/50d MA 65%/65%. | SPY breadth improves confidence in the primary path, but forward validation is still required. |
| QQQ | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0483 | 0 | 9 | QQQ breadth supports bounce_path: internal resonance is mixed, support score 88%, above 20d/50d MA 50%/50%. | QQQ breadth improves confidence in the primary path, but forward validation is still required. |
| IWM | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0401 | -2 | 2 | IWM breadth supports bounce_path: internal resonance is mixed, support score 70%. | IWM breadth improves confidence in the primary path, but forward validation is still required. |
| DIA | False | True | MODERATE_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1902 | -30 | -12 | DIA breadth conflicts with bearish_path: conflict score 67%, internal resonance is surface_only. | DIA index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
