# High Confidence Signal Report

Generated at: `2026-08-14T03:32:09.363170+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `1.0000`, avg `0.0130`, median `0.0129`, brier `0.0772`, calibration_gap `-0.2776`
- 5d: hit_rate `0.8750`, avg `0.0082`, median `0.0097`, brier `0.1331`, calibration_gap `-0.1526`
- 10d: hit_rate `0.8750`, avg `0.0161`, median `0.0199`, brier `0.1318`, calibration_gap `-0.1526`
- 20d: hit_rate `0.2500`, avg `-0.0009`, median `-0.0114`, brier `0.4085`, calibration_gap `0.4724`
- 60d: hit_rate `0.2500`, avg `-0.0126`, median `-0.0408`, brier `0.4085`, calibration_gap `0.4724`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0052`, median `0.0046`, brier `0.2067`, calibration_gap `0.0225`
- 5d: hit_rate `0.8125`, avg `0.0070`, median `0.0088`, brier `0.1619`, calibration_gap `-0.1025`
- 10d: hit_rate `0.7500`, avg `0.0092`, median `0.0118`, brier `0.1846`, calibration_gap `-0.0400`
- 20d: hit_rate `0.5625`, avg `0.0056`, median `0.0048`, brier `0.2745`, calibration_gap `0.1475`
- 60d: hit_rate `0.3125`, avg `-0.0079`, median `-0.0322`, brier `0.3739`, calibration_gap `0.3975`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6250`, avg `0.0043`, median `0.0056`, brier `0.2348`, calibration_gap `0.0569`
- 5d: hit_rate `0.6250`, avg `0.0053`, median `0.0053`, brier `0.2334`, calibration_gap `0.0569`
- 10d: hit_rate `0.5875`, avg `0.0064`, median `0.0091`, brier `0.2481`, calibration_gap `0.0944`
- 20d: hit_rate `0.7000`, avg `0.0126`, median `0.0156`, brier `0.2127`, calibration_gap `-0.0181`
- 60d: hit_rate `0.6375`, avg `0.0239`, median `0.0456`, brier `0.2384`, calibration_gap `0.0444`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0017`, median `0.0013`, brier `0.2745`, calibration_gap `0.1610`
- 5d: hit_rate `0.3750`, avg `-0.0027`, median `-0.0045`, brier `0.3139`, calibration_gap `0.2860`
- 10d: hit_rate `0.4375`, avg `-0.0079`, median `-0.0085`, brier `0.2955`, calibration_gap `0.2235`
- 20d: hit_rate `0.5625`, avg `-0.0159`, median `0.0076`, brier `0.2561`, calibration_gap `0.0985`
- 60d: hit_rate `0.6875`, avg `-0.0010`, median `0.0547`, brier `0.2143`, calibration_gap `-0.0265`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
