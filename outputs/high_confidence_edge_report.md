# High Confidence Edge Report

Generated at: `2026-11-10T19:47:04.330771+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `180`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `180`, gate `stronger_evidence`
- 5d: completed `180`, gate `stronger_evidence`
- 10d: completed `180`, gate `stronger_evidence`
- 20d: completed `180`, gate `stronger_evidence`
- 60d: completed `180`, gate `stronger_evidence`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.002897`, median `0.004243`, mae `0.018236`
- 5d: sample `80`, hit `0.575`, avg `0.006357`, median `0.004752`, mae `0.020424`
- 10d: sample `80`, hit `0.625`, avg `0.010188`, median `0.015002`, mae `0.031581`
- 20d: sample `80`, hit `0.725`, avg `0.017285`, median `0.027343`, mae `0.038212`
- 60d: sample `80`, hit `0.85`, avg `0.053862`, median `0.068046`, mae `0.066837`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.008091`, median `0.018908`, mae `0.020005`
- 5d: sample `8`, hit `0.875`, avg `0.021151`, median `0.032932`, mae `0.028859`
- 10d: sample `8`, hit `1.0`, avg `0.04168`, median `0.050779`, mae `0.04168`
- 20d: sample `8`, hit `1.0`, avg `0.056508`, median `0.056907`, mae `0.056508`
- 60d: sample `8`, hit `1.0`, avg `0.071794`, median `0.066636`, mae `0.071794`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.001563`, median `0.001558`, mae `0.017854`
- 5d: sample `8`, hit `0.375`, avg `0.000921`, median `-0.007346`, mae `0.015631`
- 10d: sample `8`, hit `0.75`, avg `0.014659`, median `0.020918`, mae `0.023115`
- 20d: sample `8`, hit `0.75`, avg `0.021069`, median `0.028264`, mae `0.030353`
- 60d: sample `8`, hit `1.0`, avg `0.067681`, median `0.072891`, mae `0.067681`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.001563, 'median_return': 0.001558, 'mean_absolute_return': 0.017854, 'max_adverse_excursion': -0.03272, 'max_favorable_excursion': 0.031732}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.000921, 'median_return': -0.007346, 'mean_absolute_return': 0.015631, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.014659, 'median_return': 0.020918, 'mean_absolute_return': 0.023115, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.050979}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.021069, 'median_return': 0.028264, 'mean_absolute_return': 0.030353, 'max_adverse_excursion': -0.027614, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.067681, 'median_return': 0.072891, 'mean_absolute_return': 0.067681, 'max_adverse_excursion': 0.029831, 'max_favorable_excursion': 0.095045}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.003392, 'median_return': 0.004886, 'mean_absolute_return': 0.018278, 'max_adverse_excursion': -0.049442, 'max_favorable_excursion': 0.059607}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.006961, 'median_return': 0.005676, 'mean_absolute_return': 0.020957, 'max_adverse_excursion': -0.042713, 'max_favorable_excursion': 0.063815}, '10d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.009692, 'median_return': 0.015002, 'mean_absolute_return': 0.032522, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.016865, 'median_return': 0.02604, 'mean_absolute_return': 0.039086, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.096879}, '60d': {'sample_size': 72, 'hit_rate': 0.8333, 'avg_return': 0.052327, 'median_return': 0.066779, 'mean_absolute_return': 0.066743, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.140054}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.375}, '60d': {'sample_size': 80, 'hit_rate': 0.275}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.075, 'both_hit': 11, 'both_miss': 9}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.075, 'both_hit': 13, 'both_miss': 7}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.1375, 'both_hit': 15, 'both_miss': 6}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.35, 'both_hit': 14, 'both_miss': 6}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.85, 'primary_minus_secondary': -0.575, 'both_hit': 15, 'both_miss': 5}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.001629, 'median_return': 0.002574, 'mean_absolute_return': 0.017187, 'max_adverse_excursion': -0.049442, 'max_favorable_excursion': 0.033969}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.002917, 'median_return': 0.002812, 'mean_absolute_return': 0.019264, 'max_adverse_excursion': -0.042713, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.009102, 'median_return': 0.012508, 'mean_absolute_return': 0.027125, 'max_adverse_excursion': -0.058968, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.018177, 'median_return': 0.02604, 'mean_absolute_return': 0.035147, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.045861, 'median_return': 0.057501, 'mean_absolute_return': 0.062661, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.120064}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.006699, 'median_return': 0.009501, 'mean_absolute_return': 0.021382, 'max_adverse_excursion': -0.033574, 'max_favorable_excursion': 0.059607}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.016677, 'median_return': 0.007257, 'mean_absolute_return': 0.023904, 'max_adverse_excursion': -0.024748, 'max_favorable_excursion': 0.063815}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.013447, 'median_return': 0.033298, 'mean_absolute_return': 0.04495, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.065696}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.014611, 'median_return': 0.040208, 'mean_absolute_return': 0.047409, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.096879}, '60d': {'sample_size': 20, 'hit_rate': 0.95, 'avg_return': 0.077865, 'median_return': 0.079295, 'mean_absolute_return': 0.079364, 'max_adverse_excursion': -0.014985, 'max_favorable_excursion': 0.140054}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.001629`, median `0.002574`, mae `0.017187`
- 5d: sample `60`, hit `0.5167`, avg `0.002917`, median `0.002812`, mae `0.019264`
- 10d: sample `60`, hit `0.6`, avg `0.009102`, median `0.012508`, mae `0.027125`
- 20d: sample `60`, hit `0.7333`, avg `0.018177`, median `0.02604`, mae `0.035147`
- 60d: sample `60`, hit `0.8167`, avg `0.045861`, median `0.057501`, mae `0.062661`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.006699`, median `0.009501`, mae `0.021382`
- 5d: sample `20`, hit `0.75`, avg `0.016677`, median `0.007257`, mae `0.023904`
- 10d: sample `20`, hit `0.7`, avg `0.013447`, median `0.033298`, mae `0.04495`
- 20d: sample `20`, hit `0.7`, avg `0.014611`, median `0.040208`, mae `0.047409`
- 60d: sample `20`, hit `0.95`, avg `0.077865`, median `0.079295`, mae `0.079364`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001224`, median `0.005785`, mae `0.018665`
- 5d: sample `20`, hit `0.65`, avg `0.008905`, median `0.012136`, mae `0.024927`
- 10d: sample `20`, hit `0.75`, avg `0.017766`, median `0.02025`, mae `0.032094`
- 20d: sample `20`, hit `0.7`, avg `0.021939`, median `0.042224`, mae `0.039878`
- 60d: sample `20`, hit `0.75`, avg `0.041987`, median `0.056005`, mae `0.060341`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001224`, median `0.005785`, mae `0.018665`
- 5d: sample `20`, hit `0.65`, avg `0.008905`, median `0.012136`, mae `0.024927`
- 10d: sample `20`, hit `0.75`, avg `0.017766`, median `0.02025`, mae `0.032094`
- 20d: sample `20`, hit `0.7`, avg `0.021939`, median `0.042224`, mae `0.039878`
- 60d: sample `20`, hit `0.75`, avg `0.041987`, median `0.056005`, mae `0.060341`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.006699`, median `0.009501`, mae `0.021382`
- 5d: sample `20`, hit `0.75`, avg `0.016677`, median `0.007257`, mae `0.023904`
- 10d: sample `20`, hit `0.7`, avg `0.013447`, median `0.033298`, mae `0.04495`
- 20d: sample `20`, hit `0.7`, avg `0.014611`, median `0.040208`, mae `0.047409`
- 60d: sample `20`, hit `0.95`, avg `0.077865`, median `0.079295`, mae `0.079364`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.00276`, median `0.004886`, mae `0.018589`
- 5d: sample `40`, hit `0.525`, avg `0.003987`, median `0.002812`, mae `0.020169`
- 10d: sample `40`, hit `0.65`, avg `0.012654`, median `0.015002`, mae `0.027395`
- 20d: sample `40`, hit `0.725`, avg `0.0194`, median `0.027343`, mae `0.036318`
- 60d: sample `40`, hit `0.8`, avg `0.047133`, median `0.065766`, mae `0.065868`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000633`, median `-0.001641`, mae `0.014384`
- 5d: sample `20`, hit `0.5`, avg `0.000777`, median `0.00633`, mae `0.017454`
- 10d: sample `20`, hit `0.5`, avg `0.001998`, median `0.009031`, mae `0.026586`
- 20d: sample `20`, hit `0.75`, avg `0.015731`, median `0.02604`, mae `0.032805`
- 60d: sample `20`, hit `0.85`, avg `0.043317`, median `0.052632`, mae `0.056249`

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
- 3d: sample `80`, hit `0.55`, avg `0.002897`, median `0.004243`, mae `0.018236`
- 5d: sample `80`, hit `0.575`, avg `0.006357`, median `0.004752`, mae `0.020424`
- 10d: sample `80`, hit `0.625`, avg `0.010188`, median `0.015002`, mae `0.031581`
- 20d: sample `80`, hit `0.725`, avg `0.017285`, median `0.027343`, mae `0.038212`
- 60d: sample `80`, hit `0.85`, avg `0.053862`, median `0.068046`, mae `0.066837`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.002897`, median `0.004243`, mae `0.018236`
- 5d: sample `80`, hit `0.575`, avg `0.006357`, median `0.004752`, mae `0.020424`
- 10d: sample `80`, hit `0.625`, avg `0.010188`, median `0.015002`, mae `0.031581`
- 20d: sample `80`, hit `0.725`, avg `0.017285`, median `0.027343`, mae `0.038212`
- 60d: sample `80`, hit `0.85`, avg `0.053862`, median `0.068046`, mae `0.066837`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001224`, median `0.005785`, mae `0.018665`
- 5d: sample `20`, hit `0.65`, avg `0.008905`, median `0.012136`, mae `0.024927`
- 10d: sample `20`, hit `0.75`, avg `0.017766`, median `0.02025`, mae `0.032094`
- 20d: sample `20`, hit `0.7`, avg `0.021939`, median `0.042224`, mae `0.039878`
- 60d: sample `20`, hit `0.75`, avg `0.041987`, median `0.056005`, mae `0.060341`

### bounce_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001224`, median `0.005785`, mae `0.018665`
- 5d: sample `20`, hit `0.65`, avg `0.008905`, median `0.012136`, mae `0.024927`
- 10d: sample `20`, hit `0.75`, avg `0.017766`, median `0.02025`, mae `0.032094`
- 20d: sample `20`, hit `0.7`, avg `0.021939`, median `0.042224`, mae `0.039878`
- 60d: sample `20`, hit `0.75`, avg `0.041987`, median `0.056005`, mae `0.060341`

### risk_path_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.003455`, median `0.002574`, mae `0.018093`
- 5d: sample `60`, hit `0.55`, avg `0.005508`, median `0.00338`, mae `0.018923`
- 10d: sample `60`, hit `0.5833`, avg `0.007662`, median `0.012964`, mae `0.03141`
- 20d: sample `60`, hit `0.7333`, avg `0.015734`, median `0.027343`, mae `0.037657`
- 60d: sample `60`, hit `0.8833`, avg `0.057821`, median `0.072059`, mae `0.069002`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
