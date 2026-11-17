# High Confidence Edge Report

Generated at: `2026-11-17T12:28:39.716717+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `196`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `196`, gate `stronger_evidence`
- 5d: completed `196`, gate `stronger_evidence`
- 10d: completed `196`, gate `stronger_evidence`
- 20d: completed `196`, gate `stronger_evidence`
- 60d: completed `196`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.525`, avg `0.00119`, median `0.00531`, mae `0.02136`
- 5d: sample `80`, hit `0.5125`, avg `-0.000877`, median `0.000688`, mae `0.022311`
- 10d: sample `80`, hit `0.5125`, avg `0.001941`, median `0.005519`, mae `0.025844`
- 20d: sample `80`, hit `0.625`, avg `0.010443`, median `0.024811`, mae `0.039167`
- 60d: sample `80`, hit `0.675`, avg `0.045819`, median `0.067551`, mae `0.078649`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.014081`, median `0.025079`, mae `0.027283`
- 5d: sample `8`, hit `0.625`, avg `0.001344`, median `0.015669`, mae `0.027716`
- 10d: sample `8`, hit `0.5`, avg `0.018349`, median `0.01609`, mae `0.031986`
- 20d: sample `8`, hit `0.875`, avg `0.034973`, median `0.038387`, mae `0.046915`
- 60d: sample `8`, hit `0.75`, avg `0.060364`, median `0.123132`, mae `0.103532`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.001204`, median `0.007289`, mae `0.017387`
- 5d: sample `8`, hit `0.5`, avg `-0.01031`, median `0.000208`, mae `0.013975`
- 10d: sample `8`, hit `0.375`, avg `-0.003462`, median `-0.001222`, mae `0.019045`
- 20d: sample `8`, hit `0.625`, avg `0.018282`, median `0.031196`, mae `0.033993`
- 60d: sample `8`, hit `0.5`, avg `0.031788`, median `0.085257`, mae `0.078897`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.001204, 'median_return': 0.007289, 'mean_absolute_return': 0.017387, 'max_adverse_excursion': -0.030262, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.01031, 'median_return': 0.000208, 'mean_absolute_return': 0.013975, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.003462, 'median_return': -0.001222, 'mean_absolute_return': 0.019045, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.018282, 'median_return': 0.031196, 'mean_absolute_return': 0.033993, 'max_adverse_excursion': -0.034684, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.031788, 'median_return': 0.085257, 'mean_absolute_return': 0.078897, 'max_adverse_excursion': -0.061859, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.001455, 'median_return': 0.00531, 'mean_absolute_return': 0.021801, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.059607}, '5d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.000171, 'median_return': 0.001303, 'mean_absolute_return': 0.023237, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.063815}, '10d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.002541, 'median_return': 0.006298, 'mean_absolute_return': 0.0266, 'max_adverse_excursion': -0.065085, 'max_favorable_excursion': 0.080589}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.009572, 'median_return': 0.024811, 'mean_absolute_return': 0.039742, 'max_adverse_excursion': -0.098675, 'max_favorable_excursion': 0.108196}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.047378, 'median_return': 0.067551, 'mean_absolute_return': 0.078622, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.255401}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.5}, '60d': {'sample_size': 80, 'hit_rate': 0.4}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.0375, 'both_hit': 0, 'both_miss': 1}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': 0.000805, 'median_return': 0.000496, 'mean_absolute_return': 0.019099, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.002988, 'median_return': 0.000208, 'mean_absolute_return': 0.019942, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': 0.001339, 'median_return': -0.001222, 'mean_absolute_return': 0.024055, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.080589}, '20d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.019874, 'median_return': 0.029289, 'mean_absolute_return': 0.03342, 'max_adverse_excursion': -0.048112, 'max_favorable_excursion': 0.092742}, '60d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.044388, 'median_return': 0.072891, 'mean_absolute_return': 0.078499, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.160798}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.002344, 'median_return': 0.010008, 'mean_absolute_return': 0.028143, 'max_adverse_excursion': -0.05525, 'max_favorable_excursion': 0.059607}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.005457, 'median_return': 0.005676, 'mean_absolute_return': 0.029416, 'max_adverse_excursion': -0.045386, 'max_favorable_excursion': 0.063815}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.003746, 'median_return': 0.013222, 'mean_absolute_return': 0.031211, 'max_adverse_excursion': -0.065085, 'max_favorable_excursion': 0.077422}, '20d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.017848, 'median_return': -0.022621, 'mean_absolute_return': 0.05641, 'max_adverse_excursion': -0.098675, 'max_favorable_excursion': 0.108196}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.05011, 'median_return': 0.045529, 'mean_absolute_return': 0.079101, 'max_adverse_excursion': -0.096885, 'max_favorable_excursion': 0.255401}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `0.000805`, median `0.000496`, mae `0.019099`
- 5d: sample `60`, hit `0.5`, avg `-0.002988`, median `0.000208`, mae `0.019942`
- 10d: sample `60`, hit `0.4667`, avg `0.001339`, median `-0.001222`, mae `0.024055`
- 20d: sample `60`, hit `0.7`, avg `0.019874`, median `0.029289`, mae `0.03342`
- 60d: sample `60`, hit `0.6667`, avg `0.044388`, median `0.072891`, mae `0.078499`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002344`, median `0.010008`, mae `0.028143`
- 5d: sample `20`, hit `0.55`, avg `0.005457`, median `0.005676`, mae `0.029416`
- 10d: sample `20`, hit `0.65`, avg `0.003746`, median `0.013222`, mae `0.031211`
- 20d: sample `20`, hit `0.4`, avg `-0.017848`, median `-0.022621`, mae `0.05641`
- 60d: sample `20`, hit `0.7`, avg `0.05011`, median `0.045529`, mae `0.079101`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008438`, median `0.01152`, mae `0.024981`
- 5d: sample `20`, hit `0.65`, avg `0.004735`, median `0.013131`, mae `0.026667`
- 10d: sample `20`, hit `0.5`, avg `0.004664`, median `0.006356`, mae `0.031882`
- 20d: sample `20`, hit `0.75`, avg `0.024465`, median `0.035803`, mae `0.041614`
- 60d: sample `20`, hit `0.65`, avg `0.049574`, median `0.113901`, mae `0.098316`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002066`, median `-0.001641`, mae `0.014187`
- 5d: sample `20`, hit `0.45`, avg `-0.006281`, median `-0.006464`, mae `0.014506`
- 10d: sample `20`, hit `0.45`, avg `-0.003415`, median `0.0`, mae `0.018347`
- 20d: sample `20`, hit `0.8`, avg `0.019018`, median `0.029234`, mae `0.02548`
- 60d: sample `20`, hit `0.75`, avg `0.045395`, median `0.063683`, mae `0.063196`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008438`, median `0.01152`, mae `0.024981`
- 5d: sample `20`, hit `0.65`, avg `0.004735`, median `0.013131`, mae `0.026667`
- 10d: sample `20`, hit `0.5`, avg `0.004664`, median `0.006356`, mae `0.031882`
- 20d: sample `20`, hit `0.75`, avg `0.024465`, median `0.035803`, mae `0.041614`
- 60d: sample `20`, hit `0.65`, avg `0.049574`, median `0.113901`, mae `0.098316`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002066`, median `-0.001641`, mae `0.014187`
- 5d: sample `20`, hit `0.45`, avg `-0.006281`, median `-0.006464`, mae `0.014506`
- 10d: sample `20`, hit `0.45`, avg `-0.003415`, median `0.0`, mae `0.018347`
- 20d: sample `20`, hit `0.8`, avg `0.019018`, median `0.029234`, mae `0.02548`
- 60d: sample `20`, hit `0.75`, avg `0.045395`, median `0.063683`, mae `0.063196`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002344`, median `0.010008`, mae `0.028143`
- 5d: sample `20`, hit `0.55`, avg `0.005457`, median `0.005676`, mae `0.029416`
- 10d: sample `20`, hit `0.65`, avg `0.003746`, median `0.013222`, mae `0.031211`
- 20d: sample `20`, hit `0.4`, avg `-0.017848`, median `-0.022621`, mae `0.05641`
- 60d: sample `20`, hit `0.7`, avg `0.05011`, median `0.045529`, mae `0.079101`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `0.000805`, median `0.000496`, mae `0.019099`
- 5d: sample `60`, hit `0.5`, avg `-0.002988`, median `0.000208`, mae `0.019942`
- 10d: sample `60`, hit `0.4667`, avg `0.001339`, median `-0.001222`, mae `0.024055`
- 20d: sample `60`, hit `0.7`, avg `0.019874`, median `0.029289`, mae `0.03342`
- 60d: sample `60`, hit `0.6667`, avg `0.044388`, median `0.072891`, mae `0.078499`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- 3d: sample `80`, hit `0.525`, avg `0.00119`, median `0.00531`, mae `0.02136`
- 5d: sample `80`, hit `0.5125`, avg `-0.000877`, median `0.000688`, mae `0.022311`
- 10d: sample `80`, hit `0.5125`, avg `0.001941`, median `0.005519`, mae `0.025844`
- 20d: sample `80`, hit `0.625`, avg `0.010443`, median `0.024811`, mae `0.039167`
- 60d: sample `80`, hit `0.675`, avg `0.045819`, median `0.067551`, mae `0.078649`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.00119`, median `0.00531`, mae `0.02136`
- 5d: sample `80`, hit `0.5125`, avg `-0.000877`, median `0.000688`, mae `0.022311`
- 10d: sample `80`, hit `0.5125`, avg `0.001941`, median `0.005519`, mae `0.025844`
- 20d: sample `80`, hit `0.625`, avg `0.010443`, median `0.024811`, mae `0.039167`
- 60d: sample `80`, hit `0.675`, avg `0.045819`, median `0.067551`, mae `0.078649`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008438`, median `0.01152`, mae `0.024981`
- 5d: sample `20`, hit `0.65`, avg `0.004735`, median `0.013131`, mae `0.026667`
- 10d: sample `20`, hit `0.5`, avg `0.004664`, median `0.006356`, mae `0.031882`
- 20d: sample `20`, hit `0.75`, avg `0.024465`, median `0.035803`, mae `0.041614`
- 60d: sample `20`, hit `0.65`, avg `0.049574`, median `0.113901`, mae `0.098316`

### bounce_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008438`, median `0.01152`, mae `0.024981`
- 5d: sample `20`, hit `0.65`, avg `0.004735`, median `0.013131`, mae `0.026667`
- 10d: sample `20`, hit `0.5`, avg `0.004664`, median `0.006356`, mae `0.031882`
- 20d: sample `20`, hit `0.75`, avg `0.024465`, median `0.035803`, mae `0.041614`
- 60d: sample `20`, hit `0.65`, avg `0.049574`, median `0.113901`, mae `0.098316`

### risk_path_with_flow_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.00119`, median `0.00531`, mae `0.02136`
- 5d: sample `80`, hit `0.5125`, avg `-0.000877`, median `0.000688`, mae `0.022311`
- 10d: sample `80`, hit `0.5125`, avg `0.001941`, median `0.005519`, mae `0.025844`
- 20d: sample `80`, hit `0.625`, avg `0.010443`, median `0.024811`, mae `0.039167`
- 60d: sample `80`, hit `0.675`, avg `0.045819`, median `0.067551`, mae `0.078649`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
