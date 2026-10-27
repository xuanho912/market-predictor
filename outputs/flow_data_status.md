# Flow / Positioning Proxy Status

Generated at: `2026-10-27T00:00:23.988274+00:00`
Latest date: `2026-10-26`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `54.26`
- overall_flow_conflict_score: `65.62`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.37 | 65.62 | 64.7 | 100.0 | -0.7076 | 0.8142 | 0.775 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.64 | 65.62 | 65.12 | 100.0 | -0.2772 | 0.8399 | 0.8905 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.33 | 65.62 | 65.67 | 100.0 | -1.4528 | 0.7088 | 0.6001 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.71 | 65.62 | 65.8 | 100.0 | -1.5188 | 0.7328 | 0.6351 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
