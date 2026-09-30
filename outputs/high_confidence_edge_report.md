# High Confidence Edge Report

Generated at: `2026-09-30T00:55:33.241603+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `60`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `60`, gate `moderate_evidence`
- 5d: completed `60`, gate `moderate_evidence`
- 10d: completed `60`, gate `moderate_evidence`
- 20d: completed `60`, gate `moderate_evidence`
- 60d: completed `60`, gate `moderate_evidence`

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
- 3d: sample `40`, hit `0.55`, avg `0.001227`, median `0.002957`, mae `0.013329`
- 5d: sample `40`, hit `0.575`, avg `0.003134`, median `0.005986`, mae `0.015067`
- 10d: sample `40`, hit `0.725`, avg `0.008464`, median `0.011031`, mae `0.018555`
- 20d: sample `40`, hit `0.8`, avg `0.033205`, median `0.03801`, mae `0.03858`
- 60d: sample `40`, hit `0.925`, avg `0.091424`, median `0.108121`, mae `0.096521`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.004618`, median `-0.007114`, mae `0.019043`
- 5d: sample `40`, hit `0.375`, avg `-0.003444`, median `-0.005796`, mae `0.019722`
- 10d: sample `40`, hit `0.475`, avg `3.4e-05`, median `-0.001818`, mae `0.026309`
- 20d: sample `40`, hit `0.65`, avg `0.014323`, median `0.025198`, mae `0.040977`
- 60d: sample `40`, hit `0.9`, avg `0.093743`, median `0.114377`, mae `0.099162`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.001227, 'median_return': 0.002957, 'mean_absolute_return': 0.013329, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.025934}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.003134, 'median_return': 0.005986, 'mean_absolute_return': 0.015067, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.030717}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.008464, 'median_return': 0.011031, 'mean_absolute_return': 0.018555, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.039009}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.033205, 'median_return': 0.03801, 'mean_absolute_return': 0.03858, 'max_adverse_excursion': -0.026142, 'max_favorable_excursion': 0.088842}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.091424, 'median_return': 0.108121, 'mean_absolute_return': 0.096521, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005815, 'median_return': 0.012272, 'mean_absolute_return': 0.014511, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006695, 'median_return': 0.009709, 'mean_absolute_return': 0.016592, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009347, 'median_return': 0.013069, 'mean_absolute_return': 0.017068, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026788, 'median_return': 0.043456, 'mean_absolute_return': 0.034274, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.114868, 'median_return': 0.119272, 'mean_absolute_return': 0.114868, 'max_adverse_excursion': 0.099512, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.00253, 'median_return': -0.002952, 'mean_absolute_return': 0.016372, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.000916, 'median_return': -0.002452, 'mean_absolute_return': 0.017483, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.003683, 'median_return': 0.005356, 'mean_absolute_return': 0.023028, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.023428, 'median_return': 0.032299, 'mean_absolute_return': 0.04039, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.088842}, '60d': {'sample_size': 72, 'hit_rate': 0.9028, 'avg_return': 0.090107, 'median_return': 0.108121, 'mean_absolute_return': 0.09595, 'max_adverse_excursion': -0.078345, 'max_favorable_excursion': 0.188643}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.425}, '60d': {'sample_size': 80, 'hit_rate': 0.2875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.175, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.425, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.001227, 'median_return': 0.002957, 'mean_absolute_return': 0.013329, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.025934}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.003134, 'median_return': 0.005986, 'mean_absolute_return': 0.015067, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.030717}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.008464, 'median_return': 0.011031, 'mean_absolute_return': 0.018555, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.039009}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.033205, 'median_return': 0.03801, 'mean_absolute_return': 0.03858, 'max_adverse_excursion': -0.026142, 'max_favorable_excursion': 0.088842}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.091424, 'median_return': 0.108121, 'mean_absolute_return': 0.096521, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.004618, 'median_return': -0.007114, 'mean_absolute_return': 0.019043, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.003444, 'median_return': -0.005796, 'mean_absolute_return': 0.019722, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 3.4e-05, 'median_return': -0.001818, 'mean_absolute_return': 0.026309, 'max_adverse_excursion': -0.053986, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.014323, 'median_return': 0.025198, 'mean_absolute_return': 0.040977, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.085181}, '60d': {'sample_size': 40, 'hit_rate': 0.9, 'avg_return': 0.093743, 'median_return': 0.114377, 'mean_absolute_return': 0.099162, 'max_adverse_excursion': -0.078345, 'max_favorable_excursion': 0.188643}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001227`, median `0.002957`, mae `0.013329`
- 5d: sample `40`, hit `0.575`, avg `0.003134`, median `0.005986`, mae `0.015067`
- 10d: sample `40`, hit `0.725`, avg `0.008464`, median `0.011031`, mae `0.018555`
- 20d: sample `40`, hit `0.8`, avg `0.033205`, median `0.03801`, mae `0.03858`
- 60d: sample `40`, hit `0.925`, avg `0.091424`, median `0.108121`, mae `0.096521`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.004618`, median `-0.007114`, mae `0.019043`
- 5d: sample `40`, hit `0.375`, avg `-0.003444`, median `-0.005796`, mae `0.019722`
- 10d: sample `40`, hit `0.475`, avg `3.4e-05`, median `-0.001818`, mae `0.026309`
- 20d: sample `40`, hit `0.65`, avg `0.014323`, median `0.025198`, mae `0.040977`
- 60d: sample `40`, hit `0.9`, avg `0.093743`, median `0.114377`, mae `0.099162`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003217`, median `0.007544`, mae `0.015049`
- 5d: sample `20`, hit `0.6`, avg `0.006401`, median `0.009709`, mae `0.016257`
- 10d: sample `20`, hit `0.7`, avg `0.011799`, median `0.020334`, mae `0.022391`
- 20d: sample `20`, hit `0.8`, avg `0.035897`, median `0.03801`, mae `0.039695`
- 60d: sample `20`, hit `0.9`, avg `0.087446`, median `0.109494`, mae `0.095558`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001227`, median `0.002957`, mae `0.013329`
- 5d: sample `40`, hit `0.575`, avg `0.003134`, median `0.005986`, mae `0.015067`
- 10d: sample `40`, hit `0.725`, avg `0.008464`, median `0.011031`, mae `0.018555`
- 20d: sample `40`, hit `0.8`, avg `0.033205`, median `0.03801`, mae `0.03858`
- 60d: sample `40`, hit `0.925`, avg `0.091424`, median `0.108121`, mae `0.096521`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003217`, median `0.007544`, mae `0.015049`
- 5d: sample `20`, hit `0.6`, avg `0.006401`, median `0.009709`, mae `0.016257`
- 10d: sample `20`, hit `0.7`, avg `0.011799`, median `0.020334`, mae `0.022391`
- 20d: sample `20`, hit `0.8`, avg `0.035897`, median `0.03801`, mae `0.039695`
- 60d: sample `20`, hit `0.9`, avg `0.087446`, median `0.109494`, mae `0.095558`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001227`, median `0.002957`, mae `0.013329`
- 5d: sample `40`, hit `0.575`, avg `0.003134`, median `0.005986`, mae `0.015067`
- 10d: sample `40`, hit `0.725`, avg `0.008464`, median `0.011031`, mae `0.018555`
- 20d: sample `40`, hit `0.8`, avg `0.033205`, median `0.03801`, mae `0.03858`
- 60d: sample `40`, hit `0.925`, avg `0.091424`, median `0.108121`, mae `0.096521`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.004618`, median `-0.007114`, mae `0.019043`
- 5d: sample `40`, hit `0.375`, avg `-0.003444`, median `-0.005796`, mae `0.019722`
- 10d: sample `40`, hit `0.475`, avg `3.4e-05`, median `-0.001818`, mae `0.026309`
- 20d: sample `40`, hit `0.65`, avg `0.014323`, median `0.025198`, mae `0.040977`
- 60d: sample `40`, hit `0.9`, avg `0.093743`, median `0.114377`, mae `0.099162`

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
- 3d: sample `80`, hit `0.4625`, avg `-0.001695`, median `-0.001591`, mae `0.016186`
- 5d: sample `80`, hit `0.475`, avg `-0.000155`, median `-0.001129`, mae `0.017394`
- 10d: sample `80`, hit `0.6`, avg `0.004249`, median `0.007751`, mae `0.022432`
- 20d: sample `80`, hit `0.725`, avg `0.023764`, median `0.032299`, mae `0.039779`
- 60d: sample `80`, hit `0.9125`, avg `0.092583`, median `0.110451`, mae `0.097841`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003217`, median `0.007544`, mae `0.015049`
- 5d: sample `20`, hit `0.6`, avg `0.006401`, median `0.009709`, mae `0.016257`
- 10d: sample `20`, hit `0.7`, avg `0.011799`, median `0.020334`, mae `0.022391`
- 20d: sample `20`, hit `0.8`, avg `0.035897`, median `0.03801`, mae `0.039695`
- 60d: sample `20`, hit `0.9`, avg `0.087446`, median `0.109494`, mae `0.095558`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.002006`, median `-0.001591`, mae `0.017711`
- 5d: sample `60`, hit `0.45`, avg `-0.000163`, median `-0.002452`, mae `0.018567`
- 10d: sample `60`, hit `0.55`, avg `0.003956`, median `0.004547`, mae `0.025003`
- 20d: sample `60`, hit `0.7`, avg `0.021514`, median `0.031464`, mae `0.04055`
- 60d: sample `60`, hit `0.9`, avg `0.091644`, median `0.113428`, mae `0.097961`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003217`, median `0.007544`, mae `0.015049`
- 5d: sample `20`, hit `0.6`, avg `0.006401`, median `0.009709`, mae `0.016257`
- 10d: sample `20`, hit `0.7`, avg `0.011799`, median `0.020334`, mae `0.022391`
- 20d: sample `20`, hit `0.8`, avg `0.035897`, median `0.03801`, mae `0.039695`
- 60d: sample `20`, hit `0.9`, avg `0.087446`, median `0.109494`, mae `0.095558`

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
