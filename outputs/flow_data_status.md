# Flow / Positioning Proxy Status

Generated at: `2026-10-30T18:09:17.094458+00:00`
Latest date: `2026-10-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.84`
- overall_flow_conflict_score: `72.41`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.92 | 72.41 | 71.08 | 100.0 | -0.6717 | 0.8947 | 0.7793 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 62.85 | 72.41 | 73.36 | 100.0 | 0.742 | 1.4421 | 1.2787 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.46 | 72.41 | 71.92 | 100.0 | -1.5763 | 0.6523 | 0.5132 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.11 | 72.41 | 71.8 | 100.0 | -0.045 | 1.162 | 0.9786 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
