# Breadth Impact Audit

Generated at: `2026-07-07T21:51:11.525611Z`

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
| SPY | True | False | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0287 | 0 | 9 | SPY breadth supports bounce_path: internal resonance is aligned, support score 98%, above 20d/50d MA 68%/67%. | SPY breadth improves confidence in the primary path, but forward validation is still required. |
| QQQ | True | False | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0388 | 0 | 10 | QQQ breadth supports bounce_path: internal resonance is mixed, support score 95%, above 20d/50d MA 56%/55%. | QQQ breadth improves confidence in the primary path, but forward validation is still required. |
| IWM | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0372 | 0 | 6 | IWM breadth is mixed for bounce_path: support score 64%, conflict score 25%, internal resonance is mixed. | IWM breadth is useful context but not strong enough to validate the primary path by itself. |
| DIA | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.021 | 0 | 10 | DIA breadth supports bounce_path: internal resonance is aligned, support score 98%, above 20d/50d MA 73%/67%. | DIA breadth improves confidence in the primary path, but forward validation is still required. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
