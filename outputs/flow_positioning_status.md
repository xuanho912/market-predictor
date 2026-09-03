# Flow / Positioning Proxy Status

Generated at: `2026-09-03T00:49:06.648401+00:00`
Latest date: `2026-09-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `49.55`
- overall_flow_conflict_score: `24.94`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 49.2 | 24.94 | 56.59 | 41.54 | 0.7606 | 1.2366 | 1.0627 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 49.17 | 24.94 | 56.58 | 41.54 | 0.6476 | 1.2645 | 1.0805 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.03 | 24.94 | 57.52 | 41.54 | 1.8199 | 1.4474 | 1.3743 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 47.78 | 24.94 | 56.12 | 41.54 | 0.2741 | 1.4359 | 1.0202 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
