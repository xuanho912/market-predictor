# High Confidence Signal Report

Generated at: `2026-10-24T01:22:25.629903+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0082`, median `0.0189`, brier `0.2490`, calibration_gap `0.0828`
- 5d: hit_rate `0.6250`, avg `0.0112`, median `0.0149`, brier `0.2490`, calibration_gap `0.0828`
- 10d: hit_rate `0.5000`, avg `0.0004`, median `0.0030`, brier `0.2995`, calibration_gap `0.2078`
- 20d: hit_rate `0.5000`, avg `-0.0145`, median `-0.0039`, brier `0.2995`, calibration_gap `0.2078`
- 60d: hit_rate `0.8750`, avg `0.0595`, median `0.0674`, brier `0.1475`, calibration_gap `-0.1672`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0002`, median `-0.0028`, brier `0.3161`, calibration_gap `0.2612`
- 5d: hit_rate `0.5000`, avg `-0.0037`, median `-0.0080`, brier `0.2930`, calibration_gap `0.1987`
- 10d: hit_rate `0.3750`, avg `-0.0130`, median `-0.0293`, brier `0.3408`, calibration_gap `0.3237`
- 20d: hit_rate `0.3125`, avg `-0.0235`, median `-0.0324`, brier `0.3644`, calibration_gap `0.3862`
- 60d: hit_rate `0.8750`, avg `0.0514`, median `0.0458`, brier `0.1445`, calibration_gap `-0.1763`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0092`, median `0.0117`, brier `0.2271`, calibration_gap `-0.1103`
- 5d: hit_rate `0.7500`, avg `0.0068`, median `0.0190`, brier `0.2185`, calibration_gap `-0.1728`
- 10d: hit_rate `0.6875`, avg `0.0156`, median `0.0252`, brier `0.2271`, calibration_gap `-0.1103`
- 20d: hit_rate `0.8125`, avg `0.0227`, median `0.0231`, brier `0.2071`, calibration_gap `-0.2353`
- 60d: hit_rate `0.9375`, avg `0.1063`, median `0.1182`, brier `0.1876`, calibration_gap `-0.3603`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
