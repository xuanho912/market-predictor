# Alpha Candidate v1 Stress Test

Signal: `bounce_probability_top_decile_v1`
Frozen threshold: `0.32534311`

## Threshold Stability

Top 20% and top 30% are stability checks only. They are not allowed to replace the frozen top-decile rule.

| Threshold | Signal count | 3d avg | 5d avg | 10d avg | 20d avg | 60d avg |
| --- | --- | --- | --- | --- | --- | --- |
| top 10% frozen | 1776 | 0.395% | 0.733% | 1.323% | 1.745% | 5.924% |
| top 20% stress | 3556 | 0.259% | 0.379% | 0.906% | 1.772% | 3.711% |
| top 30% stress | 5332 | 0.234% | 0.332% | 0.752% | 1.389% | 3.688% |

## Time Period Stability

| Period | Signals | 3d avg | 5d avg | 10d avg | 20d avg | 60d avg |
| --- | --- | --- | --- | --- | --- | --- |
| 2007-2012 | 1136 | 0.002% | 0.241% | 0.262% | -0.101% | 3.850% |
| 2013-2017 | 12 | 2.978% | 3.298% | 4.858% | 3.471% | 8.984% |
| 2018-2021 | 364 | 0.864% | 1.338% | 2.719% | 3.698% | 7.122% |
| 2022-2026 | 264 | 1.041% | 1.292% | 2.146% | 2.986% | 6.983% |

## Symbol Stability

| symbol | Signals | 3d avg | 5d avg | 10d avg | 20d avg | 60d avg |
| --- | --- | --- | --- | --- | --- | --- |
| DIA | 444 | 0.325% | 0.631% | 1.158% | 1.645% | 5.334% |
| IWM | 444 | 0.399% | 0.832% | 1.495% | 1.711% | 5.567% |
| QQQ | 444 | 0.501% | 0.814% | 1.457% | 2.054% | 7.245% |
| SPY | 444 | 0.353% | 0.653% | 1.183% | 1.572% | 5.549% |

## Regime Stability

| regime | Signals | 3d avg | 5d avg | 10d avg | 20d avg | 60d avg |
| --- | --- | --- | --- | --- | --- | --- |
| crisis | 718 | 0.427% | 0.598% | 0.982% | 1.672% | 3.883% |
| high_volatility | 1058 | 0.288% | 0.361% | 0.502% | 0.632% | 3.204% |

## Simple Baseline Comparison

Each baseline uses the same signal frequency as alpha v1 and non-overlapping horizon samples.

| Signal | Count | 3d avg | 5d avg | 10d avg | 20d avg | 60d avg |
| --- | --- | --- | --- | --- | --- | --- |
| alpha_v1_bounce_top_decile | 1776 | 0.395% | 0.733% | 1.323% | 1.745% | 5.924% |
| RSI oversold same-frequency | 1776 | 0.512% | 0.725% | 0.993% | 1.757% | 3.626% |
| VIX spike same-frequency | 1776 | 0.270% | 0.460% | 0.646% | 1.137% | 3.819% |
| 20d drawdown same-frequency | 1776 | 0.367% | 0.450% | 0.928% | 1.976% | 4.336% |
| simple mean reversion same-frequency | 1776 | 0.329% | 0.487% | 0.895% | 1.415% | 3.957% |
| random same-frequency | 1776 | 0.186% | 0.180% | 0.509% | 0.949% | 2.682% |

## Data-Mining / Overfitting Answer

- Is this only ordinary oversold bounce repackaged? The candidate is stronger than the simple mean-reversion baseline on most horizons, but this remains a post-hoc stress result.
- Does it beat simple mean reversion? It beats simple mean reversion on 5/5 horizons under this same-frequency stress test.
- This does not confirm live alpha because all tests still use the historical discovery sample.
- The valid next step is forward-only observation with the frozen threshold.
