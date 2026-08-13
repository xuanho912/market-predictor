# Flow / Positioning Proxy Status

Generated at: `2026-08-13T13:50:40.137427+00:00`
Latest date: `2026-08-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `73.8`
- overall_flow_conflict_score: `19.4`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 73.8 | 19.4 | 96.95 | 33.45 | -2.7815 | 0.0807 | 0.0629 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 73.8 | 19.4 | 96.95 | 33.45 | -2.3973 | 0.1679 | 0.1212 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 73.8 | 19.4 | 96.95 | 33.45 | -2.7923 | 0.1663 | 0.1273 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 73.8 | 19.4 | 96.95 | 33.45 | -2.2553 | 0.1315 | 0.1018 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
