# High Confidence Signal Report

Generated at: `2026-10-13T19:21:34.642186+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0049`, median `-0.0033`, brier `0.3147`, calibration_gap `0.2511`
- 5d: hit_rate `0.5000`, avg `-0.0038`, median `-0.0042`, brier `0.3147`, calibration_gap `0.2511`
- 10d: hit_rate `0.5000`, avg `-0.0029`, median `-0.0048`, brier `0.3146`, calibration_gap `0.2511`
- 20d: hit_rate `0.6250`, avg `0.0147`, median `0.0173`, brier `0.2480`, calibration_gap `0.1261`
- 60d: hit_rate `0.8750`, avg `0.0265`, median `0.0378`, brier `0.1240`, calibration_gap `-0.1239`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0042`, median `-0.0033`, brier `0.3106`, calibration_gap `0.2436`
- 5d: hit_rate `0.4375`, avg `-0.0087`, median `-0.0098`, brier `0.3395`, calibration_gap `0.3061`
- 10d: hit_rate `0.3750`, avg `-0.0131`, median `-0.0116`, brier `0.3669`, calibration_gap `0.3686`
- 20d: hit_rate `0.5625`, avg `0.0104`, median `0.0078`, brier `0.2768`, calibration_gap `0.1811`
- 60d: hit_rate `0.7500`, avg `0.0228`, median `0.0378`, brier `0.1856`, calibration_gap `-0.0064`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.4250`, avg `-0.0075`, median `-0.0056`, brier `0.3291`, calibration_gap `0.2906`
- 5d: hit_rate `0.4250`, avg `-0.0107`, median `-0.0162`, brier `0.3309`, calibration_gap `0.2906`
- 10d: hit_rate `0.3500`, avg `-0.0127`, median `-0.0109`, brier `0.3612`, calibration_gap `0.3656`
- 20d: hit_rate `0.6000`, avg `0.0068`, median `0.0095`, brier `0.2539`, calibration_gap `0.1156`
- 60d: hit_rate `0.6750`, avg `0.0178`, median `0.0484`, brier `0.2180`, calibration_gap `0.0406`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0007`, median `0.0027`, brier `0.2739`, calibration_gap `0.1577`
- 5d: hit_rate `0.5625`, avg `-0.0025`, median `0.0016`, brier `0.2553`, calibration_gap `0.0952`
- 10d: hit_rate `0.5625`, avg `-0.0019`, median `0.0014`, brier `0.2569`, calibration_gap `0.0952`
- 20d: hit_rate `0.6875`, avg `0.0131`, median `0.0157`, brier `0.2158`, calibration_gap `-0.0298`
- 60d: hit_rate `0.7500`, avg `0.0384`, median `0.0356`, brier `0.1966`, calibration_gap `-0.0923`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
