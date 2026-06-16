# High Confidence Signal Report

Generated at: `2026-06-16T00:16:16.329328+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0003`, median `0.0031`, brier `0.2441`, calibration_gap `0.0887`
- 5d: hit_rate `0.5000`, avg `-0.0034`, median `-0.0047`, brier `0.2985`, calibration_gap `0.2137`
- 10d: hit_rate `0.8750`, avg `0.0113`, median `0.0135`, brier `0.1385`, calibration_gap `-0.1613`
- 20d: hit_rate `0.7500`, avg `0.0076`, median `0.0123`, brier `0.1839`, calibration_gap `-0.0363`
- 60d: hit_rate `0.2500`, avg `-0.0320`, median `-0.0398`, brier `0.4008`, calibration_gap `0.4637`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0024`, median `0.0002`, brier `0.2882`, calibration_gap `0.2012`
- 5d: hit_rate `0.3750`, avg `-0.0052`, median `-0.0057`, brier `0.3403`, calibration_gap `0.3262`
- 10d: hit_rate `0.6250`, avg `0.0045`, median `0.0069`, brier `0.2355`, calibration_gap `0.0762`
- 20d: hit_rate `0.8125`, avg `0.0101`, median `0.0143`, brier `0.1649`, calibration_gap `-0.1113`
- 60d: hit_rate `0.3750`, avg `-0.0049`, median `-0.0252`, brier `0.3415`, calibration_gap `0.3262`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6125`, avg `0.0038`, median `0.0046`, brier `0.2457`, calibration_gap `0.0503`
- 5d: hit_rate `0.6250`, avg `0.0049`, median `0.0052`, brier `0.2446`, calibration_gap `0.0378`
- 10d: hit_rate `0.5875`, avg `0.0061`, median `0.0066`, brier `0.2499`, calibration_gap `0.0753`
- 20d: hit_rate `0.6750`, avg `0.0057`, median `0.0143`, brier `0.2177`, calibration_gap `-0.0122`
- 60d: hit_rate `0.5875`, avg `0.0230`, median `0.0314`, brier `0.2525`, calibration_gap `0.0753`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0060`, median `0.0129`, brier `0.2189`, calibration_gap `-0.0583`
- 5d: hit_rate `0.7500`, avg `0.0093`, median `0.0123`, brier `0.2028`, calibration_gap `-0.1208`
- 10d: hit_rate `0.7500`, avg `0.0136`, median `0.0176`, brier `0.2034`, calibration_gap `-0.1208`
- 20d: hit_rate `0.7500`, avg `0.0154`, median `0.0095`, brier `0.2030`, calibration_gap `-0.1208`
- 60d: hit_rate `0.6250`, avg `0.0281`, median `0.0373`, brier `0.2345`, calibration_gap `0.0042`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
