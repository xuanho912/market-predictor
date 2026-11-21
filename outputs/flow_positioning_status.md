# Flow / Positioning Proxy Status

Generated at: `2026-11-21T03:56:51.890522+00:00`
Latest date: `2026-11-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `50.95`
- overall_flow_conflict_score: `75.38`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 50.95 | 75.38 | 65.86 | 100.0 | 2.9934 | 2.4515 | 2.8819 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 50.95 | 75.38 | 65.86 | 100.0 | 2.6701 | 2.6041 | 2.5886 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 50.95 | 75.38 | 65.86 | 100.0 | 2.9529 | 2.2666 | 2.3477 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 50.95 | 75.38 | 65.86 | 100.0 | 0.8332 | 1.4858 | 1.4763 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
