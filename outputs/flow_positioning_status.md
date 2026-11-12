# Flow / Positioning Proxy Status

Generated at: `2026-11-12T02:35:12.506633+00:00`
Latest date: `2026-11-11`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.26`
- overall_flow_conflict_score: `62.88`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.63 | 62.88 | 84.15 | 95.07 | -0.3931 | 0.6163 | 0.8375 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 62.78 | 62.88 | 83.87 | 95.07 | -0.5313 | 0.5453 | 0.7603 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.52 | 62.88 | 84.11 | 95.07 | -0.4903 | 0.6846 | 0.8275 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.11 | 62.88 | 83.98 | 95.07 | -0.4041 | 0.5378 | 0.7905 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
