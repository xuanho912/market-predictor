# High Confidence Signal Report

Generated at: `2026-11-27T21:20:19.968345+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0097`, median `-0.0097`, brier `0.5347`, calibration_gap `0.6485`
- 5d: hit_rate `0.2500`, avg `-0.0148`, median `-0.0166`, brier `0.4658`, calibration_gap `0.5235`
- 10d: hit_rate `0.2500`, avg `-0.0097`, median `-0.0082`, brier `0.4648`, calibration_gap `0.5235`
- 20d: hit_rate `0.3750`, avg `0.0048`, median `-0.0070`, brier `0.4018`, calibration_gap `0.3985`
- 60d: hit_rate `0.2500`, avg `-0.0036`, median `-0.0362`, brier `0.4656`, calibration_gap `0.5235`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.1875`, avg `-0.0099`, median `-0.0097`, brier `0.4852`, calibration_gap `0.5734`
- 5d: hit_rate `0.2500`, avg `-0.0147`, median `-0.0166`, brier `0.4506`, calibration_gap `0.5109`
- 10d: hit_rate `0.2500`, avg `-0.0118`, median `-0.0126`, brier `0.4506`, calibration_gap `0.5109`
- 20d: hit_rate `0.3750`, avg `-0.0006`, median `-0.0107`, brier `0.3876`, calibration_gap `0.3859`
- 60d: hit_rate `0.3125`, avg `-0.0029`, median `-0.0362`, brier `0.4195`, calibration_gap `0.4484`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0114`, median `-0.0087`, brier `0.3063`, calibration_gap `0.3011`
- 5d: hit_rate `0.5000`, avg `0.0045`, median `-0.0053`, brier `0.2644`, calibration_gap `0.1136`
- 10d: hit_rate `0.8125`, avg `0.0247`, median `0.0231`, brier `0.1937`, calibration_gap `-0.1989`
- 20d: hit_rate `0.5625`, avg `0.0107`, median `0.0224`, brier `0.2485`, calibration_gap `0.0511`
- 60d: hit_rate `0.6250`, avg `0.0289`, median `0.0592`, brier `0.2348`, calibration_gap `-0.0114`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
