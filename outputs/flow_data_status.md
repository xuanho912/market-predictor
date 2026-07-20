# Flow / Positioning Proxy Status

Generated at: `2026-07-20T14:36:32.896885+00:00`
Latest date: `2026-07-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `51.13`
- overall_flow_conflict_score: `56.48`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 49.91 | 56.48 | 61.72 | 93.77 | -3.1093 | 0.1892 | 0.1674 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 49.91 | 56.48 | 61.72 | 93.77 | -2.8518 | 0.2348 | 0.2159 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 54.79 | 56.48 | 63.32 | 93.77 | -2.6144 | 0.2011 | 0.187 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 49.91 | 56.48 | 61.72 | 93.77 | -2.525 | 0.2468 | 0.2062 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
