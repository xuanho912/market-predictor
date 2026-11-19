# Flow / Positioning Proxy Status

Generated at: `2026-11-19T04:07:07.901545+00:00`
Latest date: `2026-11-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.44`
- overall_flow_conflict_score: `68.36`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.59 | 68.36 | 73.18 | 100.0 | 0.0144 | 1.007 | 1.0259 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 54.87 | 68.36 | 72.62 | 100.0 | -0.3064 | 0.994 | 0.8723 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.65 | 68.36 | 72.87 | 100.0 | -0.221 | 0.9952 | 0.9429 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.66 | 68.36 | 73.86 | 100.0 | 0.2679 | 1.4905 | 1.1697 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
