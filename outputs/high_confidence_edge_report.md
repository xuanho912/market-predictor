# High Confidence Edge Report

Generated at: `2026-09-29T18:07:43.147664+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `60`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `60`, gate `moderate_evidence`
- 5d: completed `60`, gate `moderate_evidence`
- 10d: completed `60`, gate `moderate_evidence`
- 20d: completed `60`, gate `moderate_evidence`
- 60d: completed `60`, gate `moderate_evidence`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.001615`, median `0.001405`, mae `0.016132`
- 5d: sample `60`, hit `0.5167`, avg `-0.005312`, median `0.000863`, mae `0.017433`
- 10d: sample `60`, hit `0.5167`, avg `-0.004716`, median `0.001607`, mae `0.021376`
- 20d: sample `60`, hit `0.6667`, avg `0.011492`, median `0.01927`, mae `0.037909`
- 60d: sample `60`, hit `0.85`, avg `0.050467`, median `0.059131`, mae `0.076897`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.2`, avg `-0.011267`, median `-0.01091`, mae `0.015551`
- 5d: sample `20`, hit `0.2`, avg `-0.015058`, median `-0.013446`, mae `0.021053`
- 10d: sample `20`, hit `0.45`, avg `-0.003613`, median `-0.001818`, mae `0.038837`
- 20d: sample `20`, hit `0.45`, avg `0.009894`, median `-0.00045`, mae `0.055192`
- 60d: sample `20`, hit `0.9`, avg `0.090968`, median `0.133092`, mae `0.127122`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.009635`, median `0.012217`, mae `0.011445`
- 5d: sample `8`, hit `0.75`, avg `0.003391`, median `0.007043`, mae `0.011208`
- 10d: sample `8`, hit `0.75`, avg `0.002911`, median `0.007751`, mae `0.011968`
- 20d: sample `8`, hit `0.625`, avg `0.020574`, median `0.045453`, mae `0.029895`
- 60d: sample `8`, hit `1.0`, avg `0.063318`, median `0.084216`, mae `0.063318`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.009635`, median `0.012217`, mae `0.011445`
- 5d: sample `8`, hit `0.75`, avg `0.003391`, median `0.007043`, mae `0.011208`
- 10d: sample `8`, hit `0.75`, avg `0.002911`, median `0.007751`, mae `0.011968`
- 20d: sample `8`, hit `0.625`, avg `0.020574`, median `0.045453`, mae `0.029895`
- 60d: sample `8`, hit `1.0`, avg `0.063318`, median `0.084216`, mae `0.063318`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009635, 'median_return': 0.012217, 'mean_absolute_return': 0.011445, 'max_adverse_excursion': -0.003995, 'max_favorable_excursion': 0.023486}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.003391, 'median_return': 0.007043, 'mean_absolute_return': 0.011208, 'max_adverse_excursion': -0.018034, 'max_favorable_excursion': 0.018625}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.002911, 'median_return': 0.007751, 'mean_absolute_return': 0.011968, 'max_adverse_excursion': -0.022813, 'max_favorable_excursion': 0.018352}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.020574, 'median_return': 0.045453, 'mean_absolute_return': 0.029895, 'max_adverse_excursion': -0.015145, 'max_favorable_excursion': 0.056558}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.063318, 'median_return': 0.084216, 'mean_absolute_return': 0.063318, 'max_adverse_excursion': 0.002294, 'max_favorable_excursion': 0.114629}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.005546, 'median_return': -0.004907, 'mean_absolute_return': 0.016491, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.008987, 'median_return': -0.00693, 'mean_absolute_return': 0.01913, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.005257, 'median_return': -0.0004, 'mean_absolute_return': 0.027271, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.010039, 'median_return': 0.016745, 'mean_absolute_return': 0.0436, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.8472, 'avg_return': 0.060289, 'median_return': 0.075909, 'mean_absolute_return': 0.092358, 'max_adverse_excursion': -0.184447, 'max_favorable_excursion': 0.176653}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.3875}, '60d': {'sample_size': 80, 'hit_rate': 0.1375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.1375, 'secondary_hit_rate': 0.8625, 'primary_minus_secondary': -0.725, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.00283, 'median_return': 0.0054, 'mean_absolute_return': 0.014736, 'max_adverse_excursion': -0.029438, 'max_favorable_excursion': 0.026049}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.001374, 'median_return': 0.006609, 'mean_absolute_return': 0.018197, 'max_adverse_excursion': -0.049407, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.00473, 'median_return': 0.004196, 'mean_absolute_return': 0.020775, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.009844, 'median_return': 0.015416, 'mean_absolute_return': 0.028962, 'max_adverse_excursion': -0.051442, 'max_favorable_excursion': 0.057835}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.052197, 'median_return': 0.059104, 'mean_absolute_return': 0.068146, 'max_adverse_excursion': -0.089779, 'max_favorable_excursion': 0.142584}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.006313, 'median_return': -0.004936, 'mean_absolute_return': 0.016403, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.009874, 'median_return': -0.00693, 'mean_absolute_return': 0.018385, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.004343, 'median_return': -0.0004, 'mean_absolute_return': 0.027396, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.011509, 'median_return': 0.021759, 'mean_absolute_return': 0.046652, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 60, 'hit_rate': 0.8667, 'avg_return': 0.06339, 'median_return': 0.077304, 'mean_absolute_return': 0.096556, 'max_adverse_excursion': -0.184447, 'max_favorable_excursion': 0.176653}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.000698`, median `0.002957`, mae `0.017497`
- 5d: sample `40`, hit `0.475`, avg `-0.005716`, median `-0.001429`, mae `0.019568`
- 10d: sample `40`, hit `0.475`, avg `-0.00902`, median `-0.000231`, mae `0.022406`
- 20d: sample `40`, hit `0.575`, avg `0.004986`, median `0.014747`, mae `0.036239`
- 60d: sample `40`, hit `0.825`, avg `0.050769`, median `0.065995`, mae `0.0809`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.007357`, median `-0.006207`, mae `0.014476`
- 5d: sample `40`, hit `0.4`, avg `-0.009782`, median `-0.005632`, mae `0.017107`
- 10d: sample `40`, hit `0.525`, avg `0.00014`, median `0.005535`, mae `0.029075`
- 20d: sample `40`, hit `0.65`, avg `0.017199`, median `0.032102`, mae `0.048221`
- 60d: sample `40`, hit `0.9`, avg `0.070415`, median `0.077304`, mae `0.098007`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.007357`, median `-0.006207`, mae `0.014476`
- 5d: sample `40`, hit `0.4`, avg `-0.009782`, median `-0.005632`, mae `0.017107`
- 10d: sample `40`, hit `0.525`, avg `0.00014`, median `0.005535`, mae `0.029075`
- 20d: sample `40`, hit `0.65`, avg `0.017199`, median `0.032102`, mae `0.048221`
- 60d: sample `40`, hit `0.9`, avg `0.070415`, median `0.077304`, mae `0.098007`

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
- 3d: sample `80`, hit `0.4375`, avg `-0.004028`, median `-0.002952`, mae `0.015987`
- 5d: sample `80`, hit `0.4375`, avg `-0.007749`, median `-0.003262`, mae `0.018338`
- 10d: sample `80`, hit `0.5`, avg `-0.00444`, median `0.000397`, mae `0.025741`
- 20d: sample `80`, hit `0.6125`, avg `0.011093`, median `0.016745`, mae `0.04223`
- 60d: sample `80`, hit `0.8625`, avg `0.060592`, median `0.075909`, mae `0.089454`

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
