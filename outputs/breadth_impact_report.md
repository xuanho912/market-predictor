# Breadth Impact Audit

Generated at: `2026-07-09T22:54:31.033140Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `3`
- breadth_conflicts_primary_count: `1`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | False | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0434 | 0 | 8 | SPY breadth supports bounce_path: internal resonance is mixed, support score 85%, above 20d/50d MA 67%/67%. | SPY breadth improves confidence in the primary path, but forward validation is still required. |
| QQQ | False | True | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0957 | 0 | -3 | QQQ breadth conflicts with bounce_path: conflict score 66%, internal resonance is weak. | QQQ breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| IWM | True | False | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.046 | 0 | 4 | IWM breadth is mixed for bounce_path: support score 58%, conflict score 32%, internal resonance is mixed. | IWM breadth is useful context but not strong enough to validate the primary path by itself. |
| DIA | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0313 | 0 | 8 | DIA breadth supports bounce_path: internal resonance is aligned, support score 98%, above 20d/50d MA 63%/63%. | DIA breadth improves confidence in the primary path, but forward validation is still required. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
