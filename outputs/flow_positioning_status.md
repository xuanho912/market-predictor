# Flow / Positioning Proxy Status

Generated at: `2026-11-28T20:06:39.883884+00:00`
Latest date: `2026-11-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.29`
- overall_flow_conflict_score: `68.41`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.73 | 68.41 | 70.35 | 100.0 | -0.8421 | 0.4455 | 0.6215 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.13 | 68.41 | 70.15 | 100.0 | -1.005 | 0.4117 | 0.5578 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.16 | 68.41 | 70.16 | 100.0 | -1.1632 | 0.4418 | 0.5695 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.13 | 68.41 | 70.15 | 100.0 | -1.0234 | 0.4642 | 0.5109 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
