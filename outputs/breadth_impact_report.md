# Breadth Impact Audit

Generated at: `2026-10-21T23:36:14.172994Z`

## Summary

- data_completeness_without_true_breadth: `80`
- data_completeness_with_true_breadth: `79`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `2`
- breadth_conflicts_primary_count: `4`
- forward_validation_status: `forward_ready`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | True | STRONG_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1272 | -2 | 0 | SPY breadth supports bounce_path: internal resonance is surface_only, support score 86%, above 20d/50d MA 65%/43%. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | STRONG_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.2005 | -36 | -13 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | False | True | STRONG_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1699 | -23 | -3 | IWM breadth conflicts with bearish_path: conflict score 58%, internal resonance is surface_only. | IWM index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| DIA | True | True | STRONG_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1095 | -5 | 2 | DIA breadth supports bounce_path: internal resonance is surface_only, support score 97%, above 20d/50d MA 67%/43%. | DIA index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |

## Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
