# Breadth Impact Audit

Generated at: `2026-10-27T09:22:13.427043Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `3`
- breadth_conflicts_primary_count: `4`
- forward_validation_status: `forward_ready`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | True | WEAK_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1251 | -11 | -10 | SPY breadth supports bearish_path: internal resonance is surface_only, support score 92%, above 20d/50d MA 71%/58%. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | WEAK_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.2103 | -45 | -18 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | True | True | WEAK_EDGE | RISK_WARNING | bounce_path | bearish_path | 0.152 | -15 | -11 | IWM breadth is mixed for bearish_path: support score 60%, conflict score 52%, internal resonance is surface_only. | IWM index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| DIA | True | True | MODERATE_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1343 | -10 | 0 | DIA breadth supports bearish_path: internal resonance is surface_only, support score 89%, above 20d/50d MA 77%/63%. | DIA index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |

## Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
