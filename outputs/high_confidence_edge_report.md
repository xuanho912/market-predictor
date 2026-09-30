# High Confidence Edge Report

Generated at: `2026-09-30T06:49:02.961792+00:00`

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
- 3d: sample `40`, hit `0.55`, avg `-0.001186`, median `0.002957`, mae `0.017985`
- 5d: sample `40`, hit `0.475`, avg `-0.006329`, median `-0.001429`, mae `0.020181`
- 10d: sample `40`, hit `0.475`, avg `-0.008901`, median `-0.000231`, mae `0.022288`
- 20d: sample `40`, hit `0.6`, avg `0.006182`, median `0.015416`, mae `0.0365`
- 60d: sample `40`, hit `0.825`, avg `0.050801`, median `0.065995`, mae `0.080932`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.006741`, median `-0.006207`, mae `0.013626`
- 5d: sample `40`, hit `0.4`, avg `-0.010218`, median `-0.005632`, mae `0.017543`
- 10d: sample `40`, hit `0.55`, avg `0.001217`, median `0.006604`, mae `0.028557`
- 20d: sample `40`, hit `0.625`, avg `0.015475`, median `0.029852`, mae `0.048226`
- 60d: sample `40`, hit `0.875`, avg `0.063231`, median `0.075909`, mae `0.093976`

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
- 3d: sample `8`, hit `0.5`, avg `-0.003446`, median `0.012272`, mae `0.022855`
- 5d: sample `8`, hit `0.625`, avg `-0.006543`, median `0.007948`, mae `0.021487`
- 10d: sample `8`, hit `0.25`, avg `-0.008101`, median `-0.011432`, mae `0.019002`
- 20d: sample `8`, hit `0.75`, avg `0.018437`, median `0.043456`, mae `0.048564`
- 60d: sample `8`, hit `0.875`, avg `0.062084`, median `0.099838`, mae `0.097365`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.003446`, median `0.012272`, mae `0.022855`
- 5d: sample `8`, hit `0.625`, avg `-0.006543`, median `0.007948`, mae `0.021487`
- 10d: sample `8`, hit `0.25`, avg `-0.008101`, median `-0.011432`, mae `0.019002`
- 20d: sample `8`, hit `0.75`, avg `0.018437`, median `0.043456`, mae `0.048564`
- 60d: sample `8`, hit `0.875`, avg `0.062084`, median `0.099838`, mae `0.097365`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.001186, 'median_return': 0.002957, 'mean_absolute_return': 0.017985, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.006329, 'median_return': -0.001429, 'mean_absolute_return': 0.020181, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.008901, 'median_return': -0.000231, 'mean_absolute_return': 0.022288, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.006182, 'median_return': 0.015416, 'mean_absolute_return': 0.0365, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.050801, 'median_return': 0.065995, 'mean_absolute_return': 0.080932, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003446, 'median_return': 0.012272, 'mean_absolute_return': 0.022855, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.006543, 'median_return': 0.007948, 'mean_absolute_return': 0.021487, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.008101, 'median_return': -0.011432, 'mean_absolute_return': 0.019002, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.018437, 'median_return': 0.043456, 'mean_absolute_return': 0.048564, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.062084, 'median_return': 0.099838, 'mean_absolute_return': 0.097365, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.004021, 'median_return': -0.003244, 'mean_absolute_return': 0.015022, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.008465, 'median_return': -0.005632, 'mean_absolute_return': 0.01857, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.003369, 'median_return': 0.004196, 'mean_absolute_return': 0.026136, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.009983, 'median_return': 0.015416, 'mean_absolute_return': 0.041674, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.8472, 'avg_return': 0.056453, 'median_return': 0.075128, 'mean_absolute_return': 0.086353, 'max_adverse_excursion': -0.184447, 'max_favorable_excursion': 0.176653}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.3875}, '60d': {'sample_size': 80, 'hit_rate': 0.15}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.15, 'secondary_hit_rate': 0.85, 'primary_minus_secondary': -0.7, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.001186, 'median_return': 0.002957, 'mean_absolute_return': 0.017985, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.006329, 'median_return': -0.001429, 'mean_absolute_return': 0.020181, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.008901, 'median_return': -0.000231, 'mean_absolute_return': 0.022288, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.006182, 'median_return': 0.015416, 'mean_absolute_return': 0.0365, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.050801, 'median_return': 0.065995, 'mean_absolute_return': 0.080932, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.006741, 'median_return': -0.006207, 'mean_absolute_return': 0.013626, 'max_adverse_excursion': -0.036265, 'max_favorable_excursion': 0.022103}, '5d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.010218, 'median_return': -0.005632, 'mean_absolute_return': 0.017543, 'max_adverse_excursion': -0.061537, 'max_favorable_excursion': 0.023861}, '10d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.001217, 'median_return': 0.006604, 'mean_absolute_return': 0.028557, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.015475, 'median_return': 0.029852, 'mean_absolute_return': 0.048226, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.063231, 'median_return': 0.075909, 'mean_absolute_return': 0.093976, 'max_adverse_excursion': -0.184447, 'max_favorable_excursion': 0.176653}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.001186`, median `0.002957`, mae `0.017985`
- 5d: sample `40`, hit `0.475`, avg `-0.006329`, median `-0.001429`, mae `0.020181`
- 10d: sample `40`, hit `0.475`, avg `-0.008901`, median `-0.000231`, mae `0.022288`
- 20d: sample `40`, hit `0.6`, avg `0.006182`, median `0.015416`, mae `0.0365`
- 60d: sample `40`, hit `0.825`, avg `0.050801`, median `0.065995`, mae `0.080932`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.006741`, median `-0.006207`, mae `0.013626`
- 5d: sample `40`, hit `0.4`, avg `-0.010218`, median `-0.005632`, mae `0.017543`
- 10d: sample `40`, hit `0.55`, avg `0.001217`, median `0.006604`, mae `0.028557`
- 20d: sample `40`, hit `0.625`, avg `0.015475`, median `0.029852`, mae `0.048226`
- 60d: sample `40`, hit `0.875`, avg `0.063231`, median `0.075909`, mae `0.093976`

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
- 3d: sample `40`, hit `0.55`, avg `-0.001186`, median `0.002957`, mae `0.017985`
- 5d: sample `40`, hit `0.475`, avg `-0.006329`, median `-0.001429`, mae `0.020181`
- 10d: sample `40`, hit `0.475`, avg `-0.008901`, median `-0.000231`, mae `0.022288`
- 20d: sample `40`, hit `0.6`, avg `0.006182`, median `0.015416`, mae `0.0365`
- 60d: sample `40`, hit `0.825`, avg `0.050801`, median `0.065995`, mae `0.080932`

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
- 3d: sample `40`, hit `0.55`, avg `-0.001186`, median `0.002957`, mae `0.017985`
- 5d: sample `40`, hit `0.475`, avg `-0.006329`, median `-0.001429`, mae `0.020181`
- 10d: sample `40`, hit `0.475`, avg `-0.008901`, median `-0.000231`, mae `0.022288`
- 20d: sample `40`, hit `0.6`, avg `0.006182`, median `0.015416`, mae `0.0365`
- 60d: sample `40`, hit `0.825`, avg `0.050801`, median `0.065995`, mae `0.080932`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.006741`, median `-0.006207`, mae `0.013626`
- 5d: sample `40`, hit `0.4`, avg `-0.010218`, median `-0.005632`, mae `0.017543`
- 10d: sample `40`, hit `0.55`, avg `0.001217`, median `0.006604`, mae `0.028557`
- 20d: sample `40`, hit `0.625`, avg `0.015475`, median `0.029852`, mae `0.048226`
- 60d: sample `40`, hit `0.875`, avg `0.063231`, median `0.075909`, mae `0.093976`

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
- 3d: sample `80`, hit `0.4375`, avg `-0.003963`, median `-0.002952`, mae `0.015806`
- 5d: sample `80`, hit `0.4375`, avg `-0.008273`, median `-0.003262`, mae `0.018862`
- 10d: sample `80`, hit `0.5125`, avg `-0.003842`, median `0.001607`, mae `0.025422`
- 20d: sample `80`, hit `0.6125`, avg `0.010828`, median `0.016745`, mae `0.042363`
- 60d: sample `80`, hit `0.85`, avg `0.057016`, median `0.075128`, mae `0.087454`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.006228`, median `-0.004936`, mae `0.016162`
- 5d: sample `60`, hit `0.3833`, avg `-0.010573`, median `-0.00693`, mae `0.019084`
- 10d: sample `60`, hit `0.4833`, avg `-0.003546`, median `-0.000231`, mae `0.026971`
- 20d: sample `60`, hit `0.6`, avg `0.011157`, median `0.021759`, mae `0.04683`
- 60d: sample `60`, hit `0.85`, avg `0.058622`, median `0.075909`, mae `0.09389`

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
