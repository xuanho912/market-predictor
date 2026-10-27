# High Confidence Signal Report

Generated at: `2026-10-27T00:58:20.147503+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0065`, median `-0.0165`, brier `0.3971`, calibration_gap `0.4558`
- 5d: hit_rate `0.2500`, avg `-0.0123`, median `-0.0221`, brier `0.3971`, calibration_gap `0.4558`
- 10d: hit_rate `0.2500`, avg `-0.0224`, median `-0.0344`, brier `0.3971`, calibration_gap `0.4558`
- 20d: hit_rate `0.2500`, avg `-0.0333`, median `-0.0437`, brier `0.3971`, calibration_gap `0.4558`
- 60d: hit_rate `0.8750`, avg `0.0432`, median `0.0403`, brier `0.1473`, calibration_gap `-0.1692`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `0.0000`, median `-0.0046`, brier `0.3418`, calibration_gap `0.3216`
- 5d: hit_rate `0.4375`, avg `-0.0024`, median `-0.0119`, brier `0.3183`, calibration_gap `0.2591`
- 10d: hit_rate `0.3750`, avg `-0.0147`, median `-0.0293`, brier `0.3419`, calibration_gap `0.3216`
- 20d: hit_rate `0.2500`, avg `-0.0243`, median `-0.0254`, brier `0.3886`, calibration_gap `0.4466`
- 60d: hit_rate `0.8125`, avg `0.0547`, median `0.0458`, brier `0.1694`, calibration_gap `-0.1159`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0149`, median `0.0224`, brier `0.2282`, calibration_gap `-0.1073`
- 5d: hit_rate `0.7500`, avg `0.0112`, median `0.0185`, brier `0.2181`, calibration_gap `-0.1698`
- 10d: hit_rate `0.7500`, avg `0.0175`, median `0.0213`, brier `0.2181`, calibration_gap `-0.1698`
- 20d: hit_rate `0.7500`, avg `0.0250`, median `0.0233`, brier `0.2177`, calibration_gap `-0.1698`
- 60d: hit_rate `0.8750`, avg `0.0965`, median `0.1044`, brier `0.1974`, calibration_gap `-0.2948`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
