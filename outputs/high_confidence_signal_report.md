# High Confidence Signal Report

Generated at: `2026-06-26T23:46:17.932057+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0028`, median `0.0017`, brier `0.3260`, calibration_gap `0.2689`
- 5d: hit_rate `0.2500`, avg `-0.0055`, median `-0.0077`, brier `0.4603`, calibration_gap `0.5189`
- 10d: hit_rate `0.3750`, avg `0.0011`, median `-0.0021`, brier `0.3840`, calibration_gap `0.3939`
- 20d: hit_rate `0.8750`, avg `0.0246`, median `0.0284`, brier `0.1228`, calibration_gap `-0.1061`
- 60d: hit_rate `1.0000`, avg `0.0788`, median `0.0834`, brier `0.0535`, calibration_gap `-0.2311`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0025`, median `0.0004`, brier `0.3193`, calibration_gap `0.2585`
- 5d: hit_rate `0.2500`, avg `-0.0073`, median `-0.0077`, brier `0.4482`, calibration_gap `0.5085`
- 10d: hit_rate `0.4375`, avg `0.0039`, median `-0.0014`, brier `0.3464`, calibration_gap `0.3210`
- 20d: hit_rate `0.9375`, avg `0.0238`, median `0.0265`, brier `0.0932`, calibration_gap `-0.1790`
- 60d: hit_rate `1.0000`, avg `0.0752`, median `0.0745`, brier `0.0585`, calibration_gap `-0.2415`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4500`, avg `-0.0003`, median `-0.0036`, brier `0.2896`, calibration_gap `0.1961`
- 5d: hit_rate `0.4833`, avg `-0.0005`, median `-0.0012`, brier `0.2793`, calibration_gap `0.1628`
- 10d: hit_rate `0.5000`, avg `-0.0007`, median `-0.0003`, brier `0.2752`, calibration_gap `0.1461`
- 20d: hit_rate `0.6833`, avg `0.0093`, median `0.0193`, brier `0.2190`, calibration_gap `-0.0372`
- 60d: hit_rate `0.7500`, avg `0.0395`, median `0.0514`, brier `0.2040`, calibration_gap `-0.1039`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0017`, median `-0.0039`, brier `0.2727`, calibration_gap `0.1594`
- 5d: hit_rate `0.5000`, avg `-0.0010`, median `0.0011`, brier `0.2588`, calibration_gap `0.0969`
- 10d: hit_rate `0.5000`, avg `-0.0000`, median `-0.0014`, brier `0.2608`, calibration_gap `0.0969`
- 20d: hit_rate `0.6875`, avg `0.0127`, median `0.0274`, brier `0.2233`, calibration_gap `-0.0906`
- 60d: hit_rate `0.8125`, avg `0.0580`, median `0.0748`, brier `0.1994`, calibration_gap `-0.2156`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
