# Flow / Positioning Proxy Status

Generated at: `2026-10-29T18:31:16.910934+00:00`
Latest date: `2026-10-29`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.51`
- overall_flow_conflict_score: `67.56`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.52 | 67.56 | 71.36 | 100.0 | -1.4263 | 0.5567 | 0.521 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.52 | 67.56 | 71.36 | 100.0 | -1.1939 | 0.5268 | 0.5443 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.77 | 67.56 | 71.44 | 100.0 | -1.3408 | 0.7363 | 0.5891 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.24 | 67.56 | 69.95 | 100.0 | -1.4879 | 0.7676 | 0.6213 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
