# High Confidence Signal Report

Generated at: `2026-07-24T14:15:30.648049+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0056`, median `0.0050`, brier `0.2675`, calibration_gap `0.1855`
- 5d: hit_rate `0.5000`, avg `-0.0150`, median `-0.0029`, brier `0.3456`, calibration_gap `0.3105`
- 10d: hit_rate `0.2500`, avg `-0.0081`, median `-0.0096`, brier `0.5029`, calibration_gap `0.5605`
- 20d: hit_rate `0.2500`, avg `-0.0016`, median `-0.0047`, brier `0.5017`, calibration_gap `0.5605`
- 60d: hit_rate `0.5000`, avg `0.0145`, median `0.0101`, brier `0.3456`, calibration_gap `0.3105`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0073`, median `-0.0042`, brier `0.3399`, calibration_gap `0.3034`
- 5d: hit_rate `0.4375`, avg `-0.0125`, median `-0.0045`, brier `0.3776`, calibration_gap `0.3659`
- 10d: hit_rate `0.4375`, avg `-0.0020`, median `-0.0066`, brier `0.3840`, calibration_gap `0.3659`
- 20d: hit_rate `0.4375`, avg `0.0060`, median `-0.0018`, brier `0.3825`, calibration_gap `0.3659`
- 60d: hit_rate `0.5625`, avg `0.0255`, median `0.0352`, brier `0.3044`, calibration_gap `0.2409`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5833`, avg `-0.0026`, median `0.0013`, brier `0.2782`, calibration_gap `0.1756`
- 5d: hit_rate `0.5333`, avg `-0.0025`, median `0.0010`, brier `0.3051`, calibration_gap `0.2256`
- 10d: hit_rate `0.5500`, avg `0.0065`, median `0.0027`, brier `0.3095`, calibration_gap `0.2089`
- 20d: hit_rate `0.6667`, avg `0.0216`, median `0.0239`, brier `0.2387`, calibration_gap `0.0923`
- 60d: hit_rate `0.7167`, avg `0.0384`, median `0.0580`, brier `0.2092`, calibration_gap `0.0423`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0015`, median `-0.0034`, brier `0.2873`, calibration_gap `0.1912`
- 5d: hit_rate `0.3125`, avg `-0.0077`, median `-0.0083`, brier `0.3587`, calibration_gap `0.3787`
- 10d: hit_rate `0.6875`, avg `0.0091`, median `0.0259`, brier `0.2152`, calibration_gap `0.0037`
- 20d: hit_rate `0.5625`, avg `-0.0015`, median `0.0130`, brier `0.2632`, calibration_gap `0.1287`
- 60d: hit_rate `0.5625`, avg `-0.0117`, median `0.0361`, brier `0.2621`, calibration_gap `0.1287`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
