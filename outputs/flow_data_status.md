# Flow / Positioning Proxy Status

Generated at: `2026-10-14T09:03:51.345366+00:00`
Latest date: `2026-10-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.44`
- overall_flow_conflict_score: `30.79`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.69 | 30.79 | 80.46 | 49.59 | -1.3543 | 0.8666 | 0.5923 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.57 | 30.79 | 81.41 | 49.59 | -0.6167 | 0.9666 | 0.8541 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.54 | 30.79 | 82.71 | 49.59 | 0.563 | 1.1761 | 1.1155 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 65.94 | 30.79 | 83.49 | 49.59 | -0.0514 | 0.9957 | 0.9897 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
