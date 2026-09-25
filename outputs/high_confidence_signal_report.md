# High Confidence Signal Report

Generated at: `2026-09-25T17:15:36.079979+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0085`, median `0.0126`, brier `0.1088`, calibration_gap `-0.0393`
- 5d: hit_rate `0.8750`, avg `0.0062`, median `0.0076`, brier `0.1088`, calibration_gap `-0.0393`
- 10d: hit_rate `0.6250`, avg `-0.0013`, median `0.0021`, brier `0.2784`, calibration_gap `0.2107`
- 20d: hit_rate `0.8750`, avg `0.0338`, median `0.0460`, brier `0.1123`, calibration_gap `-0.0393`
- 60d: hit_rate `1.0000`, avg `0.0480`, median `0.0565`, brier `0.0271`, calibration_gap `-0.1643`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0043`, median `0.0088`, brier `0.2279`, calibration_gap `0.1357`
- 5d: hit_rate `0.6875`, avg `0.0043`, median `0.0076`, brier `0.2279`, calibration_gap `0.1357`
- 10d: hit_rate `0.6875`, avg `0.0010`, median `0.0060`, brier `0.2341`, calibration_gap `0.1357`
- 20d: hit_rate `0.7500`, avg `0.0164`, median `0.0173`, brier `0.1903`, calibration_gap `0.0732`
- 60d: hit_rate `0.9375`, avg `0.0643`, median `0.0625`, brier `0.0691`, calibration_gap `-0.1143`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5750`, avg `0.0019`, median `0.0040`, brier `0.2632`, calibration_gap `0.1644`
- 5d: hit_rate `0.6000`, avg `-0.0025`, median `0.0016`, brier `0.2606`, calibration_gap `0.1394`
- 10d: hit_rate `0.5750`, avg `-0.0036`, median `0.0049`, brier `0.2728`, calibration_gap `0.1644`
- 20d: hit_rate `0.6750`, avg `0.0068`, median `0.0143`, brier `0.2364`, calibration_gap `0.0644`
- 60d: hit_rate `0.8500`, avg `0.0384`, median `0.0434`, brier `0.1427`, calibration_gap `-0.1106`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0013`, median `0.0004`, brier `0.2736`, calibration_gap `0.1553`
- 5d: hit_rate `0.5625`, avg `-0.0049`, median `0.0009`, brier `0.2523`, calibration_gap `0.0928`
- 10d: hit_rate `0.5625`, avg `-0.0047`, median `0.0061`, brier `0.2533`, calibration_gap `0.0928`
- 20d: hit_rate `0.6875`, avg `-0.0018`, median `0.0127`, brier `0.2172`, calibration_gap `-0.0322`
- 60d: hit_rate `0.8125`, avg `0.0211`, median `0.0306`, brier `0.1776`, calibration_gap `-0.1572`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
