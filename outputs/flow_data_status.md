# Flow / Positioning Proxy Status

Generated at: `2026-07-10T07:05:19.296162+00:00`
Latest date: `2026-07-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.25`
- overall_flow_conflict_score: `21.43`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.16 | 21.43 | 71.71 | 34.43 | -1.3943 | 0.8524 | 0.6686 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.26 | 21.43 | 70.1 | 34.43 | -1.4697 | 0.839 | 0.6666 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.24 | 21.43 | 69.77 | 34.43 | -1.4256 | 0.8027 | 0.5741 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.34 | 21.43 | 71.44 | 34.43 | -1.3455 | 0.8357 | 0.5937 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
