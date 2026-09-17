# High Confidence Signal Report

Generated at: `2026-09-17T17:03:05.143583+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0005`, median `0.0050`, brier `0.2729`, calibration_gap `0.1928`
- 5d: hit_rate `0.5000`, avg `-0.0070`, median `-0.0029`, brier `0.3516`, calibration_gap `0.3178`
- 10d: hit_rate `0.5000`, avg `-0.0057`, median `-0.0036`, brier `0.3504`, calibration_gap `0.3178`
- 20d: hit_rate `0.5000`, avg `0.0164`, median `0.0087`, brier `0.3494`, calibration_gap `0.3178`
- 60d: hit_rate `0.6250`, avg `0.0258`, median `0.0434`, brier `0.2707`, calibration_gap `0.1928`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0038`, median `0.0011`, brier `0.3071`, calibration_gap `0.2462`
- 5d: hit_rate `0.5000`, avg `-0.0073`, median `-0.0029`, brier `0.3465`, calibration_gap `0.3087`
- 10d: hit_rate `0.4375`, avg `-0.0047`, median `-0.0074`, brier `0.3842`, calibration_gap `0.3712`
- 20d: hit_rate `0.6250`, avg `0.0223`, median `0.0293`, brier `0.2698`, calibration_gap `0.1837`
- 60d: hit_rate `0.7500`, avg `0.0373`, median `0.0557`, brier `0.1921`, calibration_gap `0.0587`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6250`, avg `-0.0005`, median `0.0065`, brier `0.2552`, calibration_gap `0.1213`
- 5d: hit_rate `0.6250`, avg `0.0012`, median `0.0026`, brier `0.2658`, calibration_gap `0.1213`
- 10d: hit_rate `0.6000`, avg `0.0064`, median `0.0048`, brier `0.2825`, calibration_gap `0.1463`
- 20d: hit_rate `0.7250`, avg `0.0298`, median `0.0308`, brier `0.2189`, calibration_gap `0.0213`
- 60d: hit_rate `0.8250`, avg `0.0627`, median `0.0618`, brier `0.1640`, calibration_gap `-0.0787`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0022`, median `0.0078`, brier `0.2387`, calibration_gap `0.0590`
- 5d: hit_rate `0.5625`, avg `-0.0000`, median `0.0026`, brier `0.2621`, calibration_gap `0.1215`
- 10d: hit_rate `0.6250`, avg `0.0115`, median `0.0190`, brier `0.2395`, calibration_gap `0.0590`
- 20d: hit_rate `0.8125`, avg `0.0432`, median `0.0464`, brier `0.1695`, calibration_gap `-0.1285`
- 60d: hit_rate `0.9375`, avg `0.0893`, median `0.1071`, brier `0.1230`, calibration_gap `-0.2535`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
