# High Confidence Edge Report

Generated at: `2026-09-25T17:15:36.083443+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.00873`, median `-0.010033`, mae `0.02267`
- 5d: sample `20`, hit `0.3`, avg `-0.015526`, median `-0.010073`, mae `0.023661`
- 10d: sample `20`, hit `0.25`, avg `-0.017661`, median `-0.013832`, mae `0.02467`
- 20d: sample `20`, hit `0.55`, avg `5.5e-05`, median `0.016745`, mae `0.046506`
- 60d: sample `20`, hit `0.75`, avg `0.037365`, median `0.059131`, mae `0.087366`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.005165`, median `-0.003649`, mae `0.015477`
- 5d: sample `60`, hit `0.4833`, avg `-0.008969`, median `-0.001562`, mae `0.019869`
- 10d: sample `60`, hit `0.5333`, avg `-0.00545`, median `0.004196`, mae `0.028655`
- 20d: sample `60`, hit `0.6`, avg `0.003853`, median `0.013156`, mae `0.043002`
- 60d: sample `60`, hit `0.8`, avg `0.037438`, median `0.053855`, mae `0.079235`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.00873, 'median_return': -0.010033, 'mean_absolute_return': 0.02267, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.015526, 'median_return': -0.010073, 'mean_absolute_return': 0.023661, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.017661, 'median_return': -0.013832, 'mean_absolute_return': 0.02467, 'max_adverse_excursion': -0.064399, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 5.5e-05, 'median_return': 0.016745, 'mean_absolute_return': 0.046506, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.037365, 'median_return': 0.059131, 'mean_absolute_return': 0.087366, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003118, 'median_return': 0.012272, 'mean_absolute_return': 0.022526, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.007215, 'median_return': 0.007948, 'mean_absolute_return': 0.022159, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.006535, 'median_return': -0.011432, 'mean_absolute_return': 0.017437, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016651, 'median_return': 0.029166, 'mean_absolute_return': 0.046777, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.055371, 'median_return': 0.072696, 'mean_absolute_return': 0.090652, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.006383, 'median_return': -0.003995, 'mean_absolute_return': 0.016692, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.010985, 'median_return': -0.007994, 'mean_absolute_return': 0.020668, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.008721, 'median_return': -0.000231, 'mean_absolute_return': 0.028794, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.001376, 'median_return': 0.012153, 'mean_absolute_return': 0.043555, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.035425, 'median_return': 0.053855, 'mean_absolute_return': 0.080225, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.5375}, '20d': {'sample_size': 80, 'hit_rate': 0.4125}, '60d': {'sample_size': 80, 'hit_rate': 0.2125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.175, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_minus_secondary': -0.575, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.00167, 'median_return': 0.001405, 'mean_absolute_return': 0.016044, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.006834, 'median_return': 0.000688, 'mean_absolute_return': 0.017853, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.008309, 'median_return': -0.0004, 'mean_absolute_return': 0.021821, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.036168}, '20d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.004579, 'median_return': 0.015416, 'mean_absolute_return': 0.036436, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.03805, 'median_return': 0.046407, 'mean_absolute_return': 0.068479, 'max_adverse_excursion': -0.146095, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.1, 'avg_return': -0.019213, 'median_return': -0.013218, 'mean_absolute_return': 0.020971, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.011534}, '5d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.021929, 'median_return': -0.021161, 'mean_absolute_return': 0.029709, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.023861}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.009083, 'median_return': -0.027227, 'mean_absolute_return': 0.045171, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.002123, 'median_return': -0.009713, 'mean_absolute_return': 0.066202, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.035529, 'median_return': 0.098256, 'mean_absolute_return': 0.119635, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.154804}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.4125`, avg `-0.006056`, median `-0.003676`, mae `0.017275`
- 5d: sample `80`, hit `0.4375`, avg `-0.010608`, median `-0.007113`, mae `0.020817`
- 10d: sample `80`, hit `0.4625`, avg `-0.008503`, median `-0.004767`, mae `0.027659`
- 20d: sample `80`, hit `0.5875`, avg `0.002903`, median `0.014747`, mae `0.043878`
- 60d: sample `80`, hit `0.7875`, avg `0.03742`, median `0.053855`, mae `0.081268`

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
- 3d: sample `20`, hit `0.4`, avg `-0.00873`, median `-0.010033`, mae `0.02267`
- 5d: sample `20`, hit `0.3`, avg `-0.015526`, median `-0.010073`, mae `0.023661`
- 10d: sample `20`, hit `0.25`, avg `-0.017661`, median `-0.013832`, mae `0.02467`
- 20d: sample `20`, hit `0.55`, avg `5.5e-05`, median `0.016745`, mae `0.046506`
- 60d: sample `20`, hit `0.75`, avg `0.037365`, median `0.059131`, mae `0.087366`

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
- 3d: sample `80`, hit `0.4125`, avg `-0.006056`, median `-0.003676`, mae `0.017275`
- 5d: sample `80`, hit `0.4375`, avg `-0.010608`, median `-0.007113`, mae `0.020817`
- 10d: sample `80`, hit `0.4625`, avg `-0.008503`, median `-0.004767`, mae `0.027659`
- 20d: sample `80`, hit `0.5875`, avg `0.002903`, median `0.014747`, mae `0.043878`
- 60d: sample `80`, hit `0.7875`, avg `0.03742`, median `0.053855`, mae `0.081268`

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
- 3d: sample `80`, hit `0.4125`, avg `-0.006056`, median `-0.003676`, mae `0.017275`
- 5d: sample `80`, hit `0.4375`, avg `-0.010608`, median `-0.007113`, mae `0.020817`
- 10d: sample `80`, hit `0.4625`, avg `-0.008503`, median `-0.004767`, mae `0.027659`
- 20d: sample `80`, hit `0.5875`, avg `0.002903`, median `0.014747`, mae `0.043878`
- 60d: sample `80`, hit `0.7875`, avg `0.03742`, median `0.053855`, mae `0.081268`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.00167`, median `0.001405`, mae `0.016044`
- 5d: sample `60`, hit `0.5`, avg `-0.006834`, median `0.000688`, mae `0.017853`
- 10d: sample `60`, hit `0.4667`, avg `-0.008309`, median `-0.0004`, mae `0.021821`
- 20d: sample `60`, hit `0.6333`, avg `0.004579`, median `0.015416`, mae `0.036436`
- 60d: sample `60`, hit `0.8167`, avg `0.03805`, median `0.046407`, mae `0.068479`

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
