# High Confidence Edge Report

Generated at: `2026-07-28T14:40:59.344635+00:00`

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
- 3d: sample `40`, hit `0.525`, avg `-0.00603`, median `0.000603`, mae `0.016443`
- 5d: sample `40`, hit `0.475`, avg `-0.008938`, median `-0.000513`, mae `0.018797`
- 10d: sample `40`, hit `0.375`, avg `-0.004244`, median `-0.007011`, mae `0.017021`
- 20d: sample `40`, hit `0.575`, avg `0.008268`, median `0.016745`, mae `0.034465`
- 60d: sample `40`, hit `0.625`, avg `0.028214`, median `0.046132`, mae `0.059933`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.00418`, median `0.010664`, mae `0.022861`
- 5d: sample `40`, hit `0.6`, avg `0.00554`, median `0.009517`, mae `0.029681`
- 10d: sample `40`, hit `0.725`, avg `0.018373`, median `0.030858`, mae `0.04191`
- 20d: sample `40`, hit `0.675`, avg `0.027247`, median `0.048862`, mae `0.064597`
- 60d: sample `40`, hit `0.7`, avg `0.043949`, median `0.087998`, mae `0.11027`

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
- 3d: sample `8`, hit `0.625`, avg `-0.004826`, median `0.000603`, mae `0.010237`
- 5d: sample `8`, hit `0.5`, avg `-0.008522`, median `0.000688`, mae `0.010823`
- 10d: sample `8`, hit `0.375`, avg `-0.0043`, median `-0.007117`, mae `0.012861`
- 20d: sample `8`, hit `0.375`, avg `0.005427`, median `-0.001203`, mae `0.014669`
- 60d: sample `8`, hit `0.5`, avg `0.020496`, median `0.032982`, mae `0.036502`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.020111`, median `-0.026364`, mae `0.025114`
- 5d: sample `8`, hit `0.25`, avg `-0.025979`, median `-0.026253`, mae `0.029675`
- 10d: sample `8`, hit `0.125`, avg `-0.01169`, median `-0.007755`, mae `0.014789`
- 20d: sample `8`, hit `0.5`, avg `0.014523`, median `0.029166`, mae `0.037305`
- 60d: sample `8`, hit `0.625`, avg `0.041575`, median `0.046132`, mae `0.070737`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.00603, 'median_return': 0.000603, 'mean_absolute_return': 0.016443, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.037139}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.008938, 'median_return': -0.000513, 'mean_absolute_return': 0.018797, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.004244, 'median_return': -0.007011, 'mean_absolute_return': 0.017021, 'max_adverse_excursion': -0.040826, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.008268, 'median_return': 0.016745, 'mean_absolute_return': 0.034465, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.028214, 'median_return': 0.046132, 'mean_absolute_return': 0.059933, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.020111, 'median_return': -0.026364, 'mean_absolute_return': 0.025114, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.025979, 'median_return': -0.026253, 'mean_absolute_return': 0.029675, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.01169, 'median_return': -0.007755, 'mean_absolute_return': 0.014789, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.012396}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.014523, 'median_return': 0.029166, 'mean_absolute_return': 0.037305, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.041575, 'median_return': 0.046132, 'mean_absolute_return': 0.070737, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.001207, 'median_return': 0.003785, 'mean_absolute_return': 0.019045, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.000999, 'median_return': 0.003005, 'mean_absolute_return': 0.023635, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.009148, 'median_return': 0.014312, 'mean_absolute_return': 0.031096, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.080212}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.018117, 'median_return': 0.026113, 'mean_absolute_return': 0.050889, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.035471, 'median_return': 0.059104, 'mean_absolute_return': 0.086698, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.21366}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.325}, '20d': {'sample_size': 80, 'hit_rate': 0.45}, '60d': {'sample_size': 80, 'hit_rate': 0.4625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.05, 'both_hit': 9, 'both_miss': 11}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.075, 'both_hit': 8, 'both_miss': 12}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.25, 'both_hit': 6, 'both_miss': 14}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.175, 'both_hit': 13, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.175, 'both_hit': 14, 'both_miss': 6}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.00603, 'median_return': 0.000603, 'mean_absolute_return': 0.016443, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.037139}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.008938, 'median_return': -0.000513, 'mean_absolute_return': 0.018797, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.004244, 'median_return': -0.007011, 'mean_absolute_return': 0.017021, 'max_adverse_excursion': -0.040826, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.008268, 'median_return': 0.016745, 'mean_absolute_return': 0.034465, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.028214, 'median_return': 0.046132, 'mean_absolute_return': 0.059933, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.00418, 'median_return': 0.010664, 'mean_absolute_return': 0.022861, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.00554, 'median_return': 0.009517, 'mean_absolute_return': 0.029681, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.018373, 'median_return': 0.030858, 'mean_absolute_return': 0.04191, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.080212}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.027247, 'median_return': 0.048862, 'mean_absolute_return': 0.064597, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.043949, 'median_return': 0.087998, 'mean_absolute_return': 0.11027, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.21366}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.00603`, median `0.000603`, mae `0.016443`
- 5d: sample `40`, hit `0.475`, avg `-0.008938`, median `-0.000513`, mae `0.018797`
- 10d: sample `40`, hit `0.375`, avg `-0.004244`, median `-0.007011`, mae `0.017021`
- 20d: sample `40`, hit `0.575`, avg `0.008268`, median `0.016745`, mae `0.034465`
- 60d: sample `40`, hit `0.625`, avg `0.028214`, median `0.046132`, mae `0.059933`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.00418`, median `0.010664`, mae `0.022861`
- 5d: sample `40`, hit `0.6`, avg `0.00554`, median `0.009517`, mae `0.029681`
- 10d: sample `40`, hit `0.725`, avg `0.018373`, median `0.030858`, mae `0.04191`
- 20d: sample `40`, hit `0.675`, avg `0.027247`, median `0.048862`, mae `0.064597`
- 60d: sample `40`, hit `0.7`, avg `0.043949`, median `0.087998`, mae `0.11027`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.00603`, median `0.000603`, mae `0.016443`
- 5d: sample `40`, hit `0.475`, avg `-0.008938`, median `-0.000513`, mae `0.018797`
- 10d: sample `40`, hit `0.375`, avg `-0.004244`, median `-0.007011`, mae `0.017021`
- 20d: sample `40`, hit `0.575`, avg `0.008268`, median `0.016745`, mae `0.034465`
- 60d: sample `40`, hit `0.625`, avg `0.028214`, median `0.046132`, mae `0.059933`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.00603`, median `0.000603`, mae `0.016443`
- 5d: sample `40`, hit `0.475`, avg `-0.008938`, median `-0.000513`, mae `0.018797`
- 10d: sample `40`, hit `0.375`, avg `-0.004244`, median `-0.007011`, mae `0.017021`
- 20d: sample `40`, hit `0.575`, avg `0.008268`, median `0.016745`, mae `0.034465`
- 60d: sample `40`, hit `0.625`, avg `0.028214`, median `0.046132`, mae `0.059933`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.00603`, median `0.000603`, mae `0.016443`
- 5d: sample `40`, hit `0.475`, avg `-0.008938`, median `-0.000513`, mae `0.018797`
- 10d: sample `40`, hit `0.375`, avg `-0.004244`, median `-0.007011`, mae `0.017021`
- 20d: sample `40`, hit `0.575`, avg `0.008268`, median `0.016745`, mae `0.034465`
- 60d: sample `40`, hit `0.625`, avg `0.028214`, median `0.046132`, mae `0.059933`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.00603`, median `0.000603`, mae `0.016443`
- 5d: sample `40`, hit `0.475`, avg `-0.008938`, median `-0.000513`, mae `0.018797`
- 10d: sample `40`, hit `0.375`, avg `-0.004244`, median `-0.007011`, mae `0.017021`
- 20d: sample `40`, hit `0.575`, avg `0.008268`, median `0.016745`, mae `0.034465`
- 60d: sample `40`, hit `0.625`, avg `0.028214`, median `0.046132`, mae `0.059933`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.00418`, median `0.010664`, mae `0.022861`
- 5d: sample `40`, hit `0.6`, avg `0.00554`, median `0.009517`, mae `0.029681`
- 10d: sample `40`, hit `0.725`, avg `0.018373`, median `0.030858`, mae `0.04191`
- 20d: sample `40`, hit `0.675`, avg `0.027247`, median `0.048862`, mae `0.064597`
- 60d: sample `40`, hit `0.7`, avg `0.043949`, median `0.087998`, mae `0.11027`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.009838`, median `-0.001658`, mae `0.020747`
- 5d: sample `20`, hit `0.4`, avg `-0.016028`, median `-0.016062`, mae `0.023803`
- 10d: sample `20`, hit `0.3`, avg `-0.00457`, median `-0.006017`, mae `0.015844`
- 20d: sample `20`, hit `0.65`, avg `0.014931`, median `0.026113`, mae `0.038989`
- 60d: sample `20`, hit `0.7`, avg `0.042471`, median `0.059131`, mae `0.076168`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.5625`, avg `-0.000925`, median `0.001199`, mae `0.019652`
- 5d: sample `80`, hit `0.5375`, avg `-0.001699`, median `0.002451`, mae `0.024239`
- 10d: sample `80`, hit `0.55`, avg `0.007065`, median `0.006208`, mae `0.029466`
- 20d: sample `80`, hit `0.625`, avg `0.017758`, median `0.026113`, mae `0.049531`
- 60d: sample `80`, hit `0.6625`, avg `0.036082`, median `0.058473`, mae `0.085102`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.00603`, median `0.000603`, mae `0.016443`
- 5d: sample `40`, hit `0.475`, avg `-0.008938`, median `-0.000513`, mae `0.018797`
- 10d: sample `40`, hit `0.375`, avg `-0.004244`, median `-0.007011`, mae `0.017021`
- 20d: sample `40`, hit `0.575`, avg `0.008268`, median `0.016745`, mae `0.034465`
- 60d: sample `40`, hit `0.625`, avg `0.028214`, median `0.046132`, mae `0.059933`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.002222`, median `0.000766`, mae `0.012139`
- 5d: sample `20`, hit `0.55`, avg `-0.001849`, median `0.000762`, mae `0.013792`
- 10d: sample `20`, hit `0.45`, avg `-0.003917`, median `-0.007117`, mae `0.018199`
- 20d: sample `20`, hit `0.5`, avg `0.001606`, median `0.003675`, mae `0.029941`
- 60d: sample `20`, hit `0.55`, avg `0.013958`, median `0.006294`, mae `0.043698`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5625`, avg `-0.000925`, median `0.001199`, mae `0.019652`
- 5d: sample `80`, hit `0.5375`, avg `-0.001699`, median `0.002451`, mae `0.024239`
- 10d: sample `80`, hit `0.55`, avg `0.007065`, median `0.006208`, mae `0.029466`
- 20d: sample `80`, hit `0.625`, avg `0.017758`, median `0.026113`, mae `0.049531`
- 60d: sample `80`, hit `0.6625`, avg `0.036082`, median `0.058473`, mae `0.085102`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.002222`, median `0.000766`, mae `0.012139`
- 5d: sample `20`, hit `0.55`, avg `-0.001849`, median `0.000762`, mae `0.013792`
- 10d: sample `20`, hit `0.45`, avg `-0.003917`, median `-0.007117`, mae `0.018199`
- 20d: sample `20`, hit `0.5`, avg `0.001606`, median `0.003675`, mae `0.029941`
- 60d: sample `20`, hit `0.55`, avg `0.013958`, median `0.006294`, mae `0.043698`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.00603`, median `0.000603`, mae `0.016443`
- 5d: sample `40`, hit `0.475`, avg `-0.008938`, median `-0.000513`, mae `0.018797`
- 10d: sample `40`, hit `0.375`, avg `-0.004244`, median `-0.007011`, mae `0.017021`
- 20d: sample `40`, hit `0.575`, avg `0.008268`, median `0.016745`, mae `0.034465`
- 60d: sample `40`, hit `0.625`, avg `0.028214`, median `0.046132`, mae `0.059933`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.00418`, median `0.010664`, mae `0.022861`
- 5d: sample `40`, hit `0.6`, avg `0.00554`, median `0.009517`, mae `0.029681`
- 10d: sample `40`, hit `0.725`, avg `0.018373`, median `0.030858`, mae `0.04191`
- 20d: sample `40`, hit `0.675`, avg `0.027247`, median `0.048862`, mae `0.064597`
- 60d: sample `40`, hit `0.7`, avg `0.043949`, median `0.087998`, mae `0.11027`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
