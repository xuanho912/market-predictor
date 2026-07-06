# High Confidence Edge Report

Generated at: `2026-07-06T23:55:54.246205+00:00`

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
- 3d: sample `40`, hit `0.475`, avg `-0.003107`, median `-0.000317`, mae `0.014199`
- 5d: sample `40`, hit `0.45`, avg `-0.004559`, median `-0.002002`, mae `0.016733`
- 10d: sample `40`, hit `0.425`, avg `0.001714`, median `-0.005891`, mae `0.0182`
- 20d: sample `40`, hit `0.575`, avg `0.005984`, median `0.009812`, mae `0.028687`
- 60d: sample `40`, hit `0.6`, avg `0.024769`, median `0.046132`, mae `0.06071`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001431`, median `-0.001166`, mae `0.008251`
- 5d: sample `20`, hit `0.6`, avg `0.000844`, median `0.003714`, mae `0.010894`
- 10d: sample `20`, hit `0.6`, avg `0.005192`, median `0.004542`, mae `0.010686`
- 20d: sample `20`, hit `0.8`, avg `0.011759`, median `0.013178`, mae `0.018731`
- 60d: sample `20`, hit `0.35`, avg `-0.020667`, median `-0.018455`, mae `0.04731`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002312`, median `0.006632`, mae `0.015496`
- 5d: sample `20`, hit `0.5`, avg `-0.001331`, median `0.004655`, mae `0.021335`
- 10d: sample `20`, hit `0.5`, avg `-0.003461`, median `0.003262`, mae `0.02642`
- 20d: sample `20`, hit `0.7`, avg `-0.005348`, median `0.007366`, mae `0.02929`
- 60d: sample `20`, hit `0.35`, avg `-0.01454`, median `-0.009954`, mae `0.048128`

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
- 3d: sample `8`, hit `0.375`, avg `-0.010839`, median `-0.009383`, mae `0.015452`
- 5d: sample `8`, hit `0.375`, avg `-0.008852`, median `-0.004438`, mae `0.015703`
- 10d: sample `8`, hit `0.25`, avg `-0.008261`, median `-0.010456`, mae `0.017874`
- 20d: sample `8`, hit `0.625`, avg `0.004923`, median `0.020068`, mae `0.028122`
- 60d: sample `8`, hit `0.5`, avg `-0.005336`, median `0.012092`, mae `0.052309`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.010839`, median `-0.009383`, mae `0.015452`
- 5d: sample `8`, hit `0.375`, avg `-0.008852`, median `-0.004438`, mae `0.015703`
- 10d: sample `8`, hit `0.25`, avg `-0.008261`, median `-0.010456`, mae `0.017874`
- 20d: sample `8`, hit `0.625`, avg `0.004923`, median `0.020068`, mae `0.028122`
- 60d: sample `8`, hit `0.5`, avg `-0.005336`, median `0.012092`, mae `0.052309`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.003107, 'median_return': -0.000317, 'mean_absolute_return': 0.014199, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.004559, 'median_return': -0.002002, 'mean_absolute_return': 0.016733, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.03091}, '10d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': 0.001714, 'median_return': -0.005891, 'mean_absolute_return': 0.0182, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.005984, 'median_return': 0.009812, 'mean_absolute_return': 0.028687, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.024769, 'median_return': 0.046132, 'mean_absolute_return': 0.06071, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.001431, 'median_return': -0.001166, 'mean_absolute_return': 0.008251, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.01781}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.000844, 'median_return': 0.003714, 'mean_absolute_return': 0.010894, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.005192, 'median_return': 0.004542, 'mean_absolute_return': 0.010686, 'max_adverse_excursion': -0.016537, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.011759, 'median_return': 0.013178, 'mean_absolute_return': 0.018731, 'max_adverse_excursion': -0.024012, 'max_favorable_excursion': 0.043353}, '60d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.020667, 'median_return': -0.018455, 'mean_absolute_return': 0.04731, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.049084}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.010839, 'median_return': -0.009383, 'mean_absolute_return': 0.015452, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008852, 'median_return': -0.004438, 'mean_absolute_return': 0.015703, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.008261, 'median_return': -0.010456, 'mean_absolute_return': 0.017874, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.004923, 'median_return': 0.020068, 'mean_absolute_return': 0.028122, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.005336, 'median_return': 0.012092, 'mean_absolute_return': 0.052309, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.099838}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.000277, 'median_return': 0.000324, 'mean_absolute_return': 0.012768, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.001684, 'median_return': 0.003026, 'mean_absolute_return': 0.016503, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.002351, 'median_return': 0.002362, 'mean_absolute_return': 0.018433, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.004559, 'median_return': 0.009812, 'mean_absolute_return': 0.026152, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.004574, 'median_return': -0.003136, 'mean_absolute_return': 0.054426, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.144029}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.6625}, '60d': {'sample_size': 80, 'hit_rate': 0.475}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 40, 'both_miss': 40}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 40, 'both_miss': 40}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.0, 'both_hit': 39, 'both_miss': 41}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': 0.0, 'both_hit': 53, 'both_miss': 27}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.0, 'both_hit': 38, 'both_miss': 42}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.001333, 'median_return': 0.000145, 'mean_absolute_return': 0.013036, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.002401, 'median_return': 0.000415, 'mean_absolute_return': 0.016423, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.00129, 'median_return': -0.000214, 'mean_absolute_return': 0.018377, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.004595, 'median_return': 0.010788, 'mean_absolute_return': 0.026349, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': 0.003583, 'median_return': -0.003136, 'mean_absolute_return': 0.054214, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001333`, median `0.000145`, mae `0.013036`
- 5d: sample `80`, hit `0.5`, avg `-0.002401`, median `0.000415`, mae `0.016423`
- 10d: sample `80`, hit `0.4875`, avg `0.00129`, median `-0.000214`, mae `0.018377`
- 20d: sample `80`, hit `0.6625`, avg `0.004595`, median `0.010788`, mae `0.026349`
- 60d: sample `80`, hit `0.475`, avg `0.003583`, median `-0.003136`, mae `0.054214`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001333`, median `0.000145`, mae `0.013036`
- 5d: sample `80`, hit `0.5`, avg `-0.002401`, median `0.000415`, mae `0.016423`
- 10d: sample `80`, hit `0.4875`, avg `0.00129`, median `-0.000214`, mae `0.018377`
- 20d: sample `80`, hit `0.6625`, avg `0.004595`, median `0.010788`, mae `0.026349`
- 60d: sample `80`, hit `0.475`, avg `0.003583`, median `-0.003136`, mae `0.054214`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.003922`, median `-0.001658`, mae `0.015453`
- 5d: sample `40`, hit `0.425`, avg `-0.005267`, median `-0.004989`, mae `0.018735`
- 10d: sample `40`, hit `0.375`, avg `-0.004874`, median `-0.007011`, mae `0.020692`
- 20d: sample `40`, hit `0.675`, avg `0.003613`, median `0.007676`, mae `0.027565`
- 60d: sample `40`, hit `0.45`, avg `0.002586`, median `-0.003136`, mae `0.053113`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001333`, median `0.000145`, mae `0.013036`
- 5d: sample `80`, hit `0.5`, avg `-0.002401`, median `0.000415`, mae `0.016423`
- 10d: sample `80`, hit `0.4875`, avg `0.00129`, median `-0.000214`, mae `0.018377`
- 20d: sample `80`, hit `0.6625`, avg `0.004595`, median `0.010788`, mae `0.026349`
- 60d: sample `80`, hit `0.475`, avg `0.003583`, median `-0.003136`, mae `0.054214`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.003922`, median `-0.001658`, mae `0.015453`
- 5d: sample `40`, hit `0.425`, avg `-0.005267`, median `-0.004989`, mae `0.018735`
- 10d: sample `40`, hit `0.375`, avg `-0.004874`, median `-0.007011`, mae `0.020692`
- 20d: sample `40`, hit `0.675`, avg `0.003613`, median `0.007676`, mae `0.027565`
- 60d: sample `40`, hit `0.45`, avg `0.002586`, median `-0.003136`, mae `0.053113`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.005794`, median `-0.002654`, mae `0.01183`
- 5d: sample `40`, hit `0.475`, avg `-0.00418`, median `-0.001796`, mae `0.013514`
- 10d: sample `40`, hit `0.425`, avg `-0.000547`, median `-0.000896`, mae `0.012825`
- 20d: sample `40`, hit `0.725`, avg `0.012167`, median `0.013178`, mae `0.022285`
- 60d: sample `40`, hit `0.45`, avg `-0.000478`, median `-0.005523`, mae `0.052704`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003127`, median `0.003538`, mae `0.014242`
- 5d: sample `40`, hit `0.525`, avg `-0.000622`, median `0.004655`, mae `0.019333`
- 10d: sample `40`, hit `0.55`, avg `0.003127`, median `0.002896`, mae `0.023928`
- 20d: sample `40`, hit `0.6`, avg `-0.002977`, median `0.004543`, mae `0.030413`
- 60d: sample `40`, hit `0.5`, avg `0.007643`, median `0.003923`, mae `0.055724`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.005794`, median `-0.002654`, mae `0.01183`
- 5d: sample `40`, hit `0.475`, avg `-0.00418`, median `-0.001796`, mae `0.013514`
- 10d: sample `40`, hit `0.425`, avg `-0.000547`, median `-0.000896`, mae `0.012825`
- 20d: sample `40`, hit `0.725`, avg `0.012167`, median `0.013178`, mae `0.022285`
- 60d: sample `40`, hit `0.45`, avg `-0.000478`, median `-0.005523`, mae `0.052704`

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
