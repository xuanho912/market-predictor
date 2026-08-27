# Flow / Positioning Proxy Status

Generated at: `2026-08-27T11:16:14.455101+00:00`
Latest date: `2026-08-26`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `70.67`
- overall_flow_conflict_score: `20.63`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 71.14 | 20.63 | 100.0 | 35.58 | -1.1684 | 0.7697 | 0.6359 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 70.52 | 20.63 | 100.0 | 35.58 | -1.3354 | 0.6077 | 0.5269 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 70.52 | 20.63 | 100.0 | 35.58 | -1.6559 | 0.6047 | 0.5621 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 70.52 | 20.63 | 100.0 | 35.58 | -1.3916 | 0.5406 | 0.4754 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
