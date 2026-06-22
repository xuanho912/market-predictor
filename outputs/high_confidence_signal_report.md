# High Confidence Signal Report

Generated at: `2026-06-22T16:01:43.908371+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0060`, median `-0.0061`, brier `0.3621`, calibration_gap `0.3535`
- 5d: hit_rate `0.0000`, avg `-0.0182`, median `-0.0150`, brier `0.5307`, calibration_gap `0.7285`
- 10d: hit_rate `0.6250`, avg `0.0048`, median `0.0061`, brier `0.2447`, calibration_gap `0.1035`
- 20d: hit_rate `1.0000`, avg `0.0281`, median `0.0302`, brier `0.0738`, calibration_gap `-0.2715`
- 60d: hit_rate `1.0000`, avg `0.0760`, median `0.0869`, brier `0.0738`, calibration_gap `-0.2715`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0017`, median `-0.0001`, brier `0.3016`, calibration_gap `0.2209`
- 5d: hit_rate `0.2500`, avg `-0.0110`, median `-0.0130`, brier `0.4129`, calibration_gap `0.4709`
- 10d: hit_rate `0.4375`, avg `0.0024`, median `-0.0008`, brier `0.3248`, calibration_gap `0.2834`
- 20d: hit_rate `0.9375`, avg `0.0279`, median `0.0290`, brier `0.1044`, calibration_gap `-0.2166`
- 60d: hit_rate `0.8750`, avg `0.0639`, median `0.0832`, brier `0.1300`, calibration_gap `-0.1541`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4667`, avg `-0.0001`, median `-0.0014`, brier `0.2989`, calibration_gap `0.2101`
- 5d: hit_rate `0.4667`, avg `-0.0030`, median `-0.0039`, brier `0.3053`, calibration_gap `0.2101`
- 10d: hit_rate `0.4000`, avg `-0.0029`, median `-0.0022`, brier `0.3221`, calibration_gap `0.2768`
- 20d: hit_rate `0.7500`, avg `0.0106`, median `0.0191`, brier `0.1853`, calibration_gap `-0.0732`
- 60d: hit_rate `0.6167`, avg `0.0223`, median `0.0346`, brier `0.2338`, calibration_gap `0.0601`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0015`, median `0.0028`, brier `0.2204`, calibration_gap `-0.0675`
- 5d: hit_rate `0.7500`, avg `0.0036`, median `0.0071`, brier `0.2048`, calibration_gap `-0.1300`
- 10d: hit_rate `0.5000`, avg `0.0011`, median `0.0004`, brier `0.2661`, calibration_gap `0.1200`
- 20d: hit_rate `0.6250`, avg `0.0084`, median `0.0095`, brier `0.2347`, calibration_gap `-0.0050`
- 60d: hit_rate `0.6875`, avg `0.0275`, median `0.0590`, brier `0.2191`, calibration_gap `-0.0675`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
