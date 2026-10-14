# High Confidence Edge Report

Generated at: `2026-10-14T01:33:17.336378+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `100`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `100`, gate `moderate_evidence`
- 5d: completed `100`, gate `moderate_evidence`
- 10d: completed `100`, gate `moderate_evidence`
- 20d: completed `100`, gate `moderate_evidence`
- 60d: completed `100`, gate `moderate_evidence`

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
- 3d: sample `40`, hit `0.775`, avg `0.00819`, median `0.012355`, mae `0.015046`
- 5d: sample `40`, hit `0.7`, avg `0.009196`, median `0.012091`, mae `0.017817`
- 10d: sample `40`, hit `0.775`, avg `0.012626`, median `0.013069`, mae `0.020597`
- 20d: sample `40`, hit `0.9`, avg `0.038789`, median `0.035222`, mae `0.04073`
- 60d: sample `40`, hit `0.925`, avg `0.084197`, median `0.090809`, mae `0.089294`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.005005`, median `-0.003676`, mae `0.018136`
- 5d: sample `40`, hit `0.325`, avg `-0.00775`, median `-0.012276`, mae `0.020477`
- 10d: sample `40`, hit `0.375`, avg `-0.006456`, median `-0.010743`, mae `0.028137`
- 20d: sample `40`, hit `0.725`, avg `0.010343`, median `0.015661`, mae `0.03258`
- 60d: sample `40`, hit `0.725`, avg `0.057717`, median `0.076106`, mae `0.078815`

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
- 3d: sample `8`, hit `0.75`, avg `0.011441`, median `0.0214`, mae `0.020136`
- 5d: sample `8`, hit `0.75`, avg `0.013802`, median `0.013852`, mae `0.021604`
- 10d: sample `8`, hit `0.625`, avg `0.016973`, median `0.024811`, mae `0.02576`
- 20d: sample `8`, hit `1.0`, avg `0.061725`, median `0.062955`, mae `0.061725`
- 60d: sample `8`, hit `0.875`, avg `0.085751`, median `0.099719`, mae `0.097241`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.011441`, median `0.0214`, mae `0.020136`
- 5d: sample `8`, hit `0.75`, avg `0.013802`, median `0.013852`, mae `0.021604`
- 10d: sample `8`, hit `0.625`, avg `0.016973`, median `0.024811`, mae `0.02576`
- 20d: sample `8`, hit `1.0`, avg `0.061725`, median `0.062955`, mae `0.061725`
- 60d: sample `8`, hit `0.875`, avg `0.085751`, median `0.099719`, mae `0.097241`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.00819, 'median_return': 0.012355, 'mean_absolute_return': 0.015046, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.031839}, '5d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.009196, 'median_return': 0.012091, 'mean_absolute_return': 0.017817, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.012626, 'median_return': 0.013069, 'mean_absolute_return': 0.020597, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 40, 'hit_rate': 0.9, 'avg_return': 0.038789, 'median_return': 0.035222, 'mean_absolute_return': 0.04073, 'max_adverse_excursion': -0.015145, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.084197, 'median_return': 0.090809, 'mean_absolute_return': 0.089294, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.011441, 'median_return': 0.0214, 'mean_absolute_return': 0.020136, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.013802, 'median_return': 0.013852, 'mean_absolute_return': 0.021604, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.016973, 'median_return': 0.024811, 'mean_absolute_return': 0.02576, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.061725, 'median_return': 0.062955, 'mean_absolute_return': 0.061725, 'max_adverse_excursion': 0.031464, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.085751, 'median_return': 0.099719, 'mean_absolute_return': 0.097241, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.000499, 'median_return': 0.006042, 'mean_absolute_return': 0.016197, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.00073, 'median_return': -0.002452, 'mean_absolute_return': 0.018874, 'max_adverse_excursion': -0.04784, 'max_favorable_excursion': 0.041233}, '10d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.001542, 'median_return': 0.003921, 'mean_absolute_return': 0.024212, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.080442}, '20d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.020437, 'median_return': 0.025541, 'mean_absolute_return': 0.03387, 'max_adverse_excursion': -0.075684, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.069313, 'median_return': 0.084301, 'mean_absolute_return': 0.082589, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.194911}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6875}, '5d': {'sample_size': 80, 'hit_rate': 0.6875}, '10d': {'sample_size': 80, 'hit_rate': 0.7}, '20d': {'sample_size': 80, 'hit_rate': 0.5875}, '60d': {'sample_size': 80, 'hit_rate': 0.6}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.225, 'both_hit': 16, 'both_miss': 4}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.275, 'both_hit': 14, 'both_miss': 6}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.25, 'both_hit': 16, 'both_miss': 4}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.025, 'both_hit': 18, 'both_miss': 2}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.025, 'both_hit': 19, 'both_miss': 1}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.00819, 'median_return': 0.012355, 'mean_absolute_return': 0.015046, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.031839}, '5d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.009196, 'median_return': 0.012091, 'mean_absolute_return': 0.017817, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.012626, 'median_return': 0.013069, 'mean_absolute_return': 0.020597, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 40, 'hit_rate': 0.9, 'avg_return': 0.038789, 'median_return': 0.035222, 'mean_absolute_return': 0.04073, 'max_adverse_excursion': -0.015145, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.084197, 'median_return': 0.090809, 'mean_absolute_return': 0.089294, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.005005, 'median_return': -0.003676, 'mean_absolute_return': 0.018136, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.00775, 'median_return': -0.012276, 'mean_absolute_return': 0.020477, 'max_adverse_excursion': -0.04784, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.006456, 'median_return': -0.010743, 'mean_absolute_return': 0.028137, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.080442}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.010343, 'median_return': 0.015661, 'mean_absolute_return': 0.03258, 'max_adverse_excursion': -0.075684, 'max_favorable_excursion': 0.085821}, '60d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.057717, 'median_return': 0.076106, 'mean_absolute_return': 0.078815, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.194911}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.775`, avg `0.00819`, median `0.012355`, mae `0.015046`
- 5d: sample `40`, hit `0.7`, avg `0.009196`, median `0.012091`, mae `0.017817`
- 10d: sample `40`, hit `0.775`, avg `0.012626`, median `0.013069`, mae `0.020597`
- 20d: sample `40`, hit `0.9`, avg `0.038789`, median `0.035222`, mae `0.04073`
- 60d: sample `40`, hit `0.925`, avg `0.084197`, median `0.090809`, mae `0.089294`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.005005`, median `-0.003676`, mae `0.018136`
- 5d: sample `40`, hit `0.325`, avg `-0.00775`, median `-0.012276`, mae `0.020477`
- 10d: sample `40`, hit `0.375`, avg `-0.006456`, median `-0.010743`, mae `0.028137`
- 20d: sample `40`, hit `0.725`, avg `0.010343`, median `0.015661`, mae `0.03258`
- 60d: sample `40`, hit `0.725`, avg `0.057717`, median `0.076106`, mae `0.078815`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.775`, avg `0.00819`, median `0.012355`, mae `0.015046`
- 5d: sample `40`, hit `0.7`, avg `0.009196`, median `0.012091`, mae `0.017817`
- 10d: sample `40`, hit `0.775`, avg `0.012626`, median `0.013069`, mae `0.020597`
- 20d: sample `40`, hit `0.9`, avg `0.038789`, median `0.035222`, mae `0.04073`
- 60d: sample `40`, hit `0.925`, avg `0.084197`, median `0.090809`, mae `0.089294`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.775`, avg `0.00819`, median `0.012355`, mae `0.015046`
- 5d: sample `40`, hit `0.7`, avg `0.009196`, median `0.012091`, mae `0.017817`
- 10d: sample `40`, hit `0.775`, avg `0.012626`, median `0.013069`, mae `0.020597`
- 20d: sample `40`, hit `0.9`, avg `0.038789`, median `0.035222`, mae `0.04073`
- 60d: sample `40`, hit `0.925`, avg `0.084197`, median `0.090809`, mae `0.089294`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.775`, avg `0.00819`, median `0.012355`, mae `0.015046`
- 5d: sample `40`, hit `0.7`, avg `0.009196`, median `0.012091`, mae `0.017817`
- 10d: sample `40`, hit `0.775`, avg `0.012626`, median `0.013069`, mae `0.020597`
- 20d: sample `40`, hit `0.9`, avg `0.038789`, median `0.035222`, mae `0.04073`
- 60d: sample `40`, hit `0.925`, avg `0.084197`, median `0.090809`, mae `0.089294`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.775`, avg `0.00819`, median `0.012355`, mae `0.015046`
- 5d: sample `40`, hit `0.7`, avg `0.009196`, median `0.012091`, mae `0.017817`
- 10d: sample `40`, hit `0.775`, avg `0.012626`, median `0.013069`, mae `0.020597`
- 20d: sample `40`, hit `0.9`, avg `0.038789`, median `0.035222`, mae `0.04073`
- 60d: sample `40`, hit `0.925`, avg `0.084197`, median `0.090809`, mae `0.089294`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.005005`, median `-0.003676`, mae `0.018136`
- 5d: sample `40`, hit `0.325`, avg `-0.00775`, median `-0.012276`, mae `0.020477`
- 10d: sample `40`, hit `0.375`, avg `-0.006456`, median `-0.010743`, mae `0.028137`
- 20d: sample `40`, hit `0.725`, avg `0.010343`, median `0.015661`, mae `0.03258`
- 60d: sample `40`, hit `0.725`, avg `0.057717`, median `0.076106`, mae `0.078815`

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
- 3d: sample `80`, hit `0.5875`, avg `0.001593`, median `0.006632`, mae `0.016591`
- 5d: sample `80`, hit `0.5125`, avg `0.000723`, median `0.004597`, mae `0.019147`
- 10d: sample `80`, hit `0.575`, avg `0.003085`, median `0.004187`, mae `0.024367`
- 20d: sample `80`, hit `0.8125`, avg `0.024566`, median `0.029072`, mae `0.036655`
- 60d: sample `80`, hit `0.825`, avg `0.070957`, median `0.085781`, mae `0.084055`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.775`, avg `0.00819`, median `0.012355`, mae `0.015046`
- 5d: sample `40`, hit `0.7`, avg `0.009196`, median `0.012091`, mae `0.017817`
- 10d: sample `40`, hit `0.775`, avg `0.012626`, median `0.013069`, mae `0.020597`
- 20d: sample `40`, hit `0.9`, avg `0.038789`, median `0.035222`, mae `0.04073`
- 60d: sample `40`, hit `0.925`, avg `0.084197`, median `0.090809`, mae `0.089294`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.000807`, median `0.006632`, mae `0.014263`
- 5d: sample `40`, hit `0.525`, avg `-0.000467`, median `0.00774`, mae `0.01747`
- 10d: sample `40`, hit `0.55`, avg `0.001566`, median `0.003815`, mae `0.016783`
- 20d: sample `40`, hit `0.925`, avg `0.024621`, median `0.025541`, mae `0.026223`
- 60d: sample `40`, hit `0.775`, avg `0.056204`, median `0.059104`, mae `0.068966`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.006341`, median `0.011414`, mae `0.012217`
- 5d: sample `20`, hit `0.7`, avg `0.006866`, median `0.012091`, mae `0.014905`
- 10d: sample `20`, hit `0.8`, avg `0.008886`, median `0.011619`, mae `0.015172`
- 20d: sample `20`, hit `0.9`, avg `0.028388`, median `0.032299`, mae `0.031272`
- 60d: sample `20`, hit `0.95`, avg `0.081268`, median `0.084216`, mae `0.083349`

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
