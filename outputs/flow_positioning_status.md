# Flow / Positioning Proxy Status

Generated at: `2026-07-22T14:24:48.580713+00:00`
Latest date: `2026-07-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.97`
- overall_flow_conflict_score: `34.85`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.97 | 34.85 | 65.53 | 60.09 | -3.1868 | 0.1161 | 0.1097 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.97 | 34.85 | 65.53 | 60.09 | -2.8472 | 0.197 | 0.1854 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.97 | 34.85 | 65.53 | 60.09 | -2.6047 | 0.1713 | 0.1666 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.97 | 34.85 | 65.53 | 60.09 | -2.4959 | 0.3303 | 0.2915 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
