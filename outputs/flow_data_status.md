# Flow / Positioning Proxy Status

Generated at: `2026-10-02T00:00:34.447251+00:00`
Latest date: `2026-10-01`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.41`
- overall_flow_conflict_score: `38.13`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.09 | 38.13 | 95.3 | 53.36 | 0.1536 | 1.0624 | 1.0499 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 68.44 | 38.13 | 97.05 | 53.36 | 0.2771 | 1.1198 | 1.0714 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 67.24 | 38.13 | 96.66 | 53.36 | 2.0956 | 1.4332 | 1.4591 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.86 | 38.13 | 96.53 | 53.36 | 0.9118 | 1.6207 | 1.2589 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
