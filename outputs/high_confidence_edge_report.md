# High Confidence Edge Report

Generated at: `2026-06-22T23:54:26.866892+00:00`

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
- 3d: sample `80`, hit `0.4625`, avg `-0.000697`, median `-0.001166`, mae `0.013866`
- 5d: sample `80`, hit `0.4375`, avg `-0.004072`, median `-0.004389`, mae `0.016818`
- 10d: sample `80`, hit `0.4`, avg `-0.003143`, median `-0.003263`, mae `0.020039`
- 20d: sample `80`, hit `0.6625`, avg `0.006565`, median `0.012958`, mae `0.029814`
- 60d: sample `80`, hit `0.625`, avg `0.023782`, median `0.043741`, mae `0.062834`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.000697, 'median_return': -0.001166, 'mean_absolute_return': 0.013866, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.004072, 'median_return': -0.004389, 'mean_absolute_return': 0.016818, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.003143, 'median_return': -0.003263, 'mean_absolute_return': 0.020039, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.006565, 'median_return': 0.012958, 'mean_absolute_return': 0.029814, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.023782, 'median_return': 0.043741, 'mean_absolute_return': 0.062834, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.156405}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.003193, 'median_return': -0.002654, 'mean_absolute_return': 0.006009, 'max_adverse_excursion': -0.010176, 'max_favorable_excursion': 0.006722}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.003537, 'median_return': 0.003714, 'mean_absolute_return': 0.012412, 'max_adverse_excursion': -0.023712, 'max_favorable_excursion': 0.017467}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -6.8e-05, 'median_return': 0.003491, 'mean_absolute_return': 0.01307, 'max_adverse_excursion': -0.029518, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.000868, 'median_return': 0.012291, 'mean_absolute_return': 0.024741, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.037342, 'median_return': -0.055327, 'mean_absolute_return': 0.056523, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.043741}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.000419, 'median_return': -0.000722, 'mean_absolute_return': 0.01474, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.004131, 'median_return': -0.006371, 'mean_absolute_return': 0.017308, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.003484, 'median_return': -0.004053, 'mean_absolute_return': 0.020814, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.007198, 'median_return': 0.014918, 'mean_absolute_return': 0.030378, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.030574, 'median_return': 0.054522, 'mean_absolute_return': 0.063535, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.156405}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.4}, '20d': {'sample_size': 80, 'hit_rate': 0.6625}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.0, 'both_hit': 37, 'both_miss': 43}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.0, 'both_hit': 35, 'both_miss': 45}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.0, 'both_hit': 32, 'both_miss': 48}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': 0.0, 'both_hit': 53, 'both_miss': 27}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.000229, 'median_return': -0.000756, 'mean_absolute_return': 0.016526, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.002589, 'median_return': -0.003328, 'mean_absolute_return': 0.018014, 'max_adverse_excursion': -0.045904, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': 0.00027, 'median_return': -0.001222, 'mean_absolute_return': 0.01924, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.053454}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.016728, 'median_return': 0.028626, 'mean_absolute_return': 0.033041, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.040788, 'median_return': 0.062356, 'mean_absolute_return': 0.067602, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.156405}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.001164, 'median_return': -0.001166, 'mean_absolute_return': 0.011207, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.005555, 'median_return': -0.004389, 'mean_absolute_return': 0.015622, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.036593}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.006555, 'median_return': -0.007491, 'mean_absolute_return': 0.020839, 'max_adverse_excursion': -0.050724, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.003598, 'median_return': 0.004543, 'mean_absolute_return': 0.026588, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.006776, 'median_return': 0.031838, 'mean_absolute_return': 0.058065, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.114016}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.001164`, median `-0.001166`, mae `0.011207`
- 5d: sample `40`, hit `0.4`, avg `-0.005555`, median `-0.004389`, mae `0.015622`
- 10d: sample `40`, hit `0.375`, avg `-0.006555`, median `-0.007491`, mae `0.020839`
- 20d: sample `40`, hit `0.55`, avg `-0.003598`, median `0.004543`, mae `0.026588`
- 60d: sample `40`, hit `0.525`, avg `0.006776`, median `0.031838`, mae `0.058065`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000229`, median `-0.000756`, mae `0.016526`
- 5d: sample `40`, hit `0.475`, avg `-0.002589`, median `-0.003328`, mae `0.018014`
- 10d: sample `40`, hit `0.425`, avg `0.00027`, median `-0.001222`, mae `0.01924`
- 20d: sample `40`, hit `0.775`, avg `0.016728`, median `0.028626`, mae `0.033041`
- 60d: sample `40`, hit `0.725`, avg `0.040788`, median `0.062356`, mae `0.067602`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.001164`, median `-0.001166`, mae `0.011207`
- 5d: sample `40`, hit `0.4`, avg `-0.005555`, median `-0.004389`, mae `0.015622`
- 10d: sample `40`, hit `0.375`, avg `-0.006555`, median `-0.007491`, mae `0.020839`
- 20d: sample `40`, hit `0.55`, avg `-0.003598`, median `0.004543`, mae `0.026588`
- 60d: sample `40`, hit `0.525`, avg `0.006776`, median `0.031838`, mae `0.058065`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000229`, median `-0.000756`, mae `0.016526`
- 5d: sample `40`, hit `0.475`, avg `-0.002589`, median `-0.003328`, mae `0.018014`
- 10d: sample `40`, hit `0.425`, avg `0.00027`, median `-0.001222`, mae `0.01924`
- 20d: sample `40`, hit `0.775`, avg `0.016728`, median `0.028626`, mae `0.033041`
- 60d: sample `40`, hit `0.725`, avg `0.040788`, median `0.062356`, mae `0.067602`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000229`, median `-0.000756`, mae `0.016526`
- 5d: sample `40`, hit `0.475`, avg `-0.002589`, median `-0.003328`, mae `0.018014`
- 10d: sample `40`, hit `0.425`, avg `0.00027`, median `-0.001222`, mae `0.01924`
- 20d: sample `40`, hit `0.775`, avg `0.016728`, median `0.028626`, mae `0.033041`
- 60d: sample `40`, hit `0.725`, avg `0.040788`, median `0.062356`, mae `0.067602`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.001164`, median `-0.001166`, mae `0.011207`
- 5d: sample `40`, hit `0.4`, avg `-0.005555`, median `-0.004389`, mae `0.015622`
- 10d: sample `40`, hit `0.375`, avg `-0.006555`, median `-0.007491`, mae `0.020839`
- 20d: sample `40`, hit `0.55`, avg `-0.003598`, median `0.004543`, mae `0.026588`
- 60d: sample `40`, hit `0.525`, avg `0.006776`, median `0.031838`, mae `0.058065`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000229`, median `-0.000756`, mae `0.016526`
- 5d: sample `40`, hit `0.475`, avg `-0.002589`, median `-0.003328`, mae `0.018014`
- 10d: sample `40`, hit `0.425`, avg `0.00027`, median `-0.001222`, mae `0.01924`
- 20d: sample `40`, hit `0.775`, avg `0.016728`, median `0.028626`, mae `0.033041`
- 60d: sample `40`, hit `0.725`, avg `0.040788`, median `0.062356`, mae `0.067602`

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
- 3d: sample `40`, hit `0.45`, avg `-0.001164`, median `-0.001166`, mae `0.011207`
- 5d: sample `40`, hit `0.4`, avg `-0.005555`, median `-0.004389`, mae `0.015622`
- 10d: sample `40`, hit `0.375`, avg `-0.006555`, median `-0.007491`, mae `0.020839`
- 20d: sample `40`, hit `0.55`, avg `-0.003598`, median `0.004543`, mae `0.026588`
- 60d: sample `40`, hit `0.525`, avg `0.006776`, median `0.031838`, mae `0.058065`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000229`, median `-0.000756`, mae `0.016526`
- 5d: sample `40`, hit `0.475`, avg `-0.002589`, median `-0.003328`, mae `0.018014`
- 10d: sample `40`, hit `0.425`, avg `0.00027`, median `-0.001222`, mae `0.01924`
- 20d: sample `40`, hit `0.775`, avg `0.016728`, median `0.028626`, mae `0.033041`
- 60d: sample `40`, hit `0.725`, avg `0.040788`, median `0.062356`, mae `0.067602`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000229`, median `-0.000756`, mae `0.016526`
- 5d: sample `40`, hit `0.475`, avg `-0.002589`, median `-0.003328`, mae `0.018014`
- 10d: sample `40`, hit `0.425`, avg `0.00027`, median `-0.001222`, mae `0.01924`
- 20d: sample `40`, hit `0.775`, avg `0.016728`, median `0.028626`, mae `0.033041`
- 60d: sample `40`, hit `0.725`, avg `0.040788`, median `0.062356`, mae `0.067602`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.000697`, median `-0.001166`, mae `0.013866`
- 5d: sample `80`, hit `0.4375`, avg `-0.004072`, median `-0.004389`, mae `0.016818`
- 10d: sample `80`, hit `0.4`, avg `-0.003143`, median `-0.003263`, mae `0.020039`
- 20d: sample `80`, hit `0.6625`, avg `0.006565`, median `0.012958`, mae `0.029814`
- 60d: sample `80`, hit `0.625`, avg `0.023782`, median `0.043741`, mae `0.062834`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.000697`, median `-0.001166`, mae `0.013866`
- 5d: sample `80`, hit `0.4375`, avg `-0.004072`, median `-0.004389`, mae `0.016818`
- 10d: sample `80`, hit `0.4`, avg `-0.003143`, median `-0.003263`, mae `0.020039`
- 20d: sample `80`, hit `0.6625`, avg `0.006565`, median `0.012958`, mae `0.029814`
- 60d: sample `80`, hit `0.625`, avg `0.023782`, median `0.043741`, mae `0.062834`

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
