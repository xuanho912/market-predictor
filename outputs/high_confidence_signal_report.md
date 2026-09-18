# High Confidence Signal Report

Generated at: `2026-09-18T08:31:20.561823+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0033`, median `0.0050`, brier `0.2718`, calibration_gap `0.1910`
- 5d: hit_rate `0.5000`, avg `-0.0090`, median `-0.0029`, brier `0.3504`, calibration_gap `0.3160`
- 10d: hit_rate `0.3750`, avg `-0.0080`, median `-0.0127`, brier `0.4267`, calibration_gap `0.4410`
- 20d: hit_rate `0.6250`, avg `0.0203`, median `0.0242`, brier `0.2724`, calibration_gap `0.1910`
- 60d: hit_rate `0.7500`, avg `0.0374`, median `0.0519`, brier `0.1936`, calibration_gap `0.0660`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0038`, median `0.0011`, brier `0.3059`, calibration_gap `0.2435`
- 5d: hit_rate `0.5000`, avg `-0.0073`, median `-0.0029`, brier `0.3452`, calibration_gap `0.3060`
- 10d: hit_rate `0.4375`, avg `-0.0047`, median `-0.0074`, brier `0.3828`, calibration_gap `0.3685`
- 20d: hit_rate `0.6250`, avg `0.0223`, median `0.0293`, brier `0.2690`, calibration_gap `0.1810`
- 60d: hit_rate `0.7500`, avg `0.0373`, median `0.0557`, brier `0.1920`, calibration_gap `0.0560`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6500`, avg `0.0006`, median `0.0081`, brier `0.2266`, calibration_gap `0.0370`
- 5d: hit_rate `0.7500`, avg `0.0051`, median `0.0062`, brier `0.1897`, calibration_gap `-0.0630`
- 10d: hit_rate `0.7500`, avg `0.0177`, median `0.0198`, brier `0.1936`, calibration_gap `-0.0630`
- 20d: hit_rate `0.8000`, avg `0.0358`, median `0.0464`, brier `0.1736`, calibration_gap `-0.1130`
- 60d: hit_rate `0.8500`, avg `0.0826`, median `0.1008`, brier `0.1552`, calibration_gap `-0.1630`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0035`, median `0.0045`, brier `0.2597`, calibration_gap `0.1164`
- 5d: hit_rate `0.5000`, avg `-0.0026`, median `0.0003`, brier `0.2836`, calibration_gap `0.1789`
- 10d: hit_rate `0.6250`, avg `0.0056`, median `0.0169`, brier `0.2372`, calibration_gap `0.0539`
- 20d: hit_rate `0.5625`, avg `0.0252`, median `0.0251`, brier `0.2602`, calibration_gap `0.1164`
- 60d: hit_rate `0.8125`, avg `0.0716`, median `0.0920`, brier `0.1702`, calibration_gap `-0.1336`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
