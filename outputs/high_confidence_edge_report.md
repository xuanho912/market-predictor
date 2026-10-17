# High Confidence Edge Report

Generated at: `2026-10-17T01:25:27.153294+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `112`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `112`, gate `stronger_evidence`
- 5d: completed `112`, gate `stronger_evidence`
- 10d: completed `112`, gate `stronger_evidence`
- 20d: completed `112`, gate `stronger_evidence`
- 60d: completed `112`, gate `stronger_evidence`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `0.000622`, median `0.002315`, mae `0.016502`
- 5d: sample `80`, hit `0.4875`, avg `-0.001656`, median `-0.000847`, mae `0.020213`
- 10d: sample `80`, hit `0.5`, avg `-0.006295`, median `0.000121`, mae `0.029639`
- 20d: sample `80`, hit `0.6`, avg `0.010975`, median `0.017149`, mae `0.037455`
- 60d: sample `80`, hit `0.775`, avg `0.075278`, median `0.079197`, mae `0.088227`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.003888`, median `0.012272`, mae `0.01549`
- 5d: sample `8`, hit `0.75`, avg `0.006352`, median `0.015202`, mae `0.018488`
- 10d: sample `8`, hit `0.625`, avg `0.01196`, median `0.015799`, mae `0.021186`
- 20d: sample `8`, hit `1.0`, avg `0.048142`, median `0.058396`, mae `0.048142`
- 60d: sample `8`, hit `0.875`, avg `0.084573`, median `0.121826`, mae `0.093364`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.003888`, median `0.012272`, mae `0.01549`
- 5d: sample `8`, hit `0.75`, avg `0.006352`, median `0.015202`, mae `0.018488`
- 10d: sample `8`, hit `0.625`, avg `0.01196`, median `0.015799`, mae `0.021186`
- 20d: sample `8`, hit `1.0`, avg `0.048142`, median `0.058396`, mae `0.048142`
- 60d: sample `8`, hit `0.875`, avg `0.084573`, median `0.121826`, mae `0.093364`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003888, 'median_return': 0.012272, 'mean_absolute_return': 0.01549, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.025934}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.006352, 'median_return': 0.015202, 'mean_absolute_return': 0.018488, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.01196, 'median_return': 0.015799, 'mean_absolute_return': 0.021186, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.037104}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.048142, 'median_return': 0.058396, 'mean_absolute_return': 0.048142, 'max_adverse_excursion': 0.017149, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.084573, 'median_return': 0.121826, 'mean_absolute_return': 0.093364, 'max_adverse_excursion': -0.035165, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.000259, 'median_return': 0.002315, 'mean_absolute_return': 0.016615, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.002545, 'median_return': -0.005615, 'mean_absolute_return': 0.020405, 'max_adverse_excursion': -0.0615, 'max_favorable_excursion': 0.075704}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.008323, 'median_return': -0.004074, 'mean_absolute_return': 0.030579, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.064813}, '20d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.006845, 'median_return': 0.01128, 'mean_absolute_return': 0.036267, 'max_adverse_excursion': -0.103293, 'max_favorable_excursion': 0.101843}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.074246, 'median_return': 0.077143, 'mean_absolute_return': 0.087657, 'max_adverse_excursion': -0.061391, 'max_favorable_excursion': 0.21254}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.4}, '60d': {'sample_size': 80, 'hit_rate': 0.225}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_minus_secondary': -0.55, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.001822, 'median_return': 0.004542, 'mean_absolute_return': 0.015191, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.001642, 'median_return': 0.005387, 'mean_absolute_return': 0.018475, 'max_adverse_excursion': -0.037174, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.002908, 'median_return': 0.000397, 'mean_absolute_return': 0.026673, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.050818}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.01386, 'median_return': 0.029072, 'mean_absolute_return': 0.038072, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.050206, 'median_return': 0.055986, 'mean_absolute_return': 0.061837, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.000578, 'median_return': -0.003528, 'mean_absolute_return': 0.017814, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.004953, 'median_return': -0.011901, 'mean_absolute_return': 0.021952, 'max_adverse_excursion': -0.0615, 'max_favorable_excursion': 0.075704}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.009682, 'median_return': 0.000121, 'mean_absolute_return': 0.032605, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.064813}, '20d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.008089, 'median_return': 0.004556, 'mean_absolute_return': 0.036837, 'max_adverse_excursion': -0.103293, 'max_favorable_excursion': 0.101843}, '60d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.100351, 'median_return': 0.134256, 'mean_absolute_return': 0.114617, 'max_adverse_excursion': -0.061391, 'max_favorable_excursion': 0.21254}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001822`, median `0.004542`, mae `0.015191`
- 5d: sample `40`, hit `0.525`, avg `0.001642`, median `0.005387`, mae `0.018475`
- 10d: sample `40`, hit `0.5`, avg `-0.002908`, median `0.000397`, mae `0.026673`
- 20d: sample `40`, hit `0.675`, avg `0.01386`, median `0.029072`, mae `0.038072`
- 60d: sample `40`, hit `0.75`, avg `0.050206`, median `0.055986`, mae `0.061837`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000578`, median `-0.003528`, mae `0.017814`
- 5d: sample `40`, hit `0.45`, avg `-0.004953`, median `-0.011901`, mae `0.021952`
- 10d: sample `40`, hit `0.5`, avg `-0.009682`, median `0.000121`, mae `0.032605`
- 20d: sample `40`, hit `0.525`, avg `0.008089`, median `0.004556`, mae `0.036837`
- 60d: sample `40`, hit `0.8`, avg `0.100351`, median `0.134256`, mae `0.114617`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.003737`, median `0.007101`, mae `0.016978`
- 5d: sample `20`, hit `0.55`, avg `0.002797`, median `0.005387`, mae `0.018658`
- 10d: sample `20`, hit `0.55`, avg `0.004225`, median `0.011031`, mae `0.024974`
- 20d: sample `20`, hit `0.8`, avg `0.027976`, median `0.034704`, mae `0.038637`
- 60d: sample `20`, hit `0.8`, avg `0.060833`, median `0.059606`, mae `0.073228`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.003737`, median `0.007101`, mae `0.016978`
- 5d: sample `20`, hit `0.55`, avg `0.002797`, median `0.005387`, mae `0.018658`
- 10d: sample `20`, hit `0.55`, avg `0.004225`, median `0.011031`, mae `0.024974`
- 20d: sample `20`, hit `0.8`, avg `0.027976`, median `0.034704`, mae `0.038637`
- 60d: sample `20`, hit `0.8`, avg `0.060833`, median `0.059606`, mae `0.073228`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000578`, median `-0.003528`, mae `0.017814`
- 5d: sample `40`, hit `0.45`, avg `-0.004953`, median `-0.011901`, mae `0.021952`
- 10d: sample `40`, hit `0.5`, avg `-0.009682`, median `0.000121`, mae `0.032605`
- 20d: sample `40`, hit `0.525`, avg `0.008089`, median `0.004556`, mae `0.036837`
- 60d: sample `40`, hit `0.8`, avg `0.100351`, median `0.134256`, mae `0.114617`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-9.4e-05`, median `0.004542`, mae `0.013404`
- 5d: sample `20`, hit `0.5`, avg `0.000488`, median `0.00774`, mae `0.018292`
- 10d: sample `20`, hit `0.45`, avg `-0.010041`, median `-0.007491`, mae `0.028373`
- 20d: sample `20`, hit `0.55`, avg `-0.000256`, median `0.025541`, mae `0.037506`
- 60d: sample `20`, hit `0.7`, avg `0.039578`, median `0.047238`, mae `0.050447`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `0.000622`, median `0.002315`, mae `0.016502`
- 5d: sample `80`, hit `0.4875`, avg `-0.001656`, median `-0.000847`, mae `0.020213`
- 10d: sample `80`, hit `0.5`, avg `-0.006295`, median `0.000121`, mae `0.029639`
- 20d: sample `80`, hit `0.6`, avg `0.010975`, median `0.017149`, mae `0.037455`
- 60d: sample `80`, hit `0.775`, avg `0.075278`, median `0.079197`, mae `0.088227`

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
- 3d: sample `80`, hit `0.5125`, avg `0.000622`, median `0.002315`, mae `0.016502`
- 5d: sample `80`, hit `0.4875`, avg `-0.001656`, median `-0.000847`, mae `0.020213`
- 10d: sample `80`, hit `0.5`, avg `-0.006295`, median `0.000121`, mae `0.029639`
- 20d: sample `80`, hit `0.6`, avg `0.010975`, median `0.017149`, mae `0.037455`
- 60d: sample `80`, hit `0.775`, avg `0.075278`, median `0.079197`, mae `0.088227`

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
- 3d: sample `80`, hit `0.5125`, avg `0.000622`, median `0.002315`, mae `0.016502`
- 5d: sample `80`, hit `0.4875`, avg `-0.001656`, median `-0.000847`, mae `0.020213`
- 10d: sample `80`, hit `0.5`, avg `-0.006295`, median `0.000121`, mae `0.029639`
- 20d: sample `80`, hit `0.6`, avg `0.010975`, median `0.017149`, mae `0.037455`
- 60d: sample `80`, hit `0.775`, avg `0.075278`, median `0.079197`, mae `0.088227`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
