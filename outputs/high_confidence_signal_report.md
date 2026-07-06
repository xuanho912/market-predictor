# High Confidence Signal Report

Generated at: `2026-07-06T14:44:23.217586+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.0000`, avg `-0.0137`, median `-0.0097`, brier `0.5176`, calibration_gap `0.7192`
- 5d: hit_rate `0.2500`, avg `-0.0124`, median `-0.0114`, brier `0.4131`, calibration_gap `0.4692`
- 10d: hit_rate `0.2500`, avg `-0.0103`, median `-0.0128`, brier `0.4111`, calibration_gap `0.4692`
- 20d: hit_rate `0.5000`, avg `-0.0062`, median `-0.0053`, brier `0.2891`, calibration_gap `0.2192`
- 60d: hit_rate `0.2500`, avg `-0.0384`, median `-0.0651`, brier `0.3963`, calibration_gap `0.4692`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.1875`, avg `-0.0092`, median `-0.0070`, brier `0.4297`, calibration_gap `0.5238`
- 5d: hit_rate `0.5000`, avg `-0.0045`, median `-0.0005`, brier `0.3008`, calibration_gap `0.2113`
- 10d: hit_rate `0.3750`, avg `-0.0016`, median `-0.0038`, brier `0.3511`, calibration_gap `0.3363`
- 20d: hit_rate `0.6875`, avg `0.0108`, median `0.0145`, brier `0.2138`, calibration_gap `0.0238`
- 60d: hit_rate `0.5000`, avg `0.0020`, median `-0.0121`, brier `0.2925`, calibration_gap `0.2113`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.4750`, avg `-0.0023`, median `-0.0005`, brier `0.3044`, calibration_gap `0.2079`
- 5d: hit_rate `0.4750`, avg `-0.0043`, median `-0.0017`, brier `0.2998`, calibration_gap `0.2079`
- 10d: hit_rate `0.4500`, avg `0.0034`, median `-0.0045`, brier `0.3098`, calibration_gap `0.2329`
- 20d: hit_rate `0.6250`, avg `0.0112`, median `0.0119`, brier `0.2377`, calibration_gap `0.0579`
- 60d: hit_rate `0.6500`, avg `0.0352`, median `0.0516`, brier `0.2295`, calibration_gap `0.0329`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0049`, median `0.0030`, brier `0.2354`, calibration_gap `0.0184`
- 5d: hit_rate `0.5000`, avg `-0.0043`, median `-0.0026`, brier `0.2727`, calibration_gap `0.1434`
- 10d: hit_rate `0.5000`, avg `0.0029`, median `0.0007`, brier `0.2721`, calibration_gap `0.1434`
- 20d: hit_rate `0.7500`, avg `0.0029`, median `0.0088`, brier `0.1999`, calibration_gap `-0.1066`
- 60d: hit_rate `0.5000`, avg `0.0107`, median `0.0031`, brier `0.2712`, calibration_gap `0.1434`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
