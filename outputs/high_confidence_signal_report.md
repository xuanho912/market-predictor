# High Confidence Signal Report

Generated at: `2026-10-21T17:21:15.092395+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0021`, median `0.0107`, brier `0.2444`, calibration_gap `0.0977`
- 5d: hit_rate `0.6250`, avg `0.0035`, median `0.0106`, brier `0.2444`, calibration_gap `0.0977`
- 10d: hit_rate `0.6250`, avg `0.0133`, median `0.0238`, brier `0.2444`, calibration_gap `0.0977`
- 20d: hit_rate `1.0000`, avg `0.0292`, median `0.0291`, brier `0.0770`, calibration_gap `-0.2773`
- 60d: hit_rate `1.0000`, avg `0.0607`, median `0.0684`, brier `0.0770`, calibration_gap `-0.2773`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0036`, median `-0.0078`, brier `0.3215`, calibration_gap `0.2775`
- 5d: hit_rate `0.5000`, avg `-0.0025`, median `-0.0040`, brier `0.2956`, calibration_gap `0.2150`
- 10d: hit_rate `0.4375`, avg `-0.0054`, median `-0.0133`, brier `0.3200`, calibration_gap `0.2775`
- 20d: hit_rate `0.8750`, avg `0.0202`, median `0.0269`, brier `0.1328`, calibration_gap `-0.1600`
- 60d: hit_rate `0.7500`, avg `0.0409`, median `0.0377`, brier `0.1837`, calibration_gap `-0.0350`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5500`, avg `0.0000`, median `0.0022`, brier `0.2663`, calibration_gap `0.1317`
- 5d: hit_rate `0.5333`, avg `0.0002`, median `0.0018`, brier `0.2704`, calibration_gap `0.1484`
- 10d: hit_rate `0.6000`, avg `0.0036`, median `0.0069`, brier `0.2485`, calibration_gap `0.0817`
- 20d: hit_rate `0.7500`, avg `0.0190`, median `0.0214`, brier `0.1914`, calibration_gap `-0.0683`
- 60d: hit_rate `0.6333`, avg `0.0302`, median `0.0337`, brier `0.2339`, calibration_gap `0.0484`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0006`, median `0.0039`, brier `0.2569`, calibration_gap `0.1057`
- 5d: hit_rate `0.5000`, avg `-0.0033`, median `-0.0015`, brier `0.2776`, calibration_gap `0.1682`
- 10d: hit_rate `0.6875`, avg `0.0029`, median `0.0103`, brier `0.2146`, calibration_gap `-0.0193`
- 20d: hit_rate `0.7500`, avg `0.0129`, median `0.0112`, brier `0.1937`, calibration_gap `-0.0818`
- 60d: hit_rate `0.6250`, avg `0.0204`, median `0.0276`, brier `0.2365`, calibration_gap `0.0432`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
