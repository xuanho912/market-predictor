# High Confidence Signal Report

Generated at: `2026-08-20T13:14:26.403983+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `20`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `2`
- 3d: hit_rate `1.0000`, avg `0.0159`, median `0.0159`, brier `0.0759`, calibration_gap `-0.2754`
- 5d: hit_rate `1.0000`, avg `0.0155`, median `0.0155`, brier `0.0759`, calibration_gap `-0.2754`
- 10d: hit_rate `1.0000`, avg `0.0234`, median `0.0234`, brier `0.0759`, calibration_gap `-0.2754`
- 20d: hit_rate `0.5000`, avg `0.0277`, median `0.0277`, brier `0.2932`, calibration_gap `0.2246`
- 60d: hit_rate `0.5000`, avg `0.0244`, median `0.0244`, brier `0.2932`, calibration_gap `0.2246`

### top_20_confidence_signals
- sample_size: `4`
- 3d: hit_rate `0.7500`, avg `0.0069`, median `0.0053`, brier `0.1810`, calibration_gap `-0.0337`
- 5d: hit_rate `1.0000`, avg `0.0101`, median `0.0096`, brier `0.0806`, calibration_gap `-0.2837`
- 10d: hit_rate `1.0000`, avg `0.0209`, median `0.0234`, brier `0.0806`, calibration_gap `-0.2837`
- 20d: hit_rate `0.5000`, avg `0.0124`, median `0.0008`, brier `0.2968`, calibration_gap `0.2163`
- 60d: hit_rate `0.2500`, avg `-0.0075`, median `-0.0359`, brier `0.3972`, calibration_gap `0.4663`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5500`, avg `0.0015`, median `0.0053`, brier `0.2627`, calibration_gap `0.1359`
- 5d: hit_rate `0.5500`, avg `0.0049`, median `0.0047`, brier `0.2590`, calibration_gap `0.1359`
- 10d: hit_rate `0.7000`, avg `0.0058`, median `0.0111`, brier `0.2033`, calibration_gap `-0.0141`
- 20d: hit_rate `0.8000`, avg `0.0226`, median `0.0261`, brier `0.1778`, calibration_gap `-0.1141`
- 60d: hit_rate `0.5500`, avg `0.0288`, median `0.0383`, brier `0.2694`, calibration_gap `0.1359`

### low_confidence_reference
- sample_size: `4`
- 3d: hit_rate `0.5000`, avg `0.0012`, median `0.0027`, brier `0.2777`, calibration_gap `0.1633`
- 5d: hit_rate `0.2500`, avg `-0.0031`, median `-0.0053`, brier `0.3583`, calibration_gap `0.4133`
- 10d: hit_rate `0.2500`, avg `-0.0222`, median `-0.0127`, brier `0.3583`, calibration_gap `0.4133`
- 20d: hit_rate `0.7500`, avg `0.0188`, median `0.0207`, brier `0.1961`, calibration_gap `-0.0867`
- 60d: hit_rate `0.5000`, avg `0.0475`, median `0.0461`, brier `0.2777`, calibration_gap `0.1633`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
