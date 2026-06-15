# Breadth Impact Audit

Generated at: `2026-06-15T14:29:14.620397Z`

## Summary

- data_completeness_without_true_breadth: `86`
- data_completeness_with_true_breadth: `90`
- changed_symbol_count: `4`
- breadth_supports_primary_count: `4`
- breadth_conflicts_primary_count: `0`
- forward_validation_status: `not_enough_forward_samples`
- conclusion: `breadth improves information quality, not proven alpha yet.`

## Symbol Impact

| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |
|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|
| SPY | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0237 | 0 | 10 | SPY breadth supports bounce_path: internal resonance is aligned, support score 98%, above 20d/50d MA 71%/60%. | SPY breadth improves confidence in the primary path, but forward validation is still required. |
| QQQ | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0445 | 0 | 10 | QQQ breadth supports bounce_path: internal resonance is mixed, support score 79%, above 20d/50d MA 54%/51%. | QQQ breadth improves confidence in the primary path, but forward validation is still required. |
| IWM | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0303 | 0 | 7 | IWM breadth supports bounce_path: internal resonance is mixed, support score 78%. | IWM breadth improves confidence in the primary path, but forward validation is still required. |
| DIA | True | False | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0271 | 0 | 10 | DIA breadth supports bounce_path: internal resonance is aligned, support score 91%, above 20d/50d MA 63%/67%. | DIA breadth improves confidence in the primary path, but forward validation is still required. |

## Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

## Guardrail

- Breadth improves information quality, not proven alpha yet.
- If completed samples are insufficient, keep status as not_enough_forward_samples.
- Alpha v1 threshold remains frozen at 0.32534311.
