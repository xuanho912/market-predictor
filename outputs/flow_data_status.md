# Flow / Positioning Proxy Status

Generated at: `2026-07-24T14:15:19.865947+00:00`
Latest date: `2026-07-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `49.0`
- overall_flow_conflict_score: `50.7`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 49.0 | 50.7 | 59.53 | 87.41 | -3.0844 | 0.1003 | 0.0974 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 49.0 | 50.7 | 59.53 | 87.41 | -2.7905 | 0.2028 | 0.1956 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 49.0 | 50.7 | 59.53 | 87.41 | -2.6027 | 0.1655 | 0.17 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 49.0 | 50.7 | 59.53 | 87.41 | -2.7591 | 0.2461 | 0.2372 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
