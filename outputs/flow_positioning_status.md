# Flow / Positioning Proxy Status

Generated at: `2026-11-12T19:57:04.935847+00:00`
Latest date: `2026-11-12`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.62`
- overall_flow_conflict_score: `61.78`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.55 | 61.78 | 76.65 | 96.59 | -1.0019 | 0.396 | 0.5142 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 61.55 | 61.78 | 76.65 | 96.59 | -0.9117 | 0.4074 | 0.5408 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.83 | 61.78 | 76.74 | 96.59 | -1.109 | 0.5058 | 0.5922 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.55 | 61.78 | 76.65 | 96.59 | -1.1486 | 0.2686 | 0.3469 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
