# Flow / Positioning Proxy Status

Generated at: `2026-10-01T18:27:15.447599+00:00`
Latest date: `2026-10-01`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `62.73`
- overall_flow_conflict_score: `37.95`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.86 | 37.95 | 93.96 | 53.05 | -1.4259 | 0.7146 | 0.7057 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.1 | 37.95 | 96.0 | 53.05 | -0.8955 | 0.8678 | 0.8297 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.01 | 37.95 | 95.97 | 53.05 | 0.7105 | 1.1196 | 1.1395 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.96 | 37.95 | 94.98 | 53.05 | -0.059 | 1.2734 | 0.9885 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
