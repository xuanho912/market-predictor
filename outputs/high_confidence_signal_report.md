# High Confidence Signal Report

Generated at: `2026-07-15T04:20:39.049857+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0008`, median `0.0033`, brier `0.2383`, calibration_gap `0.0486`
- 5d: hit_rate `0.5000`, avg `0.0003`, median `0.0005`, brier `0.2810`, calibration_gap `0.1736`
- 10d: hit_rate `0.7500`, avg `0.0118`, median `0.0176`, brier `0.1956`, calibration_gap `-0.0764`
- 20d: hit_rate `1.0000`, avg `0.0272`, median `0.0211`, brier `0.1067`, calibration_gap `-0.3264`
- 60d: hit_rate `0.5000`, avg `0.0188`, median `0.0158`, brier `0.2810`, calibration_gap `0.1736`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0006`, median `0.0033`, brier `0.2548`, calibration_gap `0.0970`
- 5d: hit_rate `0.5000`, avg `-0.0005`, median `-0.0005`, brier `0.2776`, calibration_gap `0.1595`
- 10d: hit_rate `0.6250`, avg `0.0033`, median `0.0077`, brier `0.2349`, calibration_gap `0.0345`
- 20d: hit_rate `0.9375`, avg `0.0203`, median `0.0247`, brier `0.1351`, calibration_gap `-0.2780`
- 60d: hit_rate `0.5625`, avg `0.0272`, median `0.0369`, brier `0.2589`, calibration_gap `0.0970`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6667`, avg `0.0042`, median `0.0056`, brier `0.2252`, calibration_gap `-0.0528`
- 5d: hit_rate `0.6333`, avg `0.0061`, median `0.0093`, brier `0.2302`, calibration_gap `-0.0195`
- 10d: hit_rate `0.7333`, avg `0.0152`, median `0.0157`, brier `0.2073`, calibration_gap `-0.1195`
- 20d: hit_rate `0.9000`, avg `0.0311`, median `0.0300`, brier `0.1723`, calibration_gap `-0.2861`
- 60d: hit_rate `0.8333`, avg `0.0546`, median `0.0696`, brier `0.1861`, calibration_gap `-0.2195`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0049`, median `0.0029`, brier `0.2235`, calibration_gap `-0.0982`
- 5d: hit_rate `0.6250`, avg `0.0099`, median `0.0104`, brier `0.2340`, calibration_gap `-0.0357`
- 10d: hit_rate `0.5625`, avg `0.0103`, median `0.0073`, brier `0.2459`, calibration_gap `0.0268`
- 20d: hit_rate `0.8750`, avg `0.0270`, median `0.0262`, brier `0.1922`, calibration_gap `-0.2857`
- 60d: hit_rate `0.8750`, avg `0.0418`, median `0.0554`, brier `0.1920`, calibration_gap `-0.2857`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
