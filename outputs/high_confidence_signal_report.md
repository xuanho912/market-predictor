# High Confidence Signal Report

Generated at: `2026-08-10T13:48:17.518198+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0046`, median `0.0069`, brier `0.1303`, calibration_gap `-0.1515`
- 5d: hit_rate `0.8750`, avg `0.0069`, median `0.0112`, brier `0.1303`, calibration_gap `-0.1515`
- 10d: hit_rate `0.8750`, avg `0.0149`, median `0.0199`, brier `0.1303`, calibration_gap `-0.1515`
- 20d: hit_rate `0.5000`, avg `0.0083`, median `0.0002`, brier `0.3049`, calibration_gap `0.2235`
- 60d: hit_rate `0.3750`, avg `0.0028`, median `-0.0336`, brier `0.3572`, calibration_gap `0.3485`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0032`, median `0.0019`, brier `0.2363`, calibration_gap `0.0871`
- 5d: hit_rate `0.8125`, avg `0.0102`, median `0.0112`, brier `0.1603`, calibration_gap `-0.1004`
- 10d: hit_rate `0.7500`, avg `0.0156`, median `0.0164`, brier `0.1869`, calibration_gap `-0.0379`
- 20d: hit_rate `0.6875`, avg `0.0194`, median `0.0151`, brier `0.2231`, calibration_gap `0.0246`
- 60d: hit_rate `0.3750`, avg `0.0127`, median `-0.0249`, brier `0.3486`, calibration_gap `0.3371`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6000`, avg `0.0012`, median `0.0039`, brier `0.2466`, calibration_gap `0.0898`
- 5d: hit_rate `0.6500`, avg `0.0035`, median `0.0043`, brier `0.2256`, calibration_gap `0.0398`
- 10d: hit_rate `0.5500`, avg `0.0057`, median `0.0091`, brier `0.2637`, calibration_gap `0.1398`
- 20d: hit_rate `0.6500`, avg `0.0095`, median `0.0142`, brier `0.2304`, calibration_gap `0.0398`
- 60d: hit_rate `0.4833`, avg `0.0168`, median `-0.0040`, brier `0.2944`, calibration_gap `0.2064`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0059`, median `0.0048`, brier `0.2344`, calibration_gap `0.0409`
- 5d: hit_rate `0.6875`, avg `0.0061`, median `0.0056`, brier `0.2143`, calibration_gap `-0.0216`
- 10d: hit_rate `0.5000`, avg `0.0041`, median `-0.0045`, brier `0.2771`, calibration_gap `0.1659`
- 20d: hit_rate `0.6250`, avg `0.0016`, median `0.0139`, brier `0.2359`, calibration_gap `0.0409`
- 60d: hit_rate `0.7500`, avg `0.0348`, median `0.0541`, brier `0.1924`, calibration_gap `-0.0841`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
