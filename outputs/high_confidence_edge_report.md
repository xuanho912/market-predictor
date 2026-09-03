# High Confidence Edge Report

Generated at: `2026-09-03T23:35:42.890862+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `0`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `0`, gate `insufficient`
- 5d: completed `0`, gate `insufficient`
- 10d: completed `0`, gate `insufficient`
- 20d: completed `0`, gate `insufficient`
- 60d: completed `0`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.000367`, median `0.003026`, mae `0.015337`
- 5d: sample `60`, hit `0.55`, avg `0.001758`, median `0.00297`, mae `0.018122`
- 10d: sample `60`, hit `0.4833`, avg `0.002213`, median `-0.0004`, mae `0.023181`
- 20d: sample `60`, hit `0.7`, avg `0.013393`, median `0.023981`, mae `0.032465`
- 60d: sample `60`, hit `0.7667`, avg `0.036219`, median `0.053843`, mae `0.072041`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.003162`, median `-0.001428`, mae `0.008254`
- 5d: sample `20`, hit `0.6`, avg `-0.001804`, median `0.000873`, mae `0.009499`
- 10d: sample `20`, hit `0.15`, avg `-0.014486`, median `-0.016376`, mae `0.021428`
- 20d: sample `20`, hit `0.25`, avg `-0.027969`, median `-0.016058`, mae `0.03994`
- 60d: sample `20`, hit `0.3`, avg `-0.016448`, median `-0.020815`, mae `0.054451`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.007591`, median `0.00234`, mae `0.013736`
- 5d: sample `8`, hit `0.375`, avg `-0.01205`, median `-0.012956`, mae `0.019755`
- 10d: sample `8`, hit `0.5`, avg `0.000185`, median `0.0076`, mae `0.019465`
- 20d: sample `8`, hit `0.875`, avg `0.012354`, median `0.026531`, mae `0.026179`
- 60d: sample `8`, hit `0.75`, avg `0.03306`, median `0.046132`, mae `0.05231`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.007591`, median `0.00234`, mae `0.013736`
- 5d: sample `8`, hit `0.375`, avg `-0.01205`, median `-0.012956`, mae `0.019755`
- 10d: sample `8`, hit `0.5`, avg `0.000185`, median `0.0076`, mae `0.019465`
- 20d: sample `8`, hit `0.875`, avg `0.012354`, median `0.026531`, mae `0.026179`
- 60d: sample `8`, hit `0.75`, avg `0.03306`, median `0.046132`, mae `0.05231`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.000367, 'median_return': 0.003026, 'mean_absolute_return': 0.015337, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.001758, 'median_return': 0.00297, 'mean_absolute_return': 0.018122, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': 0.002213, 'median_return': -0.0004, 'mean_absolute_return': 0.023181, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.013393, 'median_return': 0.023981, 'mean_absolute_return': 0.032465, 'max_adverse_excursion': -0.090764, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.036219, 'median_return': 0.053843, 'mean_absolute_return': 0.072041, 'max_adverse_excursion': -0.171176, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.007591, 'median_return': 0.00234, 'mean_absolute_return': 0.013736, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.01205, 'median_return': -0.012956, 'mean_absolute_return': 0.019755, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.000185, 'median_return': 0.0076, 'mean_absolute_return': 0.019465, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.012354, 'median_return': 0.026531, 'mean_absolute_return': 0.026179, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.03306, 'median_return': 0.046132, 'mean_absolute_return': 0.05231, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000271, 'median_return': 0.000707, 'mean_absolute_return': 0.013548, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.002303, 'median_return': 0.001303, 'mean_absolute_return': 0.015545, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.0022, 'median_return': -0.010327, 'mean_absolute_return': 0.023107, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.002019, 'median_return': 0.007004, 'mean_absolute_return': 0.03524, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.02194, 'median_return': 0.037781, 'mean_absolute_return': 0.069347, 'max_adverse_excursion': -0.171176, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.4625}, '60d': {'sample_size': 80, 'hit_rate': 0.425}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.000367, 'median_return': 0.003026, 'mean_absolute_return': 0.015337, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.001758, 'median_return': 0.00297, 'mean_absolute_return': 0.018122, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': 0.002213, 'median_return': -0.0004, 'mean_absolute_return': 0.023181, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.013393, 'median_return': 0.023981, 'mean_absolute_return': 0.032465, 'max_adverse_excursion': -0.090764, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.036219, 'median_return': 0.053843, 'mean_absolute_return': 0.072041, 'max_adverse_excursion': -0.171176, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.003162, 'median_return': -0.001428, 'mean_absolute_return': 0.008254, 'max_adverse_excursion': -0.024978, 'max_favorable_excursion': 0.011487}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.001804, 'median_return': 0.000873, 'mean_absolute_return': 0.009499, 'max_adverse_excursion': -0.035525, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 20, 'hit_rate': 0.15, 'avg_return': -0.014486, 'median_return': -0.016376, 'mean_absolute_return': 0.021428, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.031945}, '20d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.027969, 'median_return': -0.016058, 'mean_absolute_return': 0.03994, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.039296}, '60d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.016448, 'median_return': -0.020815, 'mean_absolute_return': 0.054451, 'max_adverse_excursion': -0.090808, 'max_favorable_excursion': 0.085951}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.000794`, median `0.000603`, mae `0.013225`
- 5d: sample `60`, hit `0.5333`, avg `-0.000848`, median `0.000688`, mae `0.014779`
- 10d: sample `60`, hit `0.3667`, avg `-0.002292`, median `-0.007491`, mae `0.022628`
- 20d: sample `60`, hit `0.5833`, avg `0.002962`, median `0.012958`, mae `0.033787`
- 60d: sample `60`, hit `0.65`, avg `0.028256`, median `0.049712`, mae `0.06712`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.000391`, median `0.003412`, mae `0.015711`
- 5d: sample `40`, hit `0.5`, avg `-0.00037`, median `0.000208`, mae `0.01742`
- 10d: sample `40`, hit `0.475`, avg `0.003805`, median `-0.0004`, mae `0.023228`
- 20d: sample `40`, hit `0.75`, avg `0.018428`, median `0.026531`, mae `0.03071`
- 60d: sample `40`, hit `0.825`, avg `0.050608`, median `0.064104`, mae `0.073455`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.000321`, median `0.003026`, mae `0.01459`
- 5d: sample `20`, hit `0.65`, avg `0.006015`, median `0.008039`, mae `0.019527`
- 10d: sample `20`, hit `0.5`, avg `-0.00097`, median `0.000655`, mae `0.023087`
- 20d: sample `20`, hit `0.6`, avg `0.003322`, median `0.013877`, mae `0.035976`
- 60d: sample `20`, hit `0.65`, avg `0.007439`, median `0.03104`, mae `0.069211`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.000794`, median `0.000603`, mae `0.013225`
- 5d: sample `60`, hit `0.5333`, avg `-0.000848`, median `0.000688`, mae `0.014779`
- 10d: sample `60`, hit `0.3667`, avg `-0.002292`, median `-0.007491`, mae `0.022628`
- 20d: sample `60`, hit `0.5833`, avg `0.002962`, median `0.012958`, mae `0.033787`
- 60d: sample `60`, hit `0.65`, avg `0.028256`, median `0.049712`, mae `0.06712`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

### aligned_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### mixed_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `-0.000515`, median `0.000766`, mae `0.013566`
- 5d: sample `80`, hit `0.5625`, avg `0.000868`, median `0.001239`, mae `0.015966`
- 10d: sample `80`, hit `0.4`, avg `-0.001961`, median `-0.007491`, mae `0.022743`
- 20d: sample `80`, hit `0.5875`, avg `0.003052`, median `0.012958`, mae `0.034334`
- 60d: sample `80`, hit `0.65`, avg `0.023052`, median `0.037781`, mae `0.067643`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.000321`, median `0.003026`, mae `0.01459`
- 5d: sample `20`, hit `0.65`, avg `0.006015`, median `0.008039`, mae `0.019527`
- 10d: sample `20`, hit `0.5`, avg `-0.00097`, median `0.000655`, mae `0.023087`
- 20d: sample `20`, hit `0.6`, avg `0.003322`, median `0.013877`, mae `0.035976`
- 60d: sample `20`, hit `0.65`, avg `0.007439`, median `0.03104`, mae `0.069211`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.003422`, median `-0.001428`, mae `0.01078`
- 5d: sample `40`, hit `0.55`, avg `-0.004249`, median `0.000688`, mae `0.01165`
- 10d: sample `40`, hit `0.25`, avg `-0.008127`, median `-0.013317`, mae `0.020047`
- 20d: sample `40`, hit `0.5`, avg `-0.004967`, median `0.000213`, mae `0.037786`
- 60d: sample `40`, hit `0.525`, avg `0.015224`, median `0.029831`, mae `0.065853`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### risk_path_with_flow_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
