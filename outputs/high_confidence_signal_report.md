# High Confidence Signal Report

Generated at: `2026-07-21T14:25:58.961812+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0068`, median `0.0007`, brier `0.2548`, calibration_gap `0.1408`
- 5d: hit_rate `0.3750`, avg `-0.0135`, median `-0.0084`, brier `0.3817`, calibration_gap `0.3908`
- 10d: hit_rate `0.1250`, avg `-0.0156`, median `-0.0189`, brier `0.5199`, calibration_gap `0.6408`
- 20d: hit_rate `0.5000`, avg `0.0034`, median `0.0084`, brier `0.3171`, calibration_gap `0.2658`
- 60d: hit_rate `0.7500`, avg `0.0328`, median `0.0519`, brier `0.1843`, calibration_gap `0.0158`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0051`, median `0.0007`, brier `0.2824`, calibration_gap `0.1930`
- 5d: hit_rate `0.4375`, avg `-0.0093`, median `-0.0045`, brier `0.3459`, calibration_gap `0.3180`
- 10d: hit_rate `0.1875`, avg `-0.0107`, median `-0.0127`, brier `0.4762`, calibration_gap `0.5680`
- 20d: hit_rate `0.6875`, avg `0.0142`, median `0.0205`, brier `0.2220`, calibration_gap `0.0680`
- 60d: hit_rate `0.8125`, avg `0.0524`, median `0.0597`, brier `0.1556`, calibration_gap `-0.0570`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.4000`, avg `-0.0105`, median `-0.0097`, brier `0.3533`, calibration_gap `0.3364`
- 5d: hit_rate `0.3500`, avg `-0.0171`, median `-0.0192`, brier `0.3760`, calibration_gap `0.3864`
- 10d: hit_rate `0.2500`, avg `-0.0052`, median `-0.0074`, brier `0.4262`, calibration_gap `0.4864`
- 20d: hit_rate `0.5500`, avg `0.0105`, median `0.0101`, brier `0.2768`, calibration_gap `0.1864`
- 60d: hit_rate `0.6000`, avg `0.0314`, median `0.0418`, brier `0.2532`, calibration_gap `0.1364`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0008`, median `0.0032`, brier `0.2390`, calibration_gap `0.0692`
- 5d: hit_rate `0.5000`, avg `0.0006`, median `0.0012`, brier `0.2883`, calibration_gap `0.1942`
- 10d: hit_rate `0.6250`, avg `0.0069`, median `0.0100`, brier `0.2398`, calibration_gap `0.0692`
- 20d: hit_rate `0.8750`, avg `0.0265`, median `0.0400`, brier `0.1423`, calibration_gap `-0.1808`
- 60d: hit_rate `0.5625`, avg `0.0319`, median `0.0822`, brier `0.2632`, calibration_gap `0.1317`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
