# High Confidence Edge Report

Generated at: `2026-06-29T23:38:12.433942+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000119`, median `-0.001658`, mae `0.015484`
- 5d: sample `40`, hit `0.45`, avg `-0.004472`, median `-0.007788`, mae `0.019346`
- 10d: sample `40`, hit `0.475`, avg `0.00227`, median `-0.0004`, mae `0.021187`
- 20d: sample `40`, hit `0.8`, avg `0.021217`, median `0.028791`, mae `0.033172`
- 60d: sample `40`, hit `0.75`, avg `0.045822`, median `0.062356`, mae `0.07025`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.00318`, median `-0.002151`, mae `0.010678`
- 5d: sample `20`, hit `0.35`, avg `-0.005388`, median `-0.004123`, mae `0.016059`
- 10d: sample `20`, hit `0.55`, avg `0.003389`, median `0.00273`, mae `0.023519`
- 20d: sample `20`, hit `0.45`, avg `0.007844`, median `-0.001638`, mae `0.032991`
- 60d: sample `20`, hit `0.65`, avg `0.06252`, median `0.069875`, mae `0.096576`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002904`, median `-0.002654`, mae `0.010123`
- 5d: sample `20`, hit `0.5`, avg `-0.004766`, median `0.002786`, mae `0.015115`
- 10d: sample `20`, hit `0.4`, avg `-0.007054`, median `-0.004918`, mae `0.018433`
- 20d: sample `20`, hit `0.65`, avg `-0.003342`, median `0.012291`, mae `0.029445`
- 60d: sample `20`, hit `0.45`, avg `-0.008556`, median `-0.005185`, mae `0.051279`

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
- 3d: sample `8`, hit `0.375`, avg `-0.004068`, median `-0.001811`, mae `0.016645`
- 5d: sample `8`, hit `0.0`, avg `-0.018992`, median `-0.016952`, mae `0.018992`
- 10d: sample `8`, hit `0.5`, avg `0.00331`, median `0.006053`, mae `0.010986`
- 20d: sample `8`, hit `1.0`, avg `0.029013`, median `0.031196`, mae `0.029013`
- 60d: sample `8`, hit `1.0`, avg `0.086977`, median `0.094627`, mae `0.086977`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.004068`, median `-0.001811`, mae `0.016645`
- 5d: sample `8`, hit `0.0`, avg `-0.018992`, median `-0.016952`, mae `0.018992`
- 10d: sample `8`, hit `0.5`, avg `0.00331`, median `0.006053`, mae `0.010986`
- 20d: sample `8`, hit `1.0`, avg `0.029013`, median `0.031196`, mae `0.029013`
- 60d: sample `8`, hit `1.0`, avg `0.086977`, median `0.094627`, mae `0.086977`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.000119, 'median_return': -0.001658, 'mean_absolute_return': 0.015484, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.004472, 'median_return': -0.007788, 'mean_absolute_return': 0.019346, 'max_adverse_excursion': -0.045904, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.00227, 'median_return': -0.0004, 'mean_absolute_return': 0.021187, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.021217, 'median_return': 0.028791, 'mean_absolute_return': 0.033172, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.045822, 'median_return': 0.062356, 'mean_absolute_return': 0.07025, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.156405}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.00318, 'median_return': -0.002151, 'mean_absolute_return': 0.010678, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.005388, 'median_return': -0.004123, 'mean_absolute_return': 0.016059, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.036593}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.003389, 'median_return': 0.00273, 'mean_absolute_return': 0.023519, 'max_adverse_excursion': -0.050161, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': 0.007844, 'median_return': -0.001638, 'mean_absolute_return': 0.032991, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.095986}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.06252, 'median_return': 0.069875, 'mean_absolute_return': 0.096576, 'max_adverse_excursion': -0.085721, 'max_favorable_excursion': 0.279401}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.004068, 'median_return': -0.001811, 'mean_absolute_return': 0.016645, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022721}, '5d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.018992, 'median_return': -0.016952, 'mean_absolute_return': 0.018992, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': -0.006798}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.00331, 'median_return': 0.006053, 'mean_absolute_return': 0.010986, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.023979}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.029013, 'median_return': 0.031196, 'mean_absolute_return': 0.029013, 'max_adverse_excursion': 0.016175, 'max_favorable_excursion': 0.041903}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.086977, 'median_return': 0.094627, 'mean_absolute_return': 0.086977, 'max_adverse_excursion': 0.046132, 'max_favorable_excursion': 0.117712}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.001304, 'median_return': -0.002151, 'mean_absolute_return': 0.012531, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.003195, 'median_return': -0.001324, 'mean_absolute_return': 0.017297, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.000125, 'median_return': -0.001083, 'mean_absolute_return': 0.022203, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.009814, 'median_return': 0.012291, 'mean_absolute_return': 0.032548, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.095986}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.030782, 'median_return': 0.032982, 'mean_absolute_return': 0.070435, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.279401}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.525}, '20d': {'sample_size': 80, 'hit_rate': 0.6}, '60d': {'sample_size': 80, 'hit_rate': 0.675}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.05, 'both_hit': 19, 'both_miss': 21}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.075, 'both_hit': 18, 'both_miss': 22}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.075, 'both_hit': 19, 'both_miss': 21}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.1, 'both_hit': 32, 'both_miss': 8}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.1, 'both_hit': 30, 'both_miss': 10}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.003073, 'median_return': 0.006632, 'mean_absolute_return': 0.01536, 'max_adverse_excursion': -0.026663, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.002285, 'median_return': 0.006107, 'mean_absolute_return': 0.021372, 'max_adverse_excursion': -0.045904, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.004139, 'median_return': 0.006378, 'mean_absolute_return': 0.029988, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.014348, 'median_return': 0.015661, 'mean_absolute_return': 0.033932, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.018674, 'median_return': 0.029229, 'mean_absolute_return': 0.058843, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.156405}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': -0.003132, 'median_return': -0.002654, 'mean_absolute_return': 0.012136, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.007127, 'median_return': -0.006798, 'mean_absolute_return': 0.016164, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.036593}, '10d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.001088, 'median_return': -0.001932, 'mean_absolute_return': 0.018112, 'max_adverse_excursion': -0.050724, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.010863, 'median_return': 0.016175, 'mean_absolute_return': 0.031616, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.095986}, '60d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.042311, 'median_return': 0.047238, 'mean_absolute_return': 0.076504, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.279401}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.001139`, median `-0.001811`, mae `0.013882`
- 5d: sample `60`, hit `0.4167`, avg `-0.004777`, median `-0.006511`, mae `0.01825`
- 10d: sample `60`, hit `0.5`, avg `0.002643`, median `0.000242`, mae `0.021964`
- 20d: sample `60`, hit `0.6833`, avg `0.01676`, median `0.01666`, mae `0.033111`
- 60d: sample `60`, hit `0.7167`, avg `0.051388`, median `0.065295`, mae `0.079025`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002904`, median `-0.002654`, mae `0.010123`
- 5d: sample `20`, hit `0.5`, avg `-0.004766`, median `0.002786`, mae `0.015115`
- 10d: sample `20`, hit `0.4`, avg `-0.007054`, median `-0.004918`, mae `0.018433`
- 20d: sample `20`, hit `0.65`, avg `-0.003342`, median `0.012291`, mae `0.029445`
- 60d: sample `20`, hit `0.45`, avg `-0.008556`, median `-0.005185`, mae `0.051279`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.001139`, median `-0.001811`, mae `0.013882`
- 5d: sample `60`, hit `0.4167`, avg `-0.004777`, median `-0.006511`, mae `0.01825`
- 10d: sample `60`, hit `0.5`, avg `0.002643`, median `0.000242`, mae `0.021964`
- 20d: sample `60`, hit `0.6833`, avg `0.01676`, median `0.01666`, mae `0.033111`
- 60d: sample `60`, hit `0.7167`, avg `0.051388`, median `0.065295`, mae `0.079025`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.001139`, median `-0.001811`, mae `0.013882`
- 5d: sample `60`, hit `0.4167`, avg `-0.004777`, median `-0.006511`, mae `0.01825`
- 10d: sample `60`, hit `0.5`, avg `0.002643`, median `0.000242`, mae `0.021964`
- 20d: sample `60`, hit `0.6833`, avg `0.01676`, median `0.01666`, mae `0.033111`
- 60d: sample `60`, hit `0.7167`, avg `0.051388`, median `0.065295`, mae `0.079025`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.001139`, median `-0.001811`, mae `0.013882`
- 5d: sample `60`, hit `0.4167`, avg `-0.004777`, median `-0.006511`, mae `0.01825`
- 10d: sample `60`, hit `0.5`, avg `0.002643`, median `0.000242`, mae `0.021964`
- 20d: sample `60`, hit `0.6833`, avg `0.01676`, median `0.01666`, mae `0.033111`
- 60d: sample `60`, hit `0.7167`, avg `0.051388`, median `0.065295`, mae `0.079025`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.001139`, median `-0.001811`, mae `0.013882`
- 5d: sample `60`, hit `0.4167`, avg `-0.004777`, median `-0.006511`, mae `0.01825`
- 10d: sample `60`, hit `0.5`, avg `0.002643`, median `0.000242`, mae `0.021964`
- 20d: sample `60`, hit `0.6833`, avg `0.01676`, median `0.01666`, mae `0.033111`
- 60d: sample `60`, hit `0.7167`, avg `0.051388`, median `0.065295`, mae `0.079025`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002904`, median `-0.002654`, mae `0.010123`
- 5d: sample `20`, hit `0.5`, avg `-0.004766`, median `0.002786`, mae `0.015115`
- 10d: sample `20`, hit `0.4`, avg `-0.007054`, median `-0.004918`, mae `0.018433`
- 20d: sample `20`, hit `0.65`, avg `-0.003342`, median `0.012291`, mae `0.029445`
- 60d: sample `20`, hit `0.45`, avg `-0.008556`, median `-0.005185`, mae `0.051279`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.001139`, median `-0.001811`, mae `0.013882`
- 5d: sample `60`, hit `0.4167`, avg `-0.004777`, median `-0.006511`, mae `0.01825`
- 10d: sample `60`, hit `0.5`, avg `0.002643`, median `0.000242`, mae `0.021964`
- 20d: sample `60`, hit `0.6833`, avg `0.01676`, median `0.01666`, mae `0.033111`
- 60d: sample `60`, hit `0.7167`, avg `0.051388`, median `0.065295`, mae `0.079025`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002904`, median `-0.002654`, mae `0.010123`
- 5d: sample `20`, hit `0.5`, avg `-0.004766`, median `0.002786`, mae `0.015115`
- 10d: sample `20`, hit `0.4`, avg `-0.007054`, median `-0.004918`, mae `0.018433`
- 20d: sample `20`, hit `0.65`, avg `-0.003342`, median `0.012291`, mae `0.029445`
- 60d: sample `20`, hit `0.45`, avg `-0.008556`, median `-0.005185`, mae `0.051279`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.003042`, median `-0.002654`, mae `0.010401`
- 5d: sample `40`, hit `0.425`, avg `-0.005077`, median `-0.004123`, mae `0.015587`
- 10d: sample `40`, hit `0.475`, avg `-0.001833`, median `-0.001676`, mae `0.020976`
- 20d: sample `40`, hit `0.55`, avg `0.002251`, median `0.007004`, mae `0.031218`
- 60d: sample `40`, hit `0.55`, avg `0.026982`, median `0.032524`, mae `0.073927`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.00318`, median `-0.002151`, mae `0.010678`
- 5d: sample `20`, hit `0.35`, avg `-0.005388`, median `-0.004123`, mae `0.016059`
- 10d: sample `20`, hit `0.55`, avg `0.003389`, median `0.00273`, mae `0.023519`
- 20d: sample `20`, hit `0.45`, avg `0.007844`, median `-0.001638`, mae `0.032991`
- 60d: sample `20`, hit `0.65`, avg `0.06252`, median `0.069875`, mae `0.096576`

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
