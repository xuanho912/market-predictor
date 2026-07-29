# Breadth Impact Audit

Generated at: `2026-07-29T21:26:31.585455Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `2`
- breadth_conflicts_primary_count: `4`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | True | STRONG_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0907 | -1 | -3 | SPY breadth supports bounce_path: internal resonance is surface_only, support score 98%, above 20d/50d MA 63%/68%. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | STRONG_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.2016 | -37 | -17 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | False | True | STRONG_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1669 | -19 | -3 | IWM breadth conflicts with bearish_path: conflict score 59%, internal resonance is surface_only. | IWM index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| DIA | True | True | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0998 | -10 | 3 | DIA breadth supports bearish_path: internal resonance is surface_only, support score 98%, above 20d/50d MA 57%/63%. | DIA index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
