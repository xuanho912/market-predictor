# Flow / Positioning Proxy Status

Generated at: `2026-07-22T00:04:36.127276+00:00`
Latest date: `2026-07-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `52.88`
- overall_flow_conflict_score: `48.6`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 50.06 | 48.6 | 61.25 | 82.4 | -2.1753 | 0.5748 | 0.5384 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.74 | 48.6 | 62.13 | 82.4 | -0.8257 | 0.8926 | 0.8115 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.41 | 48.6 | 63.33 | 82.4 | -1.1518 | 0.7275 | 0.7014 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.3 | 48.6 | 61.98 | 82.4 | -0.8377 | 0.8892 | 0.7709 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
