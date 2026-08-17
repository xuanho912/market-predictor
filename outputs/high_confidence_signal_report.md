# High Confidence Signal Report

Generated at: `2026-08-17T13:08:40.081187+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `20`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `2`
- 3d: hit_rate `1.0000`, avg `0.0159`, median `0.0159`, brier `0.0755`, calibration_gap `-0.2747`
- 5d: hit_rate `1.0000`, avg `0.0155`, median `0.0155`, brier `0.0755`, calibration_gap `-0.2747`
- 10d: hit_rate `1.0000`, avg `0.0234`, median `0.0234`, brier `0.0755`, calibration_gap `-0.2747`
- 20d: hit_rate `0.5000`, avg `0.0277`, median `0.0277`, brier `0.2944`, calibration_gap `0.2253`
- 60d: hit_rate `0.5000`, avg `0.0244`, median `0.0244`, brier `0.2944`, calibration_gap `0.2253`

### top_20_confidence_signals
- sample_size: `4`
- 3d: hit_rate `1.0000`, avg `0.0114`, median `0.0109`, brier `0.0810`, calibration_gap `-0.2844`
- 5d: hit_rate `1.0000`, avg `0.0113`, median `0.0120`, brier `0.0810`, calibration_gap `-0.2844`
- 10d: hit_rate `1.0000`, avg `0.0185`, median `0.0234`, brier `0.0810`, calibration_gap `-0.2844`
- 20d: hit_rate `0.5000`, avg `0.0162`, median `0.0086`, brier `0.2967`, calibration_gap `0.2156`
- 60d: hit_rate `0.5000`, avg `0.0223`, median `0.0237`, brier `0.2967`, calibration_gap `0.2156`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6000`, avg `0.0021`, median `0.0080`, brier `0.2471`, calibration_gap `0.0877`
- 5d: hit_rate `0.6000`, avg `0.0063`, median `0.0047`, brier `0.2446`, calibration_gap `0.0877`
- 10d: hit_rate `0.7000`, avg `0.0094`, median `0.0111`, brier `0.2067`, calibration_gap `-0.0123`
- 20d: hit_rate `0.8500`, avg `0.0246`, median `0.0261`, brier `0.1597`, calibration_gap `-0.1623`
- 60d: hit_rate `0.6000`, avg `0.0296`, median `0.0383`, brier `0.2521`, calibration_gap `0.0877`

### low_confidence_reference
- sample_size: `4`
- 3d: hit_rate `1.0000`, avg `0.0121`, median `0.0116`, brier `0.1107`, calibration_gap `-0.3328`
- 5d: hit_rate `0.7500`, avg `0.0095`, median `0.0117`, brier `0.1946`, calibration_gap `-0.0828`
- 10d: hit_rate `0.5000`, avg `-0.0001`, median `0.0035`, brier `0.2790`, calibration_gap `0.1672`
- 20d: hit_rate `1.0000`, avg `0.0282`, median `0.0273`, brier `0.1107`, calibration_gap `-0.3328`
- 60d: hit_rate `1.0000`, avg `0.0740`, median `0.0905`, brier `0.1107`, calibration_gap `-0.3328`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
