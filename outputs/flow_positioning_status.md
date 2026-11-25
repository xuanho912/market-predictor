# Flow / Positioning Proxy Status

Generated at: `2026-11-25T03:37:53.453884+00:00`
Latest date: `2026-11-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.19`
- overall_flow_conflict_score: `71.86`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.38 | 71.86 | 71.66 | 100.0 | 0.0433 | 0.7301 | 1.0505 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.26 | 71.86 | 71.29 | 100.0 | -0.1398 | 0.7275 | 0.9556 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.45 | 71.86 | 72.01 | 100.0 | 0.2435 | 0.8802 | 1.1119 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.66 | 71.86 | 71.43 | 100.0 | -0.0511 | 0.8892 | 0.992 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
