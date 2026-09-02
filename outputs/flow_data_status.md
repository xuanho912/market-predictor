# Flow / Positioning Proxy Status

Generated at: `2026-09-02T00:37:30.933739+00:00`
Latest date: `2026-09-01`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.06`
- overall_flow_conflict_score: `26.55`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.65 | 26.55 | 64.61 | 43.97 | 0.573 | 1.2061 | 1.0365 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.75 | 26.55 | 64.65 | 43.97 | 0.5176 | 1.2348 | 1.0551 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.13 | 26.55 | 65.76 | 43.97 | 1.7962 | 1.441 | 1.3682 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 50.71 | 26.55 | 63.98 | 43.97 | -0.0501 | 1.1843 | 0.9621 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
