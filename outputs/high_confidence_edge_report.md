# High Confidence Edge Report

Generated at: `2026-08-18T13:11:59.696796+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `0`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `0`, gate `insufficient`
- 5d: completed `0`, gate `insufficient`
- 10d: completed `0`, gate `insufficient`
- 20d: completed `0`, gate `insufficient`
- 60d: completed `0`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007233`, median `0.009206`, mae `0.01495`
- 5d: sample `60`, hit `0.6833`, avg `0.010309`, median `0.012091`, mae `0.020907`
- 10d: sample `60`, hit `0.7667`, avg `0.01903`, median `0.019171`, mae `0.022852`
- 20d: sample `60`, hit `0.95`, avg `0.033977`, median `0.029072`, mae `0.035209`
- 60d: sample `60`, hit `0.8333`, avg `0.046898`, median `0.059104`, mae `0.069012`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.007009`, median `0.009204`, mae `0.019159`
- 5d: sample `20`, hit `0.55`, avg `0.008189`, median `0.003789`, mae `0.022307`
- 10d: sample `20`, hit `0.55`, avg `0.021497`, median `0.006439`, mae `0.036021`
- 20d: sample `20`, hit `0.9`, avg `0.058581`, median `0.033791`, mae `0.060383`
- 60d: sample `20`, hit `0.8`, avg `0.059106`, median `0.056732`, mae `0.10306`

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
- 3d: sample `8`, hit `1.0`, avg `0.018679`, median `0.0214`, mae `0.018679`
- 5d: sample `8`, hit `0.875`, avg `0.022737`, median `0.03199`, mae `0.02475`
- 10d: sample `8`, hit `1.0`, avg `0.028959`, median `0.041976`, mae `0.028959`
- 20d: sample `8`, hit `1.0`, avg `0.059291`, median `0.075995`, mae `0.059291`
- 60d: sample `8`, hit `1.0`, avg `0.092921`, median `0.095628`, mae `0.092921`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `1.0`, avg `0.018679`, median `0.0214`, mae `0.018679`
- 5d: sample `8`, hit `0.875`, avg `0.022737`, median `0.03199`, mae `0.02475`
- 10d: sample `8`, hit `1.0`, avg `0.028959`, median `0.041976`, mae `0.028959`
- 20d: sample `8`, hit `1.0`, avg `0.059291`, median `0.075995`, mae `0.059291`
- 60d: sample `8`, hit `1.0`, avg `0.092921`, median `0.095628`, mae `0.092921`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.007233, 'median_return': 0.009206, 'mean_absolute_return': 0.01495, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.010309, 'median_return': 0.012091, 'mean_absolute_return': 0.020907, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.01903, 'median_return': 0.019171, 'mean_absolute_return': 0.022852, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 60, 'hit_rate': 0.95, 'avg_return': 0.033977, 'median_return': 0.029072, 'mean_absolute_return': 0.035209, 'max_adverse_excursion': -0.020687, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 60, 'hit_rate': 0.8333, 'avg_return': 0.046898, 'median_return': 0.059104, 'mean_absolute_return': 0.069012, 'max_adverse_excursion': -0.195048, 'max_favorable_excursion': 0.147541}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.018679, 'median_return': 0.0214, 'mean_absolute_return': 0.018679, 'max_adverse_excursion': 0.012355, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.022737, 'median_return': 0.03199, 'mean_absolute_return': 0.02475, 'max_adverse_excursion': -0.00805, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.028959, 'median_return': 0.041976, 'mean_absolute_return': 0.028959, 'max_adverse_excursion': 0.001517, 'max_favorable_excursion': 0.05207}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.059291, 'median_return': 0.075995, 'mean_absolute_return': 0.059291, 'max_adverse_excursion': 0.024743, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.092921, 'median_return': 0.095628, 'mean_absolute_return': 0.092921, 'max_adverse_excursion': 0.082251, 'max_favorable_excursion': 0.111345}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.005899, 'median_return': 0.00642, 'mean_absolute_return': 0.015705, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.008339, 'median_return': 0.008981, 'mean_absolute_return': 0.020868, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.018612, 'median_return': 0.017201, 'mean_absolute_return': 0.025832, 'max_adverse_excursion': -0.045393, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.9306, 'avg_return': 0.037999, 'median_return': 0.030922, 'mean_absolute_return': 0.039526, 'max_adverse_excursion': -0.020687, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.8056, 'avg_return': 0.045175, 'median_return': 0.046407, 'mean_absolute_return': 0.075813, 'max_adverse_excursion': -0.195048, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.625}, '10d': {'sample_size': 80, 'hit_rate': 0.6875}, '20d': {'sample_size': 80, 'hit_rate': 0.7375}, '60d': {'sample_size': 80, 'hit_rate': 0.675}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.075, 'both_hit': 43, 'both_miss': 17}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.025, 'both_hit': 41, 'both_miss': 19}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.025, 'both_hit': 46, 'both_miss': 14}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7375, 'secondary_hit_rate': 0.9375, 'primary_minus_secondary': -0.2, 'both_hit': 57, 'both_miss': 3}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.825, 'primary_minus_secondary': -0.15, 'both_hit': 50, 'both_miss': 10}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.008279, 'median_return': 0.011482, 'mean_absolute_return': 0.019576, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.010172, 'median_return': 0.013193, 'mean_absolute_return': 0.02538, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.023507, 'median_return': 0.021536, 'mean_absolute_return': 0.033488, 'max_adverse_excursion': -0.045393, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.044778, 'median_return': 0.032102, 'mean_absolute_return': 0.047526, 'max_adverse_excursion': -0.020687, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.042036, 'median_return': 0.056874, 'mean_absolute_return': 0.093846, 'max_adverse_excursion': -0.195048, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.006075, 'median_return': 0.00745, 'mean_absolute_return': 0.012429, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.031839}, '5d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.009386, 'median_return': 0.010241, 'mean_absolute_return': 0.017133, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.015787, 'median_return': 0.013997, 'mean_absolute_return': 0.018801, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 40, 'hit_rate': 1.0, 'avg_return': 0.035478, 'median_return': 0.03107, 'mean_absolute_return': 0.035478, 'max_adverse_excursion': 0.001535, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 40, 'hit_rate': 0.95, 'avg_return': 0.057863, 'median_return': 0.059104, 'mean_absolute_return': 0.061202, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.131774}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007233`, median `0.009206`, mae `0.01495`
- 5d: sample `60`, hit `0.6833`, avg `0.010309`, median `0.012091`, mae `0.020907`
- 10d: sample `60`, hit `0.7667`, avg `0.01903`, median `0.019171`, mae `0.022852`
- 20d: sample `60`, hit `0.95`, avg `0.033977`, median `0.029072`, mae `0.035209`
- 60d: sample `60`, hit `0.8333`, avg `0.046898`, median `0.059104`, mae `0.069012`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.007009`, median `0.009204`, mae `0.019159`
- 5d: sample `20`, hit `0.55`, avg `0.008189`, median `0.003789`, mae `0.022307`
- 10d: sample `20`, hit `0.55`, avg `0.021497`, median `0.006439`, mae `0.036021`
- 20d: sample `20`, hit `0.9`, avg `0.058581`, median `0.033791`, mae `0.060383`
- 60d: sample `20`, hit `0.8`, avg `0.059106`, median `0.056732`, mae `0.10306`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007233`, median `0.009206`, mae `0.01495`
- 5d: sample `60`, hit `0.6833`, avg `0.010309`, median `0.012091`, mae `0.020907`
- 10d: sample `60`, hit `0.7667`, avg `0.01903`, median `0.019171`, mae `0.022852`
- 20d: sample `60`, hit `0.95`, avg `0.033977`, median `0.029072`, mae `0.035209`
- 60d: sample `60`, hit `0.8333`, avg `0.046898`, median `0.059104`, mae `0.069012`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007233`, median `0.009206`, mae `0.01495`
- 5d: sample `60`, hit `0.6833`, avg `0.010309`, median `0.012091`, mae `0.020907`
- 10d: sample `60`, hit `0.7667`, avg `0.01903`, median `0.019171`, mae `0.022852`
- 20d: sample `60`, hit `0.95`, avg `0.033977`, median `0.029072`, mae `0.035209`
- 60d: sample `60`, hit `0.8333`, avg `0.046898`, median `0.059104`, mae `0.069012`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.007009`, median `0.009204`, mae `0.019159`
- 5d: sample `20`, hit `0.55`, avg `0.008189`, median `0.003789`, mae `0.022307`
- 10d: sample `20`, hit `0.55`, avg `0.021497`, median `0.006439`, mae `0.036021`
- 20d: sample `20`, hit `0.9`, avg `0.058581`, median `0.033791`, mae `0.060383`
- 60d: sample `20`, hit `0.8`, avg `0.059106`, median `0.056732`, mae `0.10306`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007233`, median `0.009206`, mae `0.01495`
- 5d: sample `60`, hit `0.6833`, avg `0.010309`, median `0.012091`, mae `0.020907`
- 10d: sample `60`, hit `0.7667`, avg `0.01903`, median `0.019171`, mae `0.022852`
- 20d: sample `60`, hit `0.95`, avg `0.033977`, median `0.029072`, mae `0.035209`
- 60d: sample `60`, hit `0.8333`, avg `0.046898`, median `0.059104`, mae `0.069012`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007233`, median `0.009206`, mae `0.01495`
- 5d: sample `60`, hit `0.6833`, avg `0.010309`, median `0.012091`, mae `0.020907`
- 10d: sample `60`, hit `0.7667`, avg `0.01903`, median `0.019171`, mae `0.022852`
- 20d: sample `60`, hit `0.95`, avg `0.033977`, median `0.029072`, mae `0.035209`
- 60d: sample `60`, hit `0.8333`, avg `0.046898`, median `0.059104`, mae `0.069012`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.007009`, median `0.009204`, mae `0.019159`
- 5d: sample `20`, hit `0.55`, avg `0.008189`, median `0.003789`, mae `0.022307`
- 10d: sample `20`, hit `0.55`, avg `0.021497`, median `0.006439`, mae `0.036021`
- 20d: sample `20`, hit `0.9`, avg `0.058581`, median `0.033791`, mae `0.060383`
- 60d: sample `20`, hit `0.8`, avg `0.059106`, median `0.056732`, mae `0.10306`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

### aligned_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.006075`, median `0.00745`, mae `0.012429`
- 5d: sample `40`, hit `0.675`, avg `0.009386`, median `0.010241`, mae `0.017133`
- 10d: sample `40`, hit `0.75`, avg `0.015787`, median `0.013997`, mae `0.018801`
- 20d: sample `40`, hit `1.0`, avg `0.035478`, median `0.03107`, mae `0.035478`
- 60d: sample `40`, hit `0.95`, avg `0.057863`, median `0.059104`, mae `0.061202`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.007009`, median `0.009204`, mae `0.019159`
- 5d: sample `20`, hit `0.55`, avg `0.008189`, median `0.003789`, mae `0.022307`
- 10d: sample `20`, hit `0.55`, avg `0.021497`, median `0.006439`, mae `0.036021`
- 20d: sample `20`, hit `0.9`, avg `0.058581`, median `0.033791`, mae `0.060383`
- 60d: sample `20`, hit `0.8`, avg `0.059106`, median `0.056732`, mae `0.10306`

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

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.7`, avg `0.007177`, median `0.009204`, mae `0.016002`
- 5d: sample `80`, hit `0.65`, avg `0.009779`, median `0.010241`, mae `0.021257`
- 10d: sample `80`, hit `0.7125`, avg `0.019647`, median `0.017636`, mae `0.026144`
- 20d: sample `80`, hit `0.9375`, avg `0.040128`, median `0.03107`, mae `0.041502`
- 60d: sample `80`, hit `0.825`, avg `0.04995`, median `0.056874`, mae `0.077524`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007233`, median `0.009206`, mae `0.01495`
- 5d: sample `60`, hit `0.6833`, avg `0.010309`, median `0.012091`, mae `0.020907`
- 10d: sample `60`, hit `0.7667`, avg `0.01903`, median `0.019171`, mae `0.022852`
- 20d: sample `60`, hit `0.95`, avg `0.033977`, median `0.029072`, mae `0.035209`
- 60d: sample `60`, hit `0.8333`, avg `0.046898`, median `0.059104`, mae `0.069012`

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
