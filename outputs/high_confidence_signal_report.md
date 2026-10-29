# High Confidence Signal Report

Generated at: `2026-10-29T18:31:31.152697+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0039`, median `0.0029`, brier `0.2553`, calibration_gap `0.1457`
- 5d: hit_rate `0.5000`, avg `0.0080`, median `0.0023`, brier `0.3284`, calibration_gap `0.2707`
- 10d: hit_rate `0.7500`, avg `0.0193`, median `0.0224`, brier `0.1822`, calibration_gap `0.0207`
- 20d: hit_rate `0.8750`, avg `0.0332`, median `0.0297`, brier `0.1169`, calibration_gap `-0.1043`
- 60d: hit_rate `0.8750`, avg `0.0618`, median `0.0708`, brier `0.1202`, calibration_gap `-0.1043`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0097`, median `0.0103`, brier `0.2206`, calibration_gap `0.0704`
- 5d: hit_rate `0.6250`, avg `0.0124`, median `0.0229`, brier `0.2572`, calibration_gap `0.1329`
- 10d: hit_rate `0.8125`, avg `0.0327`, median `0.0409`, brier `0.1535`, calibration_gap `-0.0546`
- 20d: hit_rate `0.8750`, avg `0.0466`, median `0.0484`, brier `0.1215`, calibration_gap `-0.1171`
- 60d: hit_rate `0.8750`, avg `0.0587`, median `0.0673`, brier `0.1232`, calibration_gap `-0.1171`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6667`, avg `0.0058`, median `0.0063`, brier `0.2225`, calibration_gap `0.0376`
- 5d: hit_rate `0.5667`, avg `0.0067`, median `0.0066`, brier `0.2716`, calibration_gap `0.1376`
- 10d: hit_rate `0.7333`, avg `0.0159`, median `0.0165`, brier `0.1997`, calibration_gap `-0.0291`
- 20d: hit_rate `0.8000`, avg `0.0259`, median `0.0287`, brier `0.1671`, calibration_gap `-0.0957`
- 60d: hit_rate `0.7667`, avg `0.0435`, median `0.0554`, brier `0.1758`, calibration_gap `-0.0624`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0066`, median `0.0096`, brier `0.2385`, calibration_gap `0.0288`
- 5d: hit_rate `0.6875`, avg `0.0119`, median `0.0137`, brier `0.2231`, calibration_gap `-0.0337`
- 10d: hit_rate `0.8125`, avg `0.0214`, median `0.0305`, brier `0.1748`, calibration_gap `-0.1587`
- 20d: hit_rate `0.7500`, avg `0.0266`, median `0.0368`, brier `0.1957`, calibration_gap `-0.0962`
- 60d: hit_rate `0.6250`, avg `0.0433`, median `0.0614`, brier `0.2324`, calibration_gap `0.0288`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
