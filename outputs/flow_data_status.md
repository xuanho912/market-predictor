# Flow / Positioning Proxy Status

Generated at: `2026-07-29T21:26:10.749392+00:00`
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
| SPY | 100.0 | 63.87 | 60.38 | 70.77 | 100.0 | 2.5262 | 1.5567 | 1.5005 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.87 | 60.38 | 70.77 | 100.0 | 1.4427 | 1.2473 | 1.3393 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.87 | 60.38 | 70.77 | 100.0 | 2.775 | 1.5394 | 1.5909 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.87 | 60.38 | 70.77 | 100.0 | 3.2021 | 1.7526 | 1.9142 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
