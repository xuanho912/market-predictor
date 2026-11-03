# High Confidence Edge Report

Generated at: `2026-11-03T11:22:52.687584+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `156`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `156`, gate `stronger_evidence`
- 5d: completed `156`, gate `stronger_evidence`
- 10d: completed `156`, gate `stronger_evidence`
- 20d: completed `156`, gate `stronger_evidence`
- 60d: completed `156`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `0.001272`, median `0.000543`, mae `0.020083`
- 5d: sample `80`, hit `0.55`, avg `0.00424`, median `0.006712`, mae `0.024655`
- 10d: sample `80`, hit `0.65`, avg `0.012919`, median `0.020244`, mae `0.035584`
- 20d: sample `80`, hit `0.725`, avg `0.027945`, median `0.038532`, mae `0.048853`
- 60d: sample `80`, hit `0.775`, avg `0.043598`, median `0.059406`, mae `0.063032`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.003696`, median `0.011103`, mae `0.012649`
- 5d: sample `8`, hit `0.625`, avg `0.007888`, median `0.011065`, mae `0.018802`
- 10d: sample `8`, hit `0.5`, avg `0.004186`, median `0.006878`, mae `0.030417`
- 20d: sample `8`, hit `0.75`, avg `0.027756`, median `0.038512`, mae `0.039017`
- 60d: sample `8`, hit `0.75`, avg `0.037654`, median `0.057501`, mae `0.055851`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.005367`, median `0.004243`, mae `0.017885`
- 5d: sample `8`, hit `0.5`, avg `0.01014`, median `0.013109`, mae `0.019127`
- 10d: sample `8`, hit `0.625`, avg `0.02204`, median `0.031247`, mae `0.033055`
- 20d: sample `8`, hit `0.875`, avg `0.040835`, median `0.062122`, mae `0.043216`
- 60d: sample `8`, hit `1.0`, avg `0.082097`, median `0.095045`, mae `0.082097`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.005367, 'median_return': 0.004243, 'mean_absolute_return': 0.017885, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.01014, 'median_return': 0.013109, 'mean_absolute_return': 0.019127, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.02204, 'median_return': 0.031247, 'mean_absolute_return': 0.033055, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.040835, 'median_return': 0.062122, 'mean_absolute_return': 0.043216, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.082097, 'median_return': 0.095045, 'mean_absolute_return': 0.082097, 'max_adverse_excursion': 0.054522, 'max_favorable_excursion': 0.105209}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.000817, 'median_return': 0.000543, 'mean_absolute_return': 0.020328, 'max_adverse_excursion': -0.083956, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.003584, 'median_return': 0.006712, 'mean_absolute_return': 0.025269, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.011905, 'median_return': 0.019449, 'mean_absolute_return': 0.035865, 'max_adverse_excursion': -0.124781, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.026513, 'median_return': 0.038532, 'mean_absolute_return': 0.049479, 'max_adverse_excursion': -0.133308, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.03932, 'median_return': 0.05488, 'mean_absolute_return': 0.060913, 'max_adverse_excursion': -0.121297, 'max_favorable_excursion': 0.179244}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.4}, '20d': {'sample_size': 80, 'hit_rate': 0.375}, '60d': {'sample_size': 80, 'hit_rate': 0.35}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.003804, 'median_return': 0.004243, 'mean_absolute_return': 0.017212, 'max_adverse_excursion': -0.03272, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.006382, 'median_return': 0.006712, 'mean_absolute_return': 0.019887, 'max_adverse_excursion': -0.0363, 'max_favorable_excursion': 0.044138}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.014765, 'median_return': 0.017689, 'mean_absolute_return': 0.030733, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.076904}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.028761, 'median_return': 0.030239, 'mean_absolute_return': 0.041763, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.085922}, '60d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.054565, 'median_return': 0.068046, 'mean_absolute_return': 0.065713, 'max_adverse_excursion': -0.076188, 'max_favorable_excursion': 0.135454}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.001259, 'median_return': 0.000543, 'mean_absolute_return': 0.022955, 'max_adverse_excursion': -0.083956, 'max_favorable_excursion': 0.047232}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.002097, 'median_return': 0.009101, 'mean_absolute_return': 0.029423, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.011072, 'median_return': 0.023772, 'mean_absolute_return': 0.040435, 'max_adverse_excursion': -0.124781, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.02713, 'median_return': 0.041918, 'mean_absolute_return': 0.055942, 'max_adverse_excursion': -0.133308, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.03263, 'median_return': 0.043979, 'mean_absolute_return': 0.06035, 'max_adverse_excursion': -0.121297, 'max_favorable_excursion': 0.179244}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `0.001522`, median `-0.000627`, mae `0.018638`
- 5d: sample `60`, hit `0.55`, avg `0.002414`, median `0.007479`, mae `0.023861`
- 10d: sample `60`, hit `0.6333`, avg `0.010263`, median `0.011727`, mae `0.033973`
- 20d: sample `60`, hit `0.6833`, avg `0.02278`, median `0.030239`, mae `0.046988`
- 60d: sample `60`, hit `0.75`, avg `0.04225`, median `0.056005`, mae `0.062796`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.000522`, median `0.001471`, mae `0.02442`
- 5d: sample `20`, hit `0.55`, avg `0.009718`, median `0.004752`, mae `0.027037`
- 10d: sample `20`, hit `0.7`, avg `0.020885`, median `0.032111`, mae `0.040417`
- 20d: sample `20`, hit `0.85`, avg `0.043442`, median `0.052608`, mae `0.054445`
- 60d: sample `20`, hit `0.85`, avg `0.047641`, median `0.068113`, mae `0.06374`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.001304`, median `0.006321`, mae `0.015844`
- 5d: sample `20`, hit `0.55`, avg `0.004863`, median `0.006712`, mae `0.019176`
- 10d: sample `20`, hit `0.6`, avg `0.010589`, median `0.014227`, mae `0.02903`
- 20d: sample `20`, hit `0.7`, avg `0.023793`, median `0.030239`, mae `0.040258`
- 60d: sample `20`, hit `0.75`, avg `0.035424`, median `0.052632`, mae `0.056705`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.001304`, median `0.006321`, mae `0.015844`
- 5d: sample `20`, hit `0.55`, avg `0.004863`, median `0.006712`, mae `0.019176`
- 10d: sample `20`, hit `0.6`, avg `0.010589`, median `0.014227`, mae `0.02903`
- 20d: sample `20`, hit `0.7`, avg `0.023793`, median `0.030239`, mae `0.040258`
- 60d: sample `20`, hit `0.75`, avg `0.035424`, median `0.052632`, mae `0.056705`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.000522`, median `0.001471`, mae `0.02442`
- 5d: sample `20`, hit `0.55`, avg `0.009718`, median `0.004752`, mae `0.027037`
- 10d: sample `20`, hit `0.7`, avg `0.020885`, median `0.032111`, mae `0.040417`
- 20d: sample `20`, hit `0.85`, avg `0.043442`, median `0.052608`, mae `0.054445`
- 60d: sample `20`, hit `0.85`, avg `0.047641`, median `0.068113`, mae `0.06374`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.003804`, median `0.004243`, mae `0.017212`
- 5d: sample `40`, hit `0.525`, avg `0.006382`, median `0.006712`, mae `0.019887`
- 10d: sample `40`, hit `0.6`, avg `0.014765`, median `0.017689`, mae `0.030733`
- 20d: sample `40`, hit `0.75`, avg `0.028761`, median `0.030239`, mae `0.041763`
- 60d: sample `40`, hit `0.85`, avg `0.054565`, median `0.068046`, mae `0.065713`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.003041`, median `-0.000627`, mae `0.02149`
- 5d: sample `20`, hit `0.6`, avg `-0.005524`, median `0.00982`, mae `0.031809`
- 10d: sample `20`, hit `0.7`, avg `0.001258`, median `0.011431`, mae `0.040454`
- 20d: sample `20`, hit `0.55`, avg `0.010818`, median `0.034842`, mae `0.057439`
- 60d: sample `20`, hit `0.55`, avg `0.01762`, median `0.01956`, mae `0.056961`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.001304`, median `0.006321`, mae `0.015844`
- 5d: sample `20`, hit `0.55`, avg `0.004863`, median `0.006712`, mae `0.019176`
- 10d: sample `20`, hit `0.6`, avg `0.010589`, median `0.014227`, mae `0.02903`
- 20d: sample `20`, hit `0.7`, avg `0.023793`, median `0.030239`, mae `0.040258`
- 60d: sample `20`, hit `0.75`, avg `0.035424`, median `0.052632`, mae `0.056705`

