# Breadth Impact Audit

Generated at: `2026-10-30T02:12:39.321382Z`

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
| SPY | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0443 | 0 | 0 | SPY breadth supports bounce_path: internal resonance is aligned, support score 90%, above 20d/50d MA 73%/59%. | SPY breadth improves confidence in the primary path, but forward validation is still required. |
| QQQ | False | True | MODERATE_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1829 | -20 | -6 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0582 | 0 | 0 | IWM breadth supports bounce_path: internal resonance is mixed, support score 68%. | IWM breadth improves confidence in the primary path, but forward validation is still required. |
| DIA | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0619 | 0 | 0 | DIA breadth supports bounce_path: internal resonance is aligned, support score 88%, above 20d/50d MA 73%/63%. | DIA breadth improves confidence in the primary path, but forward validation is still required. |

## Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
