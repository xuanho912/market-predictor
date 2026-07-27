# High Confidence Edge Report

Generated at: `2026-07-27T15:16:26.235152+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005789`, median `0.000766`, mae `0.017373`
- 5d: sample `40`, hit `0.475`, avg `-0.009539`, median `-0.001429`, mae `0.018765`
- 10d: sample `40`, hit `0.375`, avg `-0.004565`, median `-0.007011`, mae `0.017342`
- 20d: sample `40`, hit `0.625`, avg `0.011187`, median `0.020068`, mae `0.033597`
- 60d: sample `40`, hit `0.7`, avg `0.033821`, median `0.046407`, mae `0.059641`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002785`, median `0.008009`, mae `0.022084`
- 5d: sample `40`, hit `0.55`, avg `0.002522`, median `0.003476`, mae `0.029358`
- 10d: sample `40`, hit `0.725`, avg `0.016437`, median `0.030858`, mae `0.042232`
- 20d: sample `40`, hit `0.675`, avg `0.023858`, median `0.048862`, mae `0.063867`
- 60d: sample `40`, hit `0.65`, avg `0.028891`, median `0.075265`, mae `0.111233`

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
- 3d: sample `8`, hit `0.25`, avg `-0.013711`, median `-0.010033`, mae `0.023889`
- 5d: sample `8`, hit `0.375`, avg `-0.018719`, median `-0.022295`, mae `0.029028`
- 10d: sample `8`, hit `0.25`, avg `-0.005373`, median `-0.006017`, mae `0.016616`
- 20d: sample `8`, hit `0.5`, avg `0.019534`, median `0.043456`, mae `0.042316`
- 60d: sample `8`, hit `0.625`, avg `0.051405`, median `0.099838`, mae `0.080567`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.013711`, median `-0.010033`, mae `0.023889`
- 5d: sample `8`, hit `0.375`, avg `-0.018719`, median `-0.022295`, mae `0.029028`
- 10d: sample `8`, hit `0.25`, avg `-0.005373`, median `-0.006017`, mae `0.016616`
- 20d: sample `8`, hit `0.5`, avg `0.019534`, median `0.043456`, mae `0.042316`
- 60d: sample `8`, hit `0.625`, avg `0.051405`, median `0.099838`, mae `0.080567`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.005789, 'median_return': 0.000766, 'mean_absolute_return': 0.017373, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.037139}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.009539, 'median_return': -0.001429, 'mean_absolute_return': 0.018765, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.004565, 'median_return': -0.007011, 'mean_absolute_return': 0.017342, 'max_adverse_excursion': -0.040826, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.011187, 'median_return': 0.020068, 'mean_absolute_return': 0.033597, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.033821, 'median_return': 0.046407, 'mean_absolute_return': 0.059641, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.013711, 'median_return': -0.010033, 'mean_absolute_return': 0.023889, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.018719, 'median_return': -0.022295, 'mean_absolute_return': 0.029028, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.005373, 'median_return': -0.006017, 'mean_absolute_return': 0.016616, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.019534, 'median_return': 0.043456, 'mean_absolute_return': 0.042316, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.051405, 'median_return': 0.099838, 'mean_absolute_return': 0.080567, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': -0.000145, 'median_return': 0.00234, 'mean_absolute_return': 0.019266, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': -0.001818, 'median_return': 0.001303, 'mean_absolute_return': 0.02351, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.007193, 'median_return': 0.014312, 'mean_absolute_return': 0.031251, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.075}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.017299, 'median_return': 0.026005, 'mean_absolute_return': 0.049445, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.029128, 'median_return': 0.058473, 'mean_absolute_return': 0.085978, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4375}, '5d': {'sample_size': 80, 'hit_rate': 0.4875}, '10d': {'sample_size': 80, 'hit_rate': 0.45}, '20d': {'sample_size': 80, 'hit_rate': 0.35}, '60d': {'sample_size': 80, 'hit_rate': 0.325}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': -0.000448, 'median_return': 0.003785, 'mean_absolute_return': 0.019949, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': -0.000211, 'median_return': 0.003727, 'mean_absolute_return': 0.02246, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.051324}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.008726, 'median_return': 0.001607, 'mean_absolute_return': 0.02657, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.075}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.024791, 'median_return': 0.02865, 'mean_absolute_return': 0.045019, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.129427}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.046323, 'median_return': 0.059104, 'mean_absolute_return': 0.077094, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.21267}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.004664, 'median_return': -0.001058, 'mean_absolute_return': 0.019067, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.0134, 'median_return': -0.007916, 'mean_absolute_return': 0.028867, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.002434, 'median_return': 0.014312, 'mean_absolute_return': 0.039438, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.004283, 'median_return': 0.017237, 'mean_absolute_return': 0.059869, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.013547, 'median_return': 0.027637, 'mean_absolute_return': 0.110464, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.129489}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005789`, median `0.000766`, mae `0.017373`
- 5d: sample `40`, hit `0.475`, avg `-0.009539`, median `-0.001429`, mae `0.018765`
- 10d: sample `40`, hit `0.375`, avg `-0.004565`, median `-0.007011`, mae `0.017342`
- 20d: sample `40`, hit `0.625`, avg `0.011187`, median `0.020068`, mae `0.033597`
- 60d: sample `40`, hit `0.7`, avg `0.033821`, median `0.046407`, mae `0.059641`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002785`, median `0.008009`, mae `0.022084`
- 5d: sample `40`, hit `0.55`, avg `0.002522`, median `0.003476`, mae `0.029358`
- 10d: sample `40`, hit `0.725`, avg `0.016437`, median `0.030858`, mae `0.042232`
- 20d: sample `40`, hit `0.675`, avg `0.023858`, median `0.048862`, mae `0.063867`
- 60d: sample `40`, hit `0.65`, avg `0.028891`, median `0.075265`, mae `0.111233`

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
- 3d: sample `40`, hit `0.55`, avg `-0.005789`, median `0.000766`, mae `0.017373`
- 5d: sample `40`, hit `0.475`, avg `-0.009539`, median `-0.001429`, mae `0.018765`
- 10d: sample `40`, hit `0.375`, avg `-0.004565`, median `-0.007011`, mae `0.017342`
- 20d: sample `40`, hit `0.625`, avg `0.011187`, median `0.020068`, mae `0.033597`
- 60d: sample `40`, hit `0.7`, avg `0.033821`, median `0.046407`, mae `0.059641`

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
- 3d: sample `40`, hit `0.55`, avg `-0.005789`, median `0.000766`, mae `0.017373`
- 5d: sample `40`, hit `0.475`, avg `-0.009539`, median `-0.001429`, mae `0.018765`
- 10d: sample `40`, hit `0.375`, avg `-0.004565`, median `-0.007011`, mae `0.017342`
- 20d: sample `40`, hit `0.625`, avg `0.011187`, median `0.020068`, mae `0.033597`
- 60d: sample `40`, hit `0.7`, avg `0.033821`, median `0.046407`, mae `0.059641`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002785`, median `0.008009`, mae `0.022084`
- 5d: sample `40`, hit `0.55`, avg `0.002522`, median `0.003476`, mae `0.029358`
- 10d: sample `40`, hit `0.725`, avg `0.016437`, median `0.030858`, mae `0.042232`
- 20d: sample `40`, hit `0.675`, avg `0.023858`, median `0.048862`, mae `0.063867`
- 60d: sample `40`, hit `0.65`, avg `0.028891`, median `0.075265`, mae `0.111233`

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
- 3d: sample `80`, hit `0.5625`, avg `-0.001502`, median `0.001199`, mae `0.019728`
- 5d: sample `80`, hit `0.5125`, avg `-0.003508`, median `0.000762`, mae `0.024062`
- 10d: sample `80`, hit `0.55`, avg `0.005936`, median `0.006208`, mae `0.029787`
- 20d: sample `80`, hit `0.65`, avg `0.017522`, median `0.026005`, mae `0.048732`
- 60d: sample `80`, hit `0.675`, avg `0.031356`, median `0.058473`, mae `0.085437`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5625`, avg `-0.001502`, median `0.001199`, mae `0.019728`
- 5d: sample `80`, hit `0.5125`, avg `-0.003508`, median `0.000762`, mae `0.024062`
- 10d: sample `80`, hit `0.55`, avg `0.005936`, median `0.006208`, mae `0.029787`
- 20d: sample `80`, hit `0.65`, avg `0.017522`, median `0.026005`, mae `0.048732`
- 60d: sample `80`, hit `0.675`, avg `0.031356`, median `0.058473`, mae `0.085437`

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
- 3d: sample `80`, hit `0.5625`, avg `-0.001502`, median `0.001199`, mae `0.019728`
- 5d: sample `80`, hit `0.5125`, avg `-0.003508`, median `0.000762`, mae `0.024062`
- 10d: sample `80`, hit `0.55`, avg `0.005936`, median `0.006208`, mae `0.029787`
- 20d: sample `80`, hit `0.65`, avg `0.017522`, median `0.026005`, mae `0.048732`
- 60d: sample `80`, hit `0.675`, avg `0.031356`, median `0.058473`, mae `0.085437`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
