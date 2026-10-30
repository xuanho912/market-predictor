# Flow / Positioning Proxy Status

Generated at: `2026-10-30T00:11:16.363750+00:00`
Latest date: `2026-10-29`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.08`
- overall_flow_conflict_score: `67.62`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.89 | 67.62 | 72.5 | 100.0 | -0.6952 | 0.8377 | 0.7604 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 62.71 | 67.62 | 72.77 | 100.0 | -0.4745 | 0.7973 | 0.8352 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.82 | 67.62 | 72.47 | 100.0 | -0.8768 | 0.9745 | 0.7537 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.89 | 67.62 | 71.19 | 100.0 | -0.7015 | 1.0478 | 0.8409 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
