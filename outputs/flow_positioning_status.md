# Flow / Positioning Proxy Status

Generated at: `2026-10-14T01:31:48.950306+00:00`
Latest date: `2026-10-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.16`
- overall_flow_conflict_score: `30.79`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.41 | 30.79 | 80.37 | 49.59 | -2.1137 | 0.534 | 0.4171 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.31 | 30.79 | 80.99 | 49.59 | -1.0235 | 0.8471 | 0.7397 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.46 | 30.79 | 80.72 | 49.59 | -1.6684 | 0.6772 | 0.6624 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 64.46 | 30.79 | 83.01 | 49.59 | -0.6077 | 0.8418 | 0.8547 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
