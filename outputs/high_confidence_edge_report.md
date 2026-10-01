# High Confidence Edge Report

Generated at: `2026-10-01T10:29:22.225216+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `64`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `64`, gate `moderate_evidence`
- 5d: completed `64`, gate `moderate_evidence`
- 10d: completed `64`, gate `moderate_evidence`
- 20d: completed `64`, gate `moderate_evidence`
- 60d: completed `64`, gate `moderate_evidence`

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
- 3d: sample `80`, hit `0.425`, avg `-0.006249`, median `-0.003244`, mae `0.017191`
- 5d: sample `80`, hit `0.425`, avg `-0.009919`, median `-0.005796`, mae `0.019711`
- 10d: sample `80`, hit `0.475`, avg `-0.007588`, median `-0.0004`, mae `0.028437`
- 20d: sample `80`, hit `0.6125`, avg `0.007414`, median `0.015725`, mae `0.042328`
- 60d: sample `80`, hit `0.8`, avg `0.044742`, median `0.059104`, mae `0.080763`

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
- 3d: sample `8`, hit `0.5`, avg `0.000424`, median `0.004068`, mae `0.013033`
- 5d: sample `8`, hit `0.625`, avg `-0.001497`, median `0.001479`, mae `0.010224`
- 10d: sample `8`, hit `0.5`, avg `0.009167`, median `0.014793`, mae `0.017238`
- 20d: sample `8`, hit `0.875`, avg `0.032707`, median `0.034024`, mae `0.033484`
- 60d: sample `8`, hit `0.875`, avg `0.030837`, median `0.04207`, mae `0.041888`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.001908`, median `0.004815`, mae `0.014421`
- 5d: sample `8`, hit `0.625`, avg `-0.001294`, median `0.006609`, mae `0.013855`
- 10d: sample `8`, hit `0.5`, avg `-0.010725`, median `0.000397`, mae `0.02165`
- 20d: sample `8`, hit `0.625`, avg `0.011193`, median `0.01927`, mae `0.029953`
- 60d: sample `8`, hit `0.875`, avg `0.037751`, median `0.053855`, mae `0.049261`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.001908, 'median_return': 0.004815, 'mean_absolute_return': 0.014421, 'max_adverse_excursion': -0.029438, 'max_favorable_excursion': 0.023486}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.001294, 'median_return': 0.006609, 'mean_absolute_return': 0.013855, 'max_adverse_excursion': -0.027246, 'max_favorable_excursion': 0.018625}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.010725, 'median_return': 0.000397, 'mean_absolute_return': 0.02165, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.018352}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.011193, 'median_return': 0.01927, 'mean_absolute_return': 0.029953, 'max_adverse_excursion': -0.051442, 'max_favorable_excursion': 0.053054}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.037751, 'median_return': 0.053855, 'mean_absolute_return': 0.049261, 'max_adverse_excursion': -0.04604, 'max_favorable_excursion': 0.114629}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.007155, 'median_return': -0.003649, 'mean_absolute_return': 0.017499, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.010878, 'median_return': -0.00693, 'mean_absolute_return': 0.020362, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.007239, 'median_return': -0.0004, 'mean_absolute_return': 0.029191, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.006994, 'median_return': 0.015725, 'mean_absolute_return': 0.043703, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.045519, 'median_return': 0.060702, 'mean_absolute_return': 0.084263, 'max_adverse_excursion': -0.184447, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.525}, '20d': {'sample_size': 80, 'hit_rate': 0.3875}, '60d': {'sample_size': 80, 'hit_rate': 0.2}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': -0.6, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': -0.006249, 'median_return': -0.003244, 'mean_absolute_return': 0.017191, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': -0.009919, 'median_return': -0.005796, 'mean_absolute_return': 0.019711, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': -0.007588, 'median_return': -0.0004, 'mean_absolute_return': 0.028437, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.007414, 'median_return': 0.015725, 'mean_absolute_return': 0.042328, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.044742, 'median_return': 0.059104, 'mean_absolute_return': 0.080763, 'max_adverse_excursion': -0.184447, 'max_favorable_excursion': 0.154804}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.425`, avg `-0.006249`, median `-0.003244`, mae `0.017191`
- 5d: sample `80`, hit `0.425`, avg `-0.009919`, median `-0.005796`, mae `0.019711`
- 10d: sample `80`, hit `0.475`, avg `-0.007588`, median `-0.0004`, mae `0.028437`
- 20d: sample `80`, hit `0.6125`, avg `0.007414`, median `0.015725`, mae `0.042328`
- 60d: sample `80`, hit `0.8`, avg `0.044742`, median `0.059104`, mae `0.080763`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.425`, avg `-0.006249`, median `-0.003244`, mae `0.017191`
- 5d: sample `80`, hit `0.425`, avg `-0.009919`, median `-0.005796`, mae `0.019711`
- 10d: sample `80`, hit `0.475`, avg `-0.007588`, median `-0.0004`, mae `0.028437`
- 20d: sample `80`, hit `0.6125`, avg `0.007414`, median `0.015725`, mae `0.042328`
- 60d: sample `80`, hit `0.8`, avg `0.044742`, median `0.059104`, mae `0.080763`

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
- 3d: sample `80`, hit `0.425`, avg `-0.006249`, median `-0.003244`, mae `0.017191`
- 5d: sample `80`, hit `0.425`, avg `-0.009919`, median `-0.005796`, mae `0.019711`
- 10d: sample `80`, hit `0.475`, avg `-0.007588`, median `-0.0004`, mae `0.028437`
- 20d: sample `80`, hit `0.6125`, avg `0.007414`, median `0.015725`, mae `0.042328`
- 60d: sample `80`, hit `0.8`, avg `0.044742`, median `0.059104`, mae `0.080763`

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

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.425`, avg `-0.006249`, median `-0.003244`, mae `0.017191`
- 5d: sample `80`, hit `0.425`, avg `-0.009919`, median `-0.005796`, mae `0.019711`
- 10d: sample `80`, hit `0.475`, avg `-0.007588`, median `-0.0004`, mae `0.028437`
- 20d: sample `80`, hit `0.6125`, avg `0.007414`, median `0.015725`, mae `0.042328`
- 60d: sample `80`, hit `0.8`, avg `0.044742`, median `0.059104`, mae `0.080763`

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
