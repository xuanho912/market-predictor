# High Confidence Signal Report

Generated at: `2026-08-07T01:45:23.090515+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0063`, median `0.0104`, brier `0.1888`, calibration_gap `-0.0238`
- 5d: hit_rate `0.8750`, avg `0.0103`, median `0.0155`, brier `0.1332`, calibration_gap `-0.1488`
- 10d: hit_rate `0.7500`, avg `0.0118`, median `0.0199`, brier `0.1888`, calibration_gap `-0.0238`
- 20d: hit_rate `0.5000`, avg `0.0074`, median `0.0011`, brier `0.3035`, calibration_gap `0.2262`
- 60d: hit_rate `0.5000`, avg `0.0180`, median `0.0138`, brier `0.3035`, calibration_gap `0.2262`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0006`, median `0.0008`, brier `0.2674`, calibration_gap `0.1554`
- 5d: hit_rate `0.7500`, avg `0.0033`, median `0.0058`, brier `0.1875`, calibration_gap `-0.0321`
- 10d: hit_rate `0.5625`, avg `0.0059`, median `0.0098`, brier `0.2667`, calibration_gap `0.1554`
- 20d: hit_rate `0.6250`, avg `0.0085`, median `0.0103`, brier `0.2463`, calibration_gap `0.0929`
- 60d: hit_rate `0.4375`, avg `-0.0013`, median `-0.0108`, brier `0.3250`, calibration_gap `0.2804`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6375`, avg `0.0025`, median `0.0046`, brier `0.2359`, calibration_gap `0.0553`
- 5d: hit_rate `0.7000`, avg `0.0048`, median `0.0059`, brier `0.2089`, calibration_gap `-0.0072`
- 10d: hit_rate `0.5500`, avg `0.0053`, median `0.0040`, brier `0.2682`, calibration_gap `0.1428`
- 20d: hit_rate `0.6750`, avg `0.0120`, median `0.0145`, brier `0.2219`, calibration_gap `0.0178`
- 60d: hit_rate `0.5500`, avg `0.0193`, median `0.0234`, brier `0.2713`, calibration_gap `0.1428`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0109`, median `0.0128`, brier `0.1937`, calibration_gap `-0.0757`
- 5d: hit_rate `0.7500`, avg `0.0107`, median `0.0088`, brier `0.1932`, calibration_gap `-0.0757`
- 10d: hit_rate `0.6250`, avg `0.0111`, median `0.0125`, brier `0.2364`, calibration_gap `0.0493`
- 20d: hit_rate `0.7500`, avg `0.0187`, median `0.0249`, brier `0.1935`, calibration_gap `-0.0757`
- 60d: hit_rate `0.6875`, avg `0.0220`, median `0.0612`, brier `0.2155`, calibration_gap `-0.0132`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
