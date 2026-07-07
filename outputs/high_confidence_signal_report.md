# High Confidence Signal Report

Generated at: `2026-07-07T15:17:51.048570+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0138`, median `-0.0101`, brier `0.4766`, calibration_gap `0.6035`
- 5d: hit_rate `0.3750`, avg `-0.0118`, median `-0.0134`, brier `0.3673`, calibration_gap `0.3535`
- 10d: hit_rate `0.0000`, avg `-0.0139`, median `-0.0128`, brier `0.5310`, calibration_gap `0.7285`
- 20d: hit_rate `0.6250`, avg `0.0168`, median `0.0246`, brier `0.2398`, calibration_gap `0.1035`
- 60d: hit_rate `0.6250`, avg `0.0267`, median `0.0291`, brier `0.2398`, calibration_gap `0.1035`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.1875`, avg `-0.0114`, median `-0.0097`, brier `0.4388`, calibration_gap `0.5322`
- 5d: hit_rate `0.3750`, avg `-0.0114`, median `-0.0114`, brier `0.3580`, calibration_gap `0.3447`
- 10d: hit_rate `0.1875`, avg `-0.0077`, median `-0.0087`, brier `0.4387`, calibration_gap `0.5322`
- 20d: hit_rate `0.6250`, avg `0.0104`, median `0.0069`, brier `0.2411`, calibration_gap `0.0947`
- 60d: hit_rate `0.5000`, avg `0.0093`, median `-0.0095`, brier `0.2939`, calibration_gap `0.2197`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.4500`, avg `-0.0028`, median `-0.0020`, brier `0.3070`, calibration_gap `0.2329`
- 5d: hit_rate `0.5125`, avg `-0.0031`, median `0.0011`, brier `0.2796`, calibration_gap `0.1704`
- 10d: hit_rate `0.5000`, avg `0.0017`, median `0.0000`, brier `0.2858`, calibration_gap `0.1829`
- 20d: hit_rate `0.6875`, avg `0.0067`, median `0.0110`, brier `0.2156`, calibration_gap `-0.0046`
- 60d: hit_rate `0.4875`, avg `0.0056`, median `-0.0035`, brier `0.2864`, calibration_gap `0.1954`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0002`, median `0.0069`, brier `0.2546`, calibration_gap `0.0875`
- 5d: hit_rate `0.4375`, avg `-0.0026`, median `-0.0012`, brier `0.2918`, calibration_gap `0.2125`
- 10d: hit_rate `0.4375`, avg `-0.0016`, median `-0.0064`, brier `0.2919`, calibration_gap `0.2125`
- 20d: hit_rate `0.6250`, avg `0.0022`, median `0.0065`, brier `0.2360`, calibration_gap `0.0250`
- 60d: hit_rate `0.6250`, avg `0.0239`, median `0.0350`, brier `0.2352`, calibration_gap `0.0250`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
