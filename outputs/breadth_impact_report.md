# Breadth Impact Audit

Generated at: `2026-07-30T04:26:16.634168Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `2`
- breadth_conflicts_primary_count: `4`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | True | RISK_WARNING | RISK_WARNING | bounce_path | bearish_path | 0.1005 | -10 | -4 | SPY breadth supports bearish_path: internal resonance is surface_only, support score 98%, above 20d/50d MA 63%/68%. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | RISK_WARNING | RISK_WARNING | bounce_path | bearish_path | 0.2005 | -36 | -14 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | False | True | RISK_WARNING | RISK_WARNING | bounce_path | bearish_path | 0.1767 | -28 | -17 | IWM breadth conflicts with bearish_path: conflict score 59%, internal resonance is surface_only. | IWM index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| DIA | True | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0999 | -10 | -6 | DIA breadth supports bearish_path: internal resonance is surface_only, support score 98%, above 20d/50d MA 57%/63%. | DIA index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
