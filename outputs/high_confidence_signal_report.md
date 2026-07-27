# High Confidence Signal Report

Generated at: `2026-07-27T21:35:41.254750+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0138`, median `-0.0096`, brier `0.4039`, calibration_gap `0.4134`
- 5d: hit_rate `0.3750`, avg `-0.0190`, median `-0.0185`, brier `0.4023`, calibration_gap `0.4134`
- 10d: hit_rate `0.1250`, avg `-0.0121`, median `-0.0096`, brier `0.5512`, calibration_gap `0.6634`
- 20d: hit_rate `0.5000`, avg `0.0092`, median `0.0093`, brier `0.3390`, calibration_gap `0.2884`
- 60d: hit_rate `0.7500`, avg `0.0454`, median `0.0475`, brier `0.1917`, calibration_gap `0.0384`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0123`, median `-0.0096`, brier `0.3997`, calibration_gap `0.4079`
- 5d: hit_rate `0.3750`, avg `-0.0182`, median `-0.0185`, brier `0.3991`, calibration_gap `0.4079`
- 10d: hit_rate `0.2500`, avg `-0.0090`, median `-0.0076`, brier `0.4742`, calibration_gap `0.5329`
- 20d: hit_rate `0.5000`, avg `0.0067`, median `0.0093`, brier `0.3327`, calibration_gap `0.2829`
- 60d: hit_rate `0.6250`, avg `0.0296`, median `0.0418`, brier `0.2590`, calibration_gap `0.1579`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5833`, avg `-0.0023`, median `0.0013`, brier `0.2747`, calibration_gap `0.1656`
- 5d: hit_rate `0.5500`, avg `-0.0021`, median `0.0022`, brier `0.2931`, calibration_gap `0.1990`
- 10d: hit_rate `0.5333`, avg `0.0055`, median `0.0010`, brier `0.3106`, calibration_gap `0.2156`
- 20d: hit_rate `0.6667`, avg `0.0211`, median `0.0239`, brier `0.2340`, calibration_gap `0.0823`
- 60d: hit_rate `0.7167`, avg `0.0426`, median `0.0580`, brier `0.2058`, calibration_gap `0.0323`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0002`, median `0.0027`, brier `0.2617`, calibration_gap `0.1184`
- 5d: hit_rate `0.4375`, avg `-0.0049`, median `-0.0074`, brier `0.3042`, calibration_gap `0.2434`
- 10d: hit_rate `0.6250`, avg `0.0040`, median `0.0129`, brier `0.2372`, calibration_gap `0.0559`
- 20d: hit_rate `0.6250`, avg `0.0010`, median `0.0131`, brier `0.2378`, calibration_gap `0.0559`
- 60d: hit_rate `0.4375`, avg `-0.0202`, median `-0.0041`, brier `0.3044`, calibration_gap `0.2434`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
