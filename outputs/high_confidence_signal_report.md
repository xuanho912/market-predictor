# High Confidence Signal Report

Generated at: `2026-07-23T22:35:46.843017+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0017`, median `0.0050`, brier `0.2708`, calibration_gap `0.1886`
- 5d: hit_rate `0.5000`, avg `-0.0058`, median `-0.0009`, brier `0.3497`, calibration_gap `0.3136`
- 10d: hit_rate `0.5000`, avg `-0.0019`, median `-0.0036`, brier `0.3493`, calibration_gap `0.3136`
- 20d: hit_rate `0.3750`, avg `0.0030`, median `-0.0047`, brier `0.4298`, calibration_gap `0.4386`
- 60d: hit_rate `0.5000`, avg `0.0224`, median `0.0202`, brier `0.3497`, calibration_gap `0.3136`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0048`, median `0.0011`, brier `0.2679`, calibration_gap `0.1779`
- 5d: hit_rate `0.5625`, avg `-0.0064`, median `0.0010`, brier `0.3070`, calibration_gap `0.2404`
- 10d: hit_rate `0.5000`, avg `-0.0034`, median `-0.0034`, brier `0.3428`, calibration_gap `0.3029`
- 20d: hit_rate `0.5625`, avg `0.0090`, median `0.0138`, brier `0.3102`, calibration_gap `0.2404`
- 60d: hit_rate `0.5625`, avg `0.0208`, median `0.0434`, brier `0.3059`, calibration_gap `0.2404`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6167`, avg `-0.0010`, median `0.0043`, brier `0.2588`, calibration_gap `0.1374`
- 5d: hit_rate `0.5833`, avg `0.0014`, median `0.0037`, brier `0.2793`, calibration_gap `0.1707`
- 10d: hit_rate `0.6000`, avg `0.0091`, median `0.0087`, brier `0.2792`, calibration_gap `0.1541`
- 20d: hit_rate `0.7333`, avg `0.0261`, median `0.0316`, brier `0.2105`, calibration_gap `0.0207`
- 60d: hit_rate `0.7333`, avg `0.0423`, median `0.0588`, brier `0.2057`, calibration_gap `0.0207`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0015`, median `0.0030`, brier `0.2627`, calibration_gap `0.1218`
- 5d: hit_rate `0.3750`, avg `-0.0041`, median `-0.0074`, brier `0.3313`, calibration_gap `0.3093`
- 10d: hit_rate `0.6250`, avg `0.0101`, median `0.0118`, brier `0.2365`, calibration_gap `0.0593`
- 20d: hit_rate `0.6250`, avg `0.0141`, median `0.0306`, brier `0.2365`, calibration_gap `0.0593`
- 60d: hit_rate `0.7500`, avg `0.0333`, median `0.0924`, brier `0.1913`, calibration_gap `-0.0657`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
