# High Confidence Edge Report

Generated at: `2026-07-10T05:12:02.073787+00:00`

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
- 3d: sample `40`, hit `0.5`, avg `-0.003224`, median `0.001558`, mae `0.012941`
- 5d: sample `40`, hit `0.45`, avg `-0.004818`, median `-0.001324`, mae `0.016711`
- 10d: sample `40`, hit `0.45`, avg `0.001143`, median `-0.003263`, mae `0.017336`
- 20d: sample `40`, hit `0.675`, avg `0.007894`, median `0.012958`, mae `0.027511`
- 60d: sample `40`, hit `0.625`, avg `0.026604`, median `0.046132`, mae `0.062021`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.000546`, median `0.000324`, mae `0.010674`
- 5d: sample `40`, hit `0.5`, avg `-0.00251`, median `0.000688`, mae `0.014844`
- 10d: sample `40`, hit `0.45`, avg `-0.003669`, median `-0.007117`, mae `0.022963`
- 20d: sample `40`, hit `0.625`, avg `-0.006787`, median `0.007366`, mae `0.035695`
- 60d: sample `40`, hit `0.425`, avg `-0.007877`, median `-0.009954`, mae `0.050872`

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
- 3d: sample `8`, hit `0.5`, avg `-0.007945`, median `0.001558`, mae `0.012411`
- 5d: sample `8`, hit `0.375`, avg `-0.007801`, median `-0.012956`, mae `0.017182`
- 10d: sample `8`, hit `0.5`, avg `0.001184`, median `0.0076`, mae `0.018466`
- 20d: sample `8`, hit `1.0`, avg `0.029489`, median `0.031196`, mae `0.029489`
- 60d: sample `8`, hit `0.875`, avg `0.066365`, median `0.092646`, mae `0.071397`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.007945`, median `0.001558`, mae `0.012411`
- 5d: sample `8`, hit `0.375`, avg `-0.007801`, median `-0.012956`, mae `0.017182`
- 10d: sample `8`, hit `0.5`, avg `0.001184`, median `0.0076`, mae `0.018466`
- 20d: sample `8`, hit `1.0`, avg `0.029489`, median `0.031196`, mae `0.029489`
- 60d: sample `8`, hit `0.875`, avg `0.066365`, median `0.092646`, mae `0.071397`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.003224, 'median_return': 0.001558, 'mean_absolute_return': 0.012941, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.004818, 'median_return': -0.001324, 'mean_absolute_return': 0.016711, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.030501}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.001143, 'median_return': -0.003263, 'mean_absolute_return': 0.017336, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.051764}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.007894, 'median_return': 0.012958, 'mean_absolute_return': 0.027511, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.077493}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.026604, 'median_return': 0.046132, 'mean_absolute_return': 0.062021, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.000546, 'median_return': 0.000324, 'mean_absolute_return': 0.010674, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.022897}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.00251, 'median_return': 0.000688, 'mean_absolute_return': 0.014844, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.003669, 'median_return': -0.007117, 'mean_absolute_return': 0.022963, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': -0.006787, 'median_return': 0.007366, 'mean_absolute_return': 0.035695, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.062475}, '60d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.007877, 'median_return': -0.009954, 'mean_absolute_return': 0.050872, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.082366}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.007945, 'median_return': 0.001558, 'mean_absolute_return': 0.012411, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007801, 'median_return': -0.012956, 'mean_absolute_return': 0.017182, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001184, 'median_return': 0.0076, 'mean_absolute_return': 0.018466, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.029489, 'median_return': 0.031196, 'mean_absolute_return': 0.029489, 'max_adverse_excursion': 0.000213, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.066365, 'median_return': 0.092646, 'mean_absolute_return': 0.071397, 'max_adverse_excursion': -0.02013, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.001212, 'median_return': 0.000324, 'mean_absolute_return': 0.011741, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.003204, 'median_return': -0.000371, 'mean_absolute_return': 0.015622, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.001535, 'median_return': -0.00676, 'mean_absolute_return': 0.020336, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': -0.002661, 'median_return': 0.007004, 'mean_absolute_return': 0.031838, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.077493}, '60d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.00303, 'median_return': -0.005185, 'mean_absolute_return': 0.054786, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.144029}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.45}, '20d': {'sample_size': 80, 'hit_rate': 0.65}, '60d': {'sample_size': 80, 'hit_rate': 0.525}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 30, 'both_miss': 30}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': -0.025, 'both_hit': 29, 'both_miss': 31}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.025, 'both_hit': 25, 'both_miss': 35}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.1, 'both_hit': 38, 'both_miss': 22}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.025, 'both_hit': 33, 'both_miss': 27}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.001885, 'median_return': 0.000324, 'mean_absolute_return': 0.011808, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': -0.003664, 'median_return': -0.001324, 'mean_absolute_return': 0.015778, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.001263, 'median_return': -0.006017, 'mean_absolute_return': 0.020149, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.000554, 'median_return': 0.009812, 'mean_absolute_return': 0.031603, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.077493}, '60d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': 0.009363, 'median_return': 0.012092, 'mean_absolute_return': 0.056447, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001885`, median `0.000324`, mae `0.011808`
- 5d: sample `80`, hit `0.475`, avg `-0.003664`, median `-0.001324`, mae `0.015778`
- 10d: sample `80`, hit `0.45`, avg `-0.001263`, median `-0.006017`, mae `0.020149`
- 20d: sample `80`, hit `0.65`, avg `0.000554`, median `0.009812`, mae `0.031603`
- 60d: sample `80`, hit `0.525`, avg `0.009363`, median `0.012092`, mae `0.056447`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000379`, median `0.000324`, mae `0.013625`
- 5d: sample `20`, hit `0.45`, avg `-0.002495`, median `-0.004461`, mae `0.018408`
- 10d: sample `20`, hit `0.55`, avg `-0.000924`, median `0.005417`, mae `0.028548`
- 20d: sample `20`, hit `0.7`, avg `-0.007559`, median `0.007676`, mae `0.04369`
- 60d: sample `20`, hit `0.45`, avg `-0.004079`, median `-0.005997`, mae `0.052105`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001885`, median `0.000324`, mae `0.011808`
- 5d: sample `80`, hit `0.475`, avg `-0.003664`, median `-0.001324`, mae `0.015778`
- 10d: sample `80`, hit `0.45`, avg `-0.001263`, median `-0.006017`, mae `0.020149`
- 20d: sample `80`, hit `0.65`, avg `0.000554`, median `0.009812`, mae `0.031603`
- 60d: sample `80`, hit `0.525`, avg `0.009363`, median `0.012092`, mae `0.056447`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000379`, median `0.000324`, mae `0.013625`
- 5d: sample `20`, hit `0.45`, avg `-0.002495`, median `-0.004461`, mae `0.018408`
- 10d: sample `20`, hit `0.55`, avg `-0.000924`, median `0.005417`, mae `0.028548`
- 20d: sample `20`, hit `0.7`, avg `-0.007559`, median `0.007676`, mae `0.04369`
- 60d: sample `20`, hit `0.45`, avg `-0.004079`, median `-0.005997`, mae `0.052105`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.003224`, median `0.001558`, mae `0.012941`
- 5d: sample `40`, hit `0.45`, avg `-0.004818`, median `-0.001324`, mae `0.016711`
- 10d: sample `40`, hit `0.45`, avg `0.001143`, median `-0.003263`, mae `0.017336`
- 20d: sample `40`, hit `0.675`, avg `0.007894`, median `0.012958`, mae `0.027511`
- 60d: sample `40`, hit `0.625`, avg `0.026604`, median `0.046132`, mae `0.062021`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001885`, median `0.000324`, mae `0.011808`
- 5d: sample `80`, hit `0.475`, avg `-0.003664`, median `-0.001324`, mae `0.015778`
- 10d: sample `80`, hit `0.45`, avg `-0.001263`, median `-0.006017`, mae `0.020149`
- 20d: sample `80`, hit `0.65`, avg `0.000554`, median `0.009812`, mae `0.031603`
- 60d: sample `80`, hit `0.525`, avg `0.009363`, median `0.012092`, mae `0.056447`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.003224`, median `0.001558`, mae `0.012941`
- 5d: sample `40`, hit `0.45`, avg `-0.004818`, median `-0.001324`, mae `0.016711`
- 10d: sample `40`, hit `0.45`, avg `0.001143`, median `-0.003263`, mae `0.017336`
- 20d: sample `40`, hit `0.675`, avg `0.007894`, median `0.012958`, mae `0.027511`
- 60d: sample `40`, hit `0.625`, avg `0.026604`, median `0.046132`, mae `0.062021`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000714`, median `0.000603`, mae `0.007723`
- 5d: sample `20`, hit `0.55`, avg `-0.002525`, median `0.000873`, mae `0.01128`
- 10d: sample `20`, hit `0.35`, avg `-0.006414`, median `-0.007491`, mae `0.017379`
- 20d: sample `20`, hit `0.55`, avg `-0.006015`, median `0.007004`, mae `0.027701`
- 60d: sample `20`, hit `0.4`, avg `-0.011676`, median `-0.018455`, mae `0.04964`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.003224`, median `0.001558`, mae `0.012941`
- 5d: sample `40`, hit `0.45`, avg `-0.004818`, median `-0.001324`, mae `0.016711`
- 10d: sample `40`, hit `0.45`, avg `0.001143`, median `-0.003263`, mae `0.017336`
- 20d: sample `40`, hit `0.675`, avg `0.007894`, median `0.012958`, mae `0.027511`
- 60d: sample `40`, hit `0.625`, avg `0.026604`, median `0.046132`, mae `0.062021`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000714`, median `0.000603`, mae `0.007723`
- 5d: sample `20`, hit `0.55`, avg `-0.002525`, median `0.000873`, mae `0.01128`
- 10d: sample `20`, hit `0.35`, avg `-0.006414`, median `-0.007491`, mae `0.017379`
- 20d: sample `20`, hit `0.55`, avg `-0.006015`, median `0.007004`, mae `0.027701`
- 60d: sample `20`, hit `0.4`, avg `-0.011676`, median `-0.018455`, mae `0.04964`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.008224`, median `-0.001811`, mae `0.013729`
- 5d: sample `20`, hit `0.3`, avg `-0.010349`, median `-0.008162`, mae `0.016164`
- 10d: sample `20`, hit `0.3`, avg `-0.005093`, median `-0.007011`, mae `0.017546`
- 20d: sample `20`, hit `0.75`, avg `0.014507`, median `0.022652`, mae `0.030075`
- 60d: sample `20`, hit `0.65`, avg `0.034003`, median `0.059495`, mae `0.06966`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.008224`, median `-0.001811`, mae `0.013729`
- 5d: sample `20`, hit `0.3`, avg `-0.010349`, median `-0.008162`, mae `0.016164`
- 10d: sample `20`, hit `0.3`, avg `-0.005093`, median `-0.007011`, mae `0.017546`
- 20d: sample `20`, hit `0.75`, avg `0.014507`, median `0.022652`, mae `0.030075`
- 60d: sample `20`, hit `0.65`, avg `0.034003`, median `0.059495`, mae `0.06966`

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
