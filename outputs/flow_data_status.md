# Flow / Positioning Proxy Status

Generated at: `2026-09-21T18:15:39.774087+00:00`
Latest date: `2026-09-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `47.91`
- overall_flow_conflict_score: `37.23`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 50.3 | 37.23 | 70.22 | 53.93 | -1.2918 | 0.5185 | 0.6716 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.78 | 37.23 | 71.04 | 53.93 | -0.4806 | 0.7692 | 0.8978 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.26 | 37.23 | 68.25 | 53.93 | -1.5961 | 0.3964 | 0.5083 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 44.32 | 37.23 | 68.27 | 53.93 | -1.2654 | 0.5125 | 0.572 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
