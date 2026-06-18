# Breadth Impact Audit

Generated at: `2026-06-18T00:01:55.186696Z`

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
| SPY | False | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1798 | -8 | -1 | SPY breadth conflicts with bounce_path: conflict score 76%, internal resonance is surface_only. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bearish_path | 0.1923 | -12 | -1 | QQQ breadth conflicts with bearish_path: conflict score 82%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0283 | 0 | 5 | IWM breadth supports bounce_path: internal resonance is mixed, support score 76%. | IWM breadth improves confidence in the primary path, but forward validation is still required. |
| DIA | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0486 | 6 | 11 | DIA breadth supports bounce_path: internal resonance is mixed, support score 85%, above 20d/50d MA 53%/60%. | DIA breadth improves confidence in the primary path, but forward validation is still required. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
