# High Confidence Edge Report

Generated at: `2026-10-20T17:10:44.189034+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `120`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `120`, gate `stronger_evidence`
- 5d: completed `120`, gate `stronger_evidence`
- 10d: completed `120`, gate `stronger_evidence`
- 20d: completed `120`, gate `stronger_evidence`
- 60d: completed `120`, gate `stronger_evidence`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002144`, median `0.001199`, mae `0.012878`
- 5d: sample `40`, hit `0.575`, avg `-0.002782`, median `0.003005`, mae `0.014995`
- 10d: sample `40`, hit `0.45`, avg `-0.000168`, median `-0.000231`, mae `0.016903`
- 20d: sample `40`, hit `0.7`, avg `0.01702`, median `0.021759`, mae `0.029612`
- 60d: sample `40`, hit `0.6`, avg `0.014529`, median `0.032628`, mae `0.073577`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.004568`, median `-0.00589`, mae `0.018902`
- 5d: sample `40`, hit `0.45`, avg `-0.002532`, median `-0.002776`, mae `0.021909`
- 10d: sample `40`, hit `0.5`, avg `-0.001604`, median `0.001455`, mae `0.03526`
- 20d: sample `40`, hit `0.525`, avg `0.015359`, median `0.008882`, mae `0.040308`
- 60d: sample `40`, hit `0.775`, avg `0.059612`, median `0.068712`, mae `0.088872`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.00592`, median `0.00745`, mae `0.009339`
- 5d: sample `8`, hit `0.75`, avg `0.006419`, median `0.011724`, mae `0.009148`
- 10d: sample `8`, hit `0.75`, avg `0.008099`, median `0.011`, mae `0.009445`
- 20d: sample `8`, hit `0.875`, avg `0.017643`, median `0.023636`, mae `0.019868`
- 60d: sample `8`, hit `0.625`, avg `-0.009263`, median `0.046273`, mae `0.083915`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.008796`, median `-0.010033`, mae `0.017039`
- 5d: sample `8`, hit `0.375`, avg `-0.012434`, median `-0.022295`, mae `0.023462`
- 10d: sample `8`, hit `0.25`, avg `-0.00345`, median `-0.005891`, mae `0.014352`
- 20d: sample `8`, hit `0.75`, avg `0.037655`, median `0.058396`, mae `0.046085`
- 60d: sample `8`, hit `0.75`, avg `0.072565`, median `0.121826`, mae `0.094285`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.008796, 'median_return': -0.010033, 'mean_absolute_return': 0.017039, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012434, 'median_return': -0.022295, 'mean_absolute_return': 0.023462, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.00345, 'median_return': -0.005891, 'mean_absolute_return': 0.014352, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.037655, 'median_return': 0.058396, 'mean_absolute_return': 0.046085, 'max_adverse_excursion': -0.02149, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.072565, 'median_return': 0.121826, 'mean_absolute_return': 0.094285, 'max_adverse_excursion': -0.055789, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.002752, 'median_return': -0.002654, 'mean_absolute_return': 0.015763, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.04966}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': -0.001571, 'median_return': 0.001573, 'mean_absolute_return': 0.017895, 'max_adverse_excursion': -0.047223, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.000601, 'median_return': 0.000197, 'mean_absolute_return': 0.027385, 'max_adverse_excursion': -0.06893, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.013804, 'median_return': 0.012046, 'mean_absolute_return': 0.033724, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.110633}, '60d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.033127, 'median_return': 0.050036, 'mean_absolute_return': 0.079773, 'max_adverse_excursion': -0.145377, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.4875}, '10d': {'sample_size': 80, 'hit_rate': 0.525}, '20d': {'sample_size': 80, 'hit_rate': 0.3875}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.000824, 'median_return': 0.004542, 'mean_absolute_return': 0.009839, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.004675, 'median_return': 0.00774, 'mean_absolute_return': 0.012703, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.009496, 'median_return': 0.011, 'mean_absolute_return': 0.014101, 'max_adverse_excursion': -0.018062, 'max_favorable_excursion': 0.032557}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.015167, 'median_return': 0.023636, 'mean_absolute_return': 0.02563, 'max_adverse_excursion': -0.042211, 'max_favorable_excursion': 0.060476}, '60d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.00766, 'median_return': 0.022463, 'mean_absolute_return': 0.068921, 'max_adverse_excursion': -0.138565, 'max_favorable_excursion': 0.10629}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.00475, 'median_return': -0.004565, 'mean_absolute_return': 0.017907, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.04966}, '5d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.005101, 'median_return': -0.002776, 'mean_absolute_return': 0.020368, 'max_adverse_excursion': -0.047223, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': -0.004347, 'median_return': -0.010145, 'mean_absolute_return': 0.030075, 'max_adverse_excursion': -0.06893, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.01653, 'median_return': 0.01128, 'mean_absolute_return': 0.03807, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.110633}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.051981, 'median_return': 0.068256, 'mean_absolute_return': 0.085326, 'max_adverse_excursion': -0.145377, 'max_favorable_excursion': 0.21267}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002144`, median `0.001199`, mae `0.012878`
- 5d: sample `40`, hit `0.575`, avg `-0.002782`, median `0.003005`, mae `0.014995`
- 10d: sample `40`, hit `0.45`, avg `-0.000168`, median `-0.000231`, mae `0.016903`
- 20d: sample `40`, hit `0.7`, avg `0.01702`, median `0.021759`, mae `0.029612`
- 60d: sample `40`, hit `0.6`, avg `0.014529`, median `0.032628`, mae `0.073577`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.004568`, median `-0.00589`, mae `0.018902`
- 5d: sample `40`, hit `0.45`, avg `-0.002532`, median `-0.002776`, mae `0.021909`
- 10d: sample `40`, hit `0.5`, avg `-0.001604`, median `0.001455`, mae `0.03526`
- 20d: sample `40`, hit `0.525`, avg `0.015359`, median `0.008882`, mae `0.040308`
- 60d: sample `40`, hit `0.775`, avg `0.059612`, median `0.068712`, mae `0.088872`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.004568`, median `-0.00589`, mae `0.018902`
- 5d: sample `40`, hit `0.45`, avg `-0.002532`, median `-0.002776`, mae `0.021909`
- 10d: sample `40`, hit `0.5`, avg `-0.001604`, median `0.001455`, mae `0.03526`
- 20d: sample `40`, hit `0.525`, avg `0.015359`, median `0.008882`, mae `0.040308`
- 60d: sample `40`, hit `0.775`, avg `0.059612`, median `0.068712`, mae `0.088872`

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
- 3d: sample `80`, hit `0.45`, avg `-0.003356`, median `-0.002789`, mae `0.01589`
- 5d: sample `80`, hit `0.5125`, avg `-0.002657`, median `0.001087`, mae `0.018452`
- 10d: sample `80`, hit `0.475`, avg `-0.000886`, median `-0.000231`, mae `0.026082`
- 20d: sample `80`, hit `0.6125`, avg `0.016189`, median `0.01289`, mae `0.03496`
- 60d: sample `80`, hit `0.6875`, avg `0.037071`, median `0.054268`, mae `0.081225`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.003356`, median `-0.002789`, mae `0.01589`
- 5d: sample `80`, hit `0.5125`, avg `-0.002657`, median `0.001087`, mae `0.018452`
- 10d: sample `80`, hit `0.475`, avg `-0.000886`, median `-0.000231`, mae `0.026082`
- 20d: sample `80`, hit `0.6125`, avg `0.016189`, median `0.01289`, mae `0.03496`
- 60d: sample `80`, hit `0.6875`, avg `0.037071`, median `0.054268`, mae `0.081225`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.003356`, median `-0.002789`, mae `0.01589`
- 5d: sample `80`, hit `0.5125`, avg `-0.002657`, median `0.001087`, mae `0.018452`
- 10d: sample `80`, hit `0.475`, avg `-0.000886`, median `-0.000231`, mae `0.026082`
- 20d: sample `80`, hit `0.6125`, avg `0.016189`, median `0.01289`, mae `0.03496`
- 60d: sample `80`, hit `0.6875`, avg `0.037071`, median `0.054268`, mae `0.081225`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
