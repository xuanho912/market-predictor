# Flow / Positioning Proxy Status

Generated at: `2026-07-04T04:55:58.136089+00:00`
Latest date: `2026-07-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.94`
- overall_flow_conflict_score: `61.98`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.45 | 61.98 | 79.19 | 91.75 | -0.4954 | 1.0063 | 0.8938 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 61.18 | 61.98 | 77.79 | 91.75 | -0.208 | 1.1372 | 0.9494 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.42 | 61.98 | 76.89 | 91.75 | -1.2196 | 0.7801 | 0.6986 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.7 | 61.98 | 78.29 | 91.75 | -1.4897 | 0.8052 | 0.6436 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
