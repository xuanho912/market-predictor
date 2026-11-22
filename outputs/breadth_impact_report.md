# Breadth Impact Audit

Generated at: `2026-11-22T19:44:09.676288Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `0`
- breadth_conflicts_primary_count: `3`
- forward_validation_status: `forward_ready`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | False | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1208 | -9 | 0 | SPY breadth conflicts with bearish_path: conflict score 76%, internal resonance is weak. | SPY breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| QQQ | False | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1195 | -17 | -7 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is weak. | QQQ breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| IWM | False | False | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0768 | 0 | 3 | IWM breadth is mixed for bearish_path: support score 52%, conflict score 53%, internal resonance is weak. | IWM breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| DIA | False | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1318 | -19 | 0 | DIA breadth conflicts with bearish_path: conflict score 76%, internal resonance is weak. | DIA breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |

## Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
