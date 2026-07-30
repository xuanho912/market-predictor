# Flow / Positioning Proxy Status

Generated at: `2026-07-30T04:25:52.154469+00:00`
Latest date: `2026-07-29`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.87`
- overall_flow_conflict_score: `60.38`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.87 | 60.38 | 70.77 | 100.0 | 2.6233 | 1.5884 | 1.531 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.87 | 60.38 | 70.77 | 100.0 | 1.9544 | 1.3854 | 1.4876 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.87 | 60.38 | 70.77 | 100.0 | 2.8278 | 1.5583 | 1.6104 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.87 | 60.38 | 70.77 | 100.0 | 3.4287 | 1.9005 | 2.0757 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
