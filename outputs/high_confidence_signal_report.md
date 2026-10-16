# High Confidence Signal Report

Generated at: `2026-10-16T01:14:54.056468+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0127`, median `-0.0101`, brier `0.4997`, calibration_gap `0.6230`
- 5d: hit_rate `0.2500`, avg `-0.0180`, median `-0.0226`, brier `0.4361`, calibration_gap `0.4980`
- 10d: hit_rate `0.1250`, avg `-0.0177`, median `-0.0142`, brier `0.4997`, calibration_gap `0.6230`
- 20d: hit_rate `0.6250`, avg `0.0282`, median `0.0363`, brier `0.2461`, calibration_gap `0.1230`
- 60d: hit_rate `0.8750`, avg `0.0782`, median `0.0897`, brier `0.1235`, calibration_gap `-0.1270`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.2500`, avg `-0.0084`, median `-0.0101`, brier `0.4321`, calibration_gap `0.4920`
- 5d: hit_rate `0.3125`, avg `-0.0145`, median `-0.0226`, brier `0.4004`, calibration_gap `0.4295`
- 10d: hit_rate `0.3125`, avg `-0.0099`, median `-0.0082`, brier `0.4028`, calibration_gap `0.4295`
- 20d: hit_rate `0.4375`, avg `0.0168`, median `-0.0009`, brier `0.3349`, calibration_gap `0.3045`
- 60d: hit_rate `0.7500`, avg `0.0548`, median `0.0566`, brier `0.1849`, calibration_gap `-0.0080`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.4750`, avg `-0.0063`, median `-0.0010`, brier `0.3150`, calibration_gap `0.2525`
- 5d: hit_rate `0.4000`, avg `-0.0094`, median `-0.0084`, brier `0.3466`, calibration_gap `0.3275`
- 10d: hit_rate `0.3500`, avg `-0.0054`, median `-0.0087`, brier `0.3707`, calibration_gap `0.3775`
- 20d: hit_rate `0.5750`, avg `0.0113`, median `0.0180`, brier `0.2643`, calibration_gap `0.1525`
- 60d: hit_rate `0.6750`, avg `0.0315`, median `0.0521`, brier `0.2197`, calibration_gap `0.0525`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.2500`, avg `-0.0087`, median `-0.0085`, brier `0.3769`, calibration_gap `0.4334`
- 5d: hit_rate `0.3125`, avg `-0.0108`, median `-0.0181`, brier `0.3518`, calibration_gap `0.3709`
- 10d: hit_rate `0.3750`, avg `-0.0079`, median `-0.0174`, brier `0.3306`, calibration_gap `0.3084`
- 20d: hit_rate `0.8750`, avg `0.0458`, median `0.0585`, brier `0.1479`, calibration_gap `-0.1916`
- 60d: hit_rate `0.9375`, avg `0.1080`, median `0.1133`, brier `0.1244`, calibration_gap `-0.2541`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
