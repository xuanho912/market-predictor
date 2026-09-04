# Flow / Positioning Proxy Status

Generated at: `2026-09-04T22:27:08.882344+00:00`
Latest date: `2026-09-04`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `50.12`
- overall_flow_conflict_score: `24.12`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 51.27 | 24.12 | 61.77 | 38.61 | -0.657 | 0.8684 | 0.8957 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.6 | 24.12 | 62.54 | 38.61 | 0.2785 | 1.0514 | 1.0582 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 50.44 | 24.12 | 61.5 | 38.61 | -0.7798 | 0.6827 | 0.8203 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 45.17 | 24.12 | 59.78 | 38.61 | -0.7838 | 0.7341 | 0.785 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
