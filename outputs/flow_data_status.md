# Flow / Positioning Proxy Status

Generated at: `2026-06-18T00:01:36.117627+00:00`
Latest date: `2026-06-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `80.57`
- overall_flow_conflict_score: `22.74`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 81.91 | 22.74 | 100.0 | 35.18 | 1.5959 | 1.2847 | 1.5414 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 77.43 | 22.74 | 100.0 | 35.18 | -0.1021 | 0.818 | 0.9583 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 81.91 | 22.74 | 100.0 | 35.18 | 1.3858 | 1.1933 | 1.3393 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 81.03 | 22.74 | 100.0 | 35.18 | 0.8882 | 1.0825 | 1.1996 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
