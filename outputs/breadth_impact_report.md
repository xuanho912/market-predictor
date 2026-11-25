# Breadth Impact Audit

Generated at: `2026-11-25T05:25:41.158340Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `1`
- breadth_conflicts_primary_count: `3`
- forward_validation_status: `forward_ready`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | False | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1296 | -17 | -1 | SPY breadth conflicts with bearish_path: conflict score 76%, internal resonance is weak. | SPY breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| QQQ | False | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1283 | -25 | -9 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is weak. | QQQ breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| IWM | True | False | RISK_WARNING | RISK_WARNING | bounce_path | bounce_path | 0.072 | 0 | 0 | IWM breadth is mixed for bounce_path: support score 64%, conflict score 49%, internal resonance is weak. | IWM breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| DIA | False | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1417 | -28 | -11 | DIA breadth conflicts with bearish_path: conflict score 76%, internal resonance is weak. | DIA breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |

## Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
