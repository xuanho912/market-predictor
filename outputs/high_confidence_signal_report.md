# High Confidence Signal Report

Generated at: `2026-11-14T07:39:39.910342+00:00`

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
- sample_size: `80`
- 3d: hit_rate `0.4625`, avg `0.0018`, median `-0.0020`, brier `0.3303`, calibration_gap `0.2519`
- 5d: hit_rate `0.5500`, avg `0.0040`, median `0.0030`, brier `0.2877`, calibration_gap `0.1644`
- 10d: hit_rate `0.4125`, avg `0.0049`, median `-0.0081`, brier `0.3519`, calibration_gap `0.3019`
- 20d: hit_rate `0.6125`, avg `0.0158`, median `0.0171`, brier `0.2584`, calibration_gap `0.1019`
- 60d: hit_rate `0.5250`, avg `0.0202`, median `0.0045`, brier `0.2974`, calibration_gap `0.1894`

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
