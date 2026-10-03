# High Confidence Edge Report

Generated at: `2026-10-03T00:51:16.804883+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `72`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `72`, gate `moderate_evidence`
- 5d: completed `72`, gate `moderate_evidence`
- 10d: completed `72`, gate `moderate_evidence`
- 20d: completed `72`, gate `moderate_evidence`
- 60d: completed `72`, gate `moderate_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005675`, median `0.012272`, mae `0.014584`
- 5d: sample `20`, hit `0.65`, avg `0.007865`, median `0.010241`, mae `0.017287`
- 10d: sample `20`, hit `0.7`, avg `0.011045`, median `0.015799`, mae `0.021637`
- 20d: sample `20`, hit `0.8`, avg `0.033933`, median `0.034704`, mae `0.037731`
- 60d: sample `20`, hit `0.9`, avg `0.084843`, median `0.109494`, mae `0.092956`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.004385`, median `-0.003676`, mae `0.01664`
- 5d: sample `60`, hit `0.4167`, avg `-0.002335`, median `-0.005632`, mae `0.018865`
- 10d: sample `60`, hit `0.5667`, avg `0.003123`, median `0.004196`, mae `0.023`
- 20d: sample `60`, hit `0.7167`, avg `0.020023`, median `0.029348`, mae `0.039903`
- 60d: sample `60`, hit `0.9`, avg `0.087007`, median `0.103071`, mae `0.094628`

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
- 3d: sample `8`, hit `0.75`, avg `0.005815`, median `0.012272`, mae `0.014511`
- 5d: sample `8`, hit `0.625`, avg `0.006695`, median `0.009709`, mae `0.016592`
- 10d: sample `8`, hit `0.75`, avg `0.009347`, median `0.013069`, mae `0.017068`
- 20d: sample `8`, hit `0.625`, avg `0.026788`, median `0.043456`, mae `0.034274`
- 60d: sample `8`, hit `1.0`, avg `0.114868`, median `0.119272`, mae `0.114868`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.005815`, median `0.012272`, mae `0.014511`
- 5d: sample `8`, hit `0.625`, avg `0.006695`, median `0.009709`, mae `0.016592`
- 10d: sample `8`, hit `0.75`, avg `0.009347`, median `0.013069`, mae `0.017068`
- 20d: sample `8`, hit `0.625`, avg `0.026788`, median `0.043456`, mae `0.034274`
- 60d: sample `8`, hit `1.0`, avg `0.114868`, median `0.119272`, mae `0.114868`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.005675, 'median_return': 0.012272, 'mean_absolute_return': 0.014584, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.025934}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.007865, 'median_return': 0.010241, 'mean_absolute_return': 0.017287, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.035399}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.011045, 'median_return': 0.015799, 'mean_absolute_return': 0.021637, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.05207}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.033933, 'median_return': 0.034704, 'mean_absolute_return': 0.037731, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.085531}, '60d': {'sample_size': 20, 'hit_rate': 0.9, 'avg_return': 0.084843, 'median_return': 0.109494, 'mean_absolute_return': 0.092956, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005815, 'median_return': 0.012272, 'mean_absolute_return': 0.014511, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006695, 'median_return': 0.009709, 'mean_absolute_return': 0.016592, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009347, 'median_return': 0.013069, 'mean_absolute_return': 0.017068, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026788, 'median_return': 0.043456, 'mean_absolute_return': 0.034274, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.114868, 'median_return': 0.119272, 'mean_absolute_return': 0.114868, 'max_adverse_excursion': 0.099512, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.002724, 'median_return': -0.002952, 'mean_absolute_return': 0.016305, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.000505, 'median_return': -0.002452, 'mean_absolute_return': 0.018679, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.004632, 'median_return': 0.004306, 'mean_absolute_return': 0.02328, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.023135, 'median_return': 0.031464, 'mean_absolute_return': 0.039925, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.8889, 'avg_return': 0.08331, 'median_return': 0.098199, 'mean_absolute_return': 0.091915, 'max_adverse_excursion': -0.099444, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.6}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.4125}, '60d': {'sample_size': 80, 'hit_rate': 0.3}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.175, 'both_hit': 13, 'both_miss': 7}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.125, 'both_hit': 13, 'both_miss': 7}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.1, 'both_hit': 14, 'both_miss': 6}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.325, 'both_hit': 16, 'both_miss': 4}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.9, 'primary_minus_secondary': -0.6, 'both_hit': 18, 'both_miss': 2}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.000638, 'median_return': 0.001405, 'mean_absolute_return': 0.015737, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.00185, 'median_return': 0.003789, 'mean_absolute_return': 0.018367, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.007298, 'median_return': 0.008464, 'mean_absolute_return': 0.019572, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.032685, 'median_return': 0.032299, 'mean_absolute_return': 0.037088, 'max_adverse_excursion': -0.026142, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.9, 'avg_return': 0.081218, 'median_return': 0.092194, 'mean_absolute_return': 0.088082, 'max_adverse_excursion': -0.078345, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.009395, 'median_return': -0.010335, 'mean_absolute_return': 0.017291, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.00469, 'median_return': -0.005632, 'mean_absolute_return': 0.01878, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.001478, 'median_return': -0.001818, 'mean_absolute_return': 0.031921, 'max_adverse_excursion': -0.053986, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.004054, 'median_return': 0.017648, 'mean_absolute_return': 0.046174, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.067793}, '60d': {'sample_size': 20, 'hit_rate': 0.9, 'avg_return': 0.10221, 'median_return': 0.114377, 'mean_absolute_return': 0.112594, 'max_adverse_excursion': -0.099444, 'max_favorable_excursion': 0.176653}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.00187`, median `-0.001591`, mae `0.016126`
- 5d: sample `80`, hit `0.475`, avg `0.000215`, median `-0.001129`, mae `0.01847`
- 10d: sample `80`, hit `0.6`, avg `0.005104`, median `0.005356`, mae `0.022659`
- 20d: sample `80`, hit `0.7375`, avg `0.0235`, median `0.031464`, mae `0.03936`
- 60d: sample `80`, hit `0.9`, avg `0.086466`, median `0.103071`, mae `0.09421`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005675`, median `0.012272`, mae `0.014584`
- 5d: sample `20`, hit `0.65`, avg `0.007865`, median `0.010241`, mae `0.017287`
- 10d: sample `20`, hit `0.7`, avg `0.011045`, median `0.015799`, mae `0.021637`
- 20d: sample `20`, hit `0.8`, avg `0.033933`, median `0.034704`, mae `0.037731`
- 60d: sample `20`, hit `0.9`, avg `0.084843`, median `0.109494`, mae `0.092956`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.001339`, median `0.003757`, mae `0.017801`
- 5d: sample `40`, hit `0.5`, avg `0.002841`, median `0.003789`, mae `0.020612`
- 10d: sample `40`, hit `0.6`, avg `0.008382`, median `0.011031`, mae `0.021999`
- 20d: sample `40`, hit `0.825`, avg `0.033771`, median `0.031464`, mae `0.036899`
- 60d: sample `40`, hit `0.875`, avg `0.074126`, median `0.085781`, mae `0.083382`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005675`, median `0.012272`, mae `0.014584`
- 5d: sample `20`, hit `0.65`, avg `0.007865`, median `0.010241`, mae `0.017287`
- 10d: sample `20`, hit `0.7`, avg `0.011045`, median `0.015799`, mae `0.021637`
- 20d: sample `20`, hit `0.8`, avg `0.033933`, median `0.034704`, mae `0.037731`
- 60d: sample `20`, hit `0.9`, avg `0.084843`, median `0.109494`, mae `0.092956`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.004385`, median `-0.003676`, mae `0.01664`
- 5d: sample `60`, hit `0.4167`, avg `-0.002335`, median `-0.005632`, mae `0.018865`
- 10d: sample `60`, hit `0.5667`, avg `0.003123`, median `0.004196`, mae `0.023`
- 20d: sample `60`, hit `0.7167`, avg `0.020023`, median `0.029348`, mae `0.039903`
- 60d: sample `60`, hit `0.9`, avg `0.087007`, median `0.103071`, mae `0.094628`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

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
- 3d: sample `80`, hit `0.45`, avg `-0.00187`, median `-0.001591`, mae `0.016126`
- 5d: sample `80`, hit `0.475`, avg `0.000215`, median `-0.001129`, mae `0.01847`
- 10d: sample `80`, hit `0.6`, avg `0.005104`, median `0.005356`, mae `0.022659`
- 20d: sample `80`, hit `0.7375`, avg `0.0235`, median `0.031464`, mae `0.03936`
- 60d: sample `80`, hit `0.9`, avg `0.086466`, median `0.103071`, mae `0.09421`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005675`, median `0.012272`, mae `0.014584`
- 5d: sample `20`, hit `0.65`, avg `0.007865`, median `0.010241`, mae `0.017287`
- 10d: sample `20`, hit `0.7`, avg `0.011045`, median `0.015799`, mae `0.021637`
- 20d: sample `20`, hit `0.8`, avg `0.033933`, median `0.034704`, mae `0.037731`
- 60d: sample `20`, hit `0.9`, avg `0.084843`, median `0.109494`, mae `0.092956`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.00187`, median `-0.001591`, mae `0.016126`
- 5d: sample `80`, hit `0.475`, avg `0.000215`, median `-0.001129`, mae `0.01847`
- 10d: sample `80`, hit `0.6`, avg `0.005104`, median `0.005356`, mae `0.022659`
- 20d: sample `80`, hit `0.7375`, avg `0.0235`, median `0.031464`, mae `0.03936`
- 60d: sample `80`, hit `0.9`, avg `0.086466`, median `0.103071`, mae `0.09421`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005675`, median `0.012272`, mae `0.014584`
- 5d: sample `20`, hit `0.65`, avg `0.007865`, median `0.010241`, mae `0.017287`
- 10d: sample `20`, hit `0.7`, avg `0.011045`, median `0.015799`, mae `0.021637`
- 20d: sample `20`, hit `0.8`, avg `0.033933`, median `0.034704`, mae `0.037731`
- 60d: sample `20`, hit `0.9`, avg `0.084843`, median `0.109494`, mae `0.092956`

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
