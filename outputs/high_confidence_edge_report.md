# High Confidence Edge Report

Generated at: `2026-10-01T00:56:23.618116+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `64`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `64`, gate `moderate_evidence`
- 5d: completed `64`, gate `moderate_evidence`
- 10d: completed `64`, gate `moderate_evidence`
- 20d: completed `64`, gate `moderate_evidence`
- 60d: completed `64`, gate `moderate_evidence`

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
- 3d: sample `60`, hit `0.4167`, avg `-0.003515`, median `-0.002952`, mae `0.017023`
- 5d: sample `60`, hit `0.4333`, avg `-0.001444`, median `-0.005632`, mae `0.019116`
- 10d: sample `60`, hit `0.5833`, avg `0.003584`, median `0.004306`, mae `0.025437`
- 20d: sample `60`, hit `0.75`, avg `0.026259`, median `0.033164`, mae `0.043963`
- 60d: sample `60`, hit `0.9`, avg `0.091962`, median `0.108121`, mae `0.099115`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.005675, 'median_return': 0.012272, 'mean_absolute_return': 0.014584, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.025934}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.007865, 'median_return': 0.010241, 'mean_absolute_return': 0.017287, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.035399}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.011045, 'median_return': 0.015799, 'mean_absolute_return': 0.021637, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.05207}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.033933, 'median_return': 0.034704, 'mean_absolute_return': 0.037731, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.085531}, '60d': {'sample_size': 20, 'hit_rate': 0.9, 'avg_return': 0.084843, 'median_return': 0.109494, 'mean_absolute_return': 0.092956, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005815, 'median_return': 0.012272, 'mean_absolute_return': 0.014511, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006695, 'median_return': 0.009709, 'mean_absolute_return': 0.016592, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009347, 'median_return': 0.013069, 'mean_absolute_return': 0.017068, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026788, 'median_return': 0.043456, 'mean_absolute_return': 0.034274, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.114868, 'median_return': 0.119272, 'mean_absolute_return': 0.114868, 'max_adverse_excursion': 0.099512, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.001999, 'median_return': -0.001591, 'mean_absolute_return': 0.016624, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.000238, 'median_return': -0.002452, 'mean_absolute_return': 0.018888, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.005016, 'median_return': 0.005356, 'mean_absolute_return': 0.025312, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.028332, 'median_return': 0.033164, 'mean_absolute_return': 0.043309, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.8889, 'avg_return': 0.087439, 'median_return': 0.103071, 'mean_absolute_return': 0.095654, 'max_adverse_excursion': -0.085385, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.3875}, '20d': {'sample_size': 80, 'hit_rate': 0.2375}, '60d': {'sample_size': 80, 'hit_rate': 0.1}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': -0.525, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.1, 'secondary_hit_rate': 0.9, 'primary_minus_secondary': -0.8, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.002969, 'median_return': 0.004815, 'mean_absolute_return': 0.013488, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.025934}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.003947, 'median_return': 0.006609, 'mean_absolute_return': 0.015347, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.035399}, '10d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.009233, 'median_return': 0.011031, 'mean_absolute_return': 0.019271, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.05207}, '20d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.036903, 'median_return': 0.039296, 'mean_absolute_return': 0.040244, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.085531}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.090629, 'median_return': 0.108121, 'mean_absolute_return': 0.095726, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.005404, 'median_return': -0.009843, 'mean_absolute_return': 0.019337, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.00218, 'median_return': -0.00693, 'mean_absolute_return': 0.02197, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.001666, 'median_return': -0.001818, 'mean_absolute_return': 0.029704, 'max_adverse_excursion': -0.053986, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.019452, 'median_return': 0.026005, 'mean_absolute_return': 0.044567, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.089735, 'median_return': 0.11278, 'mean_absolute_return': 0.099424, 'max_adverse_excursion': -0.085385, 'max_favorable_excursion': 0.192595}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.475`, avg `-0.001217`, median `-0.001058`, mae `0.016413`
- 5d: sample `80`, hit `0.4875`, avg `0.000884`, median `-0.000402`, mae `0.018658`
- 10d: sample `80`, hit `0.6125`, avg `0.005449`, median `0.007751`, mae `0.024487`
- 20d: sample `80`, hit `0.7625`, avg `0.028177`, median `0.033164`, mae `0.042405`
- 60d: sample `80`, hit `0.9`, avg `0.090182`, median `0.108121`, mae `0.097575`

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
- 3d: sample `40`, hit `0.6`, avg `0.002969`, median `0.004815`, mae `0.013488`
- 5d: sample `40`, hit `0.6`, avg `0.003947`, median `0.006609`, mae `0.015347`
- 10d: sample `40`, hit `0.75`, avg `0.009233`, median `0.011031`, mae `0.019271`
- 20d: sample `40`, hit `0.85`, avg `0.036903`, median `0.039296`, mae `0.040244`
- 60d: sample `40`, hit `0.925`, avg `0.090629`, median `0.108121`, mae `0.095726`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.475`, avg `-0.001217`, median `-0.001058`, mae `0.016413`
- 5d: sample `80`, hit `0.4875`, avg `0.000884`, median `-0.000402`, mae `0.018658`
- 10d: sample `80`, hit `0.6125`, avg `0.005449`, median `0.007751`, mae `0.024487`
- 20d: sample `80`, hit `0.7625`, avg `0.028177`, median `0.033164`, mae `0.042405`
- 60d: sample `80`, hit `0.9`, avg `0.090182`, median `0.108121`, mae `0.097575`

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
- 3d: sample `80`, hit `0.475`, avg `-0.001217`, median `-0.001058`, mae `0.016413`
- 5d: sample `80`, hit `0.4875`, avg `0.000884`, median `-0.000402`, mae `0.018658`
- 10d: sample `80`, hit `0.6125`, avg `0.005449`, median `0.007751`, mae `0.024487`
- 20d: sample `80`, hit `0.7625`, avg `0.028177`, median `0.033164`, mae `0.042405`
- 60d: sample `80`, hit `0.9`, avg `0.090182`, median `0.108121`, mae `0.097575`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- 3d: sample `80`, hit `0.475`, avg `-0.001217`, median `-0.001058`, mae `0.016413`
- 5d: sample `80`, hit `0.4875`, avg `0.000884`, median `-0.000402`, mae `0.018658`
- 10d: sample `80`, hit `0.6125`, avg `0.005449`, median `0.007751`, mae `0.024487`
- 20d: sample `80`, hit `0.7625`, avg `0.028177`, median `0.033164`, mae `0.042405`
- 60d: sample `80`, hit `0.9`, avg `0.090182`, median `0.108121`, mae `0.097575`

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
