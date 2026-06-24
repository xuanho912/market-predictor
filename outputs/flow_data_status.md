# Flow / Positioning Proxy Status

Generated at: `2026-06-24T23:47:11.963188+00:00`
Latest date: `2026-06-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.61`
- overall_flow_conflict_score: `35.25`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.66 | 35.25 | 79.57 | 49.01 | -0.8356 | 0.6527 | 0.7566 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.05 | 35.25 | 79.7 | 49.01 | -0.5874 | 0.8137 | 0.7921 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.8 | 35.25 | 81.91 | 49.01 | -0.1865 | 0.9656 | 0.9625 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.95 | 35.25 | 79.67 | 49.01 | -1.0388 | 0.7176 | 0.7837 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
