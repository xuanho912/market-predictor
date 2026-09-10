# High Confidence Signal Report

Generated at: `2026-09-10T01:03:29.109261+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0013`, median `0.0116`, brier `0.2328`, calibration_gap `0.0523`
- 5d: hit_rate `0.6250`, avg `-0.0016`, median `0.0036`, brier `0.2552`, calibration_gap `0.0523`
- 10d: hit_rate `0.5000`, avg `0.0025`, median `-0.0002`, brier `0.2978`, calibration_gap `0.1773`
- 20d: hit_rate `0.8750`, avg `0.0367`, median `0.0515`, brier `0.1464`, calibration_gap `-0.1977`
- 60d: hit_rate `0.7500`, avg `0.0455`, median `0.0623`, brier `0.2114`, calibration_gap `-0.0727`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0019`, median `0.0122`, brier `0.2157`, calibration_gap `-0.0253`
- 5d: hit_rate `0.6875`, avg `0.0034`, median `0.0088`, brier `0.2269`, calibration_gap `-0.0253`
- 10d: hit_rate `0.5625`, avg `0.0071`, median `0.0020`, brier `0.2661`, calibration_gap `0.0997`
- 20d: hit_rate `0.8125`, avg `0.0384`, median `0.0535`, brier `0.1725`, calibration_gap `-0.1503`
- 60d: hit_rate `0.6250`, avg `0.0379`, median `0.0623`, brier `0.2405`, calibration_gap `0.0372`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.7500`, avg `0.0119`, median `0.0180`, brier `0.2065`, calibration_gap `-0.1365`
- 5d: hit_rate `0.8250`, avg `0.0184`, median `0.0222`, brier `0.1889`, calibration_gap `-0.2115`
- 10d: hit_rate `0.7250`, avg `0.0216`, median `0.0244`, brier `0.2151`, calibration_gap `-0.1115`
- 20d: hit_rate `0.8000`, avg `0.0405`, median `0.0363`, brier `0.1876`, calibration_gap `-0.1865`
- 60d: hit_rate `0.8750`, avg `0.0873`, median `0.0930`, brier `0.1780`, calibration_gap `-0.2615`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0057`, median `0.0103`, brier `0.2344`, calibration_gap `-0.0456`
- 5d: hit_rate `0.8750`, avg `0.0135`, median `0.0177`, brier `0.1963`, calibration_gap `-0.2956`
- 10d: hit_rate `0.8125`, avg `0.0001`, median `0.0208`, brier `0.2079`, calibration_gap `-0.2331`
- 20d: hit_rate `0.5625`, avg `-0.0006`, median `0.0148`, brier `0.2505`, calibration_gap `0.0169`
- 60d: hit_rate `0.9375`, avg `0.0691`, median `0.0667`, brier `0.1871`, calibration_gap `-0.3581`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
