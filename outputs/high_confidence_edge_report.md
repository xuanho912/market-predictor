# High Confidence Edge Report

Generated at: `2026-09-18T08:31:20.565124+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `28`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `28`, gate `early_evidence`
- 5d: completed `28`, gate `early_evidence`
- 10d: completed `28`, gate `early_evidence`
- 20d: completed `28`, gate `early_evidence`
- 60d: completed `28`, gate `early_evidence`

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
- 3d: sample `80`, hit `0.45`, avg `-0.005773`, median `-0.001658`, mae `0.01706`
- 5d: sample `80`, hit `0.45`, avg `-0.008498`, median `-0.004438`, mae `0.01957`
- 10d: sample `80`, hit `0.3875`, avg `-0.007962`, median `-0.01051`, mae `0.029161`
- 20d: sample `80`, hit `0.575`, avg `0.012585`, median `0.015725`, mae `0.041256`
- 60d: sample `80`, hit `0.7125`, avg `0.039128`, median `0.059104`, mae `0.08253`

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
- 3d: sample `8`, hit `0.625`, avg `0.003571`, median `0.012132`, mae `0.022004`
- 5d: sample `8`, hit `0.875`, avg `0.009276`, median `0.019244`, mae `0.018082`
- 10d: sample `8`, hit `0.75`, avg `0.021851`, median `0.027869`, mae `0.037774`
- 20d: sample `8`, hit `0.875`, avg `0.034503`, median `0.054665`, mae `0.035332`
- 60d: sample `8`, hit `0.875`, avg `0.085544`, median `0.095524`, mae `0.095351`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.003571`, median `0.012132`, mae `0.022004`
- 5d: sample `8`, hit `0.875`, avg `0.009276`, median `0.019244`, mae `0.018082`
- 10d: sample `8`, hit `0.75`, avg `0.021851`, median `0.027869`, mae `0.037774`
- 20d: sample `8`, hit `0.875`, avg `0.034503`, median `0.054665`, mae `0.035332`
- 60d: sample `8`, hit `0.875`, avg `0.085544`, median `0.095524`, mae `0.095351`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003571, 'median_return': 0.012132, 'mean_absolute_return': 0.022004, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.034318}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.009276, 'median_return': 0.019244, 'mean_absolute_return': 0.018082, 'max_adverse_excursion': -0.035224, 'max_favorable_excursion': 0.044767}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.021851, 'median_return': 0.027869, 'mean_absolute_return': 0.037774, 'max_adverse_excursion': -0.032598, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.034503, 'median_return': 0.054665, 'mean_absolute_return': 0.035332, 'max_adverse_excursion': -0.003313, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.085544, 'median_return': 0.095524, 'mean_absolute_return': 0.095351, 'max_adverse_excursion': -0.039228, 'max_favorable_excursion': 0.19145}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.006811, 'median_return': -0.001797, 'mean_absolute_return': 0.01651, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.010473, 'median_return': -0.010337, 'mean_absolute_return': 0.019735, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.3472, 'avg_return': -0.011275, 'median_return': -0.013412, 'mean_absolute_return': 0.028205, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.01015, 'median_return': 0.015416, 'mean_absolute_return': 0.041914, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.03397, 'median_return': 0.059007, 'mean_absolute_return': 0.081106, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.188643}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.425}, '60d': {'sample_size': 80, 'hit_rate': 0.2875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.425, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': -0.001605, 'median_return': 0.006513, 'mean_absolute_return': 0.016208, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.034318}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': -0.000359, 'median_return': 0.001695, 'mean_absolute_return': 0.014901, 'max_adverse_excursion': -0.035224, 'max_favorable_excursion': 0.044767}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.004298, 'median_return': 0.003815, 'mean_absolute_return': 0.025839, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.025201, 'median_return': 0.029348, 'mean_absolute_return': 0.034626, 'max_adverse_excursion': -0.051442, 'max_favorable_excursion': 0.097115}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.056186, 'median_return': 0.063683, 'mean_absolute_return': 0.076809, 'max_adverse_excursion': -0.118336, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.3, 'avg_return': -0.009941, 'median_return': -0.010033, 'mean_absolute_return': 0.017912, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.275, 'avg_return': -0.016637, 'median_return': -0.018175, 'mean_absolute_return': 0.024238, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 40, 'hit_rate': 0.2, 'avg_return': -0.020223, 'median_return': -0.01796, 'mean_absolute_return': 0.032484, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -3e-05, 'median_return': -0.00045, 'mean_absolute_return': 0.047885, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.02207, 'median_return': 0.050438, 'mean_absolute_return': 0.088252, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.145995}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.45`, avg `-0.005773`, median `-0.001658`, mae `0.01706`
- 5d: sample `80`, hit `0.45`, avg `-0.008498`, median `-0.004438`, mae `0.01957`
- 10d: sample `80`, hit `0.3875`, avg `-0.007962`, median `-0.01051`, mae `0.029161`
- 20d: sample `80`, hit `0.575`, avg `0.012585`, median `0.015725`, mae `0.041256`
- 60d: sample `80`, hit `0.7125`, avg `0.039128`, median `0.059104`, mae `0.08253`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.000631`, median `0.008223`, mae `0.017354`
- 5d: sample `20`, hit `0.75`, avg `0.005097`, median `0.008593`, mae `0.015343`
- 10d: sample `20`, hit `0.75`, avg `0.017679`, median `0.021815`, mae `0.033277`
- 20d: sample `20`, hit `0.8`, avg `0.035765`, median `0.046831`, mae `0.040153`
- 60d: sample `20`, hit `0.85`, avg `0.082621`, median `0.106076`, mae `0.10188`

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
- 3d: sample `80`, hit `0.45`, avg `-0.005773`, median `-0.001658`, mae `0.01706`
- 5d: sample `80`, hit `0.45`, avg `-0.008498`, median `-0.004438`, mae `0.01957`
- 10d: sample `80`, hit `0.3875`, avg `-0.007962`, median `-0.01051`, mae `0.029161`
- 20d: sample `80`, hit `0.575`, avg `0.012585`, median `0.015725`, mae `0.041256`
- 60d: sample `80`, hit `0.7125`, avg `0.039128`, median `0.059104`, mae `0.08253`

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
- 3d: sample `80`, hit `0.45`, avg `-0.005773`, median `-0.001658`, mae `0.01706`
- 5d: sample `80`, hit `0.45`, avg `-0.008498`, median `-0.004438`, mae `0.01957`
- 10d: sample `80`, hit `0.3875`, avg `-0.007962`, median `-0.01051`, mae `0.029161`
- 20d: sample `80`, hit `0.575`, avg `0.012585`, median `0.015725`, mae `0.041256`
- 60d: sample `80`, hit `0.7125`, avg `0.039128`, median `0.059104`, mae `0.08253`

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
