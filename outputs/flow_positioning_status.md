# Flow / Positioning Proxy Status

Generated at: `2026-08-13T21:12:21.526192+00:00`
Latest date: `2026-08-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `72.58`
- overall_flow_conflict_score: `19.93`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 73.53 | 19.93 | 91.63 | 34.35 | -1.404 | 0.7914 | 0.6172 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 74.7 | 19.93 | 92.01 | 34.35 | -0.8892 | 1.0014 | 0.7237 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 73.98 | 19.93 | 91.78 | 34.35 | -1.3392 | 0.8595 | 0.6581 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 68.1 | 19.93 | 89.85 | 34.35 | -1.4388 | 0.6265 | 0.4849 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
