# Flow / Positioning Proxy Status

Generated at: `2026-07-21T14:25:45.417501+00:00`
Latest date: `2026-07-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `51.21`
- overall_flow_conflict_score: `52.32`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 49.99 | 52.32 | 61.52 | 88.32 | -3.2245 | 0.1225 | 0.1147 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 49.99 | 52.32 | 61.52 | 88.32 | -2.8553 | 0.1809 | 0.1644 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 54.87 | 52.32 | 63.12 | 88.32 | -2.6443 | 0.1739 | 0.1676 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 49.99 | 52.32 | 61.52 | 88.32 | -2.5593 | 0.282 | 0.2444 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
