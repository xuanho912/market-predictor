# High Confidence Edge Report

Generated at: `2026-07-27T22:38:25.995693+00:00`

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
- 3d: sample `40`, hit `0.55`, avg `-0.006123`, median `0.000766`, mae `0.015952`
- 5d: sample `40`, hit `0.45`, avg `-0.009709`, median `-0.00244`, mae `0.018436`
- 10d: sample `40`, hit `0.375`, avg `-0.004463`, median `-0.007011`, mae `0.017447`
- 20d: sample `40`, hit `0.6`, avg `0.010804`, median `0.020068`, mae `0.033797`
- 60d: sample `40`, hit `0.7`, avg `0.035264`, median `0.050438`, mae `0.061497`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001737`, median `0.008009`, mae `0.021893`
- 5d: sample `40`, hit `0.575`, avg `0.002414`, median `0.006676`, mae `0.028473`
- 10d: sample `40`, hit `0.75`, avg `0.016582`, median `0.027869`, mae `0.038975`
- 20d: sample `40`, hit `0.7`, avg `0.021733`, median `0.046035`, mae `0.059323`
- 60d: sample `40`, hit `0.625`, avg `0.025493`, median `0.064934`, mae `0.098996`

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
- 3d: sample `8`, hit `0.25`, avg `-0.013711`, median `-0.010033`, mae `0.023889`
- 5d: sample `8`, hit `0.375`, avg `-0.018719`, median `-0.022295`, mae `0.029028`
- 10d: sample `8`, hit `0.25`, avg `-0.005373`, median `-0.006017`, mae `0.016616`
- 20d: sample `8`, hit `0.5`, avg `0.019534`, median `0.043456`, mae `0.042316`
- 60d: sample `8`, hit `0.625`, avg `0.051405`, median `0.099838`, mae `0.080567`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.006123, 'median_return': 0.000766, 'mean_absolute_return': 0.015952, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.009709, 'median_return': -0.00244, 'mean_absolute_return': 0.018436, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.004463, 'median_return': -0.007011, 'mean_absolute_return': 0.017447, 'max_adverse_excursion': -0.040826, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.010804, 'median_return': 0.020068, 'mean_absolute_return': 0.033797, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.035264, 'median_return': 0.050438, 'mean_absolute_return': 0.061497, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.013711, 'median_return': -0.010033, 'mean_absolute_return': 0.023889, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.018719, 'median_return': -0.022295, 'mean_absolute_return': 0.029028, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.005373, 'median_return': -0.006017, 'mean_absolute_return': 0.016616, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.019534, 'median_return': 0.043456, 'mean_absolute_return': 0.042316, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.051405, 'median_return': 0.099838, 'mean_absolute_return': 0.080567, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': -0.000913, 'median_return': 0.002067, 'mean_absolute_return': 0.018371, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': -0.001973, 'median_return': 0.001303, 'mean_absolute_return': 0.022835, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.00733, 'median_return': 0.014312, 'mean_absolute_return': 0.029499, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.074445}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.015906, 'median_return': 0.021759, 'mean_absolute_return': 0.047031, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.028042, 'median_return': 0.055167, 'mean_absolute_return': 0.080211, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.4875}, '10d': {'sample_size': 80, 'hit_rate': 0.4125}, '20d': {'sample_size': 80, 'hit_rate': 0.35}, '60d': {'sample_size': 80, 'hit_rate': 0.4125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': -0.001445, 'median_return': 0.002067, 'mean_absolute_return': 0.018758, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.001284, 'median_return': 0.003005, 'mean_absolute_return': 0.02161, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.051324}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.007938, 'median_return': 0.005691, 'mean_absolute_return': 0.025784, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.074445}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.02289, 'median_return': 0.02865, 'mean_absolute_return': 0.043507, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.110689}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.046858, 'median_return': 0.059131, 'mean_absolute_return': 0.077905, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.21267}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.004435, 'median_return': -0.0002, 'mean_absolute_return': 0.019417, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.010737, 'median_return': -0.007916, 'mean_absolute_return': 0.028987, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.000423, 'median_return': 0.014312, 'mean_absolute_return': 0.03549, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.003594, 'median_return': 0.017237, 'mean_absolute_return': 0.055719, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.01906, 'median_return': -0.00384, 'mean_absolute_return': 0.087272, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.129489}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.006123`, median `0.000766`, mae `0.015952`
- 5d: sample `40`, hit `0.45`, avg `-0.009709`, median `-0.00244`, mae `0.018436`
- 10d: sample `40`, hit `0.375`, avg `-0.004463`, median `-0.007011`, mae `0.017447`
- 20d: sample `40`, hit `0.6`, avg `0.010804`, median `0.020068`, mae `0.033797`
- 60d: sample `40`, hit `0.7`, avg `0.035264`, median `0.050438`, mae `0.061497`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001737`, median `0.008009`, mae `0.021893`
- 5d: sample `40`, hit `0.575`, avg `0.002414`, median `0.006676`, mae `0.028473`
- 10d: sample `40`, hit `0.75`, avg `0.016582`, median `0.027869`, mae `0.038975`
- 20d: sample `40`, hit `0.7`, avg `0.021733`, median `0.046035`, mae `0.059323`
- 60d: sample `40`, hit `0.625`, avg `0.025493`, median `0.064934`, mae `0.098996`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `-0.002686`, median `0.001139`, mae `0.011436`
- 5d: sample `20`, hit `0.5`, avg `-0.004159`, median `0.000688`, mae `0.013837`
- 10d: sample `20`, hit `0.45`, avg `-0.004292`, median `-0.007117`, mae `0.018986`
- 20d: sample `20`, hit `0.5`, avg `0.005133`, median `0.015416`, mae `0.027973`
- 60d: sample `20`, hit `0.65`, avg `0.022017`, median `0.032982`, mae `0.045596`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.006123`, median `0.000766`, mae `0.015952`
- 5d: sample `40`, hit `0.45`, avg `-0.009709`, median `-0.00244`, mae `0.018436`
- 10d: sample `40`, hit `0.375`, avg `-0.004463`, median `-0.007011`, mae `0.017447`
- 20d: sample `40`, hit `0.6`, avg `0.010804`, median `0.020068`, mae `0.033797`
- 60d: sample `40`, hit `0.7`, avg `0.035264`, median `0.050438`, mae `0.061497`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.007909`, median `0.011836`, mae `0.02437`
- 5d: sample `20`, hit `0.75`, avg `0.015566`, median `0.019812`, mae `0.027959`
- 10d: sample `20`, hit `0.9`, avg `0.032741`, median `0.035876`, mae `0.04246`
- 20d: sample `20`, hit `0.8`, avg `0.047061`, median `0.060775`, mae `0.062926`
- 60d: sample `20`, hit `0.8`, avg `0.070046`, median `0.100541`, mae `0.11072`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `-0.002686`, median `0.001139`, mae `0.011436`
- 5d: sample `20`, hit `0.5`, avg `-0.004159`, median `0.000688`, mae `0.013837`
- 10d: sample `20`, hit `0.45`, avg `-0.004292`, median `-0.007117`, mae `0.018986`
- 20d: sample `20`, hit `0.5`, avg `0.005133`, median `0.015416`, mae `0.027973`
- 60d: sample `20`, hit `0.65`, avg `0.022017`, median `0.032982`, mae `0.045596`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.006123`, median `0.000766`, mae `0.015952`
- 5d: sample `40`, hit `0.45`, avg `-0.009709`, median `-0.00244`, mae `0.018436`
- 10d: sample `40`, hit `0.375`, avg `-0.004463`, median `-0.007011`, mae `0.017447`
- 20d: sample `40`, hit `0.6`, avg `0.010804`, median `0.020068`, mae `0.033797`
- 60d: sample `40`, hit `0.7`, avg `0.035264`, median `0.050438`, mae `0.061497`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001737`, median `0.008009`, mae `0.021893`
- 5d: sample `40`, hit `0.575`, avg `0.002414`, median `0.006676`, mae `0.028473`
- 10d: sample `40`, hit `0.75`, avg `0.016582`, median `0.027869`, mae `0.038975`
- 20d: sample `40`, hit `0.7`, avg `0.021733`, median `0.046035`, mae `0.059323`
- 60d: sample `40`, hit `0.625`, avg `0.025493`, median `0.064934`, mae `0.098996`

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
- 3d: sample `80`, hit `0.5625`, avg `-0.002193`, median `0.001199`, mae `0.018923`
- 5d: sample `80`, hit `0.5125`, avg `-0.003647`, median `0.000762`, mae `0.023454`
- 10d: sample `80`, hit `0.5625`, avg `0.00606`, median `0.011031`, mae `0.028211`
- 20d: sample `80`, hit `0.65`, avg `0.016269`, median `0.021759`, mae `0.04656`
- 60d: sample `80`, hit `0.6625`, avg `0.030379`, median `0.055167`, mae `0.080246`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `-0.002686`, median `0.001139`, mae `0.011436`
- 5d: sample `20`, hit `0.5`, avg `-0.004159`, median `0.000688`, mae `0.013837`
- 10d: sample `20`, hit `0.45`, avg `-0.004292`, median `-0.007117`, mae `0.018986`
- 20d: sample `20`, hit `0.5`, avg `0.005133`, median `0.015416`, mae `0.027973`
- 60d: sample `20`, hit `0.65`, avg `0.022017`, median `0.032982`, mae `0.045596`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.000263`, median `0.002067`, mae `0.018408`
- 5d: sample `60`, hit `0.55`, avg `0.000223`, median `0.002451`, mae `0.023594`
- 10d: sample `60`, hit `0.65`, avg `0.009624`, median `0.017778`, mae `0.032312`
- 20d: sample `60`, hit `0.6333`, avg `0.0162`, median `0.02086`, mae `0.048873`
- 60d: sample `60`, hit `0.6333`, avg `0.024334`, median `0.053855`, mae `0.081196`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `-0.002686`, median `0.001139`, mae `0.011436`
- 5d: sample `20`, hit `0.5`, avg `-0.004159`, median `0.000688`, mae `0.013837`
- 10d: sample `20`, hit `0.45`, avg `-0.004292`, median `-0.007117`, mae `0.018986`
- 20d: sample `20`, hit `0.5`, avg `0.005133`, median `0.015416`, mae `0.027973`
- 60d: sample `20`, hit `0.65`, avg `0.022017`, median `0.032982`, mae `0.045596`

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
