# Breadth Impact Audit

Generated at: `2026-09-02T08:10:00.782409Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `1`
- breadth_conflicts_primary_count: `2`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | False | True | WEAK_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0784 | 15 | 10 | SPY breadth conflicts with bounce_path: conflict score 65%, internal resonance is weak. | SPY breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| QQQ | False | True | WEAK_EDGE | WEAK_EDGE | analog_average_path | bearish_path | 0.1096 | -8 | -4 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is weak. | QQQ breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| IWM | False | False | WEAK_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0704 | 5 | 4 | IWM breadth is mixed for bounce_path: support score 49%, conflict score 52%, internal resonance is weak. | IWM breadth is useful context but not strong enough to validate the primary path by itself. |
| DIA | True | False | WEAK_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0613 | 13 | 2 | DIA breadth supports bounce_path: internal resonance is mixed, support score 75%, above 20d/50d MA 40%/57%. | DIA breadth improves confidence in the primary path, but forward validation is still required. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
