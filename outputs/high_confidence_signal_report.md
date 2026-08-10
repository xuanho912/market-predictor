# High Confidence Signal Report

Generated at: `2026-08-10T21:09:37.925018+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0046`, median `0.0069`, brier `0.1305`, calibration_gap `-0.1514`
- 5d: hit_rate `0.8750`, avg `0.0069`, median `0.0112`, brier `0.1305`, calibration_gap `-0.1514`
- 10d: hit_rate `0.8750`, avg `0.0149`, median `0.0199`, brier `0.1305`, calibration_gap `-0.1514`
- 20d: hit_rate `0.5000`, avg `0.0083`, median `0.0002`, brier `0.3052`, calibration_gap `0.2236`
- 60d: hit_rate `0.3750`, avg `0.0028`, median `-0.0336`, brier `0.3578`, calibration_gap `0.3486`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0027`, median `0.0019`, brier `0.2365`, calibration_gap `0.0867`
- 5d: hit_rate `0.8125`, avg `0.0085`, median `0.0089`, brier `0.1603`, calibration_gap `-0.1008`
- 10d: hit_rate `0.7500`, avg `0.0152`, median `0.0146`, brier `0.1872`, calibration_gap `-0.0383`
- 20d: hit_rate `0.6875`, avg `0.0184`, median `0.0100`, brier `0.2236`, calibration_gap `0.0242`
- 60d: hit_rate `0.4375`, avg `0.0152`, median `-0.0246`, brier `0.3244`, calibration_gap `0.2742`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5833`, avg `0.0000`, median `0.0031`, brier `0.2527`, calibration_gap `0.1064`
- 5d: hit_rate `0.6333`, avg `0.0023`, median `0.0035`, brier `0.2320`, calibration_gap `0.0564`
- 10d: hit_rate `0.5500`, avg `0.0060`, median `0.0091`, brier `0.2645`, calibration_gap `0.1397`
- 20d: hit_rate `0.6667`, avg `0.0108`, median `0.0142`, brier `0.2254`, calibration_gap `0.0231`
- 60d: hit_rate `0.5167`, avg `0.0196`, median `0.0151`, brier `0.2830`, calibration_gap `0.1731`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0083`, median `0.0082`, brier `0.1727`, calibration_gap `-0.1459`
- 5d: hit_rate `0.8125`, avg `0.0108`, median `0.0065`, brier `0.1736`, calibration_gap `-0.1459`
- 10d: hit_rate `0.5000`, avg `-0.0007`, median `-0.0045`, brier `0.2778`, calibration_gap `0.1666`
- 20d: hit_rate `0.5625`, avg `-0.0077`, median `0.0120`, brier `0.2566`, calibration_gap `0.1041`
- 60d: hit_rate `0.6250`, avg `-0.0061`, median `0.0459`, brier `0.2345`, calibration_gap `0.0416`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
