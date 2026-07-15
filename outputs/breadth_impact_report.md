# Breadth Impact Audit

Generated at: `2026-07-15T14:12:59.553678Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `0`
- breadth_conflicts_primary_count: `4`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | False | True | MODERATE_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.174 | -22 | 0 | SPY breadth conflicts with bearish_path: conflict score 61%, internal resonance is surface_only. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bearish_path | 0.2015 | -12 | -4 | QQQ breadth conflicts with bearish_path: conflict score 88%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | False | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1276 | 0 | -3 | IWM breadth is mixed for bounce_path: support score 51%, conflict score 46%, internal resonance is surface_only. | IWM index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| DIA | False | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bearish_path | 0.1496 | 0 | 0 | DIA breadth conflicts with bearish_path: conflict score 61%, internal resonance is surface_only. | DIA index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