### bounce_surface_only
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `0.001272`, median `0.000543`, mae `0.020083`
- 5d: sample `80`, hit `0.55`, avg `0.00424`, median `0.006712`, mae `0.024655`
- 10d: sample `80`, hit `0.65`, avg `0.012919`, median `0.020244`, mae `0.035584`
- 20d: sample `80`, hit `0.725`, avg `0.027945`, median `0.038532`, mae `0.048853`
- 60d: sample `80`, hit `0.775`, avg `0.043598`, median `0.059406`, mae `0.063032`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `0.001272`, median `0.000543`, mae `0.020083`
- 5d: sample `80`, hit `0.55`, avg `0.00424`, median `0.006712`, mae `0.024655`
- 10d: sample `80`, hit `0.65`, avg `0.012919`, median `0.020244`, mae `0.035584`
- 20d: sample `80`, hit `0.725`, avg `0.027945`, median `0.038532`, mae `0.048853`
- 60d: sample `80`, hit `0.775`, avg `0.043598`, median `0.059406`, mae `0.063032`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.001304`, median `0.006321`, mae `0.015844`
- 5d: sample `20`, hit `0.55`, avg `0.004863`, median `0.006712`, mae `0.019176`
- 10d: sample `20`, hit `0.6`, avg `0.010589`, median `0.014227`, mae `0.02903`
- 20d: sample `20`, hit `0.7`, avg `0.023793`, median `0.030239`, mae `0.040258`
- 60d: sample `20`, hit `0.75`, avg `0.035424`, median `0.052632`, mae `0.056705`

### bounce_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.001304`, median `0.006321`, mae `0.015844`
- 5d: sample `20`, hit `0.55`, avg `0.004863`, median `0.006712`, mae `0.019176`
- 10d: sample `20`, hit `0.6`, avg `0.010589`, median `0.014227`, mae `0.02903`
- 20d: sample `20`, hit `0.7`, avg `0.023793`, median `0.030239`, mae `0.040258`
- 60d: sample `20`, hit `0.75`, avg `0.035424`, median `0.052632`, mae `0.056705`

### risk_path_with_flow_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `0.001272`, median `0.000543`, mae `0.020083`
- 5d: sample `80`, hit `0.55`, avg `0.00424`, median `0.006712`, mae `0.024655`
- 10d: sample `80`, hit `0.65`, avg `0.012919`, median `0.020244`, mae `0.035584`
- 20d: sample `80`, hit `0.725`, avg `0.027945`, median `0.038532`, mae `0.048853`
- 60d: sample `80`, hit `0.775`, avg `0.043598`, median `0.059406`, mae `0.063032`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
