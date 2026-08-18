# Flow / Positioning Proxy Status

Generated at: `2026-08-18T13:11:41.068799+00:00`
Latest date: `2026-08-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `74.81`
- overall_flow_conflict_score: `18.71`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 73.16 | 18.71 | 100.0 | 32.25 | -1.2394 | 0.8325 | 0.6469 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 76.59 | 18.71 | 100.0 | 32.25 | -1.2563 | 0.8077 | 0.5836 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 77.04 | 18.71 | 100.0 | 32.25 | -1.3925 | 0.8249 | 0.6332 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 72.44 | 18.71 | 100.0 | 32.25 | -1.1924 | 0.7643 | 0.5367 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
