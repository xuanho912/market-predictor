# High Confidence Edge Report

Generated at: `2026-09-29T00:40:24.425903+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `56`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `56`, gate `moderate_evidence`
- 5d: completed `56`, gate `moderate_evidence`
- 10d: completed `56`, gate `moderate_evidence`
- 20d: completed `56`, gate `moderate_evidence`
- 60d: completed `56`, gate `moderate_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000676`, median `0.001405`, mae `0.012752`
- 5d: sample `40`, hit `0.6`, avg `0.003522`, median `0.004597`, mae `0.014327`
- 10d: sample `40`, hit `0.75`, avg `0.009875`, median `0.011619`, mae `0.018355`
- 20d: sample `40`, hit `0.8`, avg `0.032933`, median `0.039296`, mae `0.038308`
- 60d: sample `40`, hit `0.925`, avg `0.09103`, median `0.108121`, mae `0.096127`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001666`, median `-0.001227`, mae `0.018827`
- 5d: sample `20`, hit `0.35`, avg `-0.003174`, median `-0.009444`, mae `0.020339`
- 10d: sample `20`, hit `0.55`, avg `0.00692`, median `0.003921`, mae `0.019231`
- 20d: sample `20`, hit `0.85`, avg `0.027599`, median `0.027885`, mae `0.030057`
- 60d: sample `20`, hit `0.8`, avg `0.047285`, median `0.04207`, mae `0.065041`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.004198`, median `-0.002952`, mae `0.015237`
- 5d: sample `20`, hit `0.4`, avg `-0.001176`, median `-0.002452`, mae `0.015907`
- 10d: sample `20`, hit `0.45`, avg `-0.001015`, median `-0.001818`, mae `0.031458`
- 20d: sample `20`, hit `0.5`, avg `-0.005845`, median `0.008613`, mae `0.047061`
- 60d: sample `20`, hit `0.95`, avg `0.111208`, median `0.115975`, mae `0.115851`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.000676, 'median_return': 0.001405, 'mean_absolute_return': 0.012752, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.025934}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.003522, 'median_return': 0.004597, 'mean_absolute_return': 0.014327, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.030717}, '10d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.009875, 'median_return': 0.011619, 'mean_absolute_return': 0.018355, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.039009}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.032933, 'median_return': 0.039296, 'mean_absolute_return': 0.038308, 'max_adverse_excursion': -0.026142, 'max_favorable_excursion': 0.088842}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.09103, 'median_return': 0.108121, 'mean_absolute_return': 0.096127, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005815, 'median_return': 0.012272, 'mean_absolute_return': 0.014511, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006695, 'median_return': 0.009709, 'mean_absolute_return': 0.016592, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009347, 'median_return': 0.013069, 'mean_absolute_return': 0.017068, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026788, 'median_return': 0.043456, 'mean_absolute_return': 0.034274, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.114868, 'median_return': 0.119272, 'mean_absolute_return': 0.114868, 'max_adverse_excursion': 0.099512, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.0019, 'median_return': -0.002225, 'mean_absolute_return': 0.014934, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 4e-06, 'median_return': -0.001129, 'mean_absolute_return': 0.016184, 'max_adverse_excursion': -0.035083, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.006088, 'median_return': 0.008464, 'mean_absolute_return': 0.022381, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.021362, 'median_return': 0.031464, 'mean_absolute_return': 0.038896, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.088842}, '60d': {'sample_size': 72, 'hit_rate': 0.8889, 'avg_return': 0.081835, 'median_return': 0.099883, 'mean_absolute_return': 0.090889, 'max_adverse_excursion': -0.078345, 'max_favorable_excursion': 0.176653}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5375}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.375}, '20d': {'sample_size': 80, 'hit_rate': 0.2625}, '60d': {'sample_size': 80, 'hit_rate': 0.1}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.475, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.1, 'secondary_hit_rate': 0.9, 'primary_minus_secondary': -0.8, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.000676, 'median_return': 0.001405, 'mean_absolute_return': 0.012752, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.025934}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.003522, 'median_return': 0.004597, 'mean_absolute_return': 0.014327, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.030717}, '10d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.009875, 'median_return': 0.011619, 'mean_absolute_return': 0.018355, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.039009}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.032933, 'median_return': 0.039296, 'mean_absolute_return': 0.038308, 'max_adverse_excursion': -0.026142, 'max_favorable_excursion': 0.088842}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.09103, 'median_return': 0.108121, 'mean_absolute_return': 0.096127, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.002932, 'median_return': -0.002952, 'mean_absolute_return': 0.017032, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.002175, 'median_return': -0.005796, 'mean_absolute_return': 0.018123, 'max_adverse_excursion': -0.035083, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.002953, 'median_return': 0.003262, 'mean_absolute_return': 0.025344, 'max_adverse_excursion': -0.053986, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.010877, 'median_return': 0.025198, 'mean_absolute_return': 0.038559, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.072294}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.079247, 'median_return': 0.098256, 'mean_absolute_return': 0.090446, 'max_adverse_excursion': -0.078345, 'max_favorable_excursion': 0.176653}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000676`, median `0.001405`, mae `0.012752`
- 5d: sample `40`, hit `0.6`, avg `0.003522`, median `0.004597`, mae `0.014327`
- 10d: sample `40`, hit `0.75`, avg `0.009875`, median `0.011619`, mae `0.018355`
- 20d: sample `40`, hit `0.8`, avg `0.032933`, median `0.039296`, mae `0.038308`
- 60d: sample `40`, hit `0.925`, avg `0.09103`, median `0.108121`, mae `0.096127`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.002932`, median `-0.002952`, mae `0.017032`
- 5d: sample `40`, hit `0.375`, avg `-0.002175`, median `-0.005796`, mae `0.018123`
- 10d: sample `40`, hit `0.5`, avg `0.002953`, median `0.003262`, mae `0.025344`
- 20d: sample `40`, hit `0.675`, avg `0.010877`, median `0.025198`, mae `0.038559`
- 60d: sample `40`, hit `0.875`, avg `0.079247`, median `0.098256`, mae `0.090446`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000676`, median `0.001405`, mae `0.012752`
- 5d: sample `40`, hit `0.6`, avg `0.003522`, median `0.004597`, mae `0.014327`
- 10d: sample `40`, hit `0.75`, avg `0.009875`, median `0.011619`, mae `0.018355`
- 20d: sample `40`, hit `0.8`, avg `0.032933`, median `0.039296`, mae `0.038308`
- 60d: sample `40`, hit `0.925`, avg `0.09103`, median `0.108121`, mae `0.096127`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000676`, median `0.001405`, mae `0.012752`
- 5d: sample `40`, hit `0.6`, avg `0.003522`, median `0.004597`, mae `0.014327`
- 10d: sample `40`, hit `0.75`, avg `0.009875`, median `0.011619`, mae `0.018355`
- 20d: sample `40`, hit `0.8`, avg `0.032933`, median `0.039296`, mae `0.038308`
- 60d: sample `40`, hit `0.925`, avg `0.09103`, median `0.108121`, mae `0.096127`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.002932`, median `-0.002952`, mae `0.017032`
- 5d: sample `40`, hit `0.375`, avg `-0.002175`, median `-0.005796`, mae `0.018123`
- 10d: sample `40`, hit `0.5`, avg `0.002953`, median `0.003262`, mae `0.025344`
- 20d: sample `40`, hit `0.675`, avg `0.010877`, median `0.025198`, mae `0.038559`
- 60d: sample `40`, hit `0.875`, avg `0.079247`, median `0.098256`, mae `0.090446`

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
- 3d: sample `80`, hit `0.4625`, avg `-0.001128`, median `-0.001227`, mae `0.014892`
- 5d: sample `80`, hit `0.4875`, avg `0.000673`, median `-0.000402`, mae `0.016225`
- 10d: sample `80`, hit `0.625`, avg `0.006414`, median `0.008676`, mae `0.02185`
- 20d: sample `80`, hit `0.7375`, avg `0.021905`, median `0.031464`, mae `0.038434`
- 60d: sample `80`, hit `0.9`, avg `0.085138`, median `0.10344`, mae `0.093287`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.002932`, median `-0.002952`, mae `0.017032`
- 5d: sample `40`, hit `0.375`, avg `-0.002175`, median `-0.005796`, mae `0.018123`
- 10d: sample `40`, hit `0.5`, avg `0.002953`, median `0.003262`, mae `0.025344`
- 20d: sample `40`, hit `0.675`, avg `0.010877`, median `0.025198`, mae `0.038559`
- 60d: sample `40`, hit `0.875`, avg `0.079247`, median `0.098256`, mae `0.090446`

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
