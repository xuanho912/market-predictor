# Flow / Positioning Proxy Status

Generated at: `2026-09-08T16:41:16.793619+00:00`
Latest date: `2026-09-08`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `45.18`
- overall_flow_conflict_score: `27.76`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 42.25 | 27.76 | 62.07 | 40.3 | -2.9118 | 0.4206 | 0.4333 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 47.13 | 27.76 | 63.67 | 40.3 | -2.2198 | 0.4739 | 0.4715 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 47.13 | 27.76 | 63.67 | 40.3 | -1.9492 | 0.4377 | 0.5062 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 44.21 | 27.76 | 62.71 | 40.3 | -0.845 | 0.7129 | 0.7448 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
