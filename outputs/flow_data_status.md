# Flow / Positioning Proxy Status

Generated at: `2026-08-21T20:47:50.613893+00:00`
Latest date: `2026-08-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `74.47`
- overall_flow_conflict_score: `19.44`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 73.39 | 19.44 | 100.0 | 33.52 | -0.7922 | 0.9293 | 0.7817 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 73.36 | 19.44 | 100.0 | 33.52 | -0.6733 | 0.9229 | 0.7787 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 77.72 | 19.44 | 100.0 | 33.52 | 0.5945 | 1.3449 | 1.1572 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 73.43 | 19.44 | 100.0 | 33.52 | -0.5542 | 1.0094 | 0.7862 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
