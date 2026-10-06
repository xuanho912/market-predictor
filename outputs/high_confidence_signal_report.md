# High Confidence Signal Report

Generated at: `2026-10-06T10:48:36.167078+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0055`, median `0.0085`, brier `0.1935`, calibration_gap `0.0762`
- 5d: hit_rate `0.7500`, avg `0.0040`, median `0.0068`, brier `0.1935`, calibration_gap `0.0762`
- 10d: hit_rate `0.6250`, avg `0.0016`, median `0.0041`, brier `0.2791`, calibration_gap `0.2012`
- 20d: hit_rate `0.7500`, avg `0.0178`, median `0.0104`, brier `0.1993`, calibration_gap `0.0762`
- 60d: hit_rate `1.0000`, avg `0.0613`, median `0.0565`, brier `0.0304`, calibration_gap `-0.1738`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0025`, median `0.0051`, brier `0.2675`, calibration_gap `0.1887`
- 5d: hit_rate `0.5625`, avg `-0.0024`, median `0.0056`, brier `0.3051`, calibration_gap `0.2512`
- 10d: hit_rate `0.5625`, avg `-0.0064`, median `0.0023`, brier `0.3098`, calibration_gap `0.2512`
- 20d: hit_rate `0.6250`, avg `0.0064`, median `0.0085`, brier `0.2701`, calibration_gap `0.1887`
- 60d: hit_rate `0.9375`, avg `0.0595`, median `0.0712`, brier `0.0724`, calibration_gap `-0.1238`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5000`, avg `0.0001`, median `0.0004`, brier `0.2682`, calibration_gap `0.1340`
- 5d: hit_rate `0.6000`, avg `-0.0012`, median `0.0024`, brier `0.2425`, calibration_gap `0.0340`
- 10d: hit_rate `0.5500`, avg `0.0033`, median `0.0074`, brier `0.2554`, calibration_gap `0.0840`
- 20d: hit_rate `0.6500`, avg `0.0058`, median `0.0206`, brier `0.2229`, calibration_gap `-0.0160`
- 60d: hit_rate `0.8000`, avg `0.0135`, median `0.0344`, brier `0.1826`, calibration_gap `-0.1660`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0014`, median `0.0004`, brier `0.2649`, calibration_gap `0.1271`
- 5d: hit_rate `0.6250`, avg `-0.0000`, median `0.0038`, brier `0.2328`, calibration_gap `0.0021`
- 10d: hit_rate `0.5625`, avg `0.0055`, median `0.0074`, brier `0.2489`, calibration_gap `0.0646`
- 20d: hit_rate `0.6250`, avg `0.0061`, median `0.0146`, brier `0.2309`, calibration_gap `0.0021`
- 60d: hit_rate `0.7500`, avg `0.0039`, median `0.0306`, brier `0.1997`, calibration_gap `-0.1229`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
