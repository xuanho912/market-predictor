# Breadth Impact Audit

Generated at: `2026-07-08T21:39:03.090356Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `90`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `4`
- breadth_conflicts_primary_count: `0`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | False | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0434 | 0 | 10 | SPY breadth supports bounce_path: internal resonance is mixed, support score 85%, above 20d/50d MA 67%/67%. | SPY breadth improves confidence in the primary path, but forward validation is still required. |
| QQQ | True | False | WEAK_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0386 | 8 | 7 | QQQ breadth supports bounce_path: internal resonance is mixed, support score 66%, above 20d/50d MA 53%/52%. | QQQ breadth improves confidence in the primary path, but forward validation is still required. |
| IWM | True | False | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0481 | 0 | 6 | IWM breadth is mixed for bounce_path: support score 57%, conflict score 33%, internal resonance is mixed. | IWM breadth is useful context but not strong enough to validate the primary path by itself. |
| DIA | True | False | WEAK_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0149 | 15 | 13 | DIA breadth supports bounce_path: internal resonance is aligned, support score 98%, above 20d/50d MA 63%/63%. | DIA breadth improves confidence in the primary path, but forward validation is still required. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
