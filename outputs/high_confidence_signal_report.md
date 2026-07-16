# High Confidence Signal Report

Generated at: `2026-07-16T14:26:35.300656+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0087`, median `-0.0032`, brier `0.3505`, calibration_gap `0.3385`
- 5d: hit_rate `0.2500`, avg `-0.0117`, median `-0.0142`, brier `0.4015`, calibration_gap `0.4635`
- 10d: hit_rate `0.3750`, avg `-0.0076`, median `-0.0060`, brier `0.3508`, calibration_gap `0.3385`
- 20d: hit_rate `0.8750`, avg `0.0172`, median `0.0190`, brier `0.1354`, calibration_gap `-0.1615`
- 60d: hit_rate `0.5000`, avg `0.0022`, median `0.0030`, brier `0.2935`, calibration_gap `0.2135`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0020`, median `0.0007`, brier `0.2697`, calibration_gap `0.1459`
- 5d: hit_rate `0.5000`, avg `-0.0014`, median `0.0017`, brier `0.2962`, calibration_gap `0.2084`
- 10d: hit_rate `0.5625`, avg `0.0035`, median `0.0028`, brier `0.2703`, calibration_gap `0.1459`
- 20d: hit_rate `0.7500`, avg `0.0173`, median `0.0205`, brier `0.1882`, calibration_gap `-0.0416`
- 60d: hit_rate `0.5000`, avg `-0.0006`, median `0.0030`, brier `0.2923`, calibration_gap `0.2084`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6000`, avg `0.0025`, median `0.0071`, brier `0.2491`, calibration_gap `0.0901`
- 5d: hit_rate `0.7000`, avg `0.0069`, median `0.0066`, brier `0.2136`, calibration_gap `-0.0099`
- 10d: hit_rate `0.7500`, avg `0.0154`, median `0.0181`, brier `0.1896`, calibration_gap `-0.0599`
- 20d: hit_rate `0.7000`, avg `0.0191`, median `0.0075`, brier `0.2059`, calibration_gap `-0.0099`
- 60d: hit_rate `0.6500`, avg `0.0382`, median `0.0442`, brier `0.2316`, calibration_gap `0.0401`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0006`, median `0.0051`, brier `0.2376`, calibration_gap `0.0548`
- 5d: hit_rate `0.6875`, avg `0.0007`, median `0.0092`, brier `0.2153`, calibration_gap `-0.0077`
- 10d: hit_rate `0.4375`, avg `-0.0052`, median `-0.0054`, brier `0.3053`, calibration_gap `0.2423`
- 20d: hit_rate `0.5625`, avg `-0.0044`, median `0.0007`, brier `0.2599`, calibration_gap `0.1173`
- 60d: hit_rate `0.5000`, avg `-0.0280`, median `-0.0029`, brier `0.2827`, calibration_gap `0.1798`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
