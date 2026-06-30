# High Confidence Signal Report

Generated at: `2026-06-30T23:48:02.962935+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0079`, median `-0.0022`, brier `0.4000`, calibration_gap `0.4575`
- 5d: hit_rate `0.5000`, avg `-0.0077`, median `-0.0073`, brier `0.2989`, calibration_gap `0.2075`
- 10d: hit_rate `0.5000`, avg `0.0002`, median `0.0015`, brier `0.2979`, calibration_gap `0.2075`
- 20d: hit_rate `1.0000`, avg `0.0257`, median `0.0223`, brier `0.0857`, calibration_gap `-0.2925`
- 60d: hit_rate `0.5000`, avg `-0.0004`, median `-0.0130`, brier `0.2885`, calibration_gap `0.2075`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.2500`, avg `-0.0095`, median `-0.0078`, brier `0.3907`, calibration_gap `0.4482`
- 5d: hit_rate `0.3125`, avg `-0.0137`, median `-0.0200`, brier `0.3635`, calibration_gap `0.3857`
- 10d: hit_rate `0.4375`, avg `-0.0002`, median `-0.0010`, brier `0.3157`, calibration_gap `0.2607`
- 20d: hit_rate `0.8750`, avg `0.0226`, median `0.0253`, brier `0.1395`, calibration_gap `-0.1768`
- 60d: hit_rate `0.6250`, avg `0.0279`, median `0.0557`, brier `0.2409`, calibration_gap `0.0732`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.3000`, avg `-0.0101`, median `-0.0101`, brier `0.3655`, calibration_gap `0.3899`
- 5d: hit_rate `0.3000`, avg `-0.0123`, median `-0.0150`, brier `0.3647`, calibration_gap `0.3899`
- 10d: hit_rate `0.3500`, avg `-0.0019`, median `-0.0060`, brier `0.3469`, calibration_gap `0.3399`
- 20d: hit_rate `0.7500`, avg `0.0207`, median `0.0277`, brier `0.1892`, calibration_gap `-0.0601`
- 60d: hit_rate `0.7000`, avg `0.0474`, median `0.0690`, brier `0.2069`, calibration_gap `-0.0101`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0066`, median `0.0080`, brier `0.2348`, calibration_gap `-0.0116`
- 5d: hit_rate `0.5625`, avg `0.0047`, median `0.0042`, brier `0.2490`, calibration_gap `0.0509`
- 10d: hit_rate `0.5625`, avg `0.0039`, median `0.0063`, brier `0.2479`, calibration_gap `0.0509`
- 20d: hit_rate `0.7500`, avg `0.0095`, median `0.0122`, brier `0.2061`, calibration_gap `-0.1366`
- 60d: hit_rate `0.6875`, avg `0.0398`, median `0.0407`, brier `0.2199`, calibration_gap `-0.0741`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
