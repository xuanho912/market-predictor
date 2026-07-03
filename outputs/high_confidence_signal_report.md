# High Confidence Signal Report

Generated at: `2026-07-03T05:01:41.611888+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0097`, median `-0.0059`, brier `0.4087`, calibration_gap `0.4636`
- 5d: hit_rate `0.3750`, avg `-0.0099`, median `-0.0206`, brier `0.3544`, calibration_gap `0.3386`
- 10d: hit_rate `0.3750`, avg `-0.0032`, median `-0.0054`, brier `0.3579`, calibration_gap `0.3386`
- 20d: hit_rate `0.8750`, avg `0.0337`, median `0.0363`, brier `0.1350`, calibration_gap `-0.1614`
- 60d: hit_rate `0.7500`, avg `0.0582`, median `0.0863`, brier `0.1857`, calibration_gap `-0.0364`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0090`, median `-0.0060`, brier `0.3736`, calibration_gap `0.3932`
- 5d: hit_rate `0.4375`, avg `-0.0098`, median `-0.0114`, brier `0.3214`, calibration_gap `0.2682`
- 10d: hit_rate `0.2500`, avg `-0.0047`, median `-0.0065`, brier `0.3974`, calibration_gap `0.4557`
- 20d: hit_rate `0.7500`, avg `0.0218`, median `0.0209`, brier `0.1870`, calibration_gap `-0.0443`
- 60d: hit_rate `0.6250`, avg `0.0317`, median `0.0449`, brier `0.2373`, calibration_gap `0.0807`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4167`, avg `-0.0023`, median `-0.0040`, brier `0.3117`, calibration_gap `0.2438`
- 5d: hit_rate `0.4167`, avg `-0.0053`, median `-0.0069`, brier `0.3077`, calibration_gap `0.2438`
- 10d: hit_rate `0.4833`, avg `0.0014`, median `-0.0012`, brier `0.2919`, calibration_gap `0.1771`
- 20d: hit_rate `0.6333`, avg `0.0105`, median `0.0110`, brier `0.2333`, calibration_gap `0.0271`
- 60d: hit_rate `0.5833`, avg `0.0245`, median `0.0356`, brier `0.2477`, calibration_gap `0.0771`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0069`, median `0.0020`, brier `0.2507`, calibration_gap `0.0637`
- 5d: hit_rate `0.4375`, avg `-0.0009`, median `-0.0081`, brier `0.2827`, calibration_gap `0.1887`
- 10d: hit_rate `0.6250`, avg `0.0063`, median `0.0121`, brier `0.2349`, calibration_gap `0.0012`
- 20d: hit_rate `0.6875`, avg `0.0086`, median `0.0164`, brier `0.2187`, calibration_gap `-0.0613`
- 60d: hit_rate `0.6875`, avg `0.0383`, median `0.0644`, brier `0.2195`, calibration_gap `-0.0613`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
