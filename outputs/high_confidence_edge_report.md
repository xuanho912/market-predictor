# High Confidence Edge Report

Generated at: `2026-06-22T15:54:58.793958+00:00`

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
- 3d: sample `80`, hit `0.4625`, avg `-0.000551`, median `-0.001166`, mae `0.013041`
- 5d: sample `80`, hit `0.45`, avg `-0.003843`, median `-0.003328`, mae `0.016293`
- 10d: sample `80`, hit `0.4`, avg `-0.002762`, median `-0.003263`, mae `0.02034`
- 20d: sample `80`, hit `0.675`, avg `0.007006`, median `0.015404`, mae `0.030151`
- 60d: sample `80`, hit `0.625`, avg `0.024482`, median `0.046132`, mae `0.063137`

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
- 3d: sample `8`, hit `0.375`, avg `-0.005834`, median `-0.001811`, mae `0.014879`
- 5d: sample `8`, hit `0.125`, avg `-0.017293`, median `-0.013034`, mae `0.017345`
- 10d: sample `8`, hit `0.5`, avg `0.003857`, median `0.006235`, mae `0.010826`
- 20d: sample `8`, hit `1.0`, avg `0.0278`, median `0.031196`, mae `0.0278`
- 60d: sample `8`, hit `1.0`, avg `0.07374`, median `0.085257`, mae `0.07374`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.003193`, median `-0.002654`, mae `0.006009`
- 5d: sample `8`, hit `0.625`, avg `-0.003537`, median `0.003714`, mae `0.012412`
- 10d: sample `8`, hit `0.5`, avg `-6.8e-05`, median `0.003491`, mae `0.01307`
- 20d: sample `8`, hit `0.875`, avg `0.000868`, median `0.012291`, mae `0.024741`
- 60d: sample `8`, hit `0.25`, avg `-0.037342`, median `-0.055327`, mae `0.056523`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.000551, 'median_return': -0.001166, 'mean_absolute_return': 0.013041, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.003843, 'median_return': -0.003328, 'mean_absolute_return': 0.016293, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.002762, 'median_return': -0.003263, 'mean_absolute_return': 0.02034, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.007006, 'median_return': 0.015404, 'mean_absolute_return': 0.030151, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.024482, 'median_return': 0.046132, 'mean_absolute_return': 0.063137, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.156405}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.003193, 'median_return': -0.002654, 'mean_absolute_return': 0.006009, 'max_adverse_excursion': -0.010176, 'max_favorable_excursion': 0.006722}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.003537, 'median_return': 0.003714, 'mean_absolute_return': 0.012412, 'max_adverse_excursion': -0.023712, 'max_favorable_excursion': 0.017467}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -6.8e-05, 'median_return': 0.003491, 'mean_absolute_return': 0.01307, 'max_adverse_excursion': -0.029518, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.000868, 'median_return': 0.012291, 'mean_absolute_return': 0.024741, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.037342, 'median_return': -0.055327, 'mean_absolute_return': 0.056523, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.043741}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.000258, 'median_return': -0.000722, 'mean_absolute_return': 0.013823, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.003877, 'median_return': -0.004389, 'mean_absolute_return': 0.016725, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.003061, 'median_return': -0.004053, 'mean_absolute_return': 0.021148, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.007688, 'median_return': 0.01666, 'mean_absolute_return': 0.030752, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.031351, 'median_return': 0.054765, 'mean_absolute_return': 0.063872, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.156405}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.4}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': -0.025, 'both_hit': 28, 'both_miss': 32}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.075, 'both_hit': 29, 'both_miss': 31}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': -0.075, 'both_hit': 25, 'both_miss': 35}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.2, 'both_hit': 36, 'both_miss': 24}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.2, 'both_hit': 32, 'both_miss': 28}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.001315, 'median_return': 0.000453, 'mean_absolute_return': 0.015886, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.001529, 'median_return': 0.000208, 'mean_absolute_return': 0.017895, 'max_adverse_excursion': -0.045904, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.001982, 'median_return': -0.001083, 'mean_absolute_return': 0.020394, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.016863, 'median_return': 0.028626, 'mean_absolute_return': 0.033176, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.040854, 'median_return': 0.062356, 'mean_absolute_return': 0.067668, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.156405}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.002417, 'median_return': -0.002654, 'mean_absolute_return': 0.010197, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.006156, 'median_return': -0.004389, 'mean_absolute_return': 0.014692, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.03091}, '10d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.007505, 'median_return': -0.007491, 'mean_absolute_return': 0.020287, 'max_adverse_excursion': -0.050724, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.002852, 'median_return': 0.007004, 'mean_absolute_return': 0.027126, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.00811, 'median_return': 0.031838, 'mean_absolute_return': 0.058606, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.114016}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.002417`, median `-0.002654`, mae `0.010197`
- 5d: sample `40`, hit `0.4`, avg `-0.006156`, median `-0.004389`, mae `0.014692`
- 10d: sample `40`, hit `0.35`, avg `-0.007505`, median `-0.007491`, mae `0.020287`
- 20d: sample `40`, hit `0.575`, avg `-0.002852`, median `0.007004`, mae `0.027126`
- 60d: sample `40`, hit `0.525`, avg `0.00811`, median `0.031838`, mae `0.058606`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.001315`, median `0.000453`, mae `0.015886`
- 5d: sample `40`, hit `0.5`, avg `-0.001529`, median `0.000208`, mae `0.017895`
- 10d: sample `40`, hit `0.45`, avg `0.001982`, median `-0.001083`, mae `0.020394`
- 20d: sample `40`, hit `0.775`, avg `0.016863`, median `0.028626`, mae `0.033176`
- 60d: sample `40`, hit `0.725`, avg `0.040854`, median `0.062356`, mae `0.067668`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.002417`, median `-0.002654`, mae `0.010197`
- 5d: sample `40`, hit `0.4`, avg `-0.006156`, median `-0.004389`, mae `0.014692`
- 10d: sample `40`, hit `0.35`, avg `-0.007505`, median `-0.007491`, mae `0.020287`
- 20d: sample `40`, hit `0.575`, avg `-0.002852`, median `0.007004`, mae `0.027126`
- 60d: sample `40`, hit `0.525`, avg `0.00811`, median `0.031838`, mae `0.058606`

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
- 3d: sample `40`, hit `0.425`, avg `-0.002417`, median `-0.002654`, mae `0.010197`
- 5d: sample `40`, hit `0.4`, avg `-0.006156`, median `-0.004389`, mae `0.014692`
- 10d: sample `40`, hit `0.35`, avg `-0.007505`, median `-0.007491`, mae `0.020287`
- 20d: sample `40`, hit `0.575`, avg `-0.002852`, median `0.007004`, mae `0.027126`
- 60d: sample `40`, hit `0.525`, avg `0.00811`, median `0.031838`, mae `0.058606`

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
- 3d: sample `40`, hit `0.425`, avg `-0.002417`, median `-0.002654`, mae `0.010197`
- 5d: sample `40`, hit `0.4`, avg `-0.006156`, median `-0.004389`, mae `0.014692`
- 10d: sample `40`, hit `0.35`, avg `-0.007505`, median `-0.007491`, mae `0.020287`
- 20d: sample `40`, hit `0.575`, avg `-0.002852`, median `0.007004`, mae `0.027126`
- 60d: sample `40`, hit `0.525`, avg `0.00811`, median `0.031838`, mae `0.058606`

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
- 3d: sample `80`, hit `0.4625`, avg `-0.000551`, median `-0.001166`, mae `0.013041`
- 5d: sample `80`, hit `0.45`, avg `-0.003843`, median `-0.003328`, mae `0.016293`
- 10d: sample `80`, hit `0.4`, avg `-0.002762`, median `-0.003263`, mae `0.02034`
- 20d: sample `80`, hit `0.675`, avg `0.007006`, median `0.015404`, mae `0.030151`
- 60d: sample `80`, hit `0.625`, avg `0.024482`, median `0.046132`, mae `0.063137`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.000551`, median `-0.001166`, mae `0.013041`
- 5d: sample `80`, hit `0.45`, avg `-0.003843`, median `-0.003328`, mae `0.016293`
- 10d: sample `80`, hit `0.4`, avg `-0.002762`, median `-0.003263`, mae `0.02034`
- 20d: sample `80`, hit `0.675`, avg `0.007006`, median `0.015404`, mae `0.030151`
- 60d: sample `80`, hit `0.625`, avg `0.024482`, median `0.046132`, mae `0.063137`

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
