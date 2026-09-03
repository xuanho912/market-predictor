# High Confidence Edge Report

Generated at: `2026-09-03T08:19:30.690878+00:00`

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
- 3d: sample `80`, hit `0.5625`, avg `0.000908`, median `0.000766`, mae `0.013703`
- 5d: sample `80`, hit `0.5625`, avg `-0.000322`, median `0.001303`, mae `0.018165`
- 10d: sample `80`, hit `0.4125`, avg `-0.001232`, median `-0.007491`, mae `0.024918`
- 20d: sample `80`, hit `0.65`, avg `0.008985`, median `0.01927`, mae `0.037168`
- 60d: sample `80`, hit `0.6875`, avg `0.030986`, median `0.059948`, mae `0.081193`

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
- 3d: sample `8`, hit `0.375`, avg `-0.009181`, median `-0.001658`, mae `0.015069`
- 5d: sample `8`, hit `0.375`, avg `-0.013975`, median `-0.012956`, mae `0.020145`
- 10d: sample `8`, hit `0.375`, avg `-6e-05`, median `-0.0004`, mae `0.019072`
- 20d: sample `8`, hit `0.875`, avg `0.028723`, median `0.033999`, mae `0.042549`
- 60d: sample `8`, hit `0.875`, avg `0.078668`, median `0.101282`, mae `0.092886`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.009181`, median `-0.001658`, mae `0.015069`
- 5d: sample `8`, hit `0.375`, avg `-0.013975`, median `-0.012956`, mae `0.020145`
- 10d: sample `8`, hit `0.375`, avg `-6e-05`, median `-0.0004`, mae `0.019072`
- 20d: sample `8`, hit `0.875`, avg `0.028723`, median `0.033999`, mae `0.042549`
- 60d: sample `8`, hit `0.875`, avg `0.078668`, median `0.101282`, mae `0.092886`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.009181, 'median_return': -0.001658, 'mean_absolute_return': 0.015069, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.017427}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.013975, 'median_return': -0.012956, 'mean_absolute_return': 0.020145, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -6e-05, 'median_return': -0.0004, 'mean_absolute_return': 0.019072, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.028723, 'median_return': 0.033999, 'mean_absolute_return': 0.042549, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.078668, 'median_return': 0.101282, 'mean_absolute_return': 0.092886, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.002029, 'median_return': 0.00099, 'mean_absolute_return': 0.013551, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.001195, 'median_return': 0.001695, 'mean_absolute_return': 0.017945, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.001363, 'median_return': -0.00842, 'mean_absolute_return': 0.025568, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.006792, 'median_return': 0.014522, 'mean_absolute_return': 0.03657, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.025688, 'median_return': 0.057625, 'mean_absolute_return': 0.079894, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4375}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.5875}, '20d': {'sample_size': 80, 'hit_rate': 0.35}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.175, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.001488, 'median_return': 0.003434, 'mean_absolute_return': 0.017486, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.000574, 'median_return': 0.003829, 'mean_absolute_return': 0.021213, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.005462, 'median_return': -0.0004, 'mean_absolute_return': 0.024347, 'max_adverse_excursion': -0.038411, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.023657, 'median_return': 0.029166, 'mean_absolute_return': 0.031151, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.064666, 'median_return': 0.069439, 'mean_absolute_return': 0.07882, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.000329, 'median_return': 0.000616, 'mean_absolute_return': 0.009921, 'max_adverse_excursion': -0.029438, 'max_favorable_excursion': 0.022026}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -7e-05, 'median_return': 0.001239, 'mean_absolute_return': 0.015116, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.035465}, '10d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.007927, 'median_return': -0.011522, 'mean_absolute_return': 0.02549, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.059577}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.005687, 'median_return': 0.009364, 'mean_absolute_return': 0.043186, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.002695, 'median_return': 0.029164, 'mean_absolute_return': 0.083566, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.117141}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `60`, hit `0.5167`, avg `-0.000295`, median `0.000603`, mae `0.014655`
- 5d: sample `60`, hit `0.55`, avg `-0.002071`, median `0.000873`, mae `0.01792`
- 10d: sample `60`, hit `0.4167`, avg `0.001098`, median `-0.006017`, mae `0.022847`
- 20d: sample `60`, hit `0.65`, avg `0.014711`, median `0.020226`, mae `0.031017`
- 60d: sample `60`, hit `0.75`, avg `0.050483`, median `0.064104`, mae `0.070487`

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
- 3d: sample `40`, hit `0.575`, avg `0.001488`, median `0.003434`, mae `0.017486`
- 5d: sample `40`, hit `0.55`, avg `-0.000574`, median `0.003829`, mae `0.021213`
- 10d: sample `40`, hit `0.475`, avg `0.005462`, median `-0.0004`, mae `0.024347`
- 20d: sample `40`, hit `0.725`, avg `0.023657`, median `0.029166`, mae `0.031151`
- 60d: sample `40`, hit `0.85`, avg `0.064666`, median `0.069439`, mae `0.07882`

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
- 3d: sample `60`, hit `0.5167`, avg `-0.000295`, median `0.000603`, mae `0.014655`
- 5d: sample `60`, hit `0.55`, avg `-0.002071`, median `0.000873`, mae `0.01792`
- 10d: sample `60`, hit `0.4167`, avg `0.001098`, median `-0.006017`, mae `0.022847`
- 20d: sample `60`, hit `0.65`, avg `0.014711`, median `0.020226`, mae `0.031017`
- 60d: sample `60`, hit `0.75`, avg `0.050483`, median `0.064104`, mae `0.070487`

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
- 3d: sample `80`, hit `0.5625`, avg `0.000908`, median `0.000766`, mae `0.013703`
- 5d: sample `80`, hit `0.5625`, avg `-0.000322`, median `0.001303`, mae `0.018165`
- 10d: sample `80`, hit `0.4125`, avg `-0.001232`, median `-0.007491`, mae `0.024918`
- 20d: sample `80`, hit `0.65`, avg `0.008985`, median `0.01927`, mae `0.037168`
- 60d: sample `80`, hit `0.6875`, avg `0.030986`, median `0.059948`, mae `0.081193`

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
