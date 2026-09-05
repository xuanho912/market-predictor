# High Confidence Signal Report

Generated at: `2026-09-05T00:55:28.594159+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0108`, median `0.0014`, brier `0.2811`, calibration_gap `0.1797`
- 5d: hit_rate `0.5000`, avg `-0.0089`, median `0.0016`, brier `0.2821`, calibration_gap `0.1797`
- 10d: hit_rate `0.2500`, avg `-0.0095`, median `-0.0091`, brier `0.3662`, calibration_gap `0.4297`
- 20d: hit_rate `0.6250`, avg `0.0140`, median `0.0186`, brier `0.2380`, calibration_gap `0.0547`
- 60d: hit_rate `0.5000`, avg `0.0073`, median `0.0139`, brier `0.2824`, calibration_gap `0.1797`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0046`, median `0.0117`, brier `0.1995`, calibration_gap `-0.0818`
- 5d: hit_rate `0.6250`, avg `0.0052`, median `0.0127`, brier `0.2397`, calibration_gap `0.0432`
- 10d: hit_rate `0.5625`, avg `0.0145`, median `0.0108`, brier `0.2621`, calibration_gap `0.1057`
- 20d: hit_rate `0.7500`, avg `0.0256`, median `0.0367`, brier `0.1981`, calibration_gap `-0.0818`
- 60d: hit_rate `0.5625`, avg `0.0399`, median `0.0512`, brier `0.2588`, calibration_gap `0.1057`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6333`, avg `0.0038`, median `0.0074`, brier `0.2342`, calibration_gap `-0.0196`
- 5d: hit_rate `0.6667`, avg `0.0065`, median `0.0118`, brier `0.2291`, calibration_gap `-0.0529`
- 10d: hit_rate `0.6833`, avg `0.0112`, median `0.0188`, brier `0.2292`, calibration_gap `-0.0696`
- 20d: hit_rate `0.7833`, avg `0.0250`, median `0.0322`, brier `0.1993`, calibration_gap `-0.1696`
- 60d: hit_rate `0.8000`, avg `0.0537`, median `0.0692`, brier `0.2026`, calibration_gap `-0.1862`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0046`, median `0.0064`, brier `0.2487`, calibration_gap `0.0175`
- 5d: hit_rate `0.5625`, avg `0.0033`, median `0.0068`, brier `0.2492`, calibration_gap `0.0175`
- 10d: hit_rate `0.6875`, avg `0.0131`, median `0.0166`, brier `0.2274`, calibration_gap `-0.1075`
- 20d: hit_rate `0.6875`, avg `0.0240`, median `0.0263`, brier `0.2245`, calibration_gap `-0.1075`
- 60d: hit_rate `0.6875`, avg `0.0546`, median `0.0643`, brier `0.2257`, calibration_gap `-0.1075`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
