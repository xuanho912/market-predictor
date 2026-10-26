# Breadth Impact Audit

Generated at: `2026-10-26T18:44:21.846017Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `3`
- breadth_conflicts_primary_count: `1`
- forward_validation_status: `forward_ready`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | False | WEAK_EDGE | WEAK_EDGE | bounce_path | bounce_path | 0.0534 | 0 | 2 | SPY breadth supports bounce_path: internal resonance is mixed, support score 92%, above 20d/50d MA 71%/58%. | SPY breadth improves confidence in the primary path, but forward validation is still required. |
| QQQ | False | True | WEAK_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1284 | -25 | -11 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is weak. | QQQ breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| IWM | True | False | WEAK_EDGE | WEAK_EDGE | bounce_path | bounce_path | 0.08 | -5 | 1 | IWM breadth is mixed for bounce_path: support score 60%, conflict score 51%, internal resonance is mixed. | IWM breadth is useful context but not strong enough to validate the primary path by itself. |
| DIA | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0578 | 5 | 0 | DIA breadth supports bounce_path: internal resonance is aligned, support score 89%, above 20d/50d MA 77%/63%. | DIA breadth improves confidence in the primary path, but forward validation is still required. |

## Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
