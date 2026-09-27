# High Confidence Edge Report

Generated at: `2026-09-27T17:02:37.618013+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `52`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `52`, gate `moderate_evidence`
- 5d: completed `52`, gate `moderate_evidence`
- 10d: completed `52`, gate `moderate_evidence`
- 20d: completed `52`, gate `moderate_evidence`
- 60d: completed `52`, gate `moderate_evidence`

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
- 3d: sample `40`, hit `0.525`, avg `-0.004468`, median `0.001199`, mae `0.018094`
- 5d: sample `40`, hit `0.5`, avg `-0.008804`, median `0.000688`, mae `0.021507`
- 10d: sample `40`, hit `0.425`, avg `-0.009882`, median `-0.006017`, mae `0.021409`
- 20d: sample `40`, hit `0.625`, avg `0.007185`, median `0.016021`, mae `0.035473`
- 60d: sample `40`, hit `0.8`, avg `0.043897`, median `0.059104`, mae `0.076871`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.009949`, median `-0.004936`, mae `0.016176`
- 5d: sample `40`, hit `0.4`, avg `-0.013547`, median `-0.009444`, mae `0.020585`
- 10d: sample `40`, hit `0.475`, avg `-0.007645`, median `-0.004767`, mae `0.03293`
- 20d: sample `40`, hit `0.575`, avg `0.00127`, median `0.013156`, mae `0.049654`
- 60d: sample `40`, hit `0.775`, avg `0.029046`, median `0.044683`, mae `0.083767`

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
- 3d: sample `8`, hit `0.5`, avg `-0.003118`, median `0.012272`, mae `0.022526`
- 5d: sample `8`, hit `0.625`, avg `-0.007215`, median `0.007948`, mae `0.022159`
- 10d: sample `8`, hit `0.25`, avg `-0.006535`, median `-0.011432`, mae `0.017437`
- 20d: sample `8`, hit `0.75`, avg `0.016651`, median `0.029166`, mae `0.046777`
- 60d: sample `8`, hit `0.875`, avg `0.055371`, median `0.072696`, mae `0.090652`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.003118`, median `0.012272`, mae `0.022526`
- 5d: sample `8`, hit `0.625`, avg `-0.007215`, median `0.007948`, mae `0.022159`
- 10d: sample `8`, hit `0.25`, avg `-0.006535`, median `-0.011432`, mae `0.017437`
- 20d: sample `8`, hit `0.75`, avg `0.016651`, median `0.029166`, mae `0.046777`
- 60d: sample `8`, hit `0.875`, avg `0.055371`, median `0.072696`, mae `0.090652`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.004468, 'median_return': 0.001199, 'mean_absolute_return': 0.018094, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.008804, 'median_return': 0.000688, 'mean_absolute_return': 0.021507, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.009882, 'median_return': -0.006017, 'mean_absolute_return': 0.021409, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.007185, 'median_return': 0.016021, 'mean_absolute_return': 0.035473, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.043897, 'median_return': 0.059104, 'mean_absolute_return': 0.076871, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003118, 'median_return': 0.012272, 'mean_absolute_return': 0.022526, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.007215, 'median_return': 0.007948, 'mean_absolute_return': 0.022159, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.006535, 'median_return': -0.011432, 'mean_absolute_return': 0.017437, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016651, 'median_return': 0.029166, 'mean_absolute_return': 0.046777, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.055371, 'median_return': 0.072696, 'mean_absolute_return': 0.090652, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.007663, 'median_return': -0.003995, 'mean_absolute_return': 0.016536, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.011615, 'median_return': -0.009444, 'mean_absolute_return': 0.020922, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.009011, 'median_return': -0.004767, 'mean_absolute_return': 0.028251, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.002848, 'median_return': 0.013156, 'mean_absolute_return': 0.042095, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.034371, 'median_return': 0.053855, 'mean_absolute_return': 0.079171, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.525}, '60d': {'sample_size': 80, 'hit_rate': 0.5125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.002881, 'median_return': 0.001199, 'mean_absolute_return': 0.01553, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.007073, 'median_return': 0.000935, 'mean_absolute_return': 0.018235, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.0072, 'median_return': -0.0004, 'mean_absolute_return': 0.020712, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.036168}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.006947, 'median_return': 0.016021, 'mean_absolute_return': 0.035271, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.037135, 'median_return': 0.046407, 'mean_absolute_return': 0.067563, 'max_adverse_excursion': -0.146095, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.1, 'avg_return': -0.02019, 'median_return': -0.014972, 'mean_absolute_return': 0.021948, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.011534}, '5d': {'sample_size': 20, 'hit_rate': 0.2, 'avg_return': -0.023483, 'median_return': -0.021161, 'mean_absolute_return': 0.029478, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.023861}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.013454, 'median_return': -0.032571, 'mean_absolute_return': 0.046542, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.00393, 'median_return': -0.009713, 'mean_absolute_return': 0.06444, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.034482, 'median_return': 0.092689, 'mean_absolute_return': 0.118587, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.154804}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.004468`, median `0.001199`, mae `0.018094`
- 5d: sample `40`, hit `0.5`, avg `-0.008804`, median `0.000688`, mae `0.021507`
- 10d: sample `40`, hit `0.425`, avg `-0.009882`, median `-0.006017`, mae `0.021409`
- 20d: sample `40`, hit `0.625`, avg `0.007185`, median `0.016021`, mae `0.035473`
- 60d: sample `40`, hit `0.8`, avg `0.043897`, median `0.059104`, mae `0.076871`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.009949`, median `-0.004936`, mae `0.016176`
- 5d: sample `40`, hit `0.4`, avg `-0.013547`, median `-0.009444`, mae `0.020585`
- 10d: sample `40`, hit `0.475`, avg `-0.007645`, median `-0.004767`, mae `0.03293`
- 20d: sample `40`, hit `0.575`, avg `0.00127`, median `0.013156`, mae `0.049654`
- 60d: sample `40`, hit `0.775`, avg `0.029046`, median `0.044683`, mae `0.083767`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.004468`, median `0.001199`, mae `0.018094`
- 5d: sample `40`, hit `0.5`, avg `-0.008804`, median `0.000688`, mae `0.021507`
- 10d: sample `40`, hit `0.425`, avg `-0.009882`, median `-0.006017`, mae `0.021409`
- 20d: sample `40`, hit `0.625`, avg `0.007185`, median `0.016021`, mae `0.035473`
- 60d: sample `40`, hit `0.8`, avg `0.043897`, median `0.059104`, mae `0.076871`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.004468`, median `0.001199`, mae `0.018094`
- 5d: sample `40`, hit `0.5`, avg `-0.008804`, median `0.000688`, mae `0.021507`
- 10d: sample `40`, hit `0.425`, avg `-0.009882`, median `-0.006017`, mae `0.021409`
- 20d: sample `40`, hit `0.625`, avg `0.007185`, median `0.016021`, mae `0.035473`
- 60d: sample `40`, hit `0.8`, avg `0.043897`, median `0.059104`, mae `0.076871`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.004468`, median `0.001199`, mae `0.018094`
- 5d: sample `40`, hit `0.5`, avg `-0.008804`, median `0.000688`, mae `0.021507`
- 10d: sample `40`, hit `0.425`, avg `-0.009882`, median `-0.006017`, mae `0.021409`
- 20d: sample `40`, hit `0.625`, avg `0.007185`, median `0.016021`, mae `0.035473`
- 60d: sample `40`, hit `0.8`, avg `0.043897`, median `0.059104`, mae `0.076871`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.004468`, median `0.001199`, mae `0.018094`
- 5d: sample `40`, hit `0.5`, avg `-0.008804`, median `0.000688`, mae `0.021507`
- 10d: sample `40`, hit `0.425`, avg `-0.009882`, median `-0.006017`, mae `0.021409`
- 20d: sample `40`, hit `0.625`, avg `0.007185`, median `0.016021`, mae `0.035473`
- 60d: sample `40`, hit `0.8`, avg `0.043897`, median `0.059104`, mae `0.076871`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.009949`, median `-0.004936`, mae `0.016176`
- 5d: sample `40`, hit `0.4`, avg `-0.013547`, median `-0.009444`, mae `0.020585`
- 10d: sample `40`, hit `0.475`, avg `-0.007645`, median `-0.004767`, mae `0.03293`
- 20d: sample `40`, hit `0.575`, avg `0.00127`, median `0.013156`, mae `0.049654`
- 60d: sample `40`, hit `0.775`, avg `0.029046`, median `0.044683`, mae `0.083767`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

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
- 3d: sample `80`, hit `0.4125`, avg `-0.007209`, median `-0.003676`, mae `0.017135`
- 5d: sample `80`, hit `0.45`, avg `-0.011175`, median `-0.00693`, mae `0.021046`
- 10d: sample `80`, hit `0.45`, avg `-0.008763`, median `-0.006017`, mae `0.027169`
- 20d: sample `80`, hit `0.6`, avg `0.004228`, median `0.015416`, mae `0.042563`
- 60d: sample `80`, hit `0.7875`, avg `0.036471`, median `0.053855`, mae `0.080319`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.004468`, median `0.001199`, mae `0.018094`
- 5d: sample `40`, hit `0.5`, avg `-0.008804`, median `0.000688`, mae `0.021507`
- 10d: sample `40`, hit `0.425`, avg `-0.009882`, median `-0.006017`, mae `0.021409`
- 20d: sample `40`, hit `0.625`, avg `0.007185`, median `0.016021`, mae `0.035473`
- 60d: sample `40`, hit `0.8`, avg `0.043897`, median `0.059104`, mae `0.076871`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.002881`, median `0.001199`, mae `0.01553`
- 5d: sample `60`, hit `0.5333`, avg `-0.007073`, median `0.000935`, mae `0.018235`
- 10d: sample `60`, hit `0.4667`, avg `-0.0072`, median `-0.0004`, mae `0.020712`
- 20d: sample `60`, hit `0.6667`, avg `0.006947`, median `0.016021`, mae `0.035271`
- 60d: sample `60`, hit `0.8167`, avg `0.037135`, median `0.046407`, mae `0.067563`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.004468`, median `0.001199`, mae `0.018094`
- 5d: sample `40`, hit `0.5`, avg `-0.008804`, median `0.000688`, mae `0.021507`
- 10d: sample `40`, hit `0.425`, avg `-0.009882`, median `-0.006017`, mae `0.021409`
- 20d: sample `40`, hit `0.625`, avg `0.007185`, median `0.016021`, mae `0.035473`
- 60d: sample `40`, hit `0.8`, avg `0.043897`, median `0.059104`, mae `0.076871`

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
