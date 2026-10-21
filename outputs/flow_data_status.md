# Flow / Positioning Proxy Status

Generated at: `2026-10-21T01:05:36.897045+00:00`
Latest date: `2026-10-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `50.51`
- overall_flow_conflict_score: `62.76`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 49.92 | 62.76 | 60.33 | 100.0 | -0.2295 | 0.9303 | 0.9215 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 51.44 | 62.76 | 60.83 | 100.0 | 0.1493 | 0.8339 | 1.0337 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 48.02 | 62.76 | 59.71 | 100.0 | -1.1205 | 0.6577 | 0.7488 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.67 | 62.76 | 61.23 | 100.0 | -1.1579 | 0.6528 | 0.7278 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
