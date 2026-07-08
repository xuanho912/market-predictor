# Flow / Positioning Proxy Status

Generated at: `2026-07-08T00:10:50.700549+00:00`
Latest date: `2026-07-07`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.13`
- overall_flow_conflict_score: `30.18`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.8 | 30.18 | 74.62 | 46.24 | -1.6023 | 0.7456 | 0.6199 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.27 | 30.18 | 73.47 | 46.24 | -0.8524 | 0.9567 | 0.7433 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.69 | 30.18 | 72.95 | 46.24 | -1.4119 | 0.8202 | 0.5987 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.76 | 30.18 | 75.27 | 46.24 | -0.7049 | 1.0848 | 0.7984 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
