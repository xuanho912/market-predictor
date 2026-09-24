# Flow / Positioning Proxy Status

Generated at: `2026-09-24T08:48:07.935208+00:00`
Latest date: `2026-09-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `68.42`
- overall_flow_conflict_score: `33.75`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 72.71 | 33.75 | 95.12 | 52.08 | 1.2677 | 1.0572 | 1.3222 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 68.15 | 33.75 | 93.63 | 52.08 | 0.0664 | 0.7945 | 1.0285 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.54 | 33.75 | 92.77 | 52.08 | 0.5273 | 0.9681 | 1.1536 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 67.29 | 33.75 | 93.35 | 52.08 | 0.8583 | 1.1016 | 1.2545 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
