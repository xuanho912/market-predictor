# High Confidence Signal Report

Generated at: `2026-09-09T00:46:26.418619+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0060`, median `0.0077`, brier `0.2402`, calibration_gap `0.0579`
- 5d: hit_rate `0.5000`, avg `-0.0090`, median `-0.0030`, brier `0.2970`, calibration_gap `0.1829`
- 10d: hit_rate `0.5000`, avg `-0.0016`, median `-0.0015`, brier `0.2947`, calibration_gap `0.1829`
- 20d: hit_rate `0.7500`, avg `0.0223`, median `0.0364`, brier `0.1952`, calibration_gap `-0.0671`
- 60d: hit_rate `0.6250`, avg `0.0124`, median `0.0400`, brier `0.2498`, calibration_gap `0.0579`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0014`, median `0.0101`, brier `0.2209`, calibration_gap `-0.0222`
- 5d: hit_rate `0.6875`, avg `0.0042`, median `0.0118`, brier `0.2302`, calibration_gap `-0.0222`
- 10d: hit_rate `0.5625`, avg `0.0103`, median `0.0062`, brier `0.2660`, calibration_gap `0.1028`
- 20d: hit_rate `0.8125`, avg `0.0308`, median `0.0364`, brier `0.1793`, calibration_gap `-0.1472`
- 60d: hit_rate `0.6250`, avg `0.0346`, median `0.0512`, brier `0.2433`, calibration_gap `0.0403`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.7667`, avg `0.0115`, median `0.0172`, brier `0.2068`, calibration_gap `-0.1480`
- 5d: hit_rate `0.8167`, avg `0.0160`, median `0.0183`, brier `0.1964`, calibration_gap `-0.1980`
- 10d: hit_rate `0.7333`, avg `0.0227`, median `0.0288`, brier `0.2169`, calibration_gap `-0.1146`
- 20d: hit_rate `0.8000`, avg `0.0373`, median `0.0348`, brier `0.1935`, calibration_gap `-0.1813`
- 60d: hit_rate `0.8167`, avg `0.0711`, median `0.0838`, brier `0.1967`, calibration_gap `-0.1980`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0148`, median `0.0174`, brier `0.2029`, calibration_gap `-0.2249`
- 5d: hit_rate `0.9375`, avg `0.0192`, median `0.0173`, brier `0.1821`, calibration_gap `-0.3499`
- 10d: hit_rate `0.8750`, avg `0.0269`, median `0.0332`, brier `0.1933`, calibration_gap `-0.2874`
- 20d: hit_rate `0.6875`, avg `0.0300`, median `0.0300`, brier `0.2231`, calibration_gap `-0.0999`
- 60d: hit_rate `1.0000`, avg `0.0929`, median `0.0838`, brier `0.1701`, calibration_gap `-0.4124`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
