# High Confidence Edge Report

Generated at: `2026-09-18T16:27:39.658988+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `32`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `32`, gate `early_evidence`
- 5d: completed `32`, gate `early_evidence`
- 10d: completed `32`, gate `early_evidence`
- 20d: completed `32`, gate `early_evidence`
- 60d: completed `32`, gate `early_evidence`

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
- 3d: sample `80`, hit `0.425`, avg `-0.006617`, median `-0.008838`, mae `0.017598`
- 5d: sample `80`, hit `0.45`, avg `-0.009069`, median `-0.009879`, mae `0.020824`
- 10d: sample `80`, hit `0.4`, avg `-0.007587`, median `-0.011432`, mae `0.029346`
- 20d: sample `80`, hit `0.5875`, avg `0.011576`, median `0.015725`, mae `0.03963`
- 60d: sample `80`, hit `0.75`, avg `0.043609`, median `0.059948`, mae `0.081421`

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
- 3d: sample `8`, hit `0.875`, avg `0.009739`, median `0.010664`, mae `0.013722`
- 5d: sample `8`, hit `0.875`, avg `0.012684`, median `0.019244`, mae `0.015154`
- 10d: sample `8`, hit `0.75`, avg `0.016277`, median `0.021815`, mae `0.028026`
- 20d: sample `8`, hit `0.75`, avg `0.026304`, median `0.046035`, mae `0.028417`
- 60d: sample `8`, hit `0.75`, avg `0.062563`, median `0.095524`, mae `0.081124`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.009739`, median `0.010664`, mae `0.013722`
- 5d: sample `8`, hit `0.875`, avg `0.012684`, median `0.019244`, mae `0.015154`
- 10d: sample `8`, hit `0.75`, avg `0.016277`, median `0.021815`, mae `0.028026`
- 20d: sample `8`, hit `0.75`, avg `0.026304`, median `0.046035`, mae `0.028417`
- 60d: sample `8`, hit `0.75`, avg `0.062563`, median `0.095524`, mae `0.081124`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.009739, 'median_return': 0.010664, 'mean_absolute_return': 0.013722, 'max_adverse_excursion': -0.015933, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.012684, 'median_return': 0.019244, 'mean_absolute_return': 0.015154, 'max_adverse_excursion': -0.009879, 'max_favorable_excursion': 0.02354}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016277, 'median_return': 0.021815, 'mean_absolute_return': 0.028026, 'max_adverse_excursion': -0.031093, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.026304, 'median_return': 0.046035, 'mean_absolute_return': 0.028417, 'max_adverse_excursion': -0.005136, 'max_favorable_excursion': 0.055563}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.062563, 'median_return': 0.095524, 'mean_absolute_return': 0.081124, 'max_adverse_excursion': -0.039228, 'max_favorable_excursion': 0.141614}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.008434, 'median_return': -0.010094, 'mean_absolute_return': 0.018029, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.011487, 'median_return': -0.016062, 'mean_absolute_return': 0.021453, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.044767}, '10d': {'sample_size': 72, 'hit_rate': 0.3611, 'avg_return': -0.010239, 'median_return': -0.013412, 'mean_absolute_return': 0.029492, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.00994, 'median_return': 0.015725, 'mean_absolute_return': 0.040875, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.041503, 'median_return': 0.059948, 'mean_absolute_return': 0.081453, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.4125}, '60d': {'sample_size': 80, 'hit_rate': 0.25}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.5, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.001687, 'median_return': 0.009966, 'mean_absolute_return': 0.01611, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.034318}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.004007, 'median_return': 0.008593, 'mean_absolute_return': 0.016627, 'max_adverse_excursion': -0.035224, 'max_favorable_excursion': 0.044767}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.012174, 'median_return': 0.013648, 'mean_absolute_return': 0.026817, 'max_adverse_excursion': -0.033079, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.021049, 'median_return': 0.014522, 'mean_absolute_return': 0.028496, 'max_adverse_excursion': -0.029611, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.065449, 'median_return': 0.064104, 'mean_absolute_return': 0.086058, 'max_adverse_excursion': -0.118336, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.35, 'avg_return': -0.009384, 'median_return': -0.010094, 'mean_absolute_return': 0.018094, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 60, 'hit_rate': 0.35, 'avg_return': -0.013428, 'median_return': -0.017697, 'mean_absolute_return': 0.022222, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 60, 'hit_rate': 0.3167, 'avg_return': -0.014174, 'median_return': -0.015783, 'mean_absolute_return': 0.030188, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.008418, 'median_return': 0.01927, 'mean_absolute_return': 0.043341, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.036328, 'median_return': 0.059495, 'mean_absolute_return': 0.079875, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.145995}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.425`, avg `-0.006617`, median `-0.008838`, mae `0.017598`
- 5d: sample `80`, hit `0.45`, avg `-0.009069`, median `-0.009879`, mae `0.020824`
- 10d: sample `80`, hit `0.4`, avg `-0.007587`, median `-0.011432`, mae `0.029346`
- 20d: sample `80`, hit `0.5875`, avg `0.011576`, median `0.015725`, mae `0.03963`
- 60d: sample `80`, hit `0.75`, avg `0.043609`, median `0.059948`, mae `0.081421`

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
- 3d: sample `40`, hit `0.625`, avg `-0.000137`, median `0.006513`, mae `0.014916`
- 5d: sample `40`, hit `0.65`, avg `0.000824`, median `0.003727`, mae `0.015877`
- 10d: sample `40`, hit `0.575`, avg `0.003976`, median `0.005691`, mae `0.024148`
- 20d: sample `40`, hit `0.7`, avg `0.021241`, median `0.01927`, mae `0.029942`
- 60d: sample `40`, hit `0.825`, avg `0.056364`, median `0.061844`, mae `0.071195`

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
- 3d: sample `80`, hit `0.425`, avg `-0.006617`, median `-0.008838`, mae `0.017598`
- 5d: sample `80`, hit `0.45`, avg `-0.009069`, median `-0.009879`, mae `0.020824`
- 10d: sample `80`, hit `0.4`, avg `-0.007587`, median `-0.011432`, mae `0.029346`
- 20d: sample `80`, hit `0.5875`, avg `0.011576`, median `0.015725`, mae `0.03963`
- 60d: sample `80`, hit `0.75`, avg `0.043609`, median `0.059948`, mae `0.081421`

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
- 3d: sample `80`, hit `0.425`, avg `-0.006617`, median `-0.008838`, mae `0.017598`
- 5d: sample `80`, hit `0.45`, avg `-0.009069`, median `-0.009879`, mae `0.020824`
- 10d: sample `80`, hit `0.4`, avg `-0.007587`, median `-0.011432`, mae `0.029346`
- 20d: sample `80`, hit `0.5875`, avg `0.011576`, median `0.015725`, mae `0.03963`
- 60d: sample `80`, hit `0.75`, avg `0.043609`, median `0.059948`, mae `0.081421`

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
