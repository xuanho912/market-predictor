# High Confidence Signal Report

Generated at: `2026-11-03T02:31:54.194448+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0054`, median `0.0012`, brier `0.3356`, calibration_gap `0.3094`
- 5d: hit_rate `0.5000`, avg `0.0101`, median `0.0044`, brier `0.3356`, calibration_gap `0.3094`
- 10d: hit_rate `0.6250`, avg `0.0220`, median `0.0276`, brier `0.2670`, calibration_gap `0.1844`
- 20d: hit_rate `0.8750`, avg `0.0408`, median `0.0469`, brier `0.1161`, calibration_gap `-0.0656`
- 60d: hit_rate `1.0000`, avg `0.0821`, median `0.0843`, brier `0.0365`, calibration_gap `-0.1906`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0078`, median `0.0017`, brier `0.3332`, calibration_gap `0.2965`
- 5d: hit_rate `0.5625`, avg `0.0106`, median `0.0121`, brier `0.2976`, calibration_gap `0.2340`
- 10d: hit_rate `0.6250`, avg `0.0222`, median `0.0276`, brier `0.2635`, calibration_gap `0.1715`
- 20d: hit_rate `0.8750`, avg `0.0411`, median `0.0468`, brier `0.1173`, calibration_gap `-0.0785`
- 60d: hit_rate `0.9375`, avg `0.0769`, median `0.0777`, brier `0.0775`, calibration_gap `-0.1410`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5000`, avg `0.0038`, median `0.0017`, brier `0.3154`, calibration_gap `0.2565`
- 5d: hit_rate `0.5250`, avg `0.0064`, median `0.0066`, brier `0.3035`, calibration_gap `0.2315`
- 10d: hit_rate `0.6000`, avg `0.0148`, median `0.0160`, brier `0.2661`, calibration_gap `0.1565`
- 20d: hit_rate `0.7500`, avg `0.0288`, median `0.0294`, brier `0.1843`, calibration_gap `0.0065`
- 60d: hit_rate `0.8500`, avg `0.0546`, median `0.0675`, brier `0.1298`, calibration_gap `-0.0935`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0010`, median `-0.0086`, brier `0.3013`, calibration_gap `0.2561`
- 5d: hit_rate `0.5625`, avg `0.0001`, median `0.0065`, brier `0.2517`, calibration_gap `0.0686`
- 10d: hit_rate `0.6875`, avg `-0.0033`, median `0.0100`, brier `0.2187`, calibration_gap `-0.0564`
- 20d: hit_rate `0.5000`, avg `0.0026`, median `0.0011`, brier `0.2688`, calibration_gap `0.1311`
- 60d: hit_rate `0.5000`, avg `0.0214`, median `0.0008`, brier `0.2676`, calibration_gap `0.1311`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
