# Flow / Positioning Proxy Status

Generated at: `2026-09-18T23:35:39.432711+00:00`
Latest date: `2026-09-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `52.53`
- overall_flow_conflict_score: `31.49`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.11 | 31.49 | 67.32 | 48.14 | 2.5655 | 1.3298 | 1.6331 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 57.99 | 31.49 | 68.92 | 48.14 | 2.73 | 1.4823 | 1.5627 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 53.11 | 31.49 | 67.32 | 48.14 | 1.8619 | 1.215 | 1.5372 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 45.9 | 31.49 | 64.95 | 48.14 | -0.637 | 0.6896 | 0.7989 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
