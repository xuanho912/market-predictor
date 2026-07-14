# Breadth Impact Audit

Generated at: `2026-07-14T21:30:11.087857Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `0`
- breadth_conflicts_primary_count: `3`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | False | True | MODERATE_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1652 | -14 | 0 | SPY breadth conflicts with bearish_path: conflict score 61%, internal resonance is surface_only. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | WEAK_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1612 | -5 | -1 | QQQ breadth conflicts with bearish_path: conflict score 66%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | False | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0635 | 6 | 6 | IWM breadth is mixed for bounce_path: support score 50%, conflict score 48%, internal resonance is weak. | IWM breadth is useful context but not strong enough to validate the primary path by itself. |
| DIA | False | True | WEAK_EDGE | MODERATE_EDGE | bearish_path | bounce_path | 0.0742 | 14 | 8 | DIA breadth conflicts with bounce_path: conflict score 61%, internal resonance is mixed. | DIA breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
