# High Confidence Signal Report

Generated at: `2026-06-22T17:05:12.487193+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0058`, median `-0.0061`, brier `0.3617`, calibration_gap `0.3530`
- 5d: hit_rate `0.1250`, avg `-0.0173`, median `-0.0150`, brier `0.4754`, calibration_gap `0.6030`
- 10d: hit_rate `0.5000`, avg `0.0039`, median `0.0025`, brier `0.2996`, calibration_gap `0.2280`
- 20d: hit_rate `1.0000`, avg `0.0278`, median `0.0302`, brier `0.0740`, calibration_gap `-0.2720`
- 60d: hit_rate `1.0000`, avg `0.0737`, median `0.0832`, brier `0.0740`, calibration_gap `-0.2720`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0017`, median `-0.0001`, brier `0.3016`, calibration_gap `0.2206`
- 5d: hit_rate `0.2500`, avg `-0.0110`, median `-0.0130`, brier `0.4124`, calibration_gap `0.4706`
- 10d: hit_rate `0.4375`, avg `0.0024`, median `-0.0008`, brier `0.3249`, calibration_gap `0.2831`
- 20d: hit_rate `0.9375`, avg `0.0279`, median `0.0290`, brier `0.1045`, calibration_gap `-0.2169`
- 60d: hit_rate `0.8750`, avg `0.0639`, median `0.0832`, brier `0.1300`, calibration_gap `-0.1544`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4500`, avg `-0.0012`, median `-0.0017`, brier `0.3025`, calibration_gap `0.2263`
- 5d: hit_rate `0.4500`, avg `-0.0041`, median `-0.0066`, brier `0.3090`, calibration_gap `0.2263`
- 10d: hit_rate `0.3833`, avg `-0.0039`, median `-0.0033`, brier `0.3259`, calibration_gap `0.2930`
- 20d: hit_rate `0.7500`, avg `0.0102`, median `0.0179`, brier `0.1855`, calibration_gap `-0.0737`
- 60d: hit_rate `0.6333`, avg `0.0241`, median `0.0400`, brier `0.2281`, calibration_gap `0.0430`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `-0.0019`, median `0.0028`, brier `0.2197`, calibration_gap `-0.0684`
- 5d: hit_rate `0.6875`, avg `0.0012`, median `0.0060`, brier `0.2192`, calibration_gap `-0.0684`
- 10d: hit_rate `0.4375`, avg `-0.0015`, median `-0.0035`, brier `0.2791`, calibration_gap `0.1816`
- 20d: hit_rate `0.6875`, avg `0.0116`, median `0.0143`, brier `0.2198`, calibration_gap `-0.0684`
- 60d: hit_rate `0.6875`, avg `0.0273`, median `0.0590`, brier `0.2189`, calibration_gap `-0.0684`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
