# High Confidence Signal Report

Generated at: `2026-10-22T17:14:05.174959+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0079`, median `0.0121`, brier `0.2541`, calibration_gap `0.1368`
- 5d: hit_rate `0.3750`, avg `0.0039`, median `-0.0077`, brier `0.3803`, calibration_gap `0.3868`
- 10d: hit_rate `0.7500`, avg `0.0187`, median `0.0143`, brier `0.1905`, calibration_gap `0.0118`
- 20d: hit_rate `0.8750`, avg `0.0351`, median `0.0314`, brier `0.1225`, calibration_gap `-0.1132`
- 60d: hit_rate `1.0000`, avg `0.0719`, median `0.0831`, brier `0.0568`, calibration_gap `-0.2382`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0048`, median `0.0029`, brier `0.2799`, calibration_gap `0.1886`
- 5d: hit_rate `0.5625`, avg `0.0043`, median `0.0006`, brier `0.2835`, calibration_gap `0.1886`
- 10d: hit_rate `0.6250`, avg `0.0153`, median `0.0069`, brier `0.2498`, calibration_gap `0.1261`
- 20d: hit_rate `0.9375`, avg `0.0373`, median `0.0314`, brier `0.0949`, calibration_gap `-0.1864`
- 60d: hit_rate `1.0000`, avg `0.0777`, median `0.0797`, brier `0.0621`, calibration_gap `-0.2489`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.7000`, avg `0.0048`, median `0.0055`, brier `0.2077`, calibration_gap `-0.0481`
- 5d: hit_rate `0.7000`, avg `0.0066`, median `0.0075`, brier `0.2145`, calibration_gap `-0.0481`
- 10d: hit_rate `0.7000`, avg `0.0067`, median `0.0109`, brier `0.2109`, calibration_gap `-0.0481`
- 20d: hit_rate `0.7500`, avg `0.0152`, median `0.0149`, brier `0.1995`, calibration_gap `-0.0981`
- 60d: hit_rate `0.6000`, avg `0.0134`, median `0.0186`, brier `0.2429`, calibration_gap `0.0519`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0030`, median `0.0043`, brier `0.2327`, calibration_gap `0.0220`
- 5d: hit_rate `0.7500`, avg `0.0077`, median `0.0075`, brier `0.1990`, calibration_gap `-0.1030`
- 10d: hit_rate `0.7500`, avg `0.0103`, median `0.0147`, brier `0.1956`, calibration_gap `-0.1030`
- 20d: hit_rate `0.8125`, avg `0.0180`, median `0.0163`, brier `0.1813`, calibration_gap `-0.1655`
- 60d: hit_rate `0.6250`, avg `0.0207`, median `0.0354`, brier `0.2349`, calibration_gap `0.0220`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
