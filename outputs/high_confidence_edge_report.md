# High Confidence Edge Report

Generated at: `2026-09-30T18:04:03.398566+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00283`, median `0.0054`, mae `0.014736`
- 5d: sample `20`, hit `0.6`, avg `-0.001374`, median `0.006609`, mae `0.018197`
- 10d: sample `20`, hit `0.6`, avg `-0.00473`, median `0.004196`, mae `0.020775`
- 20d: sample `20`, hit `0.65`, avg `0.009844`, median `0.015416`, mae `0.028962`
- 60d: sample `20`, hit `0.85`, avg `0.052197`, median `0.059104`, mae `0.068146`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.3667`, avg `-0.007869`, median `-0.004907`, mae `0.01773`
- 5d: sample `60`, hit `0.4167`, avg `-0.011327`, median `-0.00693`, mae `0.02096`
- 10d: sample `60`, hit `0.45`, avg `-0.005347`, median `-0.006017`, mae `0.031916`
- 20d: sample `60`, hit `0.6333`, avg `0.00629`, median `0.020068`, mae `0.0487`
- 60d: sample `60`, hit `0.7333`, avg `0.027645`, median `0.044683`, mae `0.084179`

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
- 3d: sample `8`, hit `0.625`, avg `0.000512`, median `0.004815`, mae `0.015818`
- 5d: sample `8`, hit `0.625`, avg `-0.001319`, median `0.006609`, mae `0.01388`
- 10d: sample `8`, hit `0.5`, avg `-0.003463`, median `0.000397`, mae `0.014388`
- 20d: sample `8`, hit `0.75`, avg `0.019551`, median `0.01927`, mae `0.02545`
- 60d: sample `8`, hit `1.0`, avg `0.044293`, median `0.053855`, mae `0.044293`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.016717`, median `-0.030499`, mae `0.027882`
- 5d: sample `8`, hit `0.375`, avg `-0.022926`, median `-0.024165`, mae `0.029269`
- 10d: sample `8`, hit `0.0`, avg `-0.023846`, median `-0.017071`, mae `0.023846`
- 20d: sample `8`, hit `0.625`, avg `-0.004187`, median `0.021759`, mae `0.046567`
- 60d: sample `8`, hit `0.75`, avg `0.019077`, median `0.050438`, mae `0.088012`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.00283, 'median_return': 0.0054, 'mean_absolute_return': 0.014736, 'max_adverse_excursion': -0.029438, 'max_favorable_excursion': 0.026049}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.001374, 'median_return': 0.006609, 'mean_absolute_return': 0.018197, 'max_adverse_excursion': -0.049407, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.00473, 'median_return': 0.004196, 'mean_absolute_return': 0.020775, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.009844, 'median_return': 0.015416, 'mean_absolute_return': 0.028962, 'max_adverse_excursion': -0.051442, 'max_favorable_excursion': 0.057835}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.052197, 'median_return': 0.059104, 'mean_absolute_return': 0.068146, 'max_adverse_excursion': -0.089779, 'max_favorable_excursion': 0.142584}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.016717, 'median_return': -0.030499, 'mean_absolute_return': 0.027882, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.022926, 'median_return': -0.024165, 'mean_absolute_return': 0.029269, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.010589}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.023846, 'median_return': -0.017071, 'mean_absolute_return': 0.023846, 'max_adverse_excursion': -0.064399, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.004187, 'median_return': 0.021759, 'mean_absolute_return': 0.046567, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.019077, 'median_return': 0.050438, 'mean_absolute_return': 0.088012, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.003914, 'median_return': -0.002952, 'mean_absolute_return': 0.01577, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.007273, 'median_return': -0.002452, 'mean_absolute_return': 0.019269, 'max_adverse_excursion': -0.061537, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.00312, 'median_return': 0.004196, 'mean_absolute_return': 0.029718, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.008441, 'median_return': 0.016027, 'mean_absolute_return': 0.043454, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.035417, 'median_return': 0.044826, 'mean_absolute_return': 0.079299, 'max_adverse_excursion': -0.193228, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.5375}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.3625}, '60d': {'sample_size': 80, 'hit_rate': 0.2375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': -0.525, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.00283, 'median_return': 0.0054, 'mean_absolute_return': 0.014736, 'max_adverse_excursion': -0.029438, 'max_favorable_excursion': 0.026049}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.001374, 'median_return': 0.006609, 'mean_absolute_return': 0.018197, 'max_adverse_excursion': -0.049407, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.00473, 'median_return': 0.004196, 'mean_absolute_return': 0.020775, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.009844, 'median_return': 0.015416, 'mean_absolute_return': 0.028962, 'max_adverse_excursion': -0.051442, 'max_favorable_excursion': 0.057835}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.052197, 'median_return': 0.059104, 'mean_absolute_return': 0.068146, 'max_adverse_excursion': -0.089779, 'max_favorable_excursion': 0.142584}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': -0.007869, 'median_return': -0.004907, 'mean_absolute_return': 0.01773, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.011327, 'median_return': -0.00693, 'mean_absolute_return': 0.02096, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.005347, 'median_return': -0.006017, 'mean_absolute_return': 0.031916, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.00629, 'median_return': 0.020068, 'mean_absolute_return': 0.0487, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.027645, 'median_return': 0.044683, 'mean_absolute_return': 0.084179, 'max_adverse_excursion': -0.193228, 'max_favorable_excursion': 0.154804}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.003952`, median `-0.001658`, mae `0.019297`
- 5d: sample `40`, hit `0.475`, avg `-0.00916`, median `-0.007113`, mae `0.022007`
- 10d: sample `40`, hit `0.4`, avg `-0.011952`, median `-0.007011`, mae `0.023632`
- 20d: sample `40`, hit `0.625`, avg `0.004369`, median `0.016021`, mae `0.03689`
- 60d: sample `40`, hit `0.775`, avg `0.034961`, median `0.046407`, mae `0.075271`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.006436`, median `-0.003676`, mae `0.014666`
- 5d: sample `40`, hit `0.45`, avg `-0.008517`, median `-0.002452`, mae `0.018532`
- 10d: sample `40`, hit `0.575`, avg `0.001567`, median `0.011168`, mae `0.034631`
- 20d: sample `40`, hit `0.65`, avg `0.009988`, median `0.026731`, mae `0.050641`
- 60d: sample `40`, hit `0.75`, avg `0.032605`, median `0.044683`, mae `0.08507`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00283`, median `0.0054`, mae `0.014736`
- 5d: sample `20`, hit `0.6`, avg `-0.001374`, median `0.006609`, mae `0.018197`
- 10d: sample `20`, hit `0.6`, avg `-0.00473`, median `0.004196`, mae `0.020775`
- 20d: sample `20`, hit `0.65`, avg `0.009844`, median `0.015416`, mae `0.028962`
- 60d: sample `20`, hit `0.85`, avg `0.052197`, median `0.059104`, mae `0.068146`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00283`, median `0.0054`, mae `0.014736`
- 5d: sample `20`, hit `0.6`, avg `-0.001374`, median `0.006609`, mae `0.018197`
- 10d: sample `20`, hit `0.6`, avg `-0.00473`, median `0.004196`, mae `0.020775`
- 20d: sample `20`, hit `0.65`, avg `0.009844`, median `0.015416`, mae `0.028962`
- 60d: sample `20`, hit `0.85`, avg `0.052197`, median `0.059104`, mae `0.068146`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.006436`, median `-0.003676`, mae `0.014666`
- 5d: sample `40`, hit `0.45`, avg `-0.008517`, median `-0.002452`, mae `0.018532`
- 10d: sample `40`, hit `0.575`, avg `0.001567`, median `0.011168`, mae `0.034631`
- 20d: sample `40`, hit `0.65`, avg `0.009988`, median `0.026731`, mae `0.050641`
- 60d: sample `40`, hit `0.75`, avg `0.032605`, median `0.044683`, mae `0.08507`

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
- 3d: sample `80`, hit `0.425`, avg `-0.005194`, median `-0.003244`, mae `0.016982`
- 5d: sample `80`, hit `0.4625`, avg `-0.008838`, median `-0.005632`, mae `0.020269`
- 10d: sample `80`, hit `0.4875`, avg `-0.005192`, median `-0.0004`, mae `0.029131`
- 20d: sample `80`, hit `0.6375`, avg `0.007179`, median `0.016745`, mae `0.043765`
- 60d: sample `80`, hit `0.7625`, avg `0.033783`, median `0.046132`, mae `0.080171`

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
- 3d: sample `80`, hit `0.425`, avg `-0.005194`, median `-0.003244`, mae `0.016982`
- 5d: sample `80`, hit `0.4625`, avg `-0.008838`, median `-0.005632`, mae `0.020269`
- 10d: sample `80`, hit `0.4875`, avg `-0.005192`, median `-0.0004`, mae `0.029131`
- 20d: sample `80`, hit `0.6375`, avg `0.007179`, median `0.016745`, mae `0.043765`
- 60d: sample `80`, hit `0.7625`, avg `0.033783`, median `0.046132`, mae `0.080171`

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
