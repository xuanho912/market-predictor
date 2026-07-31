# High Confidence Signal Report

Generated at: `2026-07-31T22:39:13.143886+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0100`, median `-0.0092`, brier `0.3902`, calibration_gap `0.3963`
- 5d: hit_rate `0.6250`, avg `-0.0050`, median `0.0019`, brier `0.2558`, calibration_gap `0.1463`
- 10d: hit_rate `0.1250`, avg `-0.0057`, median `-0.0129`, brier `0.5303`, calibration_gap `0.6463`
- 20d: hit_rate `0.5000`, avg `0.0015`, median `0.0094`, brier `0.3219`, calibration_gap `0.2713`
- 60d: hit_rate `0.5000`, avg `0.0079`, median `0.0045`, brier `0.3219`, calibration_gap `0.2713`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0103`, median `-0.0092`, brier `0.3822`, calibration_gap `0.3847`
- 5d: hit_rate `0.6250`, avg `-0.0095`, median `0.0010`, brier `0.2526`, calibration_gap `0.1347`
- 10d: hit_rate `0.1875`, avg `-0.0094`, median `-0.0129`, brier `0.4832`, calibration_gap `0.5722`
- 20d: hit_rate `0.3125`, avg `-0.0132`, median `-0.0105`, brier `0.4101`, calibration_gap `0.4472`
- 60d: hit_rate `0.4375`, avg `-0.0063`, median `-0.0079`, brier `0.3480`, calibration_gap `0.3222`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5750`, avg `0.0009`, median `0.0051`, brier `0.2692`, calibration_gap `0.1472`
- 5d: hit_rate `0.5000`, avg `-0.0020`, median `-0.0004`, brier `0.3005`, calibration_gap `0.2222`
- 10d: hit_rate `0.4500`, avg `0.0075`, median `-0.0020`, brier `0.3357`, calibration_gap `0.2722`
- 20d: hit_rate `0.7250`, avg `0.0243`, median `0.0339`, brier `0.2073`, calibration_gap `-0.0028`
- 60d: hit_rate `0.6750`, avg `0.0326`, median `0.0573`, brier `0.2267`, calibration_gap `0.0472`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0032`, median `0.0056`, brier `0.2607`, calibration_gap `0.1184`
- 5d: hit_rate `0.4375`, avg `0.0016`, median `-0.0082`, brier `0.3059`, calibration_gap `0.2434`
- 10d: hit_rate `0.5000`, avg `-0.0007`, median `0.0010`, brier `0.2821`, calibration_gap `0.1809`
- 20d: hit_rate `0.6250`, avg `0.0093`, median `0.0120`, brier `0.2372`, calibration_gap `0.0559`
- 60d: hit_rate `0.5625`, avg `-0.0158`, median `0.0237`, brier `0.2610`, calibration_gap `0.1184`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
