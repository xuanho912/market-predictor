# Flow / Positioning Proxy Status

Generated at: `2026-08-13T05:24:39.934633+00:00`
Latest date: `2026-08-12`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.85`
- overall_flow_conflict_score: `18.56`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 67.47 | 18.56 | 80.13 | 32.0 | -1.313 | 0.8164 | 0.6678 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 67.82 | 18.56 | 80.24 | 32.0 | -1.0181 | 0.9442 | 0.6998 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 68.06 | 18.56 | 80.32 | 32.0 | -1.1945 | 0.9238 | 0.7217 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 64.04 | 18.56 | 79.01 | 32.0 | -0.6009 | 0.9108 | 0.8005 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
