# Flow / Positioning Proxy Status

Generated at: `2026-08-27T14:48:13.536456+00:00`
Latest date: `2026-08-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `75.77`
- overall_flow_conflict_score: `20.79`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 75.77 | 20.79 | 100.0 | 35.85 | -2.3844 | 0.2601 | 0.2111 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 75.77 | 20.79 | 100.0 | 35.85 | -2.1629 | 0.3004 | 0.2474 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 75.77 | 20.79 | 100.0 | 35.85 | -2.4645 | 0.2633 | 0.2472 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 75.77 | 20.79 | 100.0 | 35.85 | -1.8146 | 0.3097 | 0.2706 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
