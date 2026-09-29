# Flow / Positioning Proxy Status

Generated at: `2026-09-29T23:50:09.776818+00:00`
Latest date: `2026-09-29`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.26`
- overall_flow_conflict_score: `38.27`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.32 | 38.27 | 85.16 | 54.22 | -0.8416 | 0.8583 | 0.8304 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 57.91 | 38.27 | 85.03 | 54.22 | -0.9904 | 0.763 | 0.7934 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.35 | 38.27 | 85.5 | 54.22 | -0.427 | 0.8556 | 0.9239 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.45 | 38.27 | 84.87 | 54.22 | -1.013 | 0.8211 | 0.7511 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
