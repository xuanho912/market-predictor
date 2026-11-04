# Flow / Positioning Proxy Status

Generated at: `2026-11-04T19:49:58.544081+00:00`
Latest date: `2026-11-04`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `68.03`
- overall_flow_conflict_score: `71.56`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.46 | 71.56 | 80.82 | 100.0 | 0.0193 | 0.8648 | 1.0185 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.43 | 71.56 | 81.47 | 100.0 | 0.3111 | 0.9597 | 1.1465 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 70.13 | 71.56 | 83.01 | 100.0 | 0.3979 | 1.256 | 1.1145 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 73.1 | 71.56 | 83.98 | 100.0 | 1.9063 | 1.4427 | 1.4828 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
