# High Confidence Edge Report

Generated at: `2026-09-17T00:58:43.829828+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `24`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `24`, gate `early_evidence`
- 5d: completed `24`, gate `early_evidence`
- 10d: completed `24`, gate `early_evidence`
- 20d: completed `24`, gate `early_evidence`
- 60d: completed `24`, gate `early_evidence`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.003279`, median `0.007316`, mae `0.019101`
- 5d: sample `80`, hit `0.55`, avg `0.003574`, median `0.002462`, mae `0.021068`
- 10d: sample `80`, hit `0.625`, avg `0.006045`, median `0.007751`, mae `0.029149`
- 20d: sample `80`, hit `0.7625`, avg `0.031885`, median `0.03495`, mae `0.045441`
- 60d: sample `80`, hit `0.8375`, avg `0.082576`, median `0.099512`, mae `0.099099`

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
- 3d: sample `8`, hit `0.5`, avg `-0.001232`, median `0.003757`, mae `0.014907`
- 5d: sample `8`, hit `0.625`, avg `0.002193`, median `0.007948`, mae `0.016848`
- 10d: sample `8`, hit `0.625`, avg `0.007992`, median `0.013069`, mae `0.017217`
- 20d: sample `8`, hit `0.75`, avg `0.039454`, median `0.058396`, mae `0.041952`
- 60d: sample `8`, hit `1.0`, avg `0.108026`, median `0.121826`, mae `0.108026`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.001232`, median `0.003757`, mae `0.014907`
- 5d: sample `8`, hit `0.625`, avg `0.002193`, median `0.007948`, mae `0.016848`
- 10d: sample `8`, hit `0.625`, avg `0.007992`, median `0.013069`, mae `0.017217`
- 20d: sample `8`, hit `0.75`, avg `0.039454`, median `0.058396`, mae `0.041952`
- 60d: sample `8`, hit `1.0`, avg `0.108026`, median `0.121826`, mae `0.108026`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.001232, 'median_return': 0.003757, 'mean_absolute_return': 0.014907, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.002193, 'median_return': 0.007948, 'mean_absolute_return': 0.016848, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.007992, 'median_return': 0.013069, 'mean_absolute_return': 0.017217, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.039454, 'median_return': 0.058396, 'mean_absolute_return': 0.041952, 'max_adverse_excursion': -0.005283, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.108026, 'median_return': 0.121826, 'mean_absolute_return': 0.108026, 'max_adverse_excursion': 0.024156, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.00378, 'median_return': 0.009349, 'mean_absolute_return': 0.019567, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.003727, 'median_return': 0.002456, 'mean_absolute_return': 0.021536, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.005829, 'median_return': 0.00693, 'mean_absolute_return': 0.030474, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.031044, 'median_return': 0.034726, 'mean_absolute_return': 0.045829, 'max_adverse_excursion': -0.078831, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.079748, 'median_return': 0.092689, 'mean_absolute_return': 0.098107, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.21366}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4125}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.375}, '20d': {'sample_size': 80, 'hit_rate': 0.2375}, '60d': {'sample_size': 80, 'hit_rate': 0.1625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': -0.525, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.1625, 'secondary_hit_rate': 0.8375, 'primary_minus_secondary': -0.675, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.003864, 'median_return': 0.003757, 'mean_absolute_return': 0.015188, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.003457, 'median_return': 0.004597, 'mean_absolute_return': 0.017903, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.005847, 'median_return': 0.013069, 'mean_absolute_return': 0.022391, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.050818}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.028406, 'median_return': 0.034704, 'mean_absolute_return': 0.03742, 'max_adverse_excursion': -0.030715, 'max_favorable_excursion': 0.092742}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.083459, 'median_return': 0.109494, 'mean_absolute_return': 0.092586, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.156899}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.003084, 'median_return': 0.009349, 'mean_absolute_return': 0.020405, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.003613, 'median_return': 0.002462, 'mean_absolute_return': 0.022123, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.006111, 'median_return': 0.00693, 'mean_absolute_return': 0.031401, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.033044, 'median_return': 0.037433, 'mean_absolute_return': 0.048114, 'max_adverse_excursion': -0.078831, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.8333, 'avg_return': 0.082281, 'median_return': 0.092689, 'mean_absolute_return': 0.101269, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.21366}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.5875`, avg `0.003279`, median `0.007316`, mae `0.019101`
- 5d: sample `80`, hit `0.55`, avg `0.003574`, median `0.002462`, mae `0.021068`
- 10d: sample `80`, hit `0.625`, avg `0.006045`, median `0.007751`, mae `0.029149`
- 20d: sample `80`, hit `0.7625`, avg `0.031885`, median `0.03495`, mae `0.045441`
- 60d: sample `80`, hit `0.8375`, avg `0.082576`, median `0.099512`, mae `0.099099`

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
- 3d: sample `40`, hit `0.6`, avg `0.003218`, median `0.004815`, mae `0.013586`
- 5d: sample `40`, hit `0.525`, avg `0.002439`, median `0.004597`, mae `0.016299`
- 10d: sample `40`, hit `0.65`, avg `0.003161`, median `0.00693`, mae `0.018293`
- 20d: sample `40`, hit `0.8`, avg `0.029224`, median `0.034704`, mae `0.035173`
- 60d: sample `40`, hit `0.85`, avg `0.08091`, median `0.096534`, mae `0.087481`

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
- 3d: sample `80`, hit `0.5875`, avg `0.003279`, median `0.007316`, mae `0.019101`
- 5d: sample `80`, hit `0.55`, avg `0.003574`, median `0.002462`, mae `0.021068`
- 10d: sample `80`, hit `0.625`, avg `0.006045`, median `0.007751`, mae `0.029149`
- 20d: sample `80`, hit `0.7625`, avg `0.031885`, median `0.03495`, mae `0.045441`
- 60d: sample `80`, hit `0.8375`, avg `0.082576`, median `0.099512`, mae `0.099099`

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
- 3d: sample `80`, hit `0.5875`, avg `0.003279`, median `0.007316`, mae `0.019101`
- 5d: sample `80`, hit `0.55`, avg `0.003574`, median `0.002462`, mae `0.021068`
- 10d: sample `80`, hit `0.625`, avg `0.006045`, median `0.007751`, mae `0.029149`
- 20d: sample `80`, hit `0.7625`, avg `0.031885`, median `0.03495`, mae `0.045441`
- 60d: sample `80`, hit `0.8375`, avg `0.082576`, median `0.099512`, mae `0.099099`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
