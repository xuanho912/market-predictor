# Flow / Positioning Proxy Status

Generated at: `2026-10-22T01:32:57.397588+00:00`
Latest date: `2026-10-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.96`
- overall_flow_conflict_score: `59.08`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.2 | 59.08 | 62.69 | 92.9 | -0.7316 | 0.6709 | 0.7685 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 51.93 | 59.08 | 61.61 | 92.9 | -0.2591 | 0.6762 | 0.9146 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 53.4 | 59.08 | 62.1 | 92.9 | -1.5782 | 0.5271 | 0.6045 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.32 | 59.08 | 62.73 | 92.9 | -0.8698 | 0.7025 | 0.7794 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
