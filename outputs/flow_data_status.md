# Flow / Positioning Proxy Status

Generated at: `2026-08-26T23:50:23.686557+00:00`
Latest date: `2026-08-26`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `70.61`
- overall_flow_conflict_score: `20.63`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 70.9 | 20.63 | 100.0 | 35.58 | -1.2547 | 0.7373 | 0.6092 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 70.52 | 20.63 | 100.0 | 35.58 | -1.4386 | 0.5633 | 0.4883 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 70.52 | 20.63 | 100.0 | 35.58 | -1.6815 | 0.597 | 0.5549 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 70.52 | 20.63 | 100.0 | 35.58 | -1.4116 | 0.532 | 0.4678 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
