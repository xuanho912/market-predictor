# High Confidence Signal Report

Generated at: `2026-08-31T23:59:30.745159+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0044`, median `-0.0004`, brier `0.3265`, calibration_gap `0.2793`
- 5d: hit_rate `0.5000`, avg `-0.0058`, median `-0.0029`, brier `0.3251`, calibration_gap `0.2793`
- 10d: hit_rate `0.2500`, avg `-0.0082`, median `-0.0127`, brier `0.4736`, calibration_gap `0.5293`
- 20d: hit_rate `0.6250`, avg `0.0156`, median `0.0250`, brier `0.2611`, calibration_gap `0.1543`
- 60d: hit_rate `0.8750`, avg `0.0521`, median `0.0588`, brier `0.1176`, calibration_gap `-0.0957`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0039`, median `-0.0015`, brier `0.3539`, calibration_gap `0.3318`
- 5d: hit_rate `0.4375`, avg `-0.0078`, median `-0.0084`, brier `0.3533`, calibration_gap `0.3318`
- 10d: hit_rate `0.3750`, avg `-0.0054`, median `-0.0080`, brier `0.3953`, calibration_gap `0.3943`
- 20d: hit_rate `0.6250`, avg `0.0035`, median `0.0166`, brier `0.2573`, calibration_gap `0.1443`
- 60d: hit_rate `0.8125`, avg `0.0410`, median `0.0588`, brier `0.1524`, calibration_gap `-0.0432`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4833`, avg `-0.0016`, median `-0.0015`, brier `0.3112`, calibration_gap `0.2436`
- 5d: hit_rate `0.5000`, avg `-0.0031`, median `-0.0011`, brier `0.3020`, calibration_gap `0.2270`
- 10d: hit_rate `0.4000`, avg `-0.0002`, median `-0.0073`, brier `0.3509`, calibration_gap `0.3270`
- 20d: hit_rate `0.6667`, avg `0.0110`, median `0.0181`, brier `0.2302`, calibration_gap `0.0603`
- 60d: hit_rate `0.7000`, avg `0.0416`, median `0.0586`, brier `0.2146`, calibration_gap `0.0270`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0023`, median `-0.0002`, brier `0.2812`, calibration_gap `0.1833`
- 5d: hit_rate `0.4375`, avg `-0.0033`, median `-0.0053`, brier `0.3048`, calibration_gap `0.2458`
- 10d: hit_rate `0.4375`, avg `-0.0045`, median `-0.0131`, brier `0.3091`, calibration_gap `0.2458`
- 20d: hit_rate `0.6875`, avg `0.0181`, median `0.0149`, brier `0.2183`, calibration_gap `-0.0042`
- 60d: hit_rate `0.8125`, avg `0.0549`, median `0.0590`, brier `0.1706`, calibration_gap `-0.1292`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
