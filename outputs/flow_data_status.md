# Flow / Positioning Proxy Status

Generated at: `2026-07-14T00:04:15.223533+00:00`
Latest date: `2026-07-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `44.35`
- overall_flow_conflict_score: `34.16`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.76 | 34.16 | 56.2 | 54.61 | -1.0585 | 0.9788 | 0.7401 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 45.16 | 34.16 | 56.33 | 54.61 | -1.0902 | 1.0492 | 0.7764 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.61 | 34.16 | 56.15 | 54.61 | -0.8873 | 1.0227 | 0.7258 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 42.86 | 34.16 | 55.58 | 54.61 | -1.381 | 0.7368 | 0.5365 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
