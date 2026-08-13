# Flow / Positioning Proxy Status

Generated at: `2026-08-13T03:35:28.836337+00:00`
Latest date: `2026-08-12`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.62`
- overall_flow_conflict_score: `18.56`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 67.4 | 18.56 | 80.11 | 32.0 | -1.336 | 0.8084 | 0.6612 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 67.78 | 18.56 | 80.23 | 32.0 | -1.0296 | 0.9392 | 0.6961 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 68.03 | 18.56 | 80.31 | 32.0 | -1.2051 | 0.9203 | 0.719 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.27 | 18.56 | 78.75 | 32.0 | -0.797 | 0.8309 | 0.7303 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
