# High Confidence Signal Report

Generated at: `2026-09-17T23:40:12.697724+00:00`

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
- sample_size: `40`
- 3d: hit_rate `0.6000`, avg `-0.0016`, median `0.0057`, brier `0.2680`, calibration_gap `0.1441`
- 5d: hit_rate `0.6250`, avg `-0.0004`, median `0.0017`, brier `0.2654`, calibration_gap `0.1191`
- 10d: hit_rate `0.5750`, avg `0.0043`, median `0.0026`, brier `0.2966`, calibration_gap `0.1691`
- 20d: hit_rate `0.6750`, avg `0.0252`, median `0.0243`, brier `0.2421`, calibration_gap `0.0691`
- 60d: hit_rate `0.7750`, avg `0.0562`, median `0.0618`, brier `0.1878`, calibration_gap `-0.0309`

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
