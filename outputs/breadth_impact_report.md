# Breadth Impact Audit

Generated at: `2026-07-20T14:37:00.677193Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `2`
- breadth_conflicts_primary_count: `1`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | False | WEAK_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0476 | 8 | 2 | SPY breadth is mixed for bounce_path: support score 61%, conflict score 39%, internal resonance is mixed. | SPY breadth is useful context but not strong enough to validate the primary path by itself. |
| QQQ | False | True | MODERATE_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1239 | -21 | -13 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is weak. | QQQ breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| IWM | False | False | WEAK_EDGE | WEAK_EDGE | bounce_path | bounce_path | 0.0714 | 0 | 2 | IWM breadth is mixed for bounce_path: support score 55%, conflict score 49%, internal resonance is weak. | IWM breadth is useful context but not strong enough to validate the primary path by itself. |
| DIA | True | False | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0644 | 9 | 7 | DIA breadth is mixed for bearish_path: support score 58%, conflict score 51%, internal resonance is mixed. | DIA breadth is useful context but not strong enough to validate the primary path by itself. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
