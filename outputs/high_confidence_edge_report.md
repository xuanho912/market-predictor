# High Confidence Edge Report

Generated at: `2026-06-22T16:01:43.911209+00:00`

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
- 3d: sample `80`, hit `0.475`, avg `-0.000142`, median `-0.000756`, mae `0.013263`
- 5d: sample `80`, hit `0.4625`, avg `-0.003108`, median `-0.001796`, mae `0.016093`
- 10d: sample `80`, hit `0.4125`, avg `-0.002479`, median `-0.002528`, mae `0.0207`
- 20d: sample `80`, hit `0.675`, avg `0.007118`, median `0.015404`, mae `0.030263`
- 60d: sample `80`, hit `0.6125`, avg `0.023037`, median `0.043741`, mae `0.062448`

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
- 3d: sample `8`, hit `0.375`, avg `-0.005957`, median `-0.001811`, mae `0.014756`
- 5d: sample `8`, hit `0.0`, avg `-0.018169`, median `-0.013034`, mae `0.018169`
- 10d: sample `8`, hit `0.625`, avg `0.004766`, median `0.006235`, mae `0.01143`
- 20d: sample `8`, hit `1.0`, avg `0.028135`, median `0.031196`, mae `0.028135`
- 60d: sample `8`, hit `1.0`, avg `0.075992`, median `0.092646`, mae `0.075992`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.003193`, median `-0.002654`, mae `0.006009`
- 5d: sample `8`, hit `0.625`, avg `-0.003537`, median `0.003714`, mae `0.012412`
- 10d: sample `8`, hit `0.5`, avg `-6.8e-05`, median `0.003491`, mae `0.01307`
- 20d: sample `8`, hit `0.875`, avg `0.000868`, median `0.012291`, mae `0.024741`
- 60d: sample `8`, hit `0.25`, avg `-0.037342`, median `-0.055327`, mae `0.056523`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': -0.000142, 'median_return': -0.000756, 'mean_absolute_return': 0.013263, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.003108, 'median_return': -0.001796, 'mean_absolute_return': 0.016093, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 80, 'hit_rate': 0.4125, 'avg_return': -0.002479, 'median_return': -0.002528, 'mean_absolute_return': 0.0207, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.007118, 'median_return': 0.015404, 'mean_absolute_return': 0.030263, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.023037, 'median_return': 0.043741, 'mean_absolute_return': 0.062448, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.156405}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.003193, 'median_return': -0.002654, 'mean_absolute_return': 0.006009, 'max_adverse_excursion': -0.010176, 'max_favorable_excursion': 0.006722}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.003537, 'median_return': 0.003714, 'mean_absolute_return': 0.012412, 'max_adverse_excursion': -0.023712, 'max_favorable_excursion': 0.017467}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -6.8e-05, 'median_return': 0.003491, 'mean_absolute_return': 0.01307, 'max_adverse_excursion': -0.029518, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.000868, 'median_return': 0.012291, 'mean_absolute_return': 0.024741, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.037342, 'median_return': -0.055327, 'mean_absolute_return': 0.056523, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.043741}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.000197, 'median_return': 0.000453, 'mean_absolute_return': 0.01407, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.00306, 'median_return': -0.002002, 'mean_absolute_return': 0.016502, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.002747, 'median_return': -0.003263, 'mean_absolute_return': 0.021548, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.007812, 'median_return': 0.01666, 'mean_absolute_return': 0.030876, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.029746, 'median_return': 0.054522, 'mean_absolute_return': 0.063106, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.156405}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.4625}, '10d': {'sample_size': 80, 'hit_rate': 0.4125}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.6125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': -0.025, 'both_hit': 29, 'both_miss': 31}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 30, 'both_miss': 30}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': -0.075, 'both_hit': 26, 'both_miss': 34}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.2, 'both_hit': 36, 'both_miss': 24}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.2, 'both_hit': 31, 'both_miss': 29}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.001315, 'median_return': 0.000453, 'mean_absolute_return': 0.015886, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.001529, 'median_return': 0.000208, 'mean_absolute_return': 0.017895, 'max_adverse_excursion': -0.045904, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.001982, 'median_return': -0.001083, 'mean_absolute_return': 0.020394, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.016863, 'median_return': 0.028626, 'mean_absolute_return': 0.033176, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.040854, 'median_return': 0.062356, 'mean_absolute_return': 0.067668, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.156405}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.001599, 'median_return': -0.001166, 'mean_absolute_return': 0.010641, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.004686, 'median_return': -0.001796, 'mean_absolute_return': 0.014291, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.03091}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.00694, 'median_return': -0.007491, 'mean_absolute_return': 0.021006, 'max_adverse_excursion': -0.050724, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.002628, 'median_return': 0.007004, 'mean_absolute_return': 0.027349, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.00522, 'median_return': 0.010234, 'mean_absolute_return': 0.057228, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.114016}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.001599`, median `-0.001166`, mae `0.010641`
- 5d: sample `40`, hit `0.425`, avg `-0.004686`, median `-0.001796`, mae `0.014291`
- 10d: sample `40`, hit `0.375`, avg `-0.00694`, median `-0.007491`, mae `0.021006`
- 20d: sample `40`, hit `0.575`, avg `-0.002628`, median `0.007004`, mae `0.027349`
- 60d: sample `40`, hit `0.5`, avg `0.00522`, median `0.010234`, mae `0.057228`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.001315`, median `0.000453`, mae `0.015886`
- 5d: sample `40`, hit `0.5`, avg `-0.001529`, median `0.000208`, mae `0.017895`
- 10d: sample `40`, hit `0.45`, avg `0.001982`, median `-0.001083`, mae `0.020394`
- 20d: sample `40`, hit `0.775`, avg `0.016863`, median `0.028626`, mae `0.033176`
- 60d: sample `40`, hit `0.725`, avg `0.040854`, median `0.062356`, mae `0.067668`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.001599`, median `-0.001166`, mae `0.010641`
- 5d: sample `40`, hit `0.425`, avg `-0.004686`, median `-0.001796`, mae `0.014291`
- 10d: sample `40`, hit `0.375`, avg `-0.00694`, median `-0.007491`, mae `0.021006`
- 20d: sample `40`, hit `0.575`, avg `-0.002628`, median `0.007004`, mae `0.027349`
- 60d: sample `40`, hit `0.5`, avg `0.00522`, median `0.010234`, mae `0.057228`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.001315`, median `0.000453`, mae `0.015886`
- 5d: sample `40`, hit `0.5`, avg `-0.001529`, median `0.000208`, mae `0.017895`
- 10d: sample `40`, hit `0.45`, avg `0.001982`, median `-0.001083`, mae `0.020394`
- 20d: sample `40`, hit `0.775`, avg `0.016863`, median `0.028626`, mae `0.033176`
- 60d: sample `40`, hit `0.725`, avg `0.040854`, median `0.062356`, mae `0.067668`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.001315`, median `0.000453`, mae `0.015886`
- 5d: sample `40`, hit `0.5`, avg `-0.001529`, median `0.000208`, mae `0.017895`
- 10d: sample `40`, hit `0.45`, avg `0.001982`, median `-0.001083`, mae `0.020394`
- 20d: sample `40`, hit `0.775`, avg `0.016863`, median `0.028626`, mae `0.033176`
- 60d: sample `40`, hit `0.725`, avg `0.040854`, median `0.062356`, mae `0.067668`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.001599`, median `-0.001166`, mae `0.010641`
- 5d: sample `40`, hit `0.425`, avg `-0.004686`, median `-0.001796`, mae `0.014291`
- 10d: sample `40`, hit `0.375`, avg `-0.00694`, median `-0.007491`, mae `0.021006`
- 20d: sample `40`, hit `0.575`, avg `-0.002628`, median `0.007004`, mae `0.027349`
- 60d: sample `40`, hit `0.5`, avg `0.00522`, median `0.010234`, mae `0.057228`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.001315`, median `0.000453`, mae `0.015886`
- 5d: sample `40`, hit `0.5`, avg `-0.001529`, median `0.000208`, mae `0.017895`
- 10d: sample `40`, hit `0.45`, avg `0.001982`, median `-0.001083`, mae `0.020394`
- 20d: sample `40`, hit `0.775`, avg `0.016863`, median `0.028626`, mae `0.033176`
- 60d: sample `40`, hit `0.725`, avg `0.040854`, median `0.062356`, mae `0.067668`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- 3d: sample `40`, hit `0.45`, avg `-0.001599`, median `-0.001166`, mae `0.010641`
- 5d: sample `40`, hit `0.425`, avg `-0.004686`, median `-0.001796`, mae `0.014291`
- 10d: sample `40`, hit `0.375`, avg `-0.00694`, median `-0.007491`, mae `0.021006`
- 20d: sample `40`, hit `0.575`, avg `-0.002628`, median `0.007004`, mae `0.027349`
- 60d: sample `40`, hit `0.5`, avg `0.00522`, median `0.010234`, mae `0.057228`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.001315`, median `0.000453`, mae `0.015886`
- 5d: sample `40`, hit `0.5`, avg `-0.001529`, median `0.000208`, mae `0.017895`
- 10d: sample `40`, hit `0.45`, avg `0.001982`, median `-0.001083`, mae `0.020394`
- 20d: sample `40`, hit `0.775`, avg `0.016863`, median `0.028626`, mae `0.033176`
- 60d: sample `40`, hit `0.725`, avg `0.040854`, median `0.062356`, mae `0.067668`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.001315`, median `0.000453`, mae `0.015886`
- 5d: sample `40`, hit `0.5`, avg `-0.001529`, median `0.000208`, mae `0.017895`
- 10d: sample `40`, hit `0.45`, avg `0.001982`, median `-0.001083`, mae `0.020394`
- 20d: sample `40`, hit `0.775`, avg `0.016863`, median `0.028626`, mae `0.033176`
- 60d: sample `40`, hit `0.725`, avg `0.040854`, median `0.062356`, mae `0.067668`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.475`, avg `-0.000142`, median `-0.000756`, mae `0.013263`
- 5d: sample `80`, hit `0.4625`, avg `-0.003108`, median `-0.001796`, mae `0.016093`
- 10d: sample `80`, hit `0.4125`, avg `-0.002479`, median `-0.002528`, mae `0.0207`
- 20d: sample `80`, hit `0.675`, avg `0.007118`, median `0.015404`, mae `0.030263`
- 60d: sample `80`, hit `0.6125`, avg `0.023037`, median `0.043741`, mae `0.062448`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.475`, avg `-0.000142`, median `-0.000756`, mae `0.013263`
- 5d: sample `80`, hit `0.4625`, avg `-0.003108`, median `-0.001796`, mae `0.016093`
- 10d: sample `80`, hit `0.4125`, avg `-0.002479`, median `-0.002528`, mae `0.0207`
- 20d: sample `80`, hit `0.675`, avg `0.007118`, median `0.015404`, mae `0.030263`
- 60d: sample `80`, hit `0.6125`, avg `0.023037`, median `0.043741`, mae `0.062448`

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
