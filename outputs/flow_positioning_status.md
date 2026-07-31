# Flow / Positioning Proxy Status

Generated at: `2026-07-31T21:35:40.062128+00:00`
Latest date: `2026-07-31`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.41`
- overall_flow_conflict_score: `36.49`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.43 | 36.49 | 60.61 | 59.94 | 1.1117 | 1.0908 | 1.238 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.1 | 36.49 | 60.5 | 59.94 | 0.9018 | 0.9586 | 1.2452 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.65 | 36.49 | 60.68 | 59.94 | 1.4221 | 1.2158 | 1.3203 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 54.44 | 36.49 | 59.3 | 59.94 | 0.145 | 0.8677 | 1.0465 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
