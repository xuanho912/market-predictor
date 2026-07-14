# Breadth Impact Audit

Generated at: `2026-07-14T00:04:38.072190Z`

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
| SPY | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0567 | 0 | 8 | SPY breadth supports bounce_path: internal resonance is mixed, support score 67%, above 20d/50d MA 62%/66%. | SPY breadth improves confidence in the primary path, but forward validation is still required. |
| QQQ | False | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0957 | 0 | -4 | QQQ breadth conflicts with bounce_path: conflict score 66%, internal resonance is weak. | QQQ breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| IWM | False | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0672 | 0 | 4 | IWM breadth is mixed for bounce_path: support score 50%, conflict score 46%, internal resonance is weak. | IWM breadth is useful context but not strong enough to validate the primary path by itself. |
| DIA | False | True | WEAK_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0841 | 5 | 5 | DIA breadth conflicts with bounce_path: conflict score 61%, internal resonance is mixed. | DIA breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
