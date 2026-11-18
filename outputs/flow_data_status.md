# Flow / Positioning Proxy Status

Generated at: `2026-11-18T20:34:44.396351+00:00`
Latest date: `2026-11-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.64`
- overall_flow_conflict_score: `68.28`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.05 | 68.28 | 72.39 | 100.0 | -0.7093 | 0.6716 | 0.6842 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.25 | 68.28 | 72.45 | 100.0 | -0.6556 | 0.8002 | 0.7023 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 53.63 | 68.28 | 72.58 | 100.0 | -0.8192 | 0.7772 | 0.7364 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 54.63 | 68.28 | 72.91 | 100.0 | -0.3224 | 1.0548 | 0.8278 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
