# Flow / Positioning Proxy Status

Generated at: `2026-07-27T15:16:16.708841+00:00`
Latest date: `2026-07-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.44`
- overall_flow_conflict_score: `55.19`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.22 | 55.19 | 62.9 | 95.16 | -2.6514 | 0.3167 | 0.3078 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.22 | 55.19 | 62.9 | 95.16 | -2.1004 | 0.4797 | 0.4633 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.22 | 55.19 | 62.9 | 95.16 | -2.0913 | 0.3764 | 0.3867 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.1 | 55.19 | 64.5 | 95.16 | -2.1892 | 0.4675 | 0.4509 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
