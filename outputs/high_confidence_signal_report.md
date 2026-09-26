# High Confidence Signal Report

Generated at: `2026-09-26T06:12:32.649298+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0085`, median `0.0126`, brier `0.1103`, calibration_gap `-0.0438`
- 5d: hit_rate `0.8750`, avg `0.0062`, median `0.0076`, brier `0.1103`, calibration_gap `-0.0438`
- 10d: hit_rate `0.6250`, avg `-0.0013`, median `0.0021`, brier `0.2771`, calibration_gap `0.2062`
- 20d: hit_rate `0.8750`, avg `0.0338`, median `0.0460`, brier `0.1125`, calibration_gap `-0.0438`
- 60d: hit_rate `1.0000`, avg `0.0480`, median `0.0565`, brier `0.0286`, calibration_gap `-0.1688`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0025`, median `0.0051`, brier `0.2650`, calibration_gap `0.1932`
- 5d: hit_rate `0.6250`, avg `0.0009`, median `0.0068`, brier `0.2650`, calibration_gap `0.1932`
- 10d: hit_rate `0.6875`, avg `0.0003`, median `0.0049`, brier `0.2342`, calibration_gap `0.1307`
- 20d: hit_rate `0.6875`, avg `0.0153`, median `0.0173`, brier `0.2269`, calibration_gap `0.1307`
- 60d: hit_rate `0.8750`, avg `0.0541`, median `0.0565`, brier `0.1081`, calibration_gap `-0.0568`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0055`, median `-0.0040`, brier `0.3173`, calibration_gap `0.2821`
- 5d: hit_rate `0.4375`, avg `-0.0097`, median `-0.0055`, brier `0.2961`, calibration_gap `0.2196`
- 10d: hit_rate `0.5000`, avg `-0.0117`, median `-0.0034`, brier `0.2751`, calibration_gap `0.1571`
- 20d: hit_rate `0.6875`, avg `-0.0052`, median `0.0127`, brier `0.2168`, calibration_gap `-0.0304`
- 60d: hit_rate `0.8125`, avg `0.0234`, median `0.0320`, brier `0.1771`, calibration_gap `-0.1554`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
