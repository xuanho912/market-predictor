# High Confidence Signal Report

Generated at: `2026-09-11T01:02:18.997233+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0096`, median `0.0122`, brier `0.1881`, calibration_gap `-0.0586`
- 5d: hit_rate `0.7500`, avg `0.0061`, median `0.0080`, brier `0.1997`, calibration_gap `-0.0586`
- 10d: hit_rate `0.6250`, avg `0.0079`, median `0.0074`, brier `0.2500`, calibration_gap `0.0664`
- 20d: hit_rate `1.0000`, avg `0.0586`, median `0.0581`, brier `0.0958`, calibration_gap `-0.3086`
- 60d: hit_rate `0.8750`, avg `0.0919`, median `0.1032`, brier `0.1577`, calibration_gap `-0.1836`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0011`, median `0.0043`, brier `0.2302`, calibration_gap `0.0420`
- 5d: hit_rate `0.6875`, avg `0.0049`, median `0.0080`, brier `0.2165`, calibration_gap `-0.0205`
- 10d: hit_rate `0.6875`, avg `0.0080`, median `0.0113`, brier `0.2262`, calibration_gap `-0.0205`
- 20d: hit_rate `0.8750`, avg `0.0413`, median `0.0460`, brier `0.1427`, calibration_gap `-0.2080`
- 60d: hit_rate `0.9375`, avg `0.0817`, median `0.0844`, brier `0.1428`, calibration_gap `-0.2705`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6875`, avg `0.0069`, median `0.0125`, brier `0.2237`, calibration_gap `-0.0910`
- 5d: hit_rate `0.6125`, avg `0.0080`, median `0.0127`, brier `0.2338`, calibration_gap `-0.0160`
- 10d: hit_rate `0.6875`, avg `0.0145`, median `0.0171`, brier `0.2231`, calibration_gap `-0.0910`
- 20d: hit_rate `0.8000`, avg `0.0322`, median `0.0347`, brier `0.1990`, calibration_gap `-0.2035`
- 60d: hit_rate `0.7875`, avg `0.0658`, median `0.0829`, brier `0.2027`, calibration_gap `-0.1910`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0087`, median `0.0118`, brier `0.2270`, calibration_gap `-0.2048`
- 5d: hit_rate `0.5000`, avg `0.0058`, median `0.0017`, brier `0.2500`, calibration_gap `0.0452`
- 10d: hit_rate `0.5625`, avg `0.0187`, median `0.0241`, brier `0.2461`, calibration_gap `-0.0173`
- 20d: hit_rate `0.8750`, avg `0.0421`, median `0.0341`, brier `0.2171`, calibration_gap `-0.3298`
- 60d: hit_rate `0.7500`, avg `0.0673`, median `0.0968`, brier `0.2300`, calibration_gap `-0.2048`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
