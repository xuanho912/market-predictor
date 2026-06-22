# Breadth Impact Audit

Generated at: `2026-06-22T23:54:32.823478Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `90`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `2`
- breadth_conflicts_primary_count: `2`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | False | True | STRONG_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1707 | 0 | -1 | SPY breadth conflicts with bounce_path: conflict score 76%, internal resonance is surface_only. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | STRONG_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.179 | 0 | -1 | QQQ breadth conflicts with bounce_path: conflict score 82%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0294 | 0 | 6 | IWM breadth supports bounce_path: internal resonance is mixed, support score 74%. | IWM breadth improves confidence in the primary path, but forward validation is still required. |
| DIA | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0552 | 0 | 9 | DIA breadth supports bounce_path: internal resonance is mixed, support score 85%, above 20d/50d MA 53%/60%. | DIA breadth improves confidence in the primary path, but forward validation is still required. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
