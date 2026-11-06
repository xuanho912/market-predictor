# Breadth Impact Audit

Generated at: `2026-11-06T07:59:00.530544Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `3`
- breadth_supports_primary_count: `3`
- breadth_conflicts_primary_count: `1`
- forward_validation_status: `forward_ready`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | False | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0228 | 9 | 0 | SPY breadth supports bearish_path: internal resonance is aligned, support score 98%, above 20d/50d MA 73%/68%. | SPY breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| QQQ | False | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1251 | -22 | -8 | QQQ breadth conflicts with bearish_path: conflict score 69%, internal resonance is weak. | QQQ breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| IWM | True | False | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0616 | 0 | 4 | IWM breadth is mixed for bearish_path: support score 63%, conflict score 42%, internal resonance is mixed. | IWM breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| DIA | True | False | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0083 | 9 | 0 | DIA breadth supports bearish_path: internal resonance is aligned, support score 99%, above 20d/50d MA 83%/77%. | DIA breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |

## Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
