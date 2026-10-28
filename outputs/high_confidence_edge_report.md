# High Confidence Edge Report

Generated at: `2026-10-28T00:59:05.349069+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `140`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `140`, gate `stronger_evidence`
- 5d: completed `140`, gate `stronger_evidence`
- 10d: completed `140`, gate `stronger_evidence`
- 20d: completed `140`, gate `stronger_evidence`
- 60d: completed `140`, gate `stronger_evidence`

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
- 3d: sample `20`, hit `0.65`, avg `0.005634`, median `0.018606`, mae `0.021511`
- 5d: sample `20`, hit `0.65`, avg `0.004608`, median `0.005387`, mae `0.025937`
- 10d: sample `20`, hit `0.55`, avg `0.006705`, median `0.024811`, mae `0.040072`
- 20d: sample `20`, hit `0.5`, avg `-0.003088`, median `0.02284`, mae `0.052527`
- 60d: sample `20`, hit `0.95`, avg `0.061751`, median `0.065766`, mae `0.062767`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.002397`, median `0.007259`, mae `0.017955`
- 5d: sample `60`, hit `0.5333`, avg `-7.2e-05`, median `0.006018`, mae `0.023602`
- 10d: sample `60`, hit `0.5`, avg `-0.006644`, median `0.000466`, mae `0.035269`
- 20d: sample `60`, hit `0.4833`, avg `-0.008454`, median `-0.002558`, mae `0.038731`
- 60d: sample `60`, hit `0.8333`, avg `0.06875`, median `0.077579`, mae `0.079797`

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
- 3d: sample `8`, hit `0.625`, avg `0.011129`, median `0.020188`, mae `0.019772`
- 5d: sample `8`, hit `0.625`, avg `0.008236`, median `0.030736`, mae `0.032516`
- 10d: sample `8`, hit `0.5`, avg `0.003698`, median `0.036012`, mae `0.044778`
- 20d: sample `8`, hit `0.5`, avg `-0.003955`, median `0.02284`, mae `0.038328`
- 60d: sample `8`, hit `0.875`, avg `0.055409`, median `0.069082`, mae `0.057947`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.011129`, median `0.020188`, mae `0.019772`
- 5d: sample `8`, hit `0.625`, avg `0.008236`, median `0.030736`, mae `0.032516`
- 10d: sample `8`, hit `0.5`, avg `0.003698`, median `0.036012`, mae `0.044778`
- 20d: sample `8`, hit `0.5`, avg `-0.003955`, median `0.02284`, mae `0.038328`
- 60d: sample `8`, hit `0.875`, avg `0.055409`, median `0.069082`, mae `0.057947`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.005634, 'median_return': 0.018606, 'mean_absolute_return': 0.021511, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.004608, 'median_return': 0.005387, 'mean_absolute_return': 0.025937, 'max_adverse_excursion': -0.041488, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.006705, 'median_return': 0.024811, 'mean_absolute_return': 0.040072, 'max_adverse_excursion': -0.104082, 'max_favorable_excursion': 0.069999}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.003088, 'median_return': 0.02284, 'mean_absolute_return': 0.052527, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.07754}, '60d': {'sample_size': 20, 'hit_rate': 0.95, 'avg_return': 0.061751, 'median_return': 0.065766, 'mean_absolute_return': 0.062767, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.117089}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.011129, 'median_return': 0.020188, 'mean_absolute_return': 0.019772, 'max_adverse_excursion': -0.018946, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.008236, 'median_return': 0.030736, 'mean_absolute_return': 0.032516, 'max_adverse_excursion': -0.039725, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003698, 'median_return': 0.036012, 'mean_absolute_return': 0.044778, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003955, 'median_return': 0.02284, 'mean_absolute_return': 0.038328, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.060367}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.055409, 'median_return': 0.069082, 'mean_absolute_return': 0.057947, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.117089}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.002326, 'median_return': 0.00745, 'mean_absolute_return': 0.018741, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.000305, 'median_return': 0.005387, 'mean_absolute_return': 0.02326, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.004085, 'median_return': 0.001411, 'mean_absolute_return': 0.035546, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.069999}, '20d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.007463, 'median_return': -0.002558, 'mean_absolute_return': 0.042608, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.8611, 'avg_return': 0.068288, 'median_return': 0.072453, 'mean_absolute_return': 0.077494, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.188608}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.4875}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.4625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.003982, 'median_return': 0.008174, 'mean_absolute_return': 0.017174, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.001842, 'median_return': 0.002574, 'mean_absolute_return': 0.023037, 'max_adverse_excursion': -0.041734, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.006531, 'median_return': -0.008597, 'mean_absolute_return': 0.040263, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.069999}, '20d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.01032, 'median_return': -0.007733, 'mean_absolute_return': 0.046808, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.053421, 'median_return': 0.059606, 'mean_absolute_return': 0.064806, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.140645}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.000881, 'median_return': 0.008574, 'mean_absolute_return': 0.023853, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.04128}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': -0.001134, 'median_return': 0.010926, 'mean_absolute_return': 0.027631, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.042725}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.006366, 'median_return': 0.010251, 'mean_absolute_return': 0.02509, 'max_adverse_excursion': -0.063826, 'max_favorable_excursion': 0.062888}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.002511, 'median_return': 0.001939, 'mean_absolute_return': 0.028296, 'max_adverse_excursion': -0.056594, 'max_favorable_excursion': 0.066803}, '60d': {'sample_size': 20, 'hit_rate': 1.0, 'avg_return': 0.107739, 'median_return': 0.109805, 'mean_absolute_return': 0.107739, 'max_adverse_excursion': 0.009335, 'max_favorable_excursion': 0.188608}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.003982`, median `0.008174`, mae `0.017174`
- 5d: sample `60`, hit `0.5333`, avg `0.001842`, median `0.002574`, mae `0.023037`
- 10d: sample `60`, hit `0.45`, avg `-0.006531`, median `-0.008597`, mae `0.040263`
- 20d: sample `60`, hit `0.4667`, avg `-0.01032`, median `-0.007733`, mae `0.046808`
- 60d: sample `60`, hit `0.8167`, avg `0.053421`, median `0.059606`, mae `0.064806`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.000881`, median `0.008574`, mae `0.023853`
- 5d: sample `20`, hit `0.65`, avg `-0.001134`, median `0.010926`, mae `0.027631`
- 10d: sample `20`, hit `0.7`, avg `0.006366`, median `0.010251`, mae `0.02509`
- 20d: sample `20`, hit `0.55`, avg `0.002511`, median `0.001939`, mae `0.028296`
- 60d: sample `20`, hit `1.0`, avg `0.107739`, median `0.109805`, mae `0.107739`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.00359`, median `0.008174`, mae `0.016983`
- 5d: sample `40`, hit `0.55`, avg `0.001676`, median `0.002812`, mae `0.023005`
- 10d: sample `40`, hit `0.45`, avg `-0.005299`, median `-0.012607`, mae `0.039222`
- 20d: sample `40`, hit `0.425`, avg `-0.010668`, median `-0.021765`, mae `0.046474`
- 60d: sample `40`, hit `0.825`, avg `0.047546`, median `0.057953`, mae `0.056494`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.00359`, median `0.008174`, mae `0.016983`
- 5d: sample `40`, hit `0.55`, avg `0.001676`, median `0.002812`, mae `0.023005`
- 10d: sample `40`, hit `0.45`, avg `-0.005299`, median `-0.012607`, mae `0.039222`
- 20d: sample `40`, hit `0.425`, avg `-0.010668`, median `-0.021765`, mae `0.046474`
- 60d: sample `40`, hit `0.825`, avg `0.047546`, median `0.057953`, mae `0.056494`

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
- 3d: sample `20`, hit `0.6`, avg `0.000881`, median `0.008574`, mae `0.023853`
- 5d: sample `20`, hit `0.65`, avg `-0.001134`, median `0.010926`, mae `0.027631`
- 10d: sample `20`, hit `0.7`, avg `0.006366`, median `0.010251`, mae `0.02509`
- 20d: sample `20`, hit `0.55`, avg `0.002511`, median `0.001939`, mae `0.028296`
- 60d: sample `20`, hit `1.0`, avg `0.107739`, median `0.109805`, mae `0.107739`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001545`, median `0.005136`, mae `0.012454`
- 5d: sample `20`, hit `0.45`, avg `-0.001256`, median `-0.005615`, mae `0.020073`
- 10d: sample `20`, hit `0.35`, avg `-0.017302`, median `-0.030112`, mae `0.038373`
- 20d: sample `20`, hit `0.35`, avg `-0.018248`, median `-0.023277`, mae `0.040422`
- 60d: sample `20`, hit `0.7`, avg `0.033341`, median `0.044344`, mae `0.050221`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.0052`, median `0.012066`, mae `0.019534`
- 5d: sample `40`, hit `0.575`, avg `0.003391`, median `0.002812`, mae `0.02452`
- 10d: sample `40`, hit `0.5`, avg `-0.001145`, median `0.001411`, mae `0.041207`
- 20d: sample `40`, hit `0.525`, avg `-0.006356`, median `0.009784`, mae `0.050001`
- 60d: sample `40`, hit `0.875`, avg `0.06346`, median `0.069082`, mae `0.072099`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.000881`, median `0.008574`, mae `0.023853`
- 5d: sample `20`, hit `0.65`, avg `-0.001134`, median `0.010926`, mae `0.027631`
- 10d: sample `20`, hit `0.7`, avg `0.006366`, median `0.010251`, mae `0.02509`
- 20d: sample `20`, hit `0.55`, avg `0.002511`, median `0.001939`, mae `0.028296`
- 60d: sample `20`, hit `1.0`, avg `0.107739`, median `0.109805`, mae `0.107739`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001545`, median `0.005136`, mae `0.012454`
- 5d: sample `20`, hit `0.45`, avg `-0.001256`, median `-0.005615`, mae `0.020073`
- 10d: sample `20`, hit `0.35`, avg `-0.017302`, median `-0.030112`, mae `0.038373`
- 20d: sample `20`, hit `0.35`, avg `-0.018248`, median `-0.023277`, mae `0.040422`
- 60d: sample `20`, hit `0.7`, avg `0.033341`, median `0.044344`, mae `0.050221`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.000881`, median `0.008574`, mae `0.023853`
- 5d: sample `20`, hit `0.65`, avg `-0.001134`, median `0.010926`, mae `0.027631`
- 10d: sample `20`, hit `0.7`, avg `0.006366`, median `0.010251`, mae `0.02509`
- 20d: sample `20`, hit `0.55`, avg `0.002511`, median `0.001939`, mae `0.028296`
- 60d: sample `20`, hit `1.0`, avg `0.107739`, median `0.109805`, mae `0.107739`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.003206`, median `0.008174`, mae `0.018844`
- 5d: sample `80`, hit `0.5625`, avg `0.001098`, median `0.005387`, mae `0.024186`
- 10d: sample `80`, hit `0.5125`, avg `-0.003306`, median `0.001411`, mae `0.036469`
- 20d: sample `80`, hit `0.4875`, avg `-0.007112`, median `-0.002558`, mae `0.04218`
- 60d: sample `80`, hit `0.8625`, avg `0.067`, median `0.06911`, mae `0.07554`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.00359`, median `0.008174`, mae `0.016983`
- 5d: sample `40`, hit `0.55`, avg `0.001676`, median `0.002812`, mae `0.023005`
- 10d: sample `40`, hit `0.45`, avg `-0.005299`, median `-0.012607`, mae `0.039222`
- 20d: sample `40`, hit `0.425`, avg `-0.010668`, median `-0.021765`, mae `0.046474`
- 60d: sample `40`, hit `0.825`, avg `0.047546`, median `0.057953`, mae `0.056494`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.002823`, median `0.008574`, mae `0.020705`
- 5d: sample `40`, hit `0.575`, avg `0.00052`, median `0.007168`, mae `0.025367`
- 10d: sample `40`, hit `0.575`, avg `-0.001314`, median `0.008188`, mae `0.033716`
- 20d: sample `40`, hit `0.55`, avg `-0.003557`, median `0.003343`, mae `0.037886`
- 60d: sample `40`, hit `0.9`, avg `0.086454`, median `0.098961`, mae `0.094585`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
