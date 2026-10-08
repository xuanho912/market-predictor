# Flow / Positioning Proxy Status

Generated at: `2026-10-08T18:54:03.335566+00:00`
Latest date: `2026-10-08`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `62.69`
- overall_flow_conflict_score: `30.69`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.77 | 30.69 | 81.73 | 50.05 | -1.9411 | 0.6323 | 0.5653 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.91 | 30.69 | 83.75 | 50.05 | 0.3159 | 1.208 | 1.07 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 62.76 | 30.69 | 82.71 | 50.05 | 0.8735 | 1.0697 | 1.1277 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.33 | 30.69 | 82.57 | 50.05 | -0.7228 | 0.7341 | 0.8001 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
