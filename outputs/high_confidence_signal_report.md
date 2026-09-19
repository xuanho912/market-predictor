# High Confidence Signal Report

Generated at: `2026-09-19T00:45:34.866127+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0090`, median `0.0116`, brier `0.1305`, calibration_gap `-0.1444`
- 5d: hit_rate `0.8750`, avg `0.0096`, median `0.0089`, brier `0.1441`, calibration_gap `-0.1444`
- 10d: hit_rate `0.7500`, avg `0.0068`, median `0.0074`, brier `0.2013`, calibration_gap `-0.0194`
- 20d: hit_rate `1.0000`, avg `0.0519`, median `0.0548`, brier `0.0733`, calibration_gap `-0.2694`
- 60d: hit_rate `0.8750`, avg `0.0724`, median `0.0751`, brier `0.1441`, calibration_gap `-0.1444`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0007`, median `0.0079`, brier `0.2254`, calibration_gap `0.0731`
- 5d: hit_rate `0.6250`, avg `0.0010`, median `0.0080`, brier `0.2323`, calibration_gap `0.0731`
- 10d: hit_rate `0.6250`, avg `-0.0017`, median `0.0040`, brier `0.2410`, calibration_gap `0.0731`
- 20d: hit_rate `0.8750`, avg `0.0354`, median `0.0445`, brier `0.1325`, calibration_gap `-0.1769`
- 60d: hit_rate `0.9375`, avg `0.0871`, median `0.0844`, brier `0.1281`, calibration_gap `-0.2394`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.5875`, avg `0.0028`, median `0.0054`, brier `0.2411`, calibration_gap `0.0284`
- 5d: hit_rate `0.5750`, avg `0.0044`, median `0.0080`, brier `0.2468`, calibration_gap `0.0409`
- 10d: hit_rate `0.6625`, avg `0.0116`, median `0.0113`, brier `0.2320`, calibration_gap `-0.0466`
- 20d: hit_rate `0.8000`, avg `0.0337`, median `0.0343`, brier `0.1933`, calibration_gap `-0.1841`
- 60d: hit_rate `0.8000`, avg `0.0702`, median `0.0923`, brier `0.1913`, calibration_gap `-0.1841`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0112`, median `-0.0119`, brier `0.2782`, calibration_gap `0.1844`
- 5d: hit_rate `0.3750`, avg `-0.0089`, median `-0.0107`, brier `0.2766`, calibration_gap `0.1844`
- 10d: hit_rate `0.6250`, avg `0.0080`, median `0.0154`, brier `0.2447`, calibration_gap `-0.0656`
- 20d: hit_rate `0.8125`, avg `0.0272`, median `0.0338`, brier `0.2181`, calibration_gap `-0.2531`
- 60d: hit_rate `0.6250`, avg `0.0427`, median `0.0781`, brier `0.2447`, calibration_gap `-0.0656`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
