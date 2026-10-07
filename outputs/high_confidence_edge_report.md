# High Confidence Edge Report

Generated at: `2026-10-07T18:59:35.616218+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `84`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `84`, gate `moderate_evidence`
- 5d: completed `84`, gate `moderate_evidence`
- 10d: completed `84`, gate `moderate_evidence`
- 20d: completed `84`, gate `moderate_evidence`
- 60d: completed `84`, gate `moderate_evidence`

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
- 3d: sample `80`, hit `0.4`, avg `-0.00607`, median `-0.003649`, mae `0.0161`
- 5d: sample `80`, hit `0.45`, avg `-0.007331`, median `-0.005632`, mae `0.019965`
- 10d: sample `80`, hit `0.4625`, avg `-0.008747`, median `-0.006389`, mae `0.029679`
- 20d: sample `80`, hit `0.5625`, avg `0.003459`, median `0.013156`, mae `0.041259`
- 60d: sample `80`, hit `0.7875`, avg `0.037608`, median `0.050438`, mae `0.075246`

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
- 3d: sample `8`, hit `0.5`, avg `-0.003344`, median `0.004068`, mae `0.012309`
- 5d: sample `8`, hit `0.5`, avg `-0.003361`, median `0.001479`, mae `0.011834`
- 10d: sample `8`, hit `0.5`, avg `0.000654`, median `0.008264`, mae `0.019158`
- 20d: sample `8`, hit `0.75`, avg `0.009033`, median `0.033164`, mae `0.038733`
- 60d: sample `8`, hit `1.0`, avg `0.047583`, median `0.044683`, mae `0.047583`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.009683`, median `0.006895`, mae `0.026003`
- 5d: sample `8`, hit `0.5`, avg `-0.014553`, median `0.005072`, mae `0.0316`
- 10d: sample `8`, hit `0.25`, avg `-0.017771`, median `-0.013832`, mae `0.025554`
- 20d: sample `8`, hit `0.5`, avg `-0.01538`, median `0.001463`, mae `0.038088`
- 60d: sample `8`, hit `0.5`, avg `-0.046636`, median `0.037425`, mae `0.105094`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.00607, 'median_return': -0.003649, 'mean_absolute_return': 0.0161, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.007331, 'median_return': -0.005632, 'mean_absolute_return': 0.019965, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.008747, 'median_return': -0.006389, 'mean_absolute_return': 0.029679, 'max_adverse_excursion': -0.095057, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.003459, 'median_return': 0.013156, 'mean_absolute_return': 0.041259, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.037608, 'median_return': 0.050438, 'mean_absolute_return': 0.075246, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.154804}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.009683, 'median_return': 0.006895, 'mean_absolute_return': 0.026003, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.014553, 'median_return': 0.005072, 'mean_absolute_return': 0.0316, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.026602}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.017771, 'median_return': -0.013832, 'mean_absolute_return': 0.025554, 'max_adverse_excursion': -0.064399, 'max_favorable_excursion': 0.027926}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.01538, 'median_return': 0.001463, 'mean_absolute_return': 0.038088, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.046636, 'median_return': 0.037425, 'mean_absolute_return': 0.105094, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.099838}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.005669, 'median_return': -0.003649, 'mean_absolute_return': 0.014999, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.006529, 'median_return': -0.005632, 'mean_absolute_return': 0.018673, 'max_adverse_excursion': -0.053563, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.007744, 'median_return': -0.0004, 'mean_absolute_return': 0.030138, 'max_adverse_excursion': -0.095057, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.005552, 'median_return': 0.015416, 'mean_absolute_return': 0.041611, 'max_adverse_excursion': -0.107747, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.046969, 'median_return': 0.056537, 'mean_absolute_return': 0.071929, 'max_adverse_excursion': -0.158935, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.4125}, '20d': {'sample_size': 80, 'hit_rate': 0.4125}, '60d': {'sample_size': 80, 'hit_rate': 0.2625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.475, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.00607, 'median_return': -0.003649, 'mean_absolute_return': 0.0161, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.007331, 'median_return': -0.005632, 'mean_absolute_return': 0.019965, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.008747, 'median_return': -0.006389, 'mean_absolute_return': 0.029679, 'max_adverse_excursion': -0.095057, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.003459, 'median_return': 0.013156, 'mean_absolute_return': 0.041259, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.037608, 'median_return': 0.050438, 'mean_absolute_return': 0.075246, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.154804}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.003674`, median `-0.002952`, mae `0.014461`
- 5d: sample `60`, hit `0.4667`, avg `-0.004644`, median `-0.001562`, mae `0.017359`
- 10d: sample `60`, hit `0.5333`, avg `-0.003599`, median `0.004196`, mae `0.029419`
- 20d: sample `60`, hit `0.6`, avg `0.009799`, median `0.016027`, mae `0.040775`
- 60d: sample `60`, hit `0.85`, avg `0.053776`, median `0.057507`, mae `0.071061`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.013259`, median `-0.012933`, mae `0.021015`
- 5d: sample `20`, hit `0.4`, avg `-0.015393`, median `-0.016421`, mae `0.027786`
- 10d: sample `20`, hit `0.25`, avg `-0.024193`, median `-0.01796`, mae `0.030459`
- 20d: sample `20`, hit `0.45`, avg `-0.015561`, median `-0.001589`, mae `0.042712`
- 60d: sample `20`, hit `0.6`, avg `-0.010894`, median `0.037425`, mae `0.087799`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.003674`, median `-0.002952`, mae `0.014461`
- 5d: sample `60`, hit `0.4667`, avg `-0.004644`, median `-0.001562`, mae `0.017359`
- 10d: sample `60`, hit `0.5333`, avg `-0.003599`, median `0.004196`, mae `0.029419`
- 20d: sample `60`, hit `0.6`, avg `0.009799`, median `0.016027`, mae `0.040775`
- 60d: sample `60`, hit `0.85`, avg `0.053776`, median `0.057507`, mae `0.071061`

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
- 3d: sample `80`, hit `0.4`, avg `-0.00607`, median `-0.003649`, mae `0.0161`
- 5d: sample `80`, hit `0.45`, avg `-0.007331`, median `-0.005632`, mae `0.019965`
- 10d: sample `80`, hit `0.4625`, avg `-0.008747`, median `-0.006389`, mae `0.029679`
- 20d: sample `80`, hit `0.5625`, avg `0.003459`, median `0.013156`, mae `0.041259`
- 60d: sample `80`, hit `0.7875`, avg `0.037608`, median `0.050438`, mae `0.075246`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.013259`, median `-0.012933`, mae `0.021015`
- 5d: sample `20`, hit `0.4`, avg `-0.015393`, median `-0.016421`, mae `0.027786`
- 10d: sample `20`, hit `0.25`, avg `-0.024193`, median `-0.01796`, mae `0.030459`
- 20d: sample `20`, hit `0.45`, avg `-0.015561`, median `-0.001589`, mae `0.042712`
- 60d: sample `20`, hit `0.6`, avg `-0.010894`, median `0.037425`, mae `0.087799`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4`, avg `-0.00607`, median `-0.003649`, mae `0.0161`
- 5d: sample `80`, hit `0.45`, avg `-0.007331`, median `-0.005632`, mae `0.019965`
- 10d: sample `80`, hit `0.4625`, avg `-0.008747`, median `-0.006389`, mae `0.029679`
- 20d: sample `80`, hit `0.5625`, avg `0.003459`, median `0.013156`, mae `0.041259`
- 60d: sample `80`, hit `0.7875`, avg `0.037608`, median `0.050438`, mae `0.075246`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.013259`, median `-0.012933`, mae `0.021015`
- 5d: sample `20`, hit `0.4`, avg `-0.015393`, median `-0.016421`, mae `0.027786`
- 10d: sample `20`, hit `0.25`, avg `-0.024193`, median `-0.01796`, mae `0.030459`
- 20d: sample `20`, hit `0.45`, avg `-0.015561`, median `-0.001589`, mae `0.042712`
- 60d: sample `20`, hit `0.6`, avg `-0.010894`, median `0.037425`, mae `0.087799`

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
