# High Confidence Edge Report

Generated at: `2026-08-04T06:18:30.725548+00:00`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.675`, avg `0.006132`, median `0.00745`, mae `0.016352`
- 5d: sample `80`, hit `0.6625`, avg `0.008757`, median `0.008152`, mae `0.019871`
- 10d: sample `80`, hit `0.8`, avg `0.018822`, median `0.021584`, mae `0.026548`
- 20d: sample `80`, hit `0.825`, avg `0.031419`, median `0.033582`, mae `0.038803`
- 60d: sample `80`, hit `0.7625`, avg `0.047019`, median `0.075061`, mae `0.08868`

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
- 3d: sample `8`, hit `0.5`, avg `0.000906`, median `0.012272`, mae `0.018894`
- 5d: sample `8`, hit `0.875`, avg `0.00731`, median `0.009709`, mae `0.013873`
- 10d: sample `8`, hit `0.625`, avg `0.005545`, median `0.011031`, mae `0.018653`
- 20d: sample `8`, hit `1.0`, avg `0.042307`, median `0.058396`, mae `0.042307`
- 60d: sample `8`, hit `0.875`, avg `0.081873`, median `0.113428`, mae `0.093608`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.000906`, median `0.012272`, mae `0.018894`
- 5d: sample `8`, hit `0.875`, avg `0.00731`, median `0.009709`, mae `0.013873`
- 10d: sample `8`, hit `0.625`, avg `0.005545`, median `0.011031`, mae `0.018653`
- 20d: sample `8`, hit `1.0`, avg `0.042307`, median `0.058396`, mae `0.042307`
- 60d: sample `8`, hit `0.875`, avg `0.081873`, median `0.113428`, mae `0.093608`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.006132, 'median_return': 0.00745, 'mean_absolute_return': 0.016352, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.008757, 'median_return': 0.008152, 'mean_absolute_return': 0.019871, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.018822, 'median_return': 0.021584, 'mean_absolute_return': 0.026548, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.825, 'avg_return': 0.031419, 'median_return': 0.033582, 'mean_absolute_return': 0.038803, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.090062}, '60d': {'sample_size': 80, 'hit_rate': 0.7625, 'avg_return': 0.047019, 'median_return': 0.075061, 'mean_absolute_return': 0.08868, 'max_adverse_excursion': -0.179568, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.000906, 'median_return': 0.012272, 'mean_absolute_return': 0.018894, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.00731, 'median_return': 0.009709, 'mean_absolute_return': 0.013873, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005545, 'median_return': 0.011031, 'mean_absolute_return': 0.018653, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.042307, 'median_return': 0.058396, 'mean_absolute_return': 0.042307, 'max_adverse_excursion': 0.011428, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.081873, 'median_return': 0.113428, 'mean_absolute_return': 0.093608, 'max_adverse_excursion': -0.04694, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.006713, 'median_return': 0.00745, 'mean_absolute_return': 0.01607, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.008917, 'median_return': 0.008152, 'mean_absolute_return': 0.020537, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.020297, 'median_return': 0.022558, 'mean_absolute_return': 0.027426, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.8056, 'avg_return': 0.030209, 'median_return': 0.030922, 'mean_absolute_return': 0.038414, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.090062}, '60d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.043146, 'median_return': 0.073403, 'mean_absolute_return': 0.088133, 'max_adverse_excursion': -0.179568, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.5875}, '10d': {'sample_size': 80, 'hit_rate': 0.65}, '20d': {'sample_size': 80, 'hit_rate': 0.65}, '60d': {'sample_size': 80, 'hit_rate': 0.7125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.125, 'both_hit': 31, 'both_miss': 9}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.075, 'both_hit': 30, 'both_miss': 10}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.05, 'both_hit': 34, 'both_miss': 6}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.025, 'both_hit': 33, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.025, 'both_hit': 38, 'both_miss': 2}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.005877, 'median_return': 0.011534, 'mean_absolute_return': 0.018675, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.009163, 'median_return': 0.009709, 'mean_absolute_return': 0.022447, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.02075, 'median_return': 0.024811, 'mean_absolute_return': 0.030795, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.03225, 'median_return': 0.033791, 'mean_absolute_return': 0.040819, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.090062}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.040754, 'median_return': 0.082251, 'mean_absolute_return': 0.095609, 'max_adverse_excursion': -0.179568, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.006897, 'median_return': 0.006315, 'mean_absolute_return': 0.009383, 'max_adverse_excursion': -0.017627, 'max_favorable_excursion': 0.019003}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.007538, 'median_return': 0.008152, 'mean_absolute_return': 0.012142, 'max_adverse_excursion': -0.018034, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 20, 'hit_rate': 0.9, 'avg_return': 0.013037, 'median_return': 0.012215, 'mean_absolute_return': 0.013808, 'max_adverse_excursion': -0.007491, 'max_favorable_excursion': 0.037487}, '20d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.028924, 'median_return': 0.033582, 'mean_absolute_return': 0.032756, 'max_adverse_excursion': -0.015145, 'max_favorable_excursion': 0.057835}, '60d': {'sample_size': 20, 'hit_rate': 0.95, 'avg_return': 0.065812, 'median_return': 0.065995, 'mean_absolute_return': 0.067894, 'max_adverse_excursion': -0.020815, 'max_favorable_excursion': 0.114629}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.775`, avg `0.007184`, median `0.010897`, mae `0.012606`
- 5d: sample `40`, hit `0.75`, avg `0.009791`, median `0.010241`, mae `0.01559`
- 10d: sample `40`, hit `0.85`, avg `0.015496`, median `0.014276`, mae `0.018804`
- 20d: sample `40`, hit `0.825`, avg `0.032217`, median `0.029072`, mae `0.036033`
- 60d: sample `40`, hit `0.95`, avg `0.078878`, median `0.084597`, mae `0.082266`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009368`, median `0.013443`, mae `0.020259`
- 5d: sample `20`, hit `0.65`, avg `0.013534`, median `0.010394`, mae `0.022581`
- 10d: sample `20`, hit `0.8`, avg `0.023771`, median `0.031262`, mae `0.034592`
- 20d: sample `20`, hit `0.85`, avg `0.037881`, median `0.041262`, mae `0.04034`
- 60d: sample `20`, hit `0.6`, avg `0.014745`, median `0.061203`, mae `0.101732`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.775`, avg `0.007184`, median `0.010897`, mae `0.012606`
- 5d: sample `40`, hit `0.75`, avg `0.009791`, median `0.010241`, mae `0.01559`
- 10d: sample `40`, hit `0.85`, avg `0.015496`, median `0.014276`, mae `0.018804`
- 20d: sample `40`, hit `0.825`, avg `0.032217`, median `0.029072`, mae `0.036033`
- 60d: sample `40`, hit `0.95`, avg `0.078878`, median `0.084597`, mae `0.082266`

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
- 3d: sample `40`, hit `0.775`, avg `0.007184`, median `0.010897`, mae `0.012606`
- 5d: sample `40`, hit `0.75`, avg `0.009791`, median `0.010241`, mae `0.01559`
- 10d: sample `40`, hit `0.85`, avg `0.015496`, median `0.014276`, mae `0.018804`
- 20d: sample `40`, hit `0.825`, avg `0.032217`, median `0.029072`, mae `0.036033`
- 60d: sample `40`, hit `0.95`, avg `0.078878`, median `0.084597`, mae `0.082266`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `0.000792`, median `-0.0002`, mae `0.019938`
- 5d: sample `20`, hit `0.5`, avg `0.00191`, median `0.004613`, mae `0.025721`
- 10d: sample `20`, hit `0.7`, avg `0.020524`, median `0.029996`, mae `0.033993`
- 20d: sample `20`, hit `0.8`, avg `0.02336`, median `0.034151`, mae `0.042809`
- 60d: sample `20`, hit `0.55`, avg `0.015573`, median `0.056874`, mae `0.088457`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009368`, median `0.013443`, mae `0.020259`
- 5d: sample `20`, hit `0.65`, avg `0.013534`, median `0.010394`, mae `0.022581`
- 10d: sample `20`, hit `0.8`, avg `0.023771`, median `0.031262`, mae `0.034592`
- 20d: sample `20`, hit `0.85`, avg `0.037881`, median `0.041262`, mae `0.04034`
- 60d: sample `20`, hit `0.6`, avg `0.014745`, median `0.061203`, mae `0.101732`

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
- 3d: sample `80`, hit `0.675`, avg `0.006132`, median `0.00745`, mae `0.016352`
- 5d: sample `80`, hit `0.6625`, avg `0.008757`, median `0.008152`, mae `0.019871`
- 10d: sample `80`, hit `0.8`, avg `0.018822`, median `0.021584`, mae `0.026548`
- 20d: sample `80`, hit `0.825`, avg `0.031419`, median `0.033582`, mae `0.038803`
- 60d: sample `80`, hit `0.7625`, avg `0.047019`, median `0.075061`, mae `0.08868`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.005053`, median `0.006315`, mae `0.01505`
- 5d: sample `60`, hit `0.6667`, avg `0.007164`, median `0.008152`, mae `0.018967`
- 10d: sample `60`, hit `0.8`, avg `0.017172`, median `0.017636`, mae `0.023867`
- 20d: sample `60`, hit `0.8167`, avg `0.029265`, median `0.030922`, mae `0.038291`
- 60d: sample `60`, hit `0.8167`, avg `0.057777`, median `0.082988`, mae `0.08433`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.675`, avg `0.006132`, median `0.00745`, mae `0.016352`
- 5d: sample `80`, hit `0.6625`, avg `0.008757`, median `0.008152`, mae `0.019871`
- 10d: sample `80`, hit `0.8`, avg `0.018822`, median `0.021584`, mae `0.026548`
- 20d: sample `80`, hit `0.825`, avg `0.031419`, median `0.033582`, mae `0.038803`
- 60d: sample `80`, hit `0.7625`, avg `0.047019`, median `0.075061`, mae `0.08868`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.005053`, median `0.006315`, mae `0.01505`
- 5d: sample `60`, hit `0.6667`, avg `0.007164`, median `0.008152`, mae `0.018967`
- 10d: sample `60`, hit `0.8`, avg `0.017172`, median `0.017636`, mae `0.023867`
- 20d: sample `60`, hit `0.8167`, avg `0.029265`, median `0.030922`, mae `0.038291`
- 60d: sample `60`, hit `0.8167`, avg `0.057777`, median `0.082988`, mae `0.08433`

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
