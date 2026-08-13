# Flow / Positioning Proxy Status

Generated at: `2026-08-13T23:54:03.688154+00:00`
Latest date: `2026-08-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `75.12`
- overall_flow_conflict_score: `19.93`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 76.11 | 19.93 | 100.0 | 34.35 | -1.404 | 0.7914 | 0.6172 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 77.06 | 19.93 | 100.0 | 34.35 | -0.8892 | 1.0014 | 0.7237 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 76.47 | 19.93 | 100.0 | 34.35 | -1.3392 | 0.8595 | 0.6581 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 70.83 | 19.93 | 98.51 | 34.35 | -1.4388 | 0.6265 | 0.4849 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
