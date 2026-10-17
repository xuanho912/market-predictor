# Breadth Impact Audit

Generated at: `2026-10-17T01:25:36.978546Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `2`
- breadth_conflicts_primary_count: `3`
- forward_validation_status: `forward_ready`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1047 | -2 | 0 | SPY breadth supports bearish_path: internal resonance is surface_only, support score 97%, above 20d/50d MA 61%/38%. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1862 | -23 | -11 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is surface_only. | QQQ index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| IWM | False | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.163 | 0 | 1 | IWM breadth conflicts with bearish_path: conflict score 71%, internal resonance is surface_only. | IWM index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| DIA | True | False | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0302 | 9 | 5 | DIA breadth supports bearish_path: internal resonance is mixed, support score 97%, above 20d/50d MA 60%/43%. | DIA index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |

## Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
