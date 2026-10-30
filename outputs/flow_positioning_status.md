# Flow / Positioning Proxy Status

Generated at: `2026-10-30T02:12:20.416366+00:00`
Latest date: `2026-10-29`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `62.99`
- overall_flow_conflict_score: `67.62`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.51 | 67.62 | 73.68 | 100.0 | 0.2132 | 1.1239 | 1.0524 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.05 | 67.62 | 73.53 | 100.0 | 0.0868 | 0.9974 | 1.0331 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.07 | 67.62 | 72.88 | 100.0 | -0.4057 | 1.0839 | 0.8675 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.32 | 67.62 | 71.33 | 100.0 | -0.4511 | 1.0869 | 0.8797 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
