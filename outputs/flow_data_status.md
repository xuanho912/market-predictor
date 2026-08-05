# Flow / Positioning Proxy Status

Generated at: `2026-08-05T14:35:49.900285+00:00`
Latest date: `2026-08-05`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.57`
- overall_flow_conflict_score: `20.1`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 66.57 | 20.1 | 79.44 | 34.65 | -2.6194 | 0.1624 | 0.2147 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 66.57 | 20.1 | 79.44 | 34.65 | -2.2892 | 0.173 | 0.2312 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 66.57 | 20.1 | 79.44 | 34.65 | -2.8084 | 0.1858 | 0.2163 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.57 | 20.1 | 79.44 | 34.65 | -1.4632 | 0.3742 | 0.4902 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
