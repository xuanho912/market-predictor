# High Confidence Signal Report

Generated at: `2026-08-29T04:11:04.726182+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0060`, median `0.0077`, brier `0.2467`, calibration_gap `0.0655`
- 5d: hit_rate `0.5000`, avg `-0.0090`, median `-0.0030`, brier `0.2906`, calibration_gap `0.1905`
- 10d: hit_rate `0.5000`, avg `-0.0016`, median `-0.0015`, brier `0.2905`, calibration_gap `0.1905`
- 20d: hit_rate `0.7500`, avg `0.0223`, median `0.0364`, brier `0.2028`, calibration_gap `-0.0595`
- 60d: hit_rate `0.6250`, avg `0.0124`, median `0.0400`, brier `0.2466`, calibration_gap `0.0655`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0013`, median `0.0117`, brier `0.2207`, calibration_gap `-0.0125`
- 5d: hit_rate `0.6875`, avg `0.0047`, median `0.0157`, brier `0.2234`, calibration_gap `-0.0125`
- 10d: hit_rate `0.6875`, avg `0.0160`, median `0.0232`, brier `0.2234`, calibration_gap `-0.0125`
- 20d: hit_rate `0.8125`, avg `0.0295`, median `0.0364`, brier `0.1795`, calibration_gap `-0.1375`
- 60d: hit_rate `0.7500`, avg `0.0495`, median `0.0671`, brier `0.2014`, calibration_gap `-0.0750`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.7500`, avg `0.0099`, median `0.0146`, brier `0.2113`, calibration_gap `-0.1312`
- 5d: hit_rate `0.7667`, avg `0.0147`, median `0.0183`, brier `0.2062`, calibration_gap `-0.1478`
- 10d: hit_rate `0.7167`, avg `0.0202`, median `0.0253`, brier `0.2170`, calibration_gap `-0.0978`
- 20d: hit_rate `0.8333`, avg `0.0384`, median `0.0364`, brier `0.1892`, calibration_gap `-0.2145`
- 60d: hit_rate `0.8167`, avg `0.0717`, median `0.0869`, brier `0.1949`, calibration_gap `-0.1978`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0106`, median `0.0178`, brier `0.2055`, calibration_gap `-0.2335`
- 5d: hit_rate `0.8125`, avg `0.0164`, median `0.0214`, brier `0.2055`, calibration_gap `-0.2335`
- 10d: hit_rate `0.7500`, avg `0.0130`, median `0.0180`, brier `0.2160`, calibration_gap `-0.1710`
- 20d: hit_rate `0.8125`, avg `0.0252`, median `0.0250`, brier `0.2039`, calibration_gap `-0.2335`
- 60d: hit_rate `0.9375`, avg `0.0706`, median `0.0684`, brier `0.1878`, calibration_gap `-0.3585`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
