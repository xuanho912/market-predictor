# Flow / Positioning Proxy Status

Generated at: `2026-07-15T06:01:09.159690+00:00`
Latest date: `2026-07-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `45.94`
- overall_flow_conflict_score: `29.24`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 48.77 | 29.24 | 56.38 | 47.44 | -1.0155 | 0.9922 | 0.7502 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 49.35 | 29.24 | 56.57 | 47.44 | -0.9467 | 1.0854 | 0.8032 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 43.76 | 29.24 | 54.74 | 47.44 | -0.8421 | 1.0409 | 0.7387 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 41.87 | 29.24 | 54.12 | 47.44 | -1.3257 | 0.764 | 0.5563 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
