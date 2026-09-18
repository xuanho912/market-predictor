# High Confidence Edge Report

Generated at: `2026-09-18T06:01:03.623271+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `-0.003732`, median `0.002067`, mae `0.017063`
- 5d: sample `60`, hit `0.55`, avg `-0.004839`, median `0.001303`, mae `0.017125`
- 10d: sample `60`, hit `0.45`, avg `-0.000945`, median `-0.006017`, mae `0.024328`
- 20d: sample `60`, hit `0.65`, avg `0.019413`, median `0.020068`, mae `0.03659`
- 60d: sample `60`, hit `0.7333`, avg `0.047834`, median `0.059495`, mae `0.078216`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.2`, avg `-0.011897`, median `-0.010273`, mae `0.01705`
- 5d: sample `20`, hit `0.15`, avg `-0.019476`, median `-0.0203`, mae `0.026903`
- 10d: sample `20`, hit `0.2`, avg `-0.029014`, median `-0.037905`, mae `0.043663`
- 20d: sample `20`, hit `0.35`, avg `-0.007899`, median `-0.011553`, mae `0.055252`
- 60d: sample `20`, hit `0.65`, avg `0.013008`, median `0.059007`, mae `0.095473`

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
- 3d: sample `8`, hit `0.25`, avg `-0.009836`, median `-0.010033`, mae `0.020014`
- 5d: sample `8`, hit `0.375`, avg `-0.010746`, median `-0.022295`, mae `0.021056`
- 10d: sample `8`, hit `0.125`, avg `-0.007656`, median `-0.010456`, mae `0.0158`
- 20d: sample `8`, hit `0.75`, avg `0.035554`, median `0.043456`, mae `0.039027`
- 60d: sample `8`, hit `0.875`, avg `0.073866`, median `0.099838`, mae `0.087813`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.003732, 'median_return': 0.002067, 'mean_absolute_return': 0.017063, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.034318}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.004839, 'median_return': 0.001303, 'mean_absolute_return': 0.017125, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.044767}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.000945, 'median_return': -0.006017, 'mean_absolute_return': 0.024328, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.019413, 'median_return': 0.020068, 'mean_absolute_return': 0.03659, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.097115}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.047834, 'median_return': 0.059495, 'mean_absolute_return': 0.078216, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.009836, 'median_return': -0.010033, 'mean_absolute_return': 0.020014, 'max_adverse_excursion': -0.033992, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.010746, 'median_return': -0.022295, 'mean_absolute_return': 0.021056, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.007656, 'median_return': -0.010456, 'mean_absolute_return': 0.0158, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.035554, 'median_return': 0.043456, 'mean_absolute_return': 0.039027, 'max_adverse_excursion': -0.012229, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.073866, 'median_return': 0.099838, 'mean_absolute_return': 0.087813, 'max_adverse_excursion': -0.055789, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.005322, 'median_return': -0.001058, 'mean_absolute_return': 0.016732, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.008248, 'median_return': -0.003585, 'mean_absolute_return': 0.019405, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.044767}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.007996, 'median_return': -0.01051, 'mean_absolute_return': 0.030646, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.010033, 'median_return': 0.014522, 'mean_absolute_return': 0.041503, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.035268, 'median_return': 0.059007, 'mean_absolute_return': 0.081944, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.675}, '10d': {'sample_size': 80, 'hit_rate': 0.7375}, '20d': {'sample_size': 80, 'hit_rate': 0.575}, '60d': {'sample_size': 80, 'hit_rate': 0.4625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.25, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.325, 'primary_minus_secondary': 0.35, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.7375, 'secondary_hit_rate': 0.2625, 'primary_minus_secondary': 0.475, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.003732, 'median_return': 0.002067, 'mean_absolute_return': 0.017063, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.034318}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.004839, 'median_return': 0.001303, 'mean_absolute_return': 0.017125, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.044767}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.000945, 'median_return': -0.006017, 'mean_absolute_return': 0.024328, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.019413, 'median_return': 0.020068, 'mean_absolute_return': 0.03659, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.097115}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.047834, 'median_return': 0.059495, 'mean_absolute_return': 0.078216, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.2, 'avg_return': -0.011897, 'median_return': -0.010273, 'mean_absolute_return': 0.01705, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.15, 'avg_return': -0.019476, 'median_return': -0.0203, 'mean_absolute_return': 0.026903, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 20, 'hit_rate': 0.2, 'avg_return': -0.029014, 'median_return': -0.037905, 'mean_absolute_return': 0.043663, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.007899, 'median_return': -0.011553, 'mean_absolute_return': 0.055252, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.013008, 'median_return': 0.059007, 'mean_absolute_return': 0.095473, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.145995}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.000631`, median `0.008223`, mae `0.017354`
- 5d: sample `20`, hit `0.75`, avg `0.005097`, median `0.008593`, mae `0.015343`
- 10d: sample `20`, hit `0.75`, avg `0.017679`, median `0.021815`, mae `0.033277`
- 20d: sample `20`, hit `0.8`, avg `0.035765`, median `0.046831`, mae `0.040153`
- 60d: sample `20`, hit `0.85`, avg `0.082621`, median `0.106076`, mae `0.10188`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `-0.003732`, median `0.002067`, mae `0.017063`
- 5d: sample `60`, hit `0.55`, avg `-0.004839`, median `0.001303`, mae `0.017125`
- 10d: sample `60`, hit `0.45`, avg `-0.000945`, median `-0.006017`, mae `0.024328`
- 20d: sample `60`, hit `0.65`, avg `0.019413`, median `0.020068`, mae `0.03659`
- 60d: sample `60`, hit `0.7333`, avg `0.047834`, median `0.059495`, mae `0.078216`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.000631`, median `0.008223`, mae `0.017354`
- 5d: sample `20`, hit `0.75`, avg `0.005097`, median `0.008593`, mae `0.015343`
- 10d: sample `20`, hit `0.75`, avg `0.017679`, median `0.021815`, mae `0.033277`
- 20d: sample `20`, hit `0.8`, avg `0.035765`, median `0.046831`, mae `0.040153`
- 60d: sample `20`, hit `0.85`, avg `0.082621`, median `0.106076`, mae `0.10188`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.007908`, median `-0.008674`, mae `0.016962`
- 5d: sample `60`, hit `0.35`, avg `-0.01303`, median `-0.015413`, mae `0.020979`
- 10d: sample `60`, hit `0.2667`, avg `-0.01651`, median `-0.015123`, mae `0.027789`
- 20d: sample `60`, hit `0.5`, avg `0.004859`, median `0.000213`, mae `0.041623`
- 60d: sample `60`, hit `0.6667`, avg `0.02463`, median `0.053855`, mae `0.076081`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.000631`, median `0.008223`, mae `0.017354`
- 5d: sample `20`, hit `0.75`, avg `0.005097`, median `0.008593`, mae `0.015343`
- 10d: sample `20`, hit `0.75`, avg `0.017679`, median `0.021815`, mae `0.033277`
- 20d: sample `20`, hit `0.8`, avg `0.035765`, median `0.046831`, mae `0.040153`
- 60d: sample `20`, hit `0.85`, avg `0.082621`, median `0.106076`, mae `0.10188`

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
