# Flow / Positioning Proxy Status

Generated at: `2026-11-24T22:30:29.780155+00:00`
Latest date: `2026-11-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.87`
- overall_flow_conflict_score: `71.86`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.17 | 71.86 | 71.59 | 100.0 | 0.0157 | 0.7202 | 1.0361 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.11 | 71.86 | 71.24 | 100.0 | -0.1673 | 0.717 | 0.9419 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.73 | 71.86 | 71.78 | 100.0 | 0.1292 | 0.8445 | 1.0668 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.48 | 71.86 | 71.37 | 100.0 | -0.0835 | 0.8743 | 0.9754 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
