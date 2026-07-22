# Flow / Positioning Proxy Status

Generated at: `2026-07-22T04:37:02.725460+00:00`
Latest date: `2026-07-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.59`
- overall_flow_conflict_score: `48.6`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 51.22 | 48.6 | 61.63 | 82.4 | -1.6526 | 0.7184 | 0.6729 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.88 | 48.6 | 62.18 | 82.4 | -0.772 | 0.9063 | 0.824 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.42 | 48.6 | 63.66 | 82.4 | -0.8145 | 0.8223 | 0.7928 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.82 | 48.6 | 62.15 | 82.4 | -0.6392 | 0.9437 | 0.8182 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
