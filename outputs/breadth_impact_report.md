# Breadth Impact Audit

Generated at: `2026-07-18T05:53:51.751855Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `85`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `2`
- breadth_conflicts_primary_count: `2`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | False | RISK_WARNING | RISK_WARNING | bounce_path | bounce_path | 0.0556 | 1 | 10 | SPY breadth supports bounce_path: internal resonance is mixed, support score 67%, above 20d/50d MA 62%/66%. | SPY breadth improves confidence in the primary path, but forward validation is still required. |
| QQQ | False | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1326 | -4 | -3 | QQQ breadth conflicts with bearish_path: conflict score 88%, internal resonance is weak. | QQQ breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |
| IWM | True | False | RISK_WARNING | RISK_WARNING | bounce_path | bearish_path | 0.058 | 1 | 7 | IWM breadth is mixed for bearish_path: support score 58%, conflict score 40%, internal resonance is weak. | IWM breadth is useful context but not strong enough to validate the primary path by itself. |
| DIA | False | True | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0841 | 5 | 0 | DIA breadth conflicts with bearish_path: conflict score 61%, internal resonance is mixed. | DIA breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
