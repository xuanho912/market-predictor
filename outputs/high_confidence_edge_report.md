# High Confidence Edge Report

Generated at: `2026-07-05T16:09:26.230897+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.008858`, median `-0.010033`, mae `0.014281`
- 5d: sample `20`, hit `0.3`, avg `-0.01116`, median `-0.008162`, mae `0.016371`
- 10d: sample `20`, hit `0.25`, avg `-0.006564`, median `-0.00676`, mae `0.01367`
- 20d: sample `20`, hit `0.75`, avg `0.015459`, median `0.021759`, mae `0.027053`
- 60d: sample `20`, hit `0.7`, avg `0.036332`, median `0.059495`, mae `0.06558`

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `0.001398`, median `0.000145`, mae `0.012974`
- 5d: sample `60`, hit `0.5167`, avg `0.000211`, median `0.003026`, mae `0.017342`
- 10d: sample `60`, hit `0.5667`, avg `0.004385`, median `0.003262`, mae `0.019945`
- 20d: sample `60`, hit `0.6667`, avg `0.005261`, median `0.010788`, mae `0.024007`
- 60d: sample `60`, hit `0.45`, avg `-0.0009`, median `-0.005523`, mae `0.050567`

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
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.008858, 'median_return': -0.010033, 'mean_absolute_return': 0.014281, 'max_adverse_excursion': -0.033992, 'max_favorable_excursion': 0.012196}, '5d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.01116, 'median_return': -0.008162, 'mean_absolute_return': 0.016371, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.006564, 'median_return': -0.00676, 'mean_absolute_return': 0.01367, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.015459, 'median_return': 0.021759, 'mean_absolute_return': 0.027053, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.036332, 'median_return': 0.059495, 'mean_absolute_return': 0.06558, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': 0.001398, 'median_return': 0.000145, 'mean_absolute_return': 0.012974, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.000211, 'median_return': 0.003026, 'mean_absolute_return': 0.017342, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.004385, 'median_return': 0.003262, 'mean_absolute_return': 0.019945, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.005261, 'median_return': 0.010788, 'mean_absolute_return': 0.024007, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.0009, 'median_return': -0.005523, 'mean_absolute_return': 0.050567, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.114016}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.010839, 'median_return': -0.009383, 'mean_absolute_return': 0.015452, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008852, 'median_return': -0.004438, 'mean_absolute_return': 0.015703, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.008261, 'median_return': -0.010456, 'mean_absolute_return': 0.017874, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.004923, 'median_return': 0.020068, 'mean_absolute_return': 0.028122, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.005336, 'median_return': 0.012092, 'mean_absolute_return': 0.052309, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.099838}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -9.1e-05, 'median_return': -0.000722, 'mean_absolute_return': 0.013061, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.001941, 'median_return': -0.001796, 'mean_absolute_return': 0.017254, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.002749, 'median_return': 0.002362, 'mean_absolute_return': 0.018432, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.008132, 'median_return': 0.011728, 'mean_absolute_return': 0.024396, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.009935, 'median_return': 0.003923, 'mean_absolute_return': 0.054544, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.144029}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.4625}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.5125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.025, 'both_hit': 26, 'both_miss': 34}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.0, 'both_hit': 27, 'both_miss': 33}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.0, 'both_hit': 29, 'both_miss': 31}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.125, 'both_hit': 40, 'both_miss': 20}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.025, 'both_hit': 32, 'both_miss': 28}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.001166, 'median_return': -0.001166, 'mean_absolute_return': 0.0133, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.002632, 'median_return': -0.002002, 'mean_absolute_return': 0.017099, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.001648, 'median_return': -0.000214, 'mean_absolute_return': 0.018376, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.007811, 'median_return': 0.012291, 'mean_absolute_return': 0.024769, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': 0.008408, 'median_return': 0.003923, 'mean_absolute_return': 0.05432, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.001166`, median `-0.001166`, mae `0.0133`
- 5d: sample `80`, hit `0.4625`, avg `-0.002632`, median `-0.002002`, mae `0.017099`
- 10d: sample `80`, hit `0.4875`, avg `0.001648`, median `-0.000214`, mae `0.018376`
- 20d: sample `80`, hit `0.6875`, avg `0.007811`, median `0.012291`, mae `0.024769`
- 60d: sample `80`, hit `0.5125`, avg `0.008408`, median `0.003923`, mae `0.05432`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.001166`, median `-0.001166`, mae `0.0133`
- 5d: sample `80`, hit `0.4625`, avg `-0.002632`, median `-0.002002`, mae `0.017099`
- 10d: sample `80`, hit `0.4875`, avg `0.001648`, median `-0.000214`, mae `0.018376`
- 20d: sample `80`, hit `0.6875`, avg `0.007811`, median `0.012291`, mae `0.024769`
- 60d: sample `80`, hit `0.5125`, avg `0.008408`, median `0.003923`, mae `0.05432`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003965`, median `-0.006856`, mae `0.015206`
- 5d: sample `40`, hit `0.4`, avg `-0.00553`, median `-0.008162`, mae `0.019014`
- 10d: sample `40`, hit `0.375`, avg `-0.004283`, median `-0.00676`, mae `0.020552`
- 20d: sample `40`, hit `0.75`, avg `0.010469`, median `0.015661`, mae `0.026058`
- 60d: sample `40`, hit `0.575`, avg `0.016463`, median `0.012092`, mae `0.055205`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.001166`, median `-0.001166`, mae `0.0133`
- 5d: sample `80`, hit `0.4625`, avg `-0.002632`, median `-0.002002`, mae `0.017099`
- 10d: sample `80`, hit `0.4875`, avg `0.001648`, median `-0.000214`, mae `0.018376`
- 20d: sample `80`, hit `0.6875`, avg `0.007811`, median `0.012291`, mae `0.024769`
- 60d: sample `80`, hit `0.5125`, avg `0.008408`, median `0.003923`, mae `0.05432`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003965`, median `-0.006856`, mae `0.015206`
- 5d: sample `40`, hit `0.4`, avg `-0.00553`, median `-0.008162`, mae `0.019014`
- 10d: sample `40`, hit `0.375`, avg `-0.004283`, median `-0.00676`, mae `0.020552`
- 20d: sample `40`, hit `0.75`, avg `0.010469`, median `0.015661`, mae `0.026058`
- 60d: sample `40`, hit `0.575`, avg `0.016463`, median `0.012092`, mae `0.055205`

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
- 3d: sample `40`, hit `0.4`, avg `-0.005145`, median `-0.002654`, mae `0.011266`
- 5d: sample `40`, hit `0.45`, avg `-0.005158`, median `-0.00428`, mae `0.013632`
- 10d: sample `40`, hit `0.425`, avg `-0.000686`, median `-0.000896`, mae `0.012178`
- 20d: sample `40`, hit `0.775`, avg `0.013609`, median `0.016175`, mae `0.022892`
- 60d: sample `40`, hit `0.525`, avg `0.007833`, median `0.012092`, mae `0.056445`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.002813`, median `0.001999`, mae `0.015335`
- 5d: sample `40`, hit `0.475`, avg `-0.000106`, median `-0.001324`, mae `0.020566`
- 10d: sample `40`, hit `0.55`, avg `0.003982`, median `0.002896`, mae `0.024575`
- 20d: sample `40`, hit `0.6`, avg `0.002012`, median `0.007366`, mae `0.026646`
- 60d: sample `40`, hit `0.5`, avg `0.008984`, median `0.003923`, mae `0.052196`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.005145`, median `-0.002654`, mae `0.011266`
- 5d: sample `40`, hit `0.45`, avg `-0.005158`, median `-0.00428`, mae `0.013632`
- 10d: sample `40`, hit `0.425`, avg `-0.000686`, median `-0.000896`, mae `0.012178`
- 20d: sample `40`, hit `0.775`, avg `0.013609`, median `0.016175`, mae `0.022892`
- 60d: sample `40`, hit `0.525`, avg `0.007833`, median `0.012092`, mae `0.056445`

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
- 3d: sample `80`, hit `0.4625`, avg `-0.001166`, median `-0.001166`, mae `0.0133`
- 5d: sample `80`, hit `0.4625`, avg `-0.002632`, median `-0.002002`, mae `0.017099`
- 10d: sample `80`, hit `0.4875`, avg `0.001648`, median `-0.000214`, mae `0.018376`
- 20d: sample `80`, hit `0.6875`, avg `0.007811`, median `0.012291`, mae `0.024769`
- 60d: sample `80`, hit `0.5125`, avg `0.008408`, median `0.003923`, mae `0.05432`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.001166`, median `-0.001166`, mae `0.0133`
- 5d: sample `80`, hit `0.4625`, avg `-0.002632`, median `-0.002002`, mae `0.017099`
- 10d: sample `80`, hit `0.4875`, avg `0.001648`, median `-0.000214`, mae `0.018376`
- 20d: sample `80`, hit `0.6875`, avg `0.007811`, median `0.012291`, mae `0.024769`
- 60d: sample `80`, hit `0.5125`, avg `0.008408`, median `0.003923`, mae `0.05432`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.001166`, median `-0.001166`, mae `0.0133`
- 5d: sample `80`, hit `0.4625`, avg `-0.002632`, median `-0.002002`, mae `0.017099`
- 10d: sample `80`, hit `0.4875`, avg `0.001648`, median `-0.000214`, mae `0.018376`
- 20d: sample `80`, hit `0.6875`, avg `0.007811`, median `0.012291`, mae `0.024769`
- 60d: sample `80`, hit `0.5125`, avg `0.008408`, median `0.003923`, mae `0.05432`

### bounce_with_flow_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.001166`, median `-0.001166`, mae `0.0133`
- 5d: sample `80`, hit `0.4625`, avg `-0.002632`, median `-0.002002`, mae `0.017099`
- 10d: sample `80`, hit `0.4875`, avg `0.001648`, median `-0.000214`, mae `0.018376`
- 20d: sample `80`, hit `0.6875`, avg `0.007811`, median `0.012291`, mae `0.024769`
- 60d: sample `80`, hit `0.5125`, avg `0.008408`, median `0.003923`, mae `0.05432`

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
