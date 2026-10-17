# High Confidence Signal Report

Generated at: `2026-10-17T01:05:44.684779+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0036`, median `0.0116`, brier `0.2348`, calibration_gap `0.0438`
- 5d: hit_rate `0.6250`, avg `0.0021`, median `0.0088`, brier `0.2233`, calibration_gap `0.0438`
- 10d: hit_rate `0.5000`, avg `0.0042`, median `0.0053`, brier `0.2727`, calibration_gap `0.1688`
- 20d: hit_rate `0.8750`, avg `0.0311`, median `0.0370`, brier `0.1479`, calibration_gap `-0.2062`
- 60d: hit_rate `0.7500`, avg `0.0592`, median `0.0666`, brier `0.1964`, calibration_gap `-0.0812`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0009`, median `-0.0016`, brier `0.2877`, calibration_gap `0.2176`
- 5d: hit_rate `0.5000`, avg `-0.0004`, median `0.0007`, brier `0.2649`, calibration_gap `0.1551`
- 10d: hit_rate `0.4375`, avg `-0.0024`, median `-0.0032`, brier `0.2895`, calibration_gap `0.2176`
- 20d: hit_rate `0.6875`, avg `0.0170`, median `0.0338`, brier `0.2097`, calibration_gap `-0.0324`
- 60d: hit_rate `0.8125`, avg `0.0603`, median `0.0525`, brier `0.1793`, calibration_gap `-0.1574`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5500`, avg `0.0037`, median `0.0054`, brier `0.2540`, calibration_gap `0.0840`
- 5d: hit_rate `0.5500`, avg `0.0028`, median `0.0050`, brier `0.2404`, calibration_gap `0.0840`
- 10d: hit_rate `0.5500`, avg `0.0042`, median `0.0104`, brier `0.2505`, calibration_gap `0.0840`
- 20d: hit_rate `0.8000`, avg `0.0280`, median `0.0331`, brier `0.1787`, calibration_gap `-0.1660`
- 60d: hit_rate `0.8000`, avg `0.0608`, median `0.0578`, brier `0.1912`, calibration_gap `-0.1660`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0032`, median `-0.0027`, brier `0.2507`, calibration_gap `0.0157`
- 5d: hit_rate `0.3750`, avg `-0.0032`, median `-0.0132`, brier `0.2573`, calibration_gap `0.1407`
- 10d: hit_rate `0.5625`, avg `-0.0075`, median `0.0036`, brier `0.2518`, calibration_gap `-0.0468`
- 20d: hit_rate `0.5000`, avg `0.0072`, median `0.0044`, brier `0.2527`, calibration_gap `0.0157`
- 60d: hit_rate `0.8125`, avg `0.0903`, median `0.0955`, brier `0.2390`, calibration_gap `-0.2968`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
