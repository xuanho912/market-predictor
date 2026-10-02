# High Confidence Signal Report

Generated at: `2026-10-02T01:37:23.608594+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0073`, median `0.0085`, brier `0.1862`, calibration_gap `0.0589`
- 5d: hit_rate `0.7500`, avg `0.0069`, median `0.0108`, brier `0.1862`, calibration_gap `0.0589`
- 10d: hit_rate `1.0000`, avg `0.0100`, median `0.0097`, brier `0.0367`, calibration_gap `-0.1911`
- 20d: hit_rate `0.7500`, avg `0.0295`, median `0.0460`, brier `0.1862`, calibration_gap `0.0589`
- 60d: hit_rate `1.0000`, avg `0.0881`, median `0.0844`, brier `0.0367`, calibration_gap `-0.1911`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0050`, median `0.0116`, brier `0.2169`, calibration_gap `0.0910`
- 5d: hit_rate `0.6875`, avg `0.0058`, median `0.0089`, brier `0.2139`, calibration_gap `0.0910`
- 10d: hit_rate `0.7500`, avg `0.0063`, median `0.0083`, brier `0.1701`, calibration_gap `0.0285`
- 20d: hit_rate `0.8750`, avg `0.0341`, median `0.0424`, brier `0.1251`, calibration_gap `-0.0965`
- 60d: hit_rate `0.9375`, avg `0.0930`, median `0.0940`, brier `0.0782`, calibration_gap `-0.1590`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5500`, avg `0.0017`, median `0.0022`, brier `0.2588`, calibration_gap `0.1508`
- 5d: hit_rate `0.5250`, avg `0.0014`, median `0.0034`, brier `0.2631`, calibration_gap `0.1758`
- 10d: hit_rate `0.7250`, avg `0.0070`, median `0.0100`, brier `0.1919`, calibration_gap `-0.0242`
- 20d: hit_rate `0.8250`, avg `0.0361`, median `0.0370`, brier `0.1681`, calibration_gap `-0.1242`
- 60d: hit_rate `0.9250`, avg `0.0942`, median `0.1112`, brier `0.1168`, calibration_gap `-0.2242`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0041`, median `-0.0156`, brier `0.2665`, calibration_gap `0.1131`
- 5d: hit_rate `0.4375`, avg `0.0032`, median `-0.0027`, brier `0.2655`, calibration_gap `0.1131`
- 10d: hit_rate `0.6875`, avg `0.0128`, median `0.0162`, brier `0.2345`, calibration_gap `-0.1369`
- 20d: hit_rate `0.8125`, avg `0.0422`, median `0.0455`, brier `0.2182`, calibration_gap `-0.2619`
- 60d: hit_rate `0.8125`, avg `0.0887`, median `0.0966`, brier `0.2200`, calibration_gap `-0.2619`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
