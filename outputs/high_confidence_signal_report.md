# High Confidence Signal Report

Generated at: `2026-08-27T14:48:27.837452+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0032`, median `0.0007`, brier `0.2549`, calibration_gap `0.1297`
- 5d: hit_rate `0.5000`, avg `-0.0046`, median `-0.0047`, brier `0.3152`, calibration_gap `0.2547`
- 10d: hit_rate `0.3750`, avg `-0.0071`, median `-0.0125`, brier `0.3807`, calibration_gap `0.3797`
- 20d: hit_rate `0.6250`, avg `0.0046`, median `0.0166`, brier `0.2471`, calibration_gap `0.1297`
- 60d: hit_rate `0.7500`, avg `0.0252`, median `0.0396`, brier `0.1832`, calibration_gap `0.0047`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0016`, median `0.0007`, brier `0.2795`, calibration_gap `0.1822`
- 5d: hit_rate `0.5000`, avg `-0.0015`, median `-0.0029`, brier `0.3098`, calibration_gap `0.2447`
- 10d: hit_rate `0.5000`, avg `0.0004`, median `0.0002`, brier `0.3140`, calibration_gap `0.2447`
- 20d: hit_rate `0.6875`, avg `0.0117`, median `0.0232`, brier `0.2174`, calibration_gap `0.0572`
- 60d: hit_rate `0.8125`, avg `0.0400`, median `0.0519`, brier `0.1565`, calibration_gap `-0.0678`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5667`, avg `-0.0001`, median `0.0034`, brier `0.2643`, calibration_gap `0.1358`
- 5d: hit_rate `0.5333`, avg `0.0000`, median `0.0008`, brier `0.2780`, calibration_gap `0.1692`
- 10d: hit_rate `0.4833`, avg `0.0036`, median `-0.0016`, brier `0.2961`, calibration_gap `0.2192`
- 20d: hit_rate `0.6833`, avg `0.0115`, median `0.0184`, brier `0.2148`, calibration_gap `0.0192`
- 60d: hit_rate `0.6833`, avg `0.0309`, median `0.0294`, brier `0.2190`, calibration_gap `0.0192`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0003`, median `0.0094`, brier `0.2577`, calibration_gap `0.1128`
- 5d: hit_rate `0.5000`, avg `-0.0030`, median `-0.0001`, brier `0.2805`, calibration_gap `0.1753`
- 10d: hit_rate `0.5000`, avg `-0.0009`, median `-0.0031`, brier `0.2810`, calibration_gap `0.1753`
- 20d: hit_rate `0.6250`, avg `0.0086`, median `0.0078`, brier `0.2412`, calibration_gap `0.0503`
- 60d: hit_rate `0.8750`, avg `0.0622`, median `0.0642`, brier `0.1500`, calibration_gap `-0.1997`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
