# High Confidence Signal Report

Generated at: `2026-11-07T01:26:32.672434+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0093`, median `-0.0148`, brier `0.4366`, calibration_gap `0.5060`
- 5d: hit_rate `0.3750`, avg `-0.0084`, median `-0.0155`, brier `0.3748`, calibration_gap `0.3810`
- 10d: hit_rate `0.3750`, avg `-0.0030`, median `-0.0200`, brier `0.3748`, calibration_gap `0.3810`
- 20d: hit_rate `0.3750`, avg `-0.0029`, median `-0.0247`, brier `0.3748`, calibration_gap `0.3810`
- 60d: hit_rate `0.7500`, avg `0.0421`, median `0.0396`, brier `0.1842`, calibration_gap `0.0060`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0044`, median `-0.0092`, brier `0.3708`, calibration_gap `0.3719`
- 5d: hit_rate `0.3750`, avg `-0.0066`, median `-0.0155`, brier `0.3707`, calibration_gap `0.3719`
- 10d: hit_rate `0.3750`, avg `-0.0027`, median `-0.0244`, brier `0.3699`, calibration_gap `0.3719`
- 20d: hit_rate `0.3125`, avg `-0.0119`, median `-0.0279`, brier `0.3986`, calibration_gap `0.4344`
- 60d: hit_rate `0.7500`, avg `0.0394`, median `0.0396`, brier `0.1878`, calibration_gap `-0.0031`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0032`, median `0.0051`, brier `0.2483`, calibration_gap `-0.0170`
- 5d: hit_rate `0.4375`, avg `-0.0035`, median `-0.0076`, brier `0.2601`, calibration_gap `0.1080`
- 10d: hit_rate `0.3125`, avg `-0.0228`, median `-0.0181`, brier `0.2702`, calibration_gap `0.2330`
- 20d: hit_rate `0.1875`, avg `-0.0492`, median `-0.0491`, brier `0.2793`, calibration_gap `0.3580`
- 60d: hit_rate `0.8125`, avg `0.0569`, median `0.0522`, brier `0.2233`, calibration_gap `-0.2670`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
