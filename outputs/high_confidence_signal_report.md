# High Confidence Signal Report

Generated at: `2026-08-18T20:47:07.951995+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `60`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `6`
- 3d: hit_rate `1.0000`, avg `0.0137`, median `0.0134`, brier `0.0839`, calibration_gap `-0.2896`
- 5d: hit_rate `0.8333`, avg `0.0057`, median `0.0071`, brier `0.1535`, calibration_gap `-0.1229`
- 10d: hit_rate `0.8333`, avg `0.0131`, median `0.0166`, brier `0.1561`, calibration_gap `-0.1229`
- 20d: hit_rate `0.3333`, avg `0.0048`, median `-0.0053`, brier `0.3631`, calibration_gap `0.3771`
- 60d: hit_rate `0.3333`, avg `-0.0030`, median `-0.0413`, brier `0.3631`, calibration_gap `0.3771`

### top_20_confidence_signals
- sample_size: `12`
- 3d: hit_rate `0.6667`, avg `0.0026`, median `0.0102`, brier `0.2173`, calibration_gap `0.0343`
- 5d: hit_rate `0.6667`, avg `0.0015`, median `0.0028`, brier `0.2206`, calibration_gap `0.0343`
- 10d: hit_rate `0.7500`, avg `0.0068`, median `0.0113`, brier `0.1895`, calibration_gap `-0.0490`
- 20d: hit_rate `0.5833`, avg `0.0028`, median `0.0100`, brier `0.2617`, calibration_gap `0.1176`
- 60d: hit_rate `0.4167`, avg `-0.0063`, median `-0.0322`, brier `0.3243`, calibration_gap `0.2843`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6333`, avg `0.0053`, median `0.0096`, brier `0.2327`, calibration_gap `0.0392`
- 5d: hit_rate `0.5833`, avg `0.0046`, median `0.0051`, brier `0.2500`, calibration_gap `0.0892`
- 10d: hit_rate `0.6333`, avg `0.0081`, median `0.0109`, brier `0.2320`, calibration_gap `0.0392`
- 20d: hit_rate `0.6833`, avg `0.0148`, median `0.0151`, brier `0.2181`, calibration_gap `-0.0108`
- 60d: hit_rate `0.6833`, avg `0.0258`, median `0.0498`, brier `0.2215`, calibration_gap `-0.0108`

### low_confidence_reference
- sample_size: `12`
- 3d: hit_rate `0.6667`, avg `0.0069`, median `0.0048`, brier `0.2217`, calibration_gap `-0.0136`
- 5d: hit_rate `0.6667`, avg `0.0012`, median `0.0051`, brier `0.2212`, calibration_gap `-0.0136`
- 10d: hit_rate `0.5000`, avg `-0.0056`, median `-0.0022`, brier `0.2738`, calibration_gap `0.1530`
- 20d: hit_rate `0.5833`, avg `-0.0007`, median `0.0185`, brier `0.2487`, calibration_gap `0.0697`
- 60d: hit_rate `0.8333`, avg `0.0387`, median `0.0459`, brier `0.1714`, calibration_gap `-0.1803`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
