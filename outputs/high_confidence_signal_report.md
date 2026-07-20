# High Confidence Signal Report

Generated at: `2026-07-20T14:36:49.187817+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0024`, median `0.0014`, brier `0.1873`, calibration_gap `0.0233`
- 5d: hit_rate `0.5000`, avg `-0.0019`, median `-0.0009`, brier `0.3202`, calibration_gap `0.2733`
- 10d: hit_rate `0.2500`, avg `-0.0095`, median `-0.0136`, brier `0.4641`, calibration_gap `0.5233`
- 20d: hit_rate `0.5000`, avg `0.0026`, median `0.0084`, brier `0.3241`, calibration_gap `0.2733`
- 60d: hit_rate `0.7500`, avg `0.0389`, median `0.0588`, brier `0.1865`, calibration_gap `0.0233`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0020`, median `0.0007`, brier `0.2504`, calibration_gap `0.1363`
- 5d: hit_rate `0.5000`, avg `-0.0066`, median `-0.0009`, brier `0.3168`, calibration_gap `0.2613`
- 10d: hit_rate `0.3750`, avg `-0.0069`, median `-0.0104`, brier `0.3889`, calibration_gap `0.3863`
- 20d: hit_rate `0.5000`, avg `0.0028`, median `0.0031`, brier `0.3168`, calibration_gap `0.2613`
- 60d: hit_rate `0.5625`, avg `0.0217`, median `0.0396`, brier `0.2792`, calibration_gap `0.1988`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.4750`, avg `-0.0044`, median `-0.0034`, brier `0.3068`, calibration_gap `0.2353`
- 5d: hit_rate `0.5000`, avg `-0.0038`, median `-0.0005`, brier `0.2971`, calibration_gap `0.2103`
- 10d: hit_rate `0.4500`, avg `0.0040`, median `-0.0020`, brier `0.3237`, calibration_gap `0.2603`
- 20d: hit_rate `0.7250`, avg `0.0216`, median `0.0300`, brier `0.2026`, calibration_gap `-0.0147`
- 60d: hit_rate `0.6500`, avg `0.0412`, median `0.0573`, brier `0.2305`, calibration_gap `0.0603`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0013`, median `0.0056`, brier `0.2623`, calibration_gap `0.1271`
- 5d: hit_rate `0.5625`, avg `0.0068`, median `0.0024`, brier `0.2621`, calibration_gap `0.1271`
- 10d: hit_rate `0.6250`, avg `0.0070`, median `0.0150`, brier `0.2390`, calibration_gap `0.0646`
- 20d: hit_rate `0.7500`, avg `0.0111`, median `0.0095`, brier `0.1923`, calibration_gap `-0.0604`
- 60d: hit_rate `0.6250`, avg `0.0239`, median `0.0460`, brier `0.2391`, calibration_gap `0.0646`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
