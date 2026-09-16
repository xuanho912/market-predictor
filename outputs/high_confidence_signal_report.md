# High Confidence Signal Report

Generated at: `2026-09-16T16:59:25.903079+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0021`, median `0.0014`, brier `0.2617`, calibration_gap `0.1959`
- 5d: hit_rate `0.6250`, avg `0.0014`, median `0.0010`, brier `0.2716`, calibration_gap `0.1959`
- 10d: hit_rate `0.2500`, avg `-0.0078`, median `-0.0136`, brier `0.5184`, calibration_gap `0.5709`
- 20d: hit_rate `0.5000`, avg `0.0041`, median `0.0087`, brier `0.3577`, calibration_gap `0.3209`
- 60d: hit_rate `0.7500`, avg `0.0399`, median `0.0588`, brier `0.1916`, calibration_gap `0.0709`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0017`, median `-0.0026`, brier `0.3686`, calibration_gap `0.3660`
- 5d: hit_rate `0.4375`, avg `-0.0078`, median `-0.0045`, brier `0.3735`, calibration_gap `0.3660`
- 10d: hit_rate `0.4375`, avg `-0.0034`, median `-0.0073`, brier `0.3890`, calibration_gap `0.3660`
- 20d: hit_rate `0.6250`, avg `0.0076`, median `0.0244`, brier `0.2738`, calibration_gap `0.1785`
- 60d: hit_rate `0.7500`, avg `0.0431`, median `0.0605`, brier `0.1907`, calibration_gap `0.0535`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.7500`, avg `0.0092`, median `0.0116`, brier `0.1926`, calibration_gap `-0.0764`
- 5d: hit_rate `0.7500`, avg `0.0126`, median `0.0153`, brier `0.1954`, calibration_gap `-0.0764`
- 10d: hit_rate `0.7000`, avg `0.0208`, median `0.0212`, brier `0.2132`, calibration_gap `-0.0264`
- 20d: hit_rate `0.8500`, avg `0.0399`, median `0.0337`, brier `0.1596`, calibration_gap `-0.1764`
- 60d: hit_rate `0.9500`, avg `0.0835`, median `0.0798`, brier `0.1260`, calibration_gap `-0.2764`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0072`, median `0.0116`, brier `0.2169`, calibration_gap `-0.0192`
- 5d: hit_rate `0.7500`, avg `0.0126`, median `0.0153`, brier `0.1954`, calibration_gap `-0.0817`
- 10d: hit_rate `0.6875`, avg `0.0186`, median `0.0183`, brier `0.2169`, calibration_gap `-0.0192`
- 20d: hit_rate `0.8125`, avg `0.0359`, median `0.0244`, brier `0.1740`, calibration_gap `-0.1442`
- 60d: hit_rate `1.0000`, avg `0.0740`, median `0.0520`, brier `0.1101`, calibration_gap `-0.3317`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
