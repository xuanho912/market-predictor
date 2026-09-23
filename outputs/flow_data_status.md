# Flow / Positioning Proxy Status

Generated at: `2026-09-23T23:03:09.369837+00:00`
Latest date: `2026-09-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `68.09`
- overall_flow_conflict_score: `33.75`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 72.71 | 33.75 | 95.12 | 52.08 | 1.254 | 1.0543 | 1.3186 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 68.06 | 33.75 | 93.6 | 52.08 | 0.0459 | 0.791 | 1.0239 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.51 | 33.75 | 92.76 | 52.08 | 0.5211 | 0.9667 | 1.152 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.07 | 33.75 | 92.95 | 52.08 | 0.6384 | 1.0382 | 1.1823 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
