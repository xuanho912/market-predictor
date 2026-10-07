# High Confidence Signal Report

Generated at: `2026-10-07T01:54:14.349495+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0003`, median `0.0031`, brier `0.2612`, calibration_gap `0.1636`
- 5d: hit_rate `0.6250`, avg `0.0018`, median `0.0058`, brier `0.2612`, calibration_gap `0.1636`
- 10d: hit_rate `0.5000`, avg `-0.0014`, median `-0.0047`, brier `0.3399`, calibration_gap `0.2886`
- 20d: hit_rate `0.7500`, avg `0.0165`, median `0.0173`, brier `0.1919`, calibration_gap `0.0386`
- 60d: hit_rate `1.0000`, avg `0.0395`, median `0.0378`, brier `0.0448`, calibration_gap `-0.2114`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0059`, median `-0.0033`, brier `0.3581`, calibration_gap `0.3405`
- 5d: hit_rate `0.5000`, avg `-0.0076`, median `-0.0043`, brier `0.3257`, calibration_gap `0.2780`
- 10d: hit_rate `0.4375`, avg `-0.0138`, median `-0.0116`, brier `0.3633`, calibration_gap `0.3405`
- 20d: hit_rate `0.5625`, avg `-0.0024`, median `0.0009`, brier `0.2906`, calibration_gap `0.2155`
- 60d: hit_rate `0.8750`, avg `0.0434`, median `0.0501`, brier `0.1163`, calibration_gap `-0.0970`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.3250`, avg `-0.0090`, median `-0.0058`, brier `0.3458`, calibration_gap `0.3442`
- 5d: hit_rate `0.3750`, avg `-0.0133`, median `-0.0082`, brier `0.3312`, calibration_gap `0.2942`
- 10d: hit_rate `0.4750`, avg `-0.0046`, median `-0.0056`, brier `0.2906`, calibration_gap `0.1942`
- 20d: hit_rate `0.6250`, avg `0.0068`, median `0.0168`, brier `0.2415`, calibration_gap `0.0442`
- 60d: hit_rate `0.7250`, avg `0.0376`, median `0.0445`, brier `0.2032`, calibration_gap `-0.0558`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0015`, median `0.0013`, brier `0.2678`, calibration_gap `0.1371`
- 5d: hit_rate `0.5625`, avg `-0.0023`, median `0.0021`, brier `0.2490`, calibration_gap `0.0746`
- 10d: hit_rate `0.5625`, avg `0.0101`, median `0.0097`, brier `0.2496`, calibration_gap `0.0746`
- 20d: hit_rate `0.7500`, avg `0.0148`, median `0.0146`, brier `0.1981`, calibration_gap `-0.1129`
- 60d: hit_rate `0.7500`, avg `0.0161`, median `0.0344`, brier `0.1977`, calibration_gap `-0.1129`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
