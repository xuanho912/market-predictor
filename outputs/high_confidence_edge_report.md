# High Confidence Edge Report

Generated at: `2026-10-08T02:42:29.093938+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `84`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `84`, gate `moderate_evidence`
- 5d: completed `84`, gate `moderate_evidence`
- 10d: completed `84`, gate `moderate_evidence`
- 20d: completed `84`, gate `moderate_evidence`
- 60d: completed `84`, gate `moderate_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.4125`, avg `-0.00571`, median `-0.003676`, mae `0.016944`
- 5d: sample `80`, hit `0.425`, avg `-0.008308`, median `-0.00693`, mae `0.020083`
- 10d: sample `80`, hit `0.45`, avg `-0.010635`, median `-0.007019`, mae `0.030582`
- 20d: sample `80`, hit `0.5625`, avg `0.001424`, median `0.015416`, mae `0.043767`
- 60d: sample `80`, hit `0.8`, avg `0.040374`, median `0.053855`, mae `0.076185`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.009683`, median `0.006895`, mae `0.026003`
- 5d: sample `8`, hit `0.5`, avg `-0.014553`, median `0.005072`, mae `0.0316`
- 10d: sample `8`, hit `0.25`, avg `-0.017771`, median `-0.013832`, mae `0.025554`
- 20d: sample `8`, hit `0.5`, avg `-0.01538`, median `0.001463`, mae `0.038088`
- 60d: sample `8`, hit `0.5`, avg `-0.046636`, median `0.037425`, mae `0.105094`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.009683`, median `0.006895`, mae `0.026003`
- 5d: sample `8`, hit `0.5`, avg `-0.014553`, median `0.005072`, mae `0.0316`
- 10d: sample `8`, hit `0.25`, avg `-0.017771`, median `-0.013832`, mae `0.025554`
- 20d: sample `8`, hit `0.5`, avg `-0.01538`, median `0.001463`, mae `0.038088`
- 60d: sample `8`, hit `0.5`, avg `-0.046636`, median `0.037425`, mae `0.105094`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4125, 'avg_return': -0.00571, 'median_return': -0.003676, 'mean_absolute_return': 0.016944, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': -0.008308, 'median_return': -0.00693, 'mean_absolute_return': 0.020083, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.010635, 'median_return': -0.007019, 'mean_absolute_return': 0.030582, 'max_adverse_excursion': -0.095057, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.001424, 'median_return': 0.015416, 'mean_absolute_return': 0.043767, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.040374, 'median_return': 0.053855, 'mean_absolute_return': 0.076185, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.154804}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.009683, 'median_return': 0.006895, 'mean_absolute_return': 0.026003, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.014553, 'median_return': 0.005072, 'mean_absolute_return': 0.0316, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.026602}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.017771, 'median_return': -0.013832, 'mean_absolute_return': 0.025554, 'max_adverse_excursion': -0.064399, 'max_favorable_excursion': 0.027926}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.01538, 'median_return': 0.001463, 'mean_absolute_return': 0.038088, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.046636, 'median_return': 0.037425, 'mean_absolute_return': 0.105094, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.099838}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.005268, 'median_return': -0.003676, 'mean_absolute_return': 0.015937, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.007614, 'median_return': -0.00693, 'mean_absolute_return': 0.018804, 'max_adverse_excursion': -0.053563, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.009842, 'median_return': -0.004767, 'mean_absolute_return': 0.03114, 'max_adverse_excursion': -0.095057, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.003291, 'median_return': 0.016021, 'mean_absolute_return': 0.044398, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.8333, 'avg_return': 0.050042, 'median_return': 0.056732, 'mean_absolute_return': 0.072973, 'max_adverse_excursion': -0.146095, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.4625}, '60d': {'sample_size': 80, 'hit_rate': 0.475}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4125, 'avg_return': -0.00571, 'median_return': -0.003676, 'mean_absolute_return': 0.016944, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': -0.008308, 'median_return': -0.00693, 'mean_absolute_return': 0.020083, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.010635, 'median_return': -0.007019, 'mean_absolute_return': 0.030582, 'max_adverse_excursion': -0.095057, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.001424, 'median_return': 0.015416, 'mean_absolute_return': 0.043767, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.040374, 'median_return': 0.053855, 'mean_absolute_return': 0.076185, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.154804}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.011521`, median `-0.012933`, mae `0.022592`
- 5d: sample `20`, hit `0.35`, avg `-0.016712`, median `-0.016421`, mae `0.027267`
- 10d: sample `20`, hit `0.2`, avg `-0.027701`, median `-0.022713`, mae `0.032078`
- 20d: sample `20`, hit `0.45`, avg `-0.017425`, median `-0.001589`, mae `0.044576`
- 60d: sample `20`, hit `0.65`, avg `-0.001741`, median `0.037425`, mae `0.081059`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.005378`, median `-0.003649`, mae `0.014298`
- 5d: sample `40`, hit `0.425`, avg `-0.005366`, median `-0.002452`, mae `0.016317`
- 10d: sample `40`, hit `0.525`, avg `-0.00209`, median `0.006604`, mae `0.032624`
- 20d: sample `40`, hit `0.6`, avg `0.009355`, median `0.026731`, mae `0.048519`
- 60d: sample `40`, hit `0.825`, avg `0.053794`, median `0.057507`, mae `0.078344`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.011521`, median `-0.012933`, mae `0.022592`
- 5d: sample `20`, hit `0.35`, avg `-0.016712`, median `-0.016421`, mae `0.027267`
- 10d: sample `20`, hit `0.2`, avg `-0.027701`, median `-0.022713`, mae `0.032078`
- 20d: sample `20`, hit `0.45`, avg `-0.017425`, median `-0.001589`, mae `0.044576`
- 60d: sample `20`, hit `0.65`, avg `-0.001741`, median `0.037425`, mae `0.081059`

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
- 3d: sample `20`, hit `0.3`, avg `-0.011521`, median `-0.012933`, mae `0.022592`
- 5d: sample `20`, hit `0.35`, avg `-0.016712`, median `-0.016421`, mae `0.027267`
- 10d: sample `20`, hit `0.2`, avg `-0.027701`, median `-0.022713`, mae `0.032078`
- 20d: sample `20`, hit `0.45`, avg `-0.017425`, median `-0.001589`, mae `0.044576`
- 60d: sample `20`, hit `0.65`, avg `-0.001741`, median `0.037425`, mae `0.081059`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.000563`, median `0.004815`, mae `0.016588`
- 5d: sample `20`, hit `0.5`, avg `-0.005789`, median `0.004557`, mae `0.020433`
- 10d: sample `20`, hit `0.55`, avg `-0.010659`, median `0.003815`, mae `0.025`
- 20d: sample `20`, hit `0.6`, avg `0.004412`, median `0.015416`, mae `0.033454`
- 60d: sample `20`, hit `0.9`, avg `0.05565`, median `0.063683`, mae `0.066995`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.005378`, median `-0.003649`, mae `0.014298`
- 5d: sample `40`, hit `0.425`, avg `-0.005366`, median `-0.002452`, mae `0.016317`
- 10d: sample `40`, hit `0.525`, avg `-0.00209`, median `0.006604`, mae `0.032624`
- 20d: sample `40`, hit `0.6`, avg `0.009355`, median `0.026731`, mae `0.048519`
- 60d: sample `40`, hit `0.825`, avg `0.053794`, median `0.057507`, mae `0.078344`

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
- 3d: sample `80`, hit `0.4125`, avg `-0.00571`, median `-0.003676`, mae `0.016944`
- 5d: sample `80`, hit `0.425`, avg `-0.008308`, median `-0.00693`, mae `0.020083`
- 10d: sample `80`, hit `0.45`, avg `-0.010635`, median `-0.007019`, mae `0.030582`
- 20d: sample `80`, hit `0.5625`, avg `0.001424`, median `0.015416`, mae `0.043767`
- 60d: sample `80`, hit `0.8`, avg `0.040374`, median `0.053855`, mae `0.076185`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.006042`, median `-0.003995`, mae `0.01959`
- 5d: sample `40`, hit `0.425`, avg `-0.011251`, median `-0.013237`, mae `0.02385`
- 10d: sample `40`, hit `0.375`, avg `-0.01918`, median `-0.013832`, mae `0.028539`
- 20d: sample `40`, hit `0.525`, avg `-0.006506`, median `0.001463`, mae `0.039015`
- 60d: sample `40`, hit `0.775`, avg `0.026954`, median `0.050438`, mae `0.074027`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4125`, avg `-0.00571`, median `-0.003676`, mae `0.016944`
- 5d: sample `80`, hit `0.425`, avg `-0.008308`, median `-0.00693`, mae `0.020083`
- 10d: sample `80`, hit `0.45`, avg `-0.010635`, median `-0.007019`, mae `0.030582`
- 20d: sample `80`, hit `0.5625`, avg `0.001424`, median `0.015416`, mae `0.043767`
- 60d: sample `80`, hit `0.8`, avg `0.040374`, median `0.053855`, mae `0.076185`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.006042`, median `-0.003995`, mae `0.01959`
- 5d: sample `40`, hit `0.425`, avg `-0.011251`, median `-0.013237`, mae `0.02385`
- 10d: sample `40`, hit `0.375`, avg `-0.01918`, median `-0.013832`, mae `0.028539`
- 20d: sample `40`, hit `0.525`, avg `-0.006506`, median `0.001463`, mae `0.039015`
- 60d: sample `40`, hit `0.775`, avg `0.026954`, median `0.050438`, mae `0.074027`

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
