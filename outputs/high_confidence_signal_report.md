# High Confidence Signal Report

Generated at: `2026-10-22T08:56:52.782910+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0032`, median `-0.0068`, brier `0.2996`, calibration_gap `0.2244`
- 5d: hit_rate `0.5000`, avg `-0.0034`, median `-0.0040`, brier `0.2996`, calibration_gap `0.2244`
- 10d: hit_rate `0.6250`, avg `0.0102`, median `0.0114`, brier `0.2458`, calibration_gap `0.0994`
- 20d: hit_rate `1.0000`, avg `0.0280`, median `0.0287`, brier `0.0760`, calibration_gap `-0.2756`
- 60d: hit_rate `1.0000`, avg `0.0611`, median `0.0700`, brier `0.0760`, calibration_gap `-0.2756`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0046`, median `-0.0112`, brier `0.3488`, calibration_gap `0.3414`
- 5d: hit_rate `0.4375`, avg `-0.0022`, median `-0.0103`, brier `0.3227`, calibration_gap `0.2789`
- 10d: hit_rate `0.4375`, avg `-0.0001`, median `-0.0141`, brier `0.3219`, calibration_gap `0.2789`
- 20d: hit_rate `0.7500`, avg `0.0162`, median `0.0269`, brier `0.1846`, calibration_gap `-0.0336`
- 60d: hit_rate `0.8125`, avg `0.0445`, median `0.0542`, brier `0.1585`, calibration_gap `-0.0961`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0005`, median `0.0025`, brier `0.2361`, calibration_gap `0.0428`
- 5d: hit_rate `0.3750`, avg `-0.0041`, median `-0.0093`, brier `0.3197`, calibration_gap `0.2928`
- 10d: hit_rate `0.5000`, avg `-0.0060`, median `-0.0032`, brier `0.2780`, calibration_gap `0.1678`
- 20d: hit_rate `0.5625`, avg `0.0087`, median `0.0064`, brier `0.2576`, calibration_gap `0.1053`
- 60d: hit_rate `0.5000`, avg `-0.0055`, median `-0.0124`, brier `0.2777`, calibration_gap `0.1678`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
