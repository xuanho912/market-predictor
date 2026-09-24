# High Confidence Signal Report

Generated at: `2026-09-24T17:17:05.137127+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0034`, median `0.0085`, brier `0.1917`, calibration_gap `0.0785`
- 5d: hit_rate `0.7500`, avg `0.0014`, median `0.0068`, brier `0.1917`, calibration_gap `0.0785`
- 10d: hit_rate `0.5000`, avg `-0.0030`, median `-0.0047`, brier `0.3640`, calibration_gap `0.3285`
- 20d: hit_rate `0.8750`, avg `0.0285`, median `0.0324`, brier `0.1171`, calibration_gap `-0.0465`
- 60d: hit_rate `1.0000`, avg `0.0405`, median `0.0415`, brier `0.0296`, calibration_gap `-0.1715`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0011`, median `0.0031`, brier `0.3071`, calibration_gap `0.2548`
- 5d: hit_rate `0.5625`, avg `-0.0032`, median `0.0056`, brier `0.3071`, calibration_gap `0.2548`
- 10d: hit_rate `0.5625`, avg `-0.0069`, median `0.0021`, brier `0.3167`, calibration_gap `0.2548`
- 20d: hit_rate `0.6875`, avg `0.0139`, median `0.0173`, brier `0.2315`, calibration_gap `0.1298`
- 60d: hit_rate `0.8125`, avg `0.0374`, median `0.0501`, brier `0.1494`, calibration_gap `0.0048`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.4250`, avg `-0.0052`, median `-0.0037`, brier `0.3327`, calibration_gap `0.2804`
- 5d: hit_rate `0.4500`, avg `-0.0107`, median `-0.0048`, brier `0.3276`, calibration_gap `0.2554`
- 10d: hit_rate `0.3750`, avg `-0.0112`, median `-0.0067`, brier `0.3678`, calibration_gap `0.3304`
- 20d: hit_rate `0.6500`, avg `0.0021`, median `0.0160`, brier `0.2338`, calibration_gap `0.0554`
- 60d: hit_rate `0.8000`, avg `0.0242`, median `0.0329`, brier `0.1745`, calibration_gap `-0.0946`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0019`, median `-0.0028`, brier `0.2972`, calibration_gap `0.2185`
- 5d: hit_rate `0.5000`, avg `-0.0090`, median `-0.0003`, brier `0.2807`, calibration_gap `0.1560`
- 10d: hit_rate `0.6250`, avg `-0.0055`, median `0.0073`, brier `0.2400`, calibration_gap `0.0310`
- 20d: hit_rate `0.5625`, avg `-0.0105`, median `0.0115`, brier `0.2558`, calibration_gap `0.0935`
- 60d: hit_rate `0.7500`, avg `0.0054`, median `0.0320`, brier `0.1984`, calibration_gap `-0.0940`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
