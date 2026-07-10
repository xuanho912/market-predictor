# High Confidence Signal Report

Generated at: `2026-07-10T05:12:02.070620+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0081`, median `-0.0003`, brier `0.3058`, calibration_gap `0.2194`
- 5d: hit_rate `0.3750`, avg `-0.0095`, median `-0.0139`, brier `0.3554`, calibration_gap `0.3444`
- 10d: hit_rate `0.5000`, avg `-0.0027`, median `0.0002`, brier `0.3059`, calibration_gap `0.2194`
- 20d: hit_rate `1.0000`, avg `0.0203`, median `0.0205`, brier `0.0789`, calibration_gap `-0.2806`
- 60d: hit_rate `0.8750`, avg `0.0394`, median `0.0449`, brier `0.1320`, calibration_gap `-0.1556`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0045`, median `-0.0014`, brier `0.3241`, calibration_gap `0.2753`
- 5d: hit_rate `0.5000`, avg `-0.0027`, median `0.0010`, brier `0.2979`, calibration_gap `0.2128`
- 10d: hit_rate `0.5625`, avg `0.0034`, median `0.0055`, brier `0.2732`, calibration_gap `0.1503`
- 20d: hit_rate `0.9375`, avg `0.0219`, median `0.0237`, brier `0.1088`, calibration_gap `-0.2247`
- 60d: hit_rate `0.6250`, avg `0.0233`, median `0.0384`, brier `0.2383`, calibration_gap `0.0878`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5000`, avg `-0.0024`, median `-0.0001`, brier `0.2913`, calibration_gap `0.1880`
- 5d: hit_rate `0.4833`, avg `-0.0041`, median `-0.0008`, brier `0.2959`, calibration_gap `0.2046`
- 10d: hit_rate `0.4167`, avg `-0.0014`, median `-0.0069`, brier `0.3211`, calibration_gap `0.2713`
- 20d: hit_rate `0.6333`, avg `0.0033`, median `0.0103`, brier `0.2336`, calibration_gap `0.0546`
- 60d: hit_rate `0.5500`, avg `0.0138`, median `0.0209`, brier `0.2666`, calibration_gap `0.1380`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0013`, median `0.0037`, brier `0.2183`, calibration_gap `-0.0347`
- 5d: hit_rate `0.5625`, avg `-0.0009`, median `0.0033`, brier `0.2566`, calibration_gap `0.0903`
- 10d: hit_rate `0.6250`, avg `0.0073`, median `0.0037`, brier `0.2357`, calibration_gap `0.0278`
- 20d: hit_rate `0.7500`, avg `0.0034`, median `0.0082`, brier `0.1969`, calibration_gap `-0.0972`
- 60d: hit_rate `0.5000`, avg `0.0132`, median `0.0021`, brier `0.2759`, calibration_gap `0.1528`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
