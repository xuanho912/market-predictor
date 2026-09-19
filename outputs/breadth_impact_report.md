# Breadth Impact Audit

Generated at: `2026-09-19T15:55:59.701352Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `0`
- breadth_conflicts_primary_count: `4`
- forward_validation_status: `forward_ready`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | False | True | STRONG_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1721 | -1 | -2 | SPY breadth conflicts with bounce_path: conflict score 76%, internal resonance is surface_only. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | STRONG_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1608 | 0 | -7 | QQQ breadth conflicts with bounce_path: conflict score 69%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | False | True | WEAK_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1708 | -10 | -6 | IWM breadth conflicts with bearish_path: conflict score 68%, internal resonance is surface_only. | IWM index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| DIA | False | True | STRONG_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1721 | -1 | -2 | DIA breadth conflicts with bounce_path: conflict score 76%, internal resonance is surface_only. | DIA index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |

## Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
