# High Confidence Signal Report

Generated at: `2026-08-15T02:22:24.756606+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `60`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `6`
- 3d: hit_rate `1.0000`, avg `0.0140`, median `0.0129`, brier `0.0766`, calibration_gap `-0.2767`
- 5d: hit_rate `0.8333`, avg `0.0083`, median `0.0106`, brier `0.1481`, calibration_gap `-0.1101`
- 10d: hit_rate `0.8333`, avg `0.0152`, median `0.0199`, brier `0.1499`, calibration_gap `-0.1101`
- 20d: hit_rate `0.1667`, avg `-0.0030`, median `-0.0114`, brier `0.4459`, calibration_gap `0.5566`
- 60d: hit_rate `0.1667`, avg `-0.0230`, median `-0.0408`, brier `0.4459`, calibration_gap `0.5566`

### top_20_confidence_signals
- sample_size: `12`
- 3d: hit_rate `0.8333`, avg `0.0075`, median `0.0069`, brier `0.1507`, calibration_gap `-0.1178`
- 5d: hit_rate `0.9167`, avg `0.0100`, median `0.0112`, brier `0.1168`, calibration_gap `-0.2011`
- 10d: hit_rate `0.7500`, avg `0.0120`, median `0.0164`, brier `0.1874`, calibration_gap `-0.0344`
- 20d: hit_rate `0.4167`, avg `0.0026`, median `-0.0053`, brier `0.3364`, calibration_gap `0.2989`
- 60d: hit_rate `0.3333`, avg `-0.0061`, median `-0.0336`, brier `0.3701`, calibration_gap `0.3822`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5833`, avg `0.0026`, median `0.0019`, brier `0.2532`, calibration_gap `0.1040`
- 5d: hit_rate `0.6500`, avg `0.0050`, median `0.0043`, brier `0.2264`, calibration_gap `0.0373`
- 10d: hit_rate `0.5667`, avg `0.0076`, median `0.0091`, brier `0.2605`, calibration_gap `0.1207`
- 20d: hit_rate `0.6500`, avg `0.0169`, median `0.0138`, brier `0.2341`, calibration_gap `0.0373`
- 60d: hit_rate `0.5833`, avg `0.0294`, median `0.0231`, brier `0.2626`, calibration_gap `0.1040`

### low_confidence_reference
- sample_size: `12`
- 3d: hit_rate `0.7500`, avg `0.0090`, median `0.0106`, brier `0.1937`, calibration_gap `-0.0879`
- 5d: hit_rate `0.6667`, avg `0.0113`, median `0.0126`, brier `0.2217`, calibration_gap `-0.0046`
- 10d: hit_rate `0.6667`, avg `0.0191`, median `0.0144`, brier `0.2245`, calibration_gap `-0.0046`
- 20d: hit_rate `0.7500`, avg `0.0382`, median `0.0332`, brier `0.1963`, calibration_gap `-0.0879`
- 60d: hit_rate `1.0000`, avg `0.0974`, median `0.0905`, brier `0.1142`, calibration_gap `-0.3379`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
