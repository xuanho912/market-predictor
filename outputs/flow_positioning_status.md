# Flow / Positioning Proxy Status

Generated at: `2026-09-17T22:57:52.575911+00:00`
Latest date: `2026-09-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `48.96`
- overall_flow_conflict_score: `33.86`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.63 | 33.86 | 58.86 | 52.27 | 1.2266 | 1.037 | 1.2522 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.11 | 33.86 | 58.69 | 52.27 | 1.2293 | 1.1683 | 1.1899 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.75 | 33.86 | 56.28 | 52.27 | 0.3806 | 0.8335 | 1.1148 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 46.35 | 33.86 | 56.8 | 52.27 | 0.6424 | 1.0016 | 1.2139 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
