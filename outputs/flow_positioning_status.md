# Flow / Positioning Proxy Status

Generated at: `2026-11-26T03:46:15.189209+00:00`
Latest date: `2026-11-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `62.54`
- overall_flow_conflict_score: `73.47`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.75 | 73.47 | 77.17 | 100.0 | 0.2684 | 0.8429 | 1.1588 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.43 | 73.47 | 78.05 | 100.0 | 0.6479 | 1.0345 | 1.336 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 62.73 | 73.47 | 77.49 | 100.0 | 0.4996 | 0.9697 | 1.207 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.25 | 73.47 | 77.01 | 100.0 | 0.2141 | 1.0146 | 1.1236 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
