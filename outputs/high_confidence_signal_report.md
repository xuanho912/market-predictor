# High Confidence Signal Report

Generated at: `2026-06-29T23:38:12.430987+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0053`, median `-0.0061`, brier `0.3479`, calibration_gap `0.3326`
- 5d: hit_rate `0.0000`, avg `-0.0193`, median `-0.0194`, brier `0.5008`, calibration_gap `0.7076`
- 10d: hit_rate `0.6250`, avg `0.0062`, median `0.0061`, brier `0.2425`, calibration_gap `0.0826`
- 20d: hit_rate `1.0000`, avg `0.0284`, median `0.0302`, brier `0.0855`, calibration_gap `-0.2924`
- 60d: hit_rate `0.8750`, avg `0.0635`, median `0.0869`, brier `0.1361`, calibration_gap `-0.1674`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0014`, median `-0.0014`, brier `0.3183`, calibration_gap `0.2658`
- 5d: hit_rate `0.1875`, avg `-0.0146`, median `-0.0176`, brier `0.4202`, calibration_gap `0.5158`
- 10d: hit_rate `0.4375`, avg `0.0010`, median `-0.0008`, brier `0.3161`, calibration_gap `0.2658`
- 20d: hit_rate `0.9375`, avg `0.0262`, median `0.0290`, brier `0.1130`, calibration_gap `-0.2342`
- 60d: hit_rate `0.8125`, avg `0.0536`, median `0.0832`, brier `0.1628`, calibration_gap `-0.1092`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.4750`, avg `-0.0001`, median `-0.0017`, brier `0.2912`, calibration_gap `0.1844`
- 5d: hit_rate `0.4500`, avg `-0.0045`, median `-0.0082`, brier `0.3059`, calibration_gap `0.2094`
- 10d: hit_rate `0.4750`, avg `0.0023`, median `-0.0007`, brier `0.2941`, calibration_gap `0.1844`
- 20d: hit_rate `0.8000`, avg `0.0212`, median `0.0287`, brier `0.1769`, calibration_gap `-0.1406`
- 60d: hit_rate `0.7500`, avg `0.0458`, median `0.0619`, brier `0.1845`, calibration_gap `-0.0906`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0001`, median `-0.0020`, brier `0.2764`, calibration_gap `0.1693`
- 5d: hit_rate `0.5000`, avg `-0.0001`, median `-0.0053`, brier `0.2636`, calibration_gap `0.1068`
- 10d: hit_rate `0.5625`, avg `0.0013`, median `0.0018`, brier `0.2498`, calibration_gap `0.0443`
- 20d: hit_rate `0.7500`, avg `0.0186`, median `0.0110`, brier `0.2077`, calibration_gap `-0.1432`
- 60d: hit_rate `0.7500`, avg `0.0798`, median `0.0738`, brier `0.2093`, calibration_gap `-0.1432`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
