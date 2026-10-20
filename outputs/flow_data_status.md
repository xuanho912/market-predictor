# Flow / Positioning Proxy Status

Generated at: `2026-10-20T23:17:28.737268+00:00`
Latest date: `2026-10-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `51.2`
- overall_flow_conflict_score: `62.76`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 48.96 | 62.76 | 60.01 | 100.0 | -0.5823 | 0.757 | 0.8338 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 48.92 | 62.76 | 60.0 | 100.0 | -0.4836 | 0.6273 | 0.8307 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 50.85 | 62.76 | 60.63 | 100.0 | 0.0125 | 0.8666 | 1.004 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.09 | 62.76 | 62.35 | 100.0 | 0.0907 | 0.9292 | 1.0225 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
