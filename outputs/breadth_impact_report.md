# Breadth Impact Audit

Generated at: `2026-09-08T22:50:10.614808Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `1`
- breadth_conflicts_primary_count: `4`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | False | True | WEAK_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1608 | -10 | 3 | SPY breadth conflicts with bearish_path: conflict score 62%, internal resonance is surface_only. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | WEAK_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1818 | -19 | -10 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | False | True | WEAK_EDGE | WEAK_EDGE | bounce_path | bounce_path | 0.1376 | -1 | 2 | IWM breadth is mixed for bounce_path: support score 51%, conflict score 52%, internal resonance is surface_only. | IWM index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| DIA | True | True | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.1031 | 7 | 0 | DIA breadth supports bearish_path: internal resonance is surface_only, support score 96%, above 20d/50d MA 53%/50%. | DIA index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
