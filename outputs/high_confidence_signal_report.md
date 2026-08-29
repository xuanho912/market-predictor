# High Confidence Signal Report

Generated at: `2026-08-29T03:21:25.246868+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0058`, median `0.0007`, brier `0.2553`, calibration_gap `0.1316`
- 5d: hit_rate `0.3750`, avg `-0.0076`, median `-0.0084`, brier `0.3775`, calibration_gap `0.3816`
- 10d: hit_rate `0.2500`, avg `-0.0116`, median `-0.0127`, brier `0.4460`, calibration_gap `0.5066`
- 20d: hit_rate `0.6250`, avg `0.0107`, median `0.0166`, brier `0.2505`, calibration_gap `0.1316`
- 60d: hit_rate `0.8750`, avg `0.0372`, median `0.0396`, brier `0.1214`, calibration_gap `-0.1184`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0043`, median `-0.0004`, brier `0.3125`, calibration_gap `0.2495`
- 5d: hit_rate `0.5625`, avg `-0.0029`, median `0.0008`, brier `0.2826`, calibration_gap `0.1870`
- 10d: hit_rate `0.3750`, avg `-0.0046`, median `-0.0093`, brier `0.3773`, calibration_gap `0.3745`
- 20d: hit_rate `0.6875`, avg `0.0095`, median `0.0191`, brier `0.2191`, calibration_gap `0.0620`
- 60d: hit_rate `0.6875`, avg `0.0309`, median `0.0396`, brier `0.2144`, calibration_gap `0.0620`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5333`, avg `-0.0013`, median `0.0021`, brier `0.2805`, calibration_gap `0.1756`
- 5d: hit_rate `0.5167`, avg `-0.0007`, median `0.0003`, brier `0.2870`, calibration_gap `0.1923`
- 10d: hit_rate `0.4667`, avg `0.0029`, median `-0.0025`, brier `0.3075`, calibration_gap `0.2423`
- 20d: hit_rate `0.7167`, avg `0.0135`, median `0.0184`, brier `0.2011`, calibration_gap `-0.0077`
- 60d: hit_rate `0.7000`, avg `0.0397`, median `0.0479`, brier `0.2110`, calibration_gap `0.0089`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0011`, median `0.0099`, brier `0.2589`, calibration_gap `0.1152`
- 5d: hit_rate `0.5000`, avg `-0.0018`, median `-0.0001`, brier `0.2808`, calibration_gap `0.1777`
- 10d: hit_rate `0.5000`, avg `0.0011`, median `0.0020`, brier `0.2831`, calibration_gap `0.1777`
- 20d: hit_rate `0.6250`, avg `0.0067`, median `0.0083`, brier `0.2412`, calibration_gap `0.0527`
- 60d: hit_rate `0.8125`, avg `0.0648`, median `0.0718`, brier `0.1708`, calibration_gap `-0.1348`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
