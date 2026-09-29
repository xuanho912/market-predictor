# High Confidence Signal Report

Generated at: `2026-09-29T01:23:31.266925+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0078`, median `0.0085`, brier `0.1901`, calibration_gap `0.0363`
- 5d: hit_rate `0.7500`, avg `0.0062`, median `0.0108`, brier `0.1901`, calibration_gap `0.0363`
- 10d: hit_rate `1.0000`, avg `0.0090`, median `0.0083`, brier `0.0458`, calibration_gap `-0.2137`
- 20d: hit_rate `0.7500`, avg `0.0316`, median `0.0460`, brier `0.1901`, calibration_gap `0.0363`
- 60d: hit_rate `1.0000`, avg `0.0881`, median `0.0844`, brier `0.0458`, calibration_gap `-0.2137`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0050`, median `0.0116`, brier `0.2135`, calibration_gap `0.0695`
- 5d: hit_rate `0.6875`, avg `0.0058`, median `0.0089`, brier `0.2088`, calibration_gap `0.0695`
- 10d: hit_rate `0.7500`, avg `0.0063`, median `0.0083`, brier `0.1658`, calibration_gap `0.0070`
- 20d: hit_rate `0.8750`, avg `0.0341`, median `0.0424`, brier `0.1324`, calibration_gap `-0.1180`
- 60d: hit_rate `0.9375`, avg `0.0930`, median `0.0940`, brier `0.0847`, calibration_gap `-0.1805`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5000`, avg `-0.0001`, median `-0.0005`, brier `0.2655`, calibration_gap `0.1556`
- 5d: hit_rate `0.5167`, avg `0.0013`, median `0.0028`, brier `0.2562`, calibration_gap `0.1389`
- 10d: hit_rate `0.6833`, avg `0.0089`, median `0.0100`, brier `0.2093`, calibration_gap `-0.0277`
- 20d: hit_rate `0.8167`, avg `0.0312`, median `0.0322`, brier `0.1844`, calibration_gap `-0.1611`
- 60d: hit_rate `0.8833`, avg `0.0764`, median `0.0921`, brier `0.1463`, calibration_gap `-0.2277`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0048`, median `0.0082`, brier `0.2359`, calibration_gap `-0.0447`
- 5d: hit_rate `0.4375`, avg `0.0025`, median `-0.0027`, brier `0.2651`, calibration_gap `0.1428`
- 10d: hit_rate `0.6250`, avg `0.0106`, median `0.0162`, brier `0.2405`, calibration_gap `-0.0447`
- 20d: hit_rate `0.7500`, avg `0.0220`, median `0.0134`, brier `0.2182`, calibration_gap `-0.1697`
- 60d: hit_rate `0.6250`, avg `0.0359`, median `0.0384`, brier `0.2363`, calibration_gap `-0.0447`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
