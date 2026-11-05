# Flow / Positioning Proxy Status

Generated at: `2026-11-05T20:01:02.853231+00:00`
Latest date: `2026-11-05`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `65.29`
- overall_flow_conflict_score: `75.35`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.29 | 75.35 | 79.53 | 100.0 | 2.0838 | 1.4859 | 1.9158 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.29 | 75.35 | 79.53 | 100.0 | 2.5857 | 1.7652 | 2.2794 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.29 | 75.35 | 79.53 | 100.0 | 2.0012 | 1.6128 | 1.61 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 65.29 | 75.35 | 79.53 | 100.0 | 2.8995 | 1.8213 | 2.2114 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
