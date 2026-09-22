# High Confidence Signal Report

Generated at: `2026-09-22T17:00:21.624412+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0032`, median `-0.0036`, brier `0.3350`, calibration_gap `0.2838`
- 5d: hit_rate `0.5000`, avg `-0.0091`, median `-0.0029`, brier `0.3352`, calibration_gap `0.2838`
- 10d: hit_rate `0.3750`, avg `-0.0075`, median `-0.0090`, brier `0.3993`, calibration_gap `0.4088`
- 20d: hit_rate `0.3750`, avg `0.0039`, median `-0.0047`, brier `0.4000`, calibration_gap `0.4088`
- 60d: hit_rate `0.5000`, avg `0.0124`, median `0.0042`, brier `0.3292`, calibration_gap `0.2838`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0082`, median `-0.0083`, brier `0.3612`, calibration_gap `0.3371`
- 5d: hit_rate `0.3750`, avg `-0.0112`, median `-0.0129`, brier `0.3940`, calibration_gap `0.3996`
- 10d: hit_rate `0.2500`, avg `-0.0123`, median `-0.0120`, brier `0.4601`, calibration_gap `0.5246`
- 20d: hit_rate `0.5000`, avg `0.0114`, median `0.0072`, brier `0.3273`, calibration_gap `0.2746`
- 60d: hit_rate `0.6875`, avg `0.0245`, median `0.0376`, brier `0.2251`, calibration_gap `0.0871`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5167`, avg `-0.0031`, median `0.0011`, brier `0.2995`, calibration_gap `0.1976`
- 5d: hit_rate `0.5000`, avg `-0.0070`, median `-0.0000`, brier `0.3087`, calibration_gap `0.2143`
- 10d: hit_rate `0.4000`, avg `-0.0057`, median `-0.0072`, brier `0.3518`, calibration_gap `0.3143`
- 20d: hit_rate `0.6000`, avg `0.0082`, median `0.0143`, brier `0.2611`, calibration_gap `0.1143`
- 60d: hit_rate `0.7000`, avg `0.0219`, median `0.0343`, brier `0.2170`, calibration_gap `0.0143`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0076`, median `0.0099`, brier `0.1964`, calibration_gap `-0.0882`
- 5d: hit_rate `0.7500`, avg `0.0060`, median `0.0098`, brier `0.1980`, calibration_gap `-0.0882`
- 10d: hit_rate `0.7500`, avg `0.0086`, median `0.0115`, brier `0.1949`, calibration_gap `-0.0882`
- 20d: hit_rate `0.6250`, avg `0.0023`, median `0.0061`, brier `0.2355`, calibration_gap `0.0368`
- 60d: hit_rate `0.7500`, avg `0.0105`, median `0.0403`, brier `0.1972`, calibration_gap `-0.0882`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
