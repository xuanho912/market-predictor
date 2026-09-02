# Flow / Positioning Proxy Status

Generated at: `2026-09-02T22:45:36.180745+00:00`
Latest date: `2026-09-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `47.05`
- overall_flow_conflict_score: `24.89`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.63 | 24.89 | 55.09 | 41.49 | -1.4618 | 0.8104 | 0.7822 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 44.13 | 24.89 | 54.93 | 41.49 | -1.2515 | 0.7671 | 0.7366 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.03 | 24.89 | 57.52 | 41.49 | 1.4905 | 1.2779 | 1.3312 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 47.4 | 24.89 | 56.0 | 41.49 | 0.1776 | 1.2482 | 1.0028 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
