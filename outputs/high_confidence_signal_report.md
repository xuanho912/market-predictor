# High Confidence Signal Report

Generated at: `2026-07-25T06:08:20.785121+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0040`, median `0.0076`, brier `0.1387`, calibration_gap `-0.1749`
- 5d: hit_rate `0.6250`, avg `0.0072`, median `0.0100`, brier `0.2340`, calibration_gap `0.0751`
- 10d: hit_rate `0.7500`, avg `0.0110`, median `0.0178`, brier `0.1844`, calibration_gap `-0.0499`
- 20d: hit_rate `1.0000`, avg `0.0426`, median `0.0445`, brier `0.0901`, calibration_gap `-0.2999`
- 60d: hit_rate `0.7500`, avg `0.0468`, median `0.0565`, brier `0.1855`, calibration_gap `-0.0499`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0052`, median `0.0056`, brier `0.2109`, calibration_gap `0.0007`
- 5d: hit_rate `0.8125`, avg `0.0142`, median `0.0160`, brier `0.1694`, calibration_gap `-0.1243`
- 10d: hit_rate `0.8125`, avg `0.0160`, median `0.0205`, brier `0.1674`, calibration_gap `-0.1243`
- 20d: hit_rate `1.0000`, avg `0.0389`, median `0.0420`, brier `0.0974`, calibration_gap `-0.3118`
- 60d: hit_rate `0.8125`, avg `0.0539`, median `0.0677`, brier `0.1674`, calibration_gap `-0.1243`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6667`, avg `0.0055`, median `0.0056`, brier `0.2186`, calibration_gap `-0.0181`
- 5d: hit_rate `0.6333`, avg `0.0094`, median `0.0089`, brier `0.2276`, calibration_gap `0.0152`
- 10d: hit_rate `0.8333`, avg `0.0167`, median `0.0186`, brier `0.1719`, calibration_gap `-0.1848`
- 20d: hit_rate `0.8500`, avg `0.0320`, median `0.0315`, brier `0.1687`, calibration_gap `-0.2015`
- 60d: hit_rate `0.8667`, avg `0.0619`, median `0.0757`, brier `0.1666`, calibration_gap `-0.2181`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0016`, median `-0.0060`, brier `0.2750`, calibration_gap `0.1657`
- 5d: hit_rate `0.4375`, avg `0.0053`, median `-0.0034`, brier `0.2743`, calibration_gap `0.1657`
- 10d: hit_rate `0.7500`, avg `0.0198`, median `0.0221`, brier `0.2096`, calibration_gap `-0.1468`
- 20d: hit_rate `0.9375`, avg `0.0390`, median `0.0361`, brier `0.1687`, calibration_gap `-0.3343`
- 60d: hit_rate `0.8750`, avg `0.0654`, median `0.0850`, brier `0.1811`, calibration_gap `-0.2718`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
