# Breadth Impact Audit

Generated at: `2026-08-05T21:41:46.376978Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `3`
- breadth_conflicts_primary_count: `4`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1102 | 0 | 1 | SPY breadth is mixed for bounce_path: support score 59%, conflict score 34%, internal resonance is surface_only. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1608 | 0 | -6 | QQQ breadth conflicts with bounce_path: conflict score 69%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | True | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.127 | 0 | 1 | IWM breadth is mixed for bounce_path: support score 58%, conflict score 46%, internal resonance is surface_only. | IWM index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| DIA | True | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0991 | 0 | 1 | DIA breadth supports bounce_path: internal resonance is surface_only, support score 96%, above 20d/50d MA 50%/60%. | DIA index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
