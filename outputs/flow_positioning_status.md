# Flow / Positioning Proxy Status

Generated at: `2026-10-13T23:49:58.696388+00:00`
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
| SPY | 100.0 | 56.7 | 30.79 | 80.47 | 49.59 | -1.3516 | 0.8679 | 0.5932 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.54 | 30.79 | 81.4 | 49.59 | -0.6263 | 0.9638 | 0.8517 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.54 | 30.79 | 82.71 | 49.59 | 0.5638 | 1.1763 | 1.1157 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 65.97 | 30.79 | 83.51 | 49.59 | -0.0403 | 0.9986 | 0.9926 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
