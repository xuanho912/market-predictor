# High Confidence Signal Report

Generated at: `2026-07-08T00:10:59.188989+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0105`, median `-0.0075`, brier `0.4752`, calibration_gap `0.6024`
- 5d: hit_rate `0.3750`, avg `-0.0085`, median `-0.0029`, brier `0.3665`, calibration_gap `0.3524`
- 10d: hit_rate `0.2500`, avg `-0.0090`, median `-0.0087`, brier `0.4201`, calibration_gap `0.4774`
- 20d: hit_rate `0.5000`, avg `0.0053`, median `0.0039`, brier `0.2939`, calibration_gap `0.2274`
- 60d: hit_rate `0.6250`, avg `0.0225`, median `0.0291`, brier `0.2401`, calibration_gap `0.1024`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.1875`, avg `-0.0093`, median `-0.0075`, brier `0.4381`, calibration_gap `0.5312`
- 5d: hit_rate `0.4375`, avg `-0.0077`, median `-0.0029`, brier `0.3312`, calibration_gap `0.2812`
- 10d: hit_rate `0.3125`, avg `-0.0029`, median `-0.0060`, brier `0.3842`, calibration_gap `0.4062`
- 20d: hit_rate `0.6250`, avg `0.0116`, median `0.0162`, brier `0.2416`, calibration_gap `0.0937`
- 60d: hit_rate `0.5625`, avg `0.0193`, median `0.0291`, brier `0.2671`, calibration_gap `0.1562`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.4625`, avg `-0.0025`, median `-0.0014`, brier `0.3016`, calibration_gap `0.2205`
- 5d: hit_rate `0.5125`, avg `-0.0039`, median `0.0008`, brier `0.2790`, calibration_gap `0.1705`
- 10d: hit_rate `0.5000`, avg `-0.0003`, median `0.0000`, brier `0.2861`, calibration_gap `0.1830`
- 20d: hit_rate `0.6250`, avg `0.0035`, median `0.0078`, brier `0.2357`, calibration_gap `0.0580`
- 60d: hit_rate `0.4750`, avg `0.0021`, median `-0.0054`, brier `0.2897`, calibration_gap `0.2080`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0007`, median `0.0069`, brier `0.2547`, calibration_gap `0.0878`
- 5d: hit_rate `0.5000`, avg `-0.0022`, median `-0.0004`, brier `0.2730`, calibration_gap `0.1503`
- 10d: hit_rate `0.5000`, avg `0.0011`, median `-0.0033`, brier `0.2733`, calibration_gap `0.1503`
- 20d: hit_rate `0.4375`, avg `-0.0039`, median `-0.0041`, brier `0.2921`, calibration_gap `0.2128`
- 60d: hit_rate `0.5625`, avg `0.0174`, median `0.0322`, brier `0.2543`, calibration_gap `0.0878`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
