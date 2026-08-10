# Flow / Positioning Proxy Status

Generated at: `2026-08-10T13:47:58.349845+00:00`
Latest date: `2026-08-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.3`
- overall_flow_conflict_score: `19.58`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 60.3 | 19.58 | 75.02 | 33.77 | -2.912 | 0.0519 | 0.0534 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.3 | 19.58 | 75.02 | 33.77 | -2.6202 | 0.0759 | 0.0734 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.3 | 19.58 | 75.02 | 33.77 | -3.1085 | 0.0806 | 0.0714 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.3 | 19.58 | 75.02 | 33.77 | -2.3134 | 0.0828 | 0.0926 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
