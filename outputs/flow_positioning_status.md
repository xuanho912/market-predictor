# Flow / Positioning Proxy Status

Generated at: `2026-09-10T08:25:28.871968+00:00`
Latest date: `2026-09-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `46.73`
- overall_flow_conflict_score: `32.81`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 45.54 | 32.81 | 57.91 | 46.11 | -0.6761 | 0.8489 | 0.8955 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 45.18 | 32.81 | 57.79 | 46.11 | -0.6654 | 0.8924 | 0.8628 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 49.37 | 32.81 | 59.17 | 46.11 | 0.5896 | 1.0264 | 1.1397 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 46.81 | 32.81 | 58.33 | 46.11 | 0.9876 | 1.1075 | 1.2964 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
