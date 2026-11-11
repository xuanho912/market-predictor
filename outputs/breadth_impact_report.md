# Breadth Impact Audit

Generated at: `2026-11-11T19:38:56.760016Z`

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
| SPY | True | False | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0704 | 0 | 8 | SPY breadth is mixed for bounce_path: support score 62%, conflict score 48%, internal resonance is mixed. | SPY breadth is useful context but not strong enough to validate the primary path by itself. |
| QQQ | False | True | STRONG_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.2015 | -37 | -16 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | True | False | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0317 | 0 | 5 | IWM breadth supports bounce_path: internal resonance is mixed, support score 76%. | IWM breadth improves confidence in the primary path, but forward validation is still required. |
| DIA | True | False | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.043 | 0 | 8 | DIA breadth supports bounce_path: internal resonance is mixed, support score 73%, above 20d/50d MA 70%/73%. | DIA breadth improves confidence in the primary path, but forward validation is still required. |

## Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
