# High Confidence Signal Report

Generated at: `2026-09-17T00:58:43.826461+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0068`, median `0.0122`, brier `0.1787`, calibration_gap `0.0049`
- 5d: hit_rate `0.7500`, avg `0.0063`, median `0.0080`, brier `0.1967`, calibration_gap `0.0049`
- 10d: hit_rate `0.6250`, avg `0.0066`, median `0.0074`, brier `0.2601`, calibration_gap `0.1299`
- 20d: hit_rate `1.0000`, avg `0.0528`, median `0.0572`, brier `0.0612`, calibration_gap `-0.2451`
- 60d: hit_rate `0.8750`, avg `0.0841`, median `0.0844`, brier `0.1425`, calibration_gap `-0.1201`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0020`, median `0.0079`, brier `0.2090`, calibration_gap `0.0343`
- 5d: hit_rate `0.6250`, avg `0.0029`, median `0.0080`, brier `0.2406`, calibration_gap `0.0968`
- 10d: hit_rate `0.6250`, avg `0.0017`, median `0.0050`, brier `0.2497`, calibration_gap `0.0968`
- 20d: hit_rate `1.0000`, avg `0.0489`, median `0.0498`, brier `0.0791`, calibration_gap `-0.2782`
- 60d: hit_rate `0.8750`, avg `0.0841`, median `0.0844`, brier `0.1431`, calibration_gap `-0.1532`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6500`, avg `0.0061`, median `0.0110`, brier `0.2340`, calibration_gap `-0.0191`
- 5d: hit_rate `0.5833`, avg `0.0072`, median `0.0063`, brier `0.2473`, calibration_gap `0.0476`
- 10d: hit_rate `0.6667`, avg `0.0100`, median `0.0088`, brier `0.2306`, calibration_gap `-0.0357`
- 20d: hit_rate `0.8167`, avg `0.0391`, median `0.0387`, brier `0.1805`, calibration_gap `-0.1857`
- 60d: hit_rate `0.8833`, avg `0.0961`, median `0.1050`, brier `0.1748`, calibration_gap `-0.2524`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0041`, median `0.0078`, brier `0.2433`, calibration_gap `-0.0284`
- 5d: hit_rate `0.5000`, avg `0.0014`, median `-0.0004`, brier `0.2520`, calibration_gap `0.0341`
- 10d: hit_rate `0.6875`, avg `0.0156`, median `0.0320`, brier `0.2362`, calibration_gap `-0.1534`
- 20d: hit_rate `0.8125`, avg `0.0392`, median `0.0529`, brier `0.2274`, calibration_gap `-0.2784`
- 60d: hit_rate `0.8125`, avg `0.0850`, median `0.0967`, brier `0.2298`, calibration_gap `-0.2784`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
