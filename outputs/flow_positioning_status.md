# Flow / Positioning Proxy Status

Generated at: `2026-10-21T17:21:00.376253+00:00`
Latest date: `2026-10-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `51.67`
- overall_flow_conflict_score: `58.07`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.89 | 58.07 | 61.78 | 91.09 | -2.0278 | 0.2804 | 0.321 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 48.01 | 58.07 | 60.18 | 91.09 | -1.3702 | 0.3788 | 0.512 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.89 | 58.07 | 61.78 | 91.09 | -2.4654 | 0.2605 | 0.2986 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.89 | 58.07 | 61.78 | 91.09 | -2.106 | 0.3806 | 0.4223 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
