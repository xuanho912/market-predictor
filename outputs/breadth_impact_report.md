# Breadth Impact Audit

Generated at: `2026-11-10T04:24:39.714769Z`

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
| SPY | False | True | RISK_WARNING | RISK_WARNING | bounce_path | bearish_path | 0.1943 | -28 | -11 | SPY breadth conflicts with bearish_path: conflict score 71%, internal resonance is surface_only. | SPY index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |
| QQQ | False | True | RISK_WARNING | RISK_WARNING | bounce_path | bearish_path | 0.1404 | -36 | -13 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is weak. | QQQ breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| IWM | True | False | RISK_WARNING | RISK_WARNING | bounce_path | bounce_path | 0.0418 | 0 | 0 | IWM breadth supports bounce_path: internal resonance is mixed, support score 78%. | IWM breadth improves confidence in the primary path, but forward validation is still required. |
| DIA | True | True | MODERATE_EDGE | RISK_WARNING | bounce_path | bearish_path | 0.1471 | -10 | 0 | DIA breadth is mixed for bearish_path: support score 58%, conflict score 52%, internal resonance is surface_only. | DIA index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens. |

## Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
