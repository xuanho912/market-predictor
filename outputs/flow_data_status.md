# Flow / Positioning Proxy Status

Generated at: `2026-11-10T02:50:26.083453+00:00`
Latest date: `2026-11-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.38`
- overall_flow_conflict_score: `72.21`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 68.67 | 72.21 | 84.61 | 100.0 | 0.066 | 0.757 | 1.065 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.3 | 72.21 | 83.18 | 100.0 | 0.1401 | 0.7652 | 1.0984 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 70.02 | 72.21 | 85.05 | 100.0 | 0.3425 | 0.9476 | 1.1381 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.55 | 72.21 | 83.92 | 100.0 | -0.2421 | 0.5976 | 0.883 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
