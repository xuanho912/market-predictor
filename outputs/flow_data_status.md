# Flow / Positioning Proxy Status

Generated at: `2026-10-03T01:33:39.665440+00:00`
Latest date: `2026-10-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `68.33`
- overall_flow_conflict_score: `37.01`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.02 | 37.01 | 97.7 | 51.44 | 0.2029 | 1.0727 | 1.0602 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 70.39 | 37.01 | 99.47 | 51.44 | 0.3304 | 1.1311 | 1.0823 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 68.96 | 37.01 | 99.0 | 51.44 | 2.153 | 1.4494 | 1.4756 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 68.96 | 37.01 | 99.0 | 51.44 | 1.0289 | 1.6651 | 1.2934 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
