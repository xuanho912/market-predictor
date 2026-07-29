# High Confidence Signal Report

Generated at: `2026-07-29T06:21:18.777720+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0142`, median `-0.0203`, brier `0.4619`, calibration_gap `0.5243`
- 5d: hit_rate `0.3750`, avg `-0.0176`, median `-0.0243`, brier `0.3935`, calibration_gap `0.3993`
- 10d: hit_rate `0.1250`, avg `-0.0092`, median `-0.0096`, brier `0.5327`, calibration_gap `0.6493`
- 20d: hit_rate `0.6250`, avg `0.0246`, median `0.0363`, brier `0.2594`, calibration_gap `0.1493`
- 60d: hit_rate `0.7500`, avg `0.0610`, median `0.0730`, brier `0.1886`, calibration_gap `0.0243`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0072`, median `-0.0002`, brier `0.3249`, calibration_gap `0.2670`
- 5d: hit_rate `0.4375`, avg `-0.0142`, median `-0.0087`, brier `0.3551`, calibration_gap `0.3295`
- 10d: hit_rate `0.3125`, avg `-0.0040`, median `-0.0069`, brier `0.4253`, calibration_gap `0.4545`
- 20d: hit_rate `0.6875`, avg `0.0177`, median `0.0316`, brier `0.2236`, calibration_gap `0.0795`
- 60d: hit_rate `0.7500`, avg `0.0536`, median `0.0689`, brier `0.1882`, calibration_gap `0.0170`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5333`, avg `-0.0025`, median `0.0007`, brier `0.2892`, calibration_gap `0.1898`
- 5d: hit_rate `0.5500`, avg `-0.0014`, median `0.0020`, brier `0.2859`, calibration_gap `0.1732`
- 10d: hit_rate `0.5000`, avg `0.0052`, median `0.0000`, brier `0.3134`, calibration_gap `0.2232`
- 20d: hit_rate `0.6667`, avg `0.0220`, median `0.0213`, brier `0.2285`, calibration_gap `0.0565`
- 60d: hit_rate `0.7333`, avg `0.0484`, median `0.0580`, brier `0.1989`, calibration_gap `-0.0102`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0043`, median `0.0033`, brier `0.2365`, calibration_gap `0.0432`
- 5d: hit_rate `0.5000`, avg `0.0001`, median `0.0010`, brier `0.2792`, calibration_gap `0.1682`
- 10d: hit_rate `0.6875`, avg `0.0114`, median `0.0165`, brier `0.2161`, calibration_gap `-0.0193`
- 20d: hit_rate `0.7500`, avg `0.0226`, median `0.0174`, brier `0.1943`, calibration_gap `-0.0818`
- 60d: hit_rate `0.6875`, avg `0.0379`, median `0.0567`, brier `0.2154`, calibration_gap `-0.0193`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
