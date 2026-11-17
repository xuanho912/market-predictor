# Flow / Positioning Proxy Status

Generated at: `2026-11-17T20:58:22.590309+00:00`
Latest date: `2026-11-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.4`
- overall_flow_conflict_score: `66.52`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.85 | 66.52 | 72.53 | 100.0 | 0.3906 | 1.2942 | 1.203 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 54.9 | 66.52 | 71.23 | 100.0 | -0.2155 | 1.0973 | 0.913 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.56 | 66.52 | 71.78 | 100.0 | 0.1336 | 1.17 | 1.0399 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.28 | 66.52 | 71.35 | 100.0 | -0.0929 | 1.2691 | 0.947 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
