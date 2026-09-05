# High Confidence Edge Report

Generated at: `2026-09-05T00:55:28.598161+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.6625`, avg `0.005507`, median `0.010897`, mae `0.018151`
- 5d: sample `80`, hit `0.6625`, avg `0.007676`, median `0.012604`, mae `0.022289`
- 10d: sample `80`, hit `0.675`, avg `0.013144`, median `0.018412`, mae `0.031959`
- 20d: sample `80`, hit `0.825`, avg `0.027525`, median `0.032954`, mae `0.040367`
- 60d: sample `80`, hit `0.7125`, avg `0.046956`, median `0.064286`, mae `0.075038`

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
- 3d: sample `8`, hit `0.5`, avg `-0.010646`, median `0.012525`, mae `0.0303`
- 5d: sample `8`, hit `0.375`, avg `-0.011518`, median `-0.011157`, mae `0.028504`
- 10d: sample `8`, hit `0.375`, avg `-0.011322`, median `-0.00304`, mae `0.034833`
- 20d: sample `8`, hit `0.5`, avg `-0.006973`, median `0.000994`, mae `0.03565`
- 60d: sample `8`, hit `0.375`, avg `-0.03393`, median `-0.003135`, mae `0.073697`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.004958`, median `0.017238`, mae `0.018589`
- 5d: sample `8`, hit `0.75`, avg `0.007918`, median `0.009709`, mae `0.01572`
- 10d: sample `8`, hit `0.625`, avg `0.012384`, median `0.023826`, mae `0.021171`
- 20d: sample `8`, hit `1.0`, avg `0.052468`, median `0.058396`, mae `0.052468`
- 60d: sample `8`, hit `0.875`, avg `0.080282`, median `0.099838`, mae `0.091772`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.004958, 'median_return': 0.017238, 'mean_absolute_return': 0.018589, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.007918, 'median_return': 0.009709, 'mean_absolute_return': 0.01572, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.03199}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.012384, 'median_return': 0.023826, 'mean_absolute_return': 0.021171, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.041976}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.052468, 'median_return': 0.058396, 'mean_absolute_return': 0.052468, 'max_adverse_excursion': 0.01983, 'max_favorable_excursion': 0.075995}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.080282, 'median_return': 0.099838, 'mean_absolute_return': 0.091772, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.005568, 'median_return': 0.009349, 'mean_absolute_return': 0.018102, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.007649, 'median_return': 0.013411, 'mean_absolute_return': 0.023019, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.013228, 'median_return': 0.018412, 'mean_absolute_return': 0.033158, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.8056, 'avg_return': 0.024753, 'median_return': 0.030922, 'mean_absolute_return': 0.039022, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.043253, 'median_return': 0.062103, 'mean_absolute_return': 0.073178, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.3375}, '5d': {'sample_size': 80, 'hit_rate': 0.3375}, '10d': {'sample_size': 80, 'hit_rate': 0.325}, '20d': {'sample_size': 80, 'hit_rate': 0.175}, '60d': {'sample_size': 80, 'hit_rate': 0.2875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.325, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.325, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.175, 'secondary_hit_rate': 0.825, 'primary_minus_secondary': -0.65, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.425, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.003799, 'median_return': 0.00745, 'mean_absolute_return': 0.018242, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.0065, 'median_return': 0.012091, 'mean_absolute_return': 0.02167, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.049196}, '10d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.011197, 'median_return': 0.019171, 'mean_absolute_return': 0.031931, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.078607}, '20d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.025015, 'median_return': 0.032954, 'mean_absolute_return': 0.042031, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.053677, 'median_return': 0.069306, 'mean_absolute_return': 0.075565, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.01063, 'median_return': 0.013598, 'mean_absolute_return': 0.017876, 'max_adverse_excursion': -0.017591, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.011203, 'median_return': 0.018242, 'mean_absolute_return': 0.024147, 'max_adverse_excursion': -0.030861, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.018985, 'median_return': 0.018412, 'mean_absolute_return': 0.032044, 'max_adverse_excursion': -0.037388, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 20, 'hit_rate': 0.95, 'avg_return': 0.035053, 'median_return': 0.033791, 'mean_absolute_return': 0.035374, 'max_adverse_excursion': -0.00321, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': 0.026792, 'median_return': -0.001675, 'mean_absolute_return': 0.073457, 'max_adverse_excursion': -0.122187, 'max_favorable_excursion': 0.19145}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007795`, median `0.012272`, mae `0.016501`
- 5d: sample `60`, hit `0.7`, avg `0.010169`, median `0.013852`, mae `0.020911`
- 10d: sample `60`, hit `0.7`, avg `0.014295`, median `0.018352`, mae `0.028625`
- 20d: sample `60`, hit `0.8667`, avg `0.032009`, median `0.033597`, mae `0.040637`
- 60d: sample `60`, hit `0.7167`, avg `0.050446`, median `0.062103`, mae `0.072652`

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
- 3d: sample `40`, hit `0.7`, avg `0.006378`, median `0.012217`, mae `0.015814`
- 5d: sample `40`, hit `0.725`, avg `0.009651`, median `0.013411`, mae `0.019294`
- 10d: sample `40`, hit `0.725`, avg `0.01195`, median `0.018352`, mae `0.026916`
- 20d: sample `40`, hit `0.825`, avg `0.030487`, median `0.033597`, mae `0.043268`
- 60d: sample `40`, hit `0.85`, avg `0.062274`, median `0.077143`, mae `0.072249`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007795`, median `0.012272`, mae `0.016501`
- 5d: sample `60`, hit `0.7`, avg `0.010169`, median `0.013852`, mae `0.020911`
- 10d: sample `60`, hit `0.7`, avg `0.014295`, median `0.018352`, mae `0.028625`
- 20d: sample `60`, hit `0.8667`, avg `0.032009`, median `0.033597`, mae `0.040637`
- 60d: sample `60`, hit `0.7167`, avg `0.050446`, median `0.062103`, mae `0.072652`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.6625`, avg `0.005507`, median `0.010897`, mae `0.018151`
- 5d: sample `80`, hit `0.6625`, avg `0.007676`, median `0.012604`, mae `0.022289`
- 10d: sample `80`, hit `0.675`, avg `0.013144`, median `0.018412`, mae `0.031959`
- 20d: sample `80`, hit `0.825`, avg `0.027525`, median `0.032954`, mae `0.040367`
- 60d: sample `80`, hit `0.7125`, avg `0.046956`, median `0.064286`, mae `0.075038`

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
