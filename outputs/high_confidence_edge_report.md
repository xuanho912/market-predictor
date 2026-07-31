# High Confidence Edge Report

Generated at: `2026-07-31T23:49:41.150197+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `-0.000726`, median `0.000766`, mae `0.017108`
- 5d: sample `60`, hit `0.5333`, avg `-0.002453`, median `0.000762`, mae `0.017659`
- 10d: sample `60`, hit `0.35`, avg `2.6e-05`, median `-0.007117`, mae `0.023824`
- 20d: sample `60`, hit `0.5667`, avg `0.010724`, median `0.012291`, mae `0.041148`
- 60d: sample `60`, hit `0.5667`, avg `0.018554`, median `0.032982`, mae `0.071975`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `0.000366`, median `-0.0002`, mae `0.01642`
- 5d: sample `20`, hit `0.5`, avg `-0.002746`, median `0.001239`, mae `0.024273`
- 10d: sample `20`, hit `0.4`, avg `-0.010756`, median `-0.0113`, mae `0.037236`
- 20d: sample `20`, hit `0.5`, avg `-0.020638`, median `0.007748`, mae `0.062011`
- 60d: sample `20`, hit `0.35`, avg `-0.062863`, median `-0.036478`, mae `0.107659`

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
- 3d: sample `8`, hit `0.25`, avg `-0.020886`, median `-0.022062`, mae `0.023511`
- 5d: sample `8`, hit `0.25`, avg `-0.026523`, median `-0.016062`, mae `0.027378`
- 10d: sample `8`, hit `0.125`, avg `-0.014898`, median `-0.015123`, mae `0.019706`
- 20d: sample `8`, hit `0.375`, avg `-0.02428`, median `-0.022761`, mae `0.045088`
- 60d: sample `8`, hit `0.375`, avg `-0.027753`, median `-0.028872`, mae `0.06763`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.020886`, median `-0.022062`, mae `0.023511`
- 5d: sample `8`, hit `0.25`, avg `-0.026523`, median `-0.016062`, mae `0.027378`
- 10d: sample `8`, hit `0.125`, avg `-0.014898`, median `-0.015123`, mae `0.019706`
- 20d: sample `8`, hit `0.375`, avg `-0.02428`, median `-0.022761`, mae `0.045088`
- 60d: sample `8`, hit `0.375`, avg `-0.027753`, median `-0.028872`, mae `0.06763`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.000726, 'median_return': 0.000766, 'mean_absolute_return': 0.017108, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.037139}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.002453, 'median_return': 0.000762, 'mean_absolute_return': 0.017659, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.046339}, '10d': {'sample_size': 60, 'hit_rate': 0.35, 'avg_return': 2.6e-05, 'median_return': -0.007117, 'mean_absolute_return': 0.023824, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.010724, 'median_return': 0.012291, 'mean_absolute_return': 0.041148, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.129427}, '60d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.018554, 'median_return': 0.032982, 'mean_absolute_return': 0.071975, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.020886, 'median_return': -0.022062, 'mean_absolute_return': 0.023511, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.026523, 'median_return': -0.016062, 'mean_absolute_return': 0.027378, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.003005}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.014898, 'median_return': -0.015123, 'mean_absolute_return': 0.019706, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.019233}, '20d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.02428, 'median_return': -0.022761, 'mean_absolute_return': 0.045088, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.027753, 'median_return': -0.028872, 'mean_absolute_return': 0.06763, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.001818, 'median_return': 0.000766, 'mean_absolute_return': 0.016205, 'max_adverse_excursion': -0.038633, 'max_favorable_excursion': 0.057206}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.00014, 'median_return': 0.001624, 'mean_absolute_return': 0.018416, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.001311, 'median_return': -0.007117, 'mean_absolute_return': 0.028007, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.094092}, '20d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.005902, 'median_return': 0.007762, 'mean_absolute_return': 0.046506, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.001084, 'median_return': 0.018072, 'mean_absolute_return': 0.08237, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5375}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.4125}, '20d': {'sample_size': 80, 'hit_rate': 0.55}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.0, 'both_hit': 23, 'both_miss': 17}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 20, 'both_miss': 20}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.125, 'both_hit': 18, 'both_miss': 22}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.125, 'both_hit': 29, 'both_miss': 11}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 27, 'both_miss': 13}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.000826, 'median_return': 0.000603, 'mean_absolute_return': 0.016261, 'max_adverse_excursion': -0.038633, 'max_favorable_excursion': 0.057206}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.000229, 'median_return': 0.001303, 'mean_absolute_return': 0.01912, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -2.1e-05, 'median_return': -0.006957, 'mean_absolute_return': 0.03027, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.094092}, '20d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.003361, 'median_return': 0.007762, 'mean_absolute_return': 0.048371, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.006735, 'median_return': -0.003034, 'mean_absolute_return': 0.08415, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.00429, 'median_return': 0.001199, 'mean_absolute_return': 0.01896, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.029522}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.010792, 'median_return': -0.001429, 'mean_absolute_return': 0.019889, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.046339}, '10d': {'sample_size': 20, 'hit_rate': 0.15, 'avg_return': -0.010616, 'median_return': -0.011432, 'mean_absolute_return': 0.0179, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.043492}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.001451, 'median_return': 0.001407, 'mean_absolute_return': 0.040342, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.086905}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.013004, 'median_return': 0.037425, 'mean_absolute_return': 0.071131, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.004086`, median `-0.000285`, mae `0.016109`
- 5d: sample `40`, hit `0.525`, avg `-0.007051`, median `0.000688`, mae `0.015344`
- 10d: sample `40`, hit `0.15`, avg `-0.012814`, median `-0.013317`, mae `0.017436`
- 20d: sample `40`, hit `0.4`, avg `-0.007537`, median `-0.004441`, mae `0.032568`
- 60d: sample `40`, hit `0.475`, avg `0.001769`, median `-0.003049`, mae `0.05591`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.003181`, median `0.006513`, mae `0.017762`
- 5d: sample `40`, hit `0.525`, avg `0.001998`, median `0.002451`, mae `0.023281`
- 10d: sample `40`, hit `0.575`, avg `0.007475`, median `0.013774`, mae `0.036918`
- 20d: sample `40`, hit `0.7`, avg `0.013304`, median `0.026005`, mae `0.06016`
- 60d: sample `40`, hit `0.55`, avg `-0.005369`, median `0.043615`, mae `0.105882`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.004086`, median `-0.000285`, mae `0.016109`
- 5d: sample `40`, hit `0.525`, avg `-0.007051`, median `0.000688`, mae `0.015344`
- 10d: sample `40`, hit `0.15`, avg `-0.012814`, median `-0.013317`, mae `0.017436`
- 20d: sample `40`, hit `0.4`, avg `-0.007537`, median `-0.004441`, mae `0.032568`
- 60d: sample `40`, hit `0.475`, avg `0.001769`, median `-0.003049`, mae `0.05591`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005996`, median `0.009701`, mae `0.019104`
- 5d: sample `20`, hit `0.55`, avg `0.006743`, median `0.009517`, mae `0.022288`
- 10d: sample `20`, hit `0.75`, avg `0.025705`, median `0.033374`, mae `0.036601`
- 20d: sample `20`, hit `0.9`, avg `0.047246`, median `0.049691`, mae `0.058309`
- 60d: sample `20`, hit `0.75`, avg `0.052124`, median `0.073651`, mae `0.104105`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005996`, median `0.009701`, mae `0.019104`
- 5d: sample `20`, hit `0.55`, avg `0.006743`, median `0.009517`, mae `0.022288`
- 10d: sample `20`, hit `0.75`, avg `0.025705`, median `0.033374`, mae `0.036601`
- 20d: sample `20`, hit `0.9`, avg `0.047246`, median `0.049691`, mae `0.058309`
- 60d: sample `20`, hit `0.75`, avg `0.052124`, median `0.073651`, mae `0.104105`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.004086`, median `-0.000285`, mae `0.016109`
- 5d: sample `40`, hit `0.525`, avg `-0.007051`, median `0.000688`, mae `0.015344`
- 10d: sample `40`, hit `0.15`, avg `-0.012814`, median `-0.013317`, mae `0.017436`
- 20d: sample `40`, hit `0.4`, avg `-0.007537`, median `-0.004441`, mae `0.032568`
- 60d: sample `40`, hit `0.475`, avg `0.001769`, median `-0.003049`, mae `0.05591`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005996`, median `0.009701`, mae `0.019104`
- 5d: sample `20`, hit `0.55`, avg `0.006743`, median `0.009517`, mae `0.022288`
- 10d: sample `20`, hit `0.75`, avg `0.025705`, median `0.033374`, mae `0.036601`
- 20d: sample `20`, hit `0.9`, avg `0.047246`, median `0.049691`, mae `0.058309`
- 60d: sample `20`, hit `0.75`, avg `0.052124`, median `0.073651`, mae `0.104105`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `0.000366`, median `-0.0002`, mae `0.01642`
- 5d: sample `20`, hit `0.5`, avg `-0.002746`, median `0.001239`, mae `0.024273`
- 10d: sample `20`, hit `0.4`, avg `-0.010756`, median `-0.0113`, mae `0.037236`
- 20d: sample `20`, hit `0.5`, avg `-0.020638`, median `0.007748`, mae `0.062011`
- 60d: sample `20`, hit `0.35`, avg `-0.062863`, median `-0.036478`, mae `0.107659`

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
- 3d: sample `80`, hit `0.5125`, avg `-0.000453`, median `0.000603`, mae `0.016936`
- 5d: sample `80`, hit `0.525`, avg `-0.002527`, median `0.000762`, mae `0.019312`
- 10d: sample `80`, hit `0.3625`, avg `-0.00267`, median `-0.007755`, mae `0.027177`
- 20d: sample `80`, hit `0.55`, avg `0.002884`, median `0.007748`, mae `0.046364`
- 60d: sample `80`, hit `0.5125`, avg `-0.0018`, median `0.007258`, mae `0.080896`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `-0.000726`, median `0.000766`, mae `0.017108`
- 5d: sample `60`, hit `0.5333`, avg `-0.002453`, median `0.000762`, mae `0.017659`
- 10d: sample `60`, hit `0.35`, avg `2.6e-05`, median `-0.007117`, mae `0.023824`
- 20d: sample `60`, hit `0.5667`, avg `0.010724`, median `0.012291`, mae `0.041148`
- 60d: sample `60`, hit `0.5667`, avg `0.018554`, median `0.032982`, mae `0.071975`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.000691`, median `0.00234`, mae `0.018162`
- 5d: sample `60`, hit `0.5`, avg `-0.002265`, median `0.000415`, mae `0.02215`
- 10d: sample `60`, hit `0.4333`, avg `0.001444`, median `-0.006017`, mae `0.030579`
- 20d: sample `60`, hit `0.65`, avg `0.009353`, median `0.017237`, mae `0.053554`
- 60d: sample `60`, hit `0.5667`, avg `0.000755`, median `0.037425`, mae `0.094298`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.000853`, median `0.006513`, mae `0.019032`
- 5d: sample `40`, hit `0.5`, avg `-0.002024`, median `0.000415`, mae `0.021089`
- 10d: sample `40`, hit `0.45`, avg `0.007545`, median `-0.0004`, mae `0.02725`
- 20d: sample `40`, hit `0.725`, avg `0.024348`, median `0.03392`, mae `0.049326`
- 60d: sample `40`, hit `0.675`, avg `0.032564`, median `0.059495`, mae `0.087618`

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
