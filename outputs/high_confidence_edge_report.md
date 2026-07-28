# High Confidence Edge Report

Generated at: `2026-07-28T00:11:27.331554+00:00`

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
- 3d: sample `40`, hit `0.55`, avg `0.000121`, median `0.005`, mae `0.021288`
- 5d: sample `40`, hit `0.55`, avg `0.00108`, median `0.003727`, mae `0.027608`
- 10d: sample `40`, hit `0.725`, avg `0.012998`, median `0.023905`, mae `0.038837`
- 20d: sample `40`, hit `0.675`, avg `0.018713`, median `0.045022`, mae `0.058781`
- 60d: sample `40`, hit `0.6`, avg `0.02059`, median `0.058473`, mae `0.098872`

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
- 3d: sample `8`, hit `0.625`, avg `-0.003324`, median `0.000766`, mae `0.011739`
- 5d: sample `8`, hit `0.5`, avg `-0.007791`, median `0.000688`, mae `0.011554`
- 10d: sample `8`, hit `0.5`, avg `-0.000342`, median `0.000254`, mae `0.013491`
- 20d: sample `8`, hit `0.5`, avg `0.012209`, median `0.020226`, mae `0.02115`
- 60d: sample `8`, hit `0.625`, avg `0.031452`, median `0.057625`, mae `0.046696`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.021369`, median `-0.030499`, mae `0.026372`
- 5d: sample `8`, hit `0.25`, avg `-0.028609`, median `-0.026253`, mae `0.032304`
- 10d: sample `8`, hit `0.0`, avg `-0.017639`, median `-0.011432`, mae `0.017639`
- 20d: sample `8`, hit `0.5`, avg `0.001093`, median `0.029166`, mae `0.050735`
- 60d: sample `8`, hit `0.625`, avg `0.027797`, median `0.046132`, mae `0.084515`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.005789, 'median_return': 0.000766, 'mean_absolute_return': 0.017373, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.037139}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.009539, 'median_return': -0.001429, 'mean_absolute_return': 0.018765, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.004565, 'median_return': -0.007011, 'mean_absolute_return': 0.017342, 'max_adverse_excursion': -0.040826, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.011187, 'median_return': 0.020068, 'mean_absolute_return': 0.033597, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.033821, 'median_return': 0.046407, 'mean_absolute_return': 0.059641, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.021369, 'median_return': -0.030499, 'mean_absolute_return': 0.026372, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.028609, 'median_return': -0.026253, 'mean_absolute_return': 0.032304, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.017639, 'median_return': -0.011432, 'mean_absolute_return': 0.017639, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001093, 'median_return': 0.029166, 'mean_absolute_return': 0.050735, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.027797, 'median_return': 0.046132, 'mean_absolute_return': 0.084515, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': -0.000775, 'median_return': 0.00234, 'mean_absolute_return': 0.018548, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.00152, 'median_return': 0.002451, 'mean_absolute_return': 0.022174, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.006645, 'median_return': 0.014312, 'mean_absolute_return': 0.029251, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.01649, 'median_return': 0.02086, 'mean_absolute_return': 0.045684, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.027139, 'median_return': 0.053855, 'mean_absolute_return': 0.078672, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.4625}, '10d': {'sample_size': 80, 'hit_rate': 0.325}, '20d': {'sample_size': 80, 'hit_rate': 0.475}, '60d': {'sample_size': 80, 'hit_rate': 0.55}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': -0.0023, 'median_return': 0.001405, 'mean_absolute_return': 0.019301, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.00206, 'median_return': 0.003005, 'mean_absolute_return': 0.021253, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.051324}, '10d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.005481, 'median_return': 0.001574, 'mean_absolute_return': 0.025623, 'max_adverse_excursion': -0.06893, 'max_favorable_excursion': 0.061544}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.021132, 'median_return': 0.026113, 'mean_absolute_return': 0.043012, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.110689}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.042627, 'median_return': 0.058473, 'mean_absolute_return': 0.076584, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.21267}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.004435, 'median_return': -0.0002, 'mean_absolute_return': 0.019417, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.010737, 'median_return': -0.007916, 'mean_absolute_return': 0.028987, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.000423, 'median_return': 0.014312, 'mean_absolute_return': 0.03549, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.003594, 'median_return': 0.017237, 'mean_absolute_return': 0.055719, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.01906, 'median_return': -0.00384, 'mean_absolute_return': 0.087272, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.129489}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `40`, hit `0.55`, avg `0.000121`, median `0.005`, mae `0.021288`
- 5d: sample `40`, hit `0.55`, avg `0.00108`, median `0.003727`, mae `0.027608`
- 10d: sample `40`, hit `0.725`, avg `0.012998`, median `0.023905`, mae `0.038837`
- 20d: sample `40`, hit `0.675`, avg `0.018713`, median `0.045022`, mae `0.058781`
- 60d: sample `40`, hit `0.6`, avg `0.02059`, median `0.058473`, mae `0.098872`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005789`, median `0.000766`, mae `0.017373`
- 5d: sample `40`, hit `0.475`, avg `-0.009539`, median `-0.001429`, mae `0.018765`
- 10d: sample `40`, hit `0.375`, avg `-0.004565`, median `-0.007011`, mae `0.017342`
- 20d: sample `40`, hit `0.625`, avg `0.011187`, median `0.020068`, mae `0.033597`
- 60d: sample `40`, hit `0.7`, avg `0.033821`, median `0.046407`, mae `0.059641`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005789`, median `0.000766`, mae `0.017373`
- 5d: sample `40`, hit `0.475`, avg `-0.009539`, median `-0.001429`, mae `0.018765`
- 10d: sample `40`, hit `0.375`, avg `-0.004565`, median `-0.007011`, mae `0.017342`
- 20d: sample `40`, hit `0.625`, avg `0.011187`, median `0.020068`, mae `0.033597`
- 60d: sample `40`, hit `0.7`, avg `0.033821`, median `0.046407`, mae `0.059641`

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
- 3d: sample `40`, hit `0.55`, avg `0.000121`, median `0.005`, mae `0.021288`
- 5d: sample `40`, hit `0.55`, avg `0.00108`, median `0.003727`, mae `0.027608`
- 10d: sample `40`, hit `0.725`, avg `0.012998`, median `0.023905`, mae `0.038837`
- 20d: sample `40`, hit `0.675`, avg `0.018713`, median `0.045022`, mae `0.058781`
- 60d: sample `40`, hit `0.6`, avg `0.02059`, median `0.058473`, mae `0.098872`

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
- 3d: sample `80`, hit `0.55`, avg `-0.002834`, median `0.001139`, mae `0.01933`
- 5d: sample `80`, hit `0.5125`, avg `-0.004229`, median `0.000762`, mae `0.023187`
- 10d: sample `80`, hit `0.55`, avg `0.004217`, median `0.008202`, mae `0.02809`
- 20d: sample `80`, hit `0.65`, avg `0.01495`, median `0.02086`, mae `0.046189`
- 60d: sample `80`, hit `0.65`, avg `0.027205`, median `0.050438`, mae `0.079256`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005789`, median `0.000766`, mae `0.017373`
- 5d: sample `40`, hit `0.475`, avg `-0.009539`, median `-0.001429`, mae `0.018765`
- 10d: sample `40`, hit `0.375`, avg `-0.004565`, median `-0.007011`, mae `0.017342`
- 20d: sample `40`, hit `0.625`, avg `0.011187`, median `0.020068`, mae `0.033597`
- 60d: sample `40`, hit `0.7`, avg `0.033821`, median `0.046407`, mae `0.059641`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `-0.000592`, median `0.001405`, mae `0.01895`
- 5d: sample `60`, hit `0.55`, avg `-0.000552`, median `0.002451`, mae `0.023237`
- 10d: sample `60`, hit `0.6333`, avg `0.007167`, median `0.017481`, mae `0.03215`
- 20d: sample `60`, hit `0.6333`, avg `0.014442`, median `0.020226`, mae `0.048378`
- 60d: sample `60`, hit `0.6167`, avg `0.020103`, median `0.046407`, mae `0.079876`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `-0.002019`, median `0.001139`, mae `0.014276`
- 5d: sample `20`, hit `0.55`, avg `-0.003818`, median `0.000762`, mae `0.014496`
- 10d: sample `20`, hit `0.45`, avg `-0.004495`, median `-0.007117`, mae `0.018776`
- 20d: sample `20`, hit `0.55`, avg `0.005899`, median `0.015416`, mae `0.027574`
- 60d: sample `20`, hit `0.65`, avg `0.01913`, median `0.029164`, mae `0.041884`

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
