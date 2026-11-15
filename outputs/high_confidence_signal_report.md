# High Confidence Signal Report

Generated at: `2026-11-15T18:53:51.193570+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.0000`, avg `-0.0173`, median `-0.0123`, brier `0.6324`, calibration_gap `0.7952`
- 5d: hit_rate `0.3750`, avg `-0.0126`, median `-0.0134`, brier `0.4165`, calibration_gap `0.4202`
- 10d: hit_rate `0.0000`, avg `-0.0165`, median `-0.0165`, brier `0.6324`, calibration_gap `0.7952`
- 20d: hit_rate `0.3750`, avg `-0.0045`, median `-0.0227`, brier `0.4095`, calibration_gap `0.4202`
- 60d: hit_rate `0.3750`, avg `-0.0045`, median `-0.0484`, brier `0.4095`, calibration_gap `0.4202`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.1875`, avg `-0.0097`, median `-0.0097`, brier `0.5102`, calibration_gap `0.5928`
- 5d: hit_rate `0.4375`, avg `-0.0095`, median `-0.0031`, brier `0.3666`, calibration_gap `0.3428`
- 10d: hit_rate `0.1250`, avg `-0.0116`, median `-0.0110`, brier `0.5440`, calibration_gap `0.6553`
- 20d: hit_rate `0.4375`, avg `0.0003`, median `-0.0017`, brier `0.3642`, calibration_gap `0.3428`
- 60d: hit_rate `0.3125`, avg `-0.0148`, median `-0.0362`, brier `0.4316`, calibration_gap `0.4678`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5333`, avg `0.0045`, median `0.0027`, brier `0.2933`, calibration_gap `0.1702`
- 5d: hit_rate `0.5500`, avg `0.0063`, median `0.0033`, brier `0.2895`, calibration_gap `0.1535`
- 10d: hit_rate `0.4333`, avg `0.0082`, median `-0.0068`, brier `0.3386`, calibration_gap `0.2702`
- 20d: hit_rate `0.6333`, avg `0.0198`, median `0.0185`, brier `0.2473`, calibration_gap `0.0702`
- 60d: hit_rate `0.5833`, avg `0.0315`, median `0.0294`, brier `0.2645`, calibration_gap `0.1202`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0057`, median `0.0085`, brier `0.2572`, calibration_gap `0.0948`
- 5d: hit_rate `0.6250`, avg `0.0103`, median `0.0099`, brier `0.2364`, calibration_gap `0.0323`
- 10d: hit_rate `0.5625`, avg `0.0126`, median `0.0140`, brier `0.2556`, calibration_gap `0.0948`
- 20d: hit_rate `0.8125`, avg `0.0316`, median `0.0280`, brier `0.1766`, calibration_gap `-0.1552`
- 60d: hit_rate `0.7500`, avg `0.0560`, median `0.0531`, brier `0.1962`, calibration_gap `-0.0927`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
