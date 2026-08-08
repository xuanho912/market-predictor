# Flow / Positioning Proxy Status

Generated at: `2026-08-08T03:02:32.709471+00:00`
Latest date: `2026-08-07`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.22`
- overall_flow_conflict_score: `22.0`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.54 | 22.0 | 67.63 | 37.93 | -0.6043 | 0.7768 | 0.8593 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.82 | 22.0 | 67.06 | 37.93 | -1.092 | 0.6589 | 0.7023 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.18 | 22.0 | 67.51 | 37.93 | -0.8764 | 0.8394 | 0.8258 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.33 | 22.0 | 66.57 | 37.93 | -1.4169 | 0.4376 | 0.5204 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
