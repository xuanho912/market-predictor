# Flow / Positioning Proxy Status

Generated at: `2026-07-30T14:34:38.256924+00:00`
Latest date: `2026-07-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `51.3`
- overall_flow_conflict_score: `45.24`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.74 | 45.24 | 62.23 | 77.87 | -2.6987 | 0.2712 | 0.3009 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 48.86 | 45.24 | 60.63 | 77.87 | -2.0601 | 0.3427 | 0.4193 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 48.86 | 45.24 | 60.63 | 77.87 | -2.6168 | 0.2666 | 0.3046 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 53.74 | 45.24 | 62.23 | 77.87 | -2.1186 | 0.2243 | 0.2825 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
