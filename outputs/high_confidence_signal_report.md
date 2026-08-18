# High Confidence Signal Report

Generated at: `2026-08-18T21:53:45.827924+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `1.0000`, avg `0.0100`, median `0.0104`, brier `0.0796`, calibration_gap `-0.2817`
- 5d: hit_rate `1.0000`, avg `0.0122`, median `0.0112`, brier `0.0796`, calibration_gap `-0.2817`
- 10d: hit_rate `1.0000`, avg `0.0174`, median `0.0199`, brier `0.0796`, calibration_gap `-0.2817`
- 20d: hit_rate `0.5000`, avg `0.0077`, median `0.0002`, brier `0.3006`, calibration_gap `0.2183`
- 60d: hit_rate `0.3750`, avg `0.0077`, median `-0.0336`, brier `0.3532`, calibration_gap `0.3433`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.8750`, avg `0.0079`, median `0.0083`, brier `0.1352`, calibration_gap `-0.1704`
- 5d: hit_rate `0.9375`, avg `0.0112`, median `0.0103`, brier `0.1111`, calibration_gap `-0.2329`
- 10d: hit_rate `0.8125`, avg `0.0136`, median `0.0199`, brier `0.1588`, calibration_gap `-0.1079`
- 20d: hit_rate `0.6875`, avg `0.0136`, median `0.0162`, brier `0.2220`, calibration_gap `0.0171`
- 60d: hit_rate `0.4375`, avg `0.0162`, median `-0.0240`, brier `0.3203`, calibration_gap `0.2671`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6375`, avg `0.0044`, median `0.0066`, brier `0.2305`, calibration_gap `0.0361`
- 5d: hit_rate `0.6250`, avg `0.0056`, median `0.0053`, brier `0.2337`, calibration_gap `0.0486`
- 10d: hit_rate `0.6375`, avg `0.0087`, median `0.0113`, brier `0.2291`, calibration_gap `0.0361`
- 20d: hit_rate `0.7250`, avg `0.0184`, median `0.0222`, brier `0.2030`, calibration_gap `-0.0514`
- 60d: hit_rate `0.6750`, avg `0.0322`, median `0.0456`, brier `0.2268`, calibration_gap `-0.0014`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0049`, median `0.0075`, brier `0.2359`, calibration_gap `0.0231`
- 5d: hit_rate `0.6250`, avg `-0.0000`, median `0.0034`, brier `0.2357`, calibration_gap `0.0231`
- 10d: hit_rate `0.5625`, avg `0.0011`, median `0.0064`, brier `0.2560`, calibration_gap `0.0856`
- 20d: hit_rate `0.5625`, avg `0.0057`, median `0.0178`, brier `0.2539`, calibration_gap `0.0856`
- 60d: hit_rate `0.9375`, avg `0.0533`, median `0.0574`, brier `0.1431`, calibration_gap `-0.2894`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
