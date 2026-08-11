# Flow / Positioning Proxy Status

Generated at: `2026-08-11T13:48:05.312811+00:00`
Latest date: `2026-08-11`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.05`
- overall_flow_conflict_score: `19.89`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.49 | 19.89 | 67.42 | 34.29 | -2.9682 | 0.046 | 0.0437 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.61 | 19.89 | 65.82 | 34.29 | -2.5806 | 0.0851 | 0.0755 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.61 | 19.89 | 65.82 | 34.29 | -3.0805 | 0.0734 | 0.0608 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.49 | 19.89 | 67.42 | 34.29 | -2.3242 | 0.0749 | 0.0797 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
