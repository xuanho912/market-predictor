# High Confidence Edge Report

Generated at: `2026-10-09T18:24:08.689813+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `92`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `92`, gate `moderate_evidence`
- 5d: completed `92`, gate `moderate_evidence`
- 10d: completed `92`, gate `moderate_evidence`
- 20d: completed `92`, gate `moderate_evidence`
- 60d: completed `92`, gate `moderate_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.3375`, avg `-0.007702`, median `-0.004936`, mae `0.01733`
- 5d: sample `80`, hit `0.4`, avg `-0.012053`, median `-0.013237`, mae `0.020962`
- 10d: sample `80`, hit `0.4`, avg `-0.009048`, median `-0.006933`, mae `0.024572`
- 20d: sample `80`, hit `0.6`, avg `0.014208`, median `0.016027`, mae `0.037597`
- 60d: sample `80`, hit `0.7875`, avg `0.039494`, median `0.046407`, mae `0.064495`

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
- 3d: sample `8`, hit `0.25`, avg `-0.016807`, median `-0.030499`, mae `0.024878`
- 5d: sample `8`, hit `0.375`, avg `-0.01718`, median `-0.016421`, mae `0.022862`
- 10d: sample `8`, hit `0.25`, avg `-0.012488`, median `-0.011432`, mae `0.015647`
- 20d: sample `8`, hit `0.75`, avg `0.014597`, median `0.029166`, mae `0.044724`
- 60d: sample `8`, hit `0.875`, avg `0.053341`, median `0.072696`, mae `0.088622`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.016807`, median `-0.030499`, mae `0.024878`
- 5d: sample `8`, hit `0.375`, avg `-0.01718`, median `-0.016421`, mae `0.022862`
- 10d: sample `8`, hit `0.25`, avg `-0.012488`, median `-0.011432`, mae `0.015647`
- 20d: sample `8`, hit `0.75`, avg `0.014597`, median `0.029166`, mae `0.044724`
- 60d: sample `8`, hit `0.875`, avg `0.053341`, median `0.072696`, mae `0.088622`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.3375, 'avg_return': -0.007702, 'median_return': -0.004936, 'mean_absolute_return': 0.01733, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.012053, 'median_return': -0.013237, 'mean_absolute_return': 0.020962, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.009048, 'median_return': -0.006933, 'mean_absolute_return': 0.024572, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.014208, 'median_return': 0.016027, 'mean_absolute_return': 0.037597, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.039494, 'median_return': 0.046407, 'mean_absolute_return': 0.064495, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.154613}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.016807, 'median_return': -0.030499, 'mean_absolute_return': 0.024878, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.01718, 'median_return': -0.016421, 'mean_absolute_return': 0.022862, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.012488, 'median_return': -0.011432, 'mean_absolute_return': 0.015647, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.011031}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.014597, 'median_return': 0.029166, 'mean_absolute_return': 0.044724, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.053341, 'median_return': 0.072696, 'mean_absolute_return': 0.088622, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3472, 'avg_return': -0.00669, 'median_return': -0.004907, 'mean_absolute_return': 0.016491, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.011484, 'median_return': -0.013229, 'mean_absolute_return': 0.02075, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.008666, 'median_return': -0.006616, 'mean_absolute_return': 0.025564, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.014165, 'median_return': 0.015725, 'mean_absolute_return': 0.036805, 'max_adverse_excursion': -0.090946, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.037955, 'median_return': 0.044826, 'mean_absolute_return': 0.061814, 'max_adverse_excursion': -0.134617, 'max_favorable_excursion': 0.154613}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.575}, '60d': {'sample_size': 80, 'hit_rate': 0.6125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.0, 'both_hit': 11, 'both_miss': 9}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.0, 'both_hit': 14, 'both_miss': 6}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.075, 'both_hit': 11, 'both_miss': 9}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.075, 'both_hit': 13, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.075, 'both_hit': 16, 'both_miss': 4}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.3375, 'avg_return': -0.007702, 'median_return': -0.004936, 'mean_absolute_return': 0.01733, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.012053, 'median_return': -0.013237, 'mean_absolute_return': 0.020962, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.009048, 'median_return': -0.006933, 'mean_absolute_return': 0.024572, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.014208, 'median_return': 0.016027, 'mean_absolute_return': 0.037597, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.039494, 'median_return': 0.046407, 'mean_absolute_return': 0.064495, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.154613}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.014318`, median `-0.013796`, mae `0.02246`
- 5d: sample `20`, hit `0.25`, avg `-0.021377`, median `-0.022295`, mae `0.027354`
- 10d: sample `20`, hit `0.2`, avg `-0.016472`, median `-0.013832`, mae `0.022917`
- 20d: sample `20`, hit `0.6`, avg `0.008013`, median `0.021759`, mae `0.040747`
- 60d: sample `20`, hit `0.7`, avg `0.031662`, median `0.050438`, mae `0.083396`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.005121`, median `-0.003676`, mae `0.015167`
- 5d: sample `40`, hit `0.45`, avg `-0.008875`, median `-0.00693`, mae `0.018256`
- 10d: sample `40`, hit `0.45`, avg `-0.005328`, median `-0.004767`, mae `0.027936`
- 20d: sample `40`, hit `0.6`, avg `0.018647`, median `0.015725`, mae `0.03952`
- 60d: sample `40`, hit `0.825`, avg `0.045811`, median `0.044771`, mae `0.059875`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.014318`, median `-0.013796`, mae `0.02246`
- 5d: sample `20`, hit `0.25`, avg `-0.021377`, median `-0.022295`, mae `0.027354`
- 10d: sample `20`, hit `0.2`, avg `-0.016472`, median `-0.013832`, mae `0.022917`
- 20d: sample `20`, hit `0.6`, avg `0.008013`, median `0.021759`, mae `0.040747`
- 60d: sample `20`, hit `0.7`, avg `0.031662`, median `0.050438`, mae `0.083396`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.003318`, median `0.003898`, mae `0.011246`
- 5d: sample `20`, hit `0.7`, avg `0.000498`, median `0.002323`, mae `0.010717`
- 10d: sample `20`, hit `0.55`, avg `0.001619`, median `0.005417`, mae `0.01331`
- 20d: sample `20`, hit `0.65`, avg `0.012984`, median `0.015725`, mae `0.021589`
- 60d: sample `20`, hit `0.8`, avg `0.02027`, median `0.02999`, mae `0.039752`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.014318`, median `-0.013796`, mae `0.02246`
- 5d: sample `20`, hit `0.25`, avg `-0.021377`, median `-0.022295`, mae `0.027354`
- 10d: sample `20`, hit `0.2`, avg `-0.016472`, median `-0.013832`, mae `0.022917`
- 20d: sample `20`, hit `0.6`, avg `0.008013`, median `0.021759`, mae `0.040747`
- 60d: sample `20`, hit `0.7`, avg `0.031662`, median `0.050438`, mae `0.083396`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.014318`, median `-0.013796`, mae `0.02246`
- 5d: sample `20`, hit `0.25`, avg `-0.021377`, median `-0.022295`, mae `0.027354`
- 10d: sample `20`, hit `0.2`, avg `-0.016472`, median `-0.013832`, mae `0.022917`
- 20d: sample `20`, hit `0.6`, avg `0.008013`, median `0.021759`, mae `0.040747`
- 60d: sample `20`, hit `0.7`, avg `0.031662`, median `0.050438`, mae `0.083396`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.001466`, median `-0.001227`, mae `0.013885`
- 5d: sample `40`, hit `0.575`, avg `-0.004295`, median `0.001104`, mae `0.015348`
- 10d: sample `40`, hit `0.525`, avg `-0.003722`, median `0.000397`, mae `0.016405`
- 20d: sample `40`, hit `0.625`, avg `0.012255`, median `0.015725`, mae `0.026096`
- 60d: sample `40`, hit `0.8`, avg `0.02748`, median `0.03276`, mae `0.047292`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.014318`, median `-0.013796`, mae `0.02246`
- 5d: sample `20`, hit `0.25`, avg `-0.021377`, median `-0.022295`, mae `0.027354`
- 10d: sample `20`, hit `0.2`, avg `-0.016472`, median `-0.013832`, mae `0.022917`
- 20d: sample `20`, hit `0.6`, avg `0.008013`, median `0.021759`, mae `0.040747`
- 60d: sample `20`, hit `0.7`, avg `0.031662`, median `0.050438`, mae `0.083396`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.15`, avg `-0.013559`, median `-0.010273`, mae `0.019089`
- 5d: sample `20`, hit `0.2`, avg `-0.018248`, median `-0.020895`, mae `0.025796`
- 10d: sample `20`, hit `0.35`, avg `-0.012275`, median `-0.027227`, mae `0.042563`
- 20d: sample `20`, hit `0.55`, avg `0.024309`, median `0.039427`, mae `0.057451`
- 60d: sample `20`, hit `0.85`, avg `0.071353`, median `0.092008`, mae `0.079999`

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
- 3d: sample `80`, hit `0.3375`, avg `-0.007702`, median `-0.004936`, mae `0.01733`
- 5d: sample `80`, hit `0.4`, avg `-0.012053`, median `-0.013237`, mae `0.020962`
- 10d: sample `80`, hit `0.4`, avg `-0.009048`, median `-0.006933`, mae `0.024572`
- 20d: sample `80`, hit `0.6`, avg `0.014208`, median `0.016027`, mae `0.037597`
- 60d: sample `80`, hit `0.7875`, avg `0.039494`, median `0.046407`, mae `0.064495`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.4`, avg `-0.00575`, median `-0.003676`, mae `0.016743`
- 5d: sample `60`, hit `0.4667`, avg `-0.009989`, median `-0.007113`, mae `0.01935`
- 10d: sample `60`, hit `0.4167`, avg `-0.007972`, median `-0.006389`, mae `0.018575`
- 20d: sample `60`, hit `0.6167`, avg `0.010841`, median `0.016027`, mae `0.030979`
- 60d: sample `60`, hit `0.7667`, avg `0.028874`, median `0.04207`, mae `0.059327`

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
