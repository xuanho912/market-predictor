# High Confidence Signal Report

Generated at: `2026-07-23T14:42:16.175982+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0017`, median `0.0050`, brier `0.2725`, calibration_gap `0.1866`
- 5d: hit_rate `0.5000`, avg `-0.0058`, median `-0.0009`, brier `0.3503`, calibration_gap `0.3116`
- 10d: hit_rate `0.5000`, avg `-0.0019`, median `-0.0036`, brier `0.3462`, calibration_gap `0.3116`
- 20d: hit_rate `0.3750`, avg `0.0030`, median `-0.0047`, brier `0.4292`, calibration_gap `0.4366`
- 60d: hit_rate `0.5000`, avg `0.0224`, median `0.0202`, brier `0.3503`, calibration_gap `0.3116`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0064`, median `0.0007`, brier `0.3031`, calibration_gap `0.2383`
- 5d: hit_rate `0.5000`, avg `-0.0086`, median `-0.0009`, brier `0.3418`, calibration_gap `0.3008`
- 10d: hit_rate `0.5000`, avg `-0.0029`, median `-0.0034`, brier `0.3399`, calibration_gap `0.3008`
- 20d: hit_rate `0.5000`, avg `0.0047`, median `0.0028`, brier `0.3448`, calibration_gap `0.3008`
- 60d: hit_rate `0.5000`, avg `0.0161`, median `0.0118`, brier `0.3410`, calibration_gap `0.3008`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5833`, avg `-0.0029`, median `0.0019`, brier `0.2730`, calibration_gap `0.1674`
- 5d: hit_rate `0.5500`, avg `-0.0014`, median `0.0029`, brier `0.2935`, calibration_gap `0.2008`
- 10d: hit_rate `0.5667`, avg `0.0063`, median `0.0053`, brier `0.2948`, calibration_gap `0.1841`
- 20d: hit_rate `0.7167`, avg `0.0218`, median `0.0277`, brier `0.2194`, calibration_gap `0.0341`
- 60d: hit_rate `0.6833`, avg `0.0326`, median `0.0521`, brier `0.2300`, calibration_gap `0.0674`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0015`, median `0.0045`, brier `0.2403`, calibration_gap `0.0568`
- 5d: hit_rate `0.4375`, avg `-0.0018`, median `-0.0035`, brier `0.3071`, calibration_gap `0.2443`
- 10d: hit_rate `0.6250`, avg `0.0050`, median `0.0152`, brier `0.2351`, calibration_gap `0.0568`
- 20d: hit_rate `0.6875`, avg `0.0113`, median `0.0306`, brier `0.2116`, calibration_gap `-0.0057`
- 60d: hit_rate `0.6250`, avg `0.0194`, median `0.0768`, brier `0.2380`, calibration_gap `0.0568`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
