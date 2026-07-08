# Flow / Positioning Proxy Status

Generated at: `2026-07-08T22:39:24.977358+00:00`
Latest date: `2026-07-08`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.36`
- overall_flow_conflict_score: `39.87`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 51.91 | 39.87 | 65.93 | 60.01 | -1.3904 | 0.8381 | 0.6864 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 51.4 | 39.87 | 65.76 | 60.01 | -1.332 | 0.7892 | 0.6399 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 53.42 | 39.87 | 66.42 | 60.01 | -0.6227 | 1.1683 | 0.8241 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.7 | 39.87 | 67.5 | 60.01 | -1.1582 | 0.9645 | 0.6782 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
