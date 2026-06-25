# High Confidence Edge Report

Generated at: `2026-06-25T23:56:24.311416+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `0`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `0`, gate `insufficient`
- 5d: completed `0`, gate `insufficient`
- 10d: completed `0`, gate `insufficient`
- 20d: completed `0`, gate `insufficient`
- 60d: completed `0`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.003585`, median `0.002296`, mae `0.016558`
- 5d: sample `60`, hit `0.45`, avg `-0.000663`, median `-0.003328`, mae `0.019844`
- 10d: sample `60`, hit `0.4667`, avg `0.002651`, median `-0.001222`, mae `0.022486`
- 20d: sample `60`, hit `0.7667`, avg `0.018674`, median `0.028065`, mae `0.036545`
- 60d: sample `60`, hit `0.8167`, avg `0.05822`, median `0.072889`, mae `0.076956`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003283`, median `-0.003921`, mae `0.012019`
- 5d: sample `20`, hit `0.35`, avg `-0.006899`, median `-0.010916`, mae `0.015744`
- 10d: sample `20`, hit `0.45`, avg `-0.00752`, median `-0.004417`, mae `0.022318`
- 20d: sample `20`, hit `0.65`, avg `-0.005379`, median `0.01251`, mae `0.031423`
- 60d: sample `20`, hit `0.6`, avg `0.006539`, median `0.036183`, mae `0.056553`

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
- 3d: sample `8`, hit `0.375`, avg `-0.000748`, median `-0.000756`, mae `0.016685`
- 5d: sample `8`, hit `0.125`, avg `-0.010783`, median `-0.00855`, mae `0.013534`
- 10d: sample `8`, hit `0.5`, avg `0.004627`, median `0.006053`, mae `0.009669`
- 20d: sample `8`, hit `0.875`, avg `0.024681`, median `0.028791`, mae `0.027062`
- 60d: sample `8`, hit `1.0`, avg `0.082149`, median `0.094627`, mae `0.082149`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.000748`, median `-0.000756`, mae `0.016685`
- 5d: sample `8`, hit `0.125`, avg `-0.010783`, median `-0.00855`, mae `0.013534`
- 10d: sample `8`, hit `0.5`, avg `0.004627`, median `0.006053`, mae `0.009669`
- 20d: sample `8`, hit `0.875`, avg `0.024681`, median `0.028791`, mae `0.027062`
- 60d: sample `8`, hit `1.0`, avg `0.082149`, median `0.094627`, mae `0.082149`

### confidence validation
- `{'strong_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.003585, 'median_return': 0.002296, 'mean_absolute_return': 0.016558, 'max_adverse_excursion': -0.036103, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.000663, 'median_return': -0.003328, 'mean_absolute_return': 0.019844, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': 0.002651, 'median_return': -0.001222, 'mean_absolute_return': 0.022486, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.018674, 'median_return': 0.028065, 'mean_absolute_return': 0.036545, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.05822, 'median_return': 0.072889, 'mean_absolute_return': 0.076956, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.200358}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.000748, 'median_return': -0.000756, 'mean_absolute_return': 0.016685, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.024354}, '5d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.010783, 'median_return': -0.00855, 'mean_absolute_return': 0.013534, 'max_adverse_excursion': -0.029067, 'max_favorable_excursion': 0.011002}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004627, 'median_return': 0.006053, 'mean_absolute_return': 0.009669, 'max_adverse_excursion': -0.011849, 'max_favorable_excursion': 0.023979}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.024681, 'median_return': 0.028791, 'mean_absolute_return': 0.027062, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.041903}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.082149, 'median_return': 0.094627, 'mean_absolute_return': 0.082149, 'max_adverse_excursion': 0.025315, 'max_favorable_excursion': 0.117712}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.002159, 'median_return': 0.001558, 'mean_absolute_return': 0.015283, 'max_adverse_excursion': -0.036103, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.001271, 'median_return': -0.003879, 'mean_absolute_return': 0.019407, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.000394, 'median_return': -0.001663, 'mean_absolute_return': 0.023864, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.011325, 'median_return': 0.016838, 'mean_absolute_return': 0.036176, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.041205, 'median_return': 0.061367, 'mean_absolute_return': 0.070711, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.200358}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.6625}, '60d': {'sample_size': 80, 'hit_rate': 0.7125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.075, 'both_hit': 32, 'both_miss': 28}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.075, 'both_hit': 27, 'both_miss': 33}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.025, 'both_hit': 28, 'both_miss': 32}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.075, 'both_hit': 46, 'both_miss': 14}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': -0.05, 'both_hit': 49, 'both_miss': 11}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.003585, 'median_return': 0.002296, 'mean_absolute_return': 0.016558, 'max_adverse_excursion': -0.036103, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.000663, 'median_return': -0.003328, 'mean_absolute_return': 0.019844, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': 0.002651, 'median_return': -0.001222, 'mean_absolute_return': 0.022486, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.018674, 'median_return': 0.028065, 'mean_absolute_return': 0.036545, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.05822, 'median_return': 0.072889, 'mean_absolute_return': 0.076956, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.200358}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.003283, 'median_return': -0.003921, 'mean_absolute_return': 0.012019, 'max_adverse_excursion': -0.023751, 'max_favorable_excursion': 0.020686}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.006899, 'median_return': -0.010916, 'mean_absolute_return': 0.015744, 'max_adverse_excursion': -0.029469, 'max_favorable_excursion': 0.034509}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.00752, 'median_return': -0.004417, 'mean_absolute_return': 0.022318, 'max_adverse_excursion': -0.050724, 'max_favorable_excursion': 0.04499}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': -0.005379, 'median_return': 0.01251, 'mean_absolute_return': 0.031423, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.036447}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.006539, 'median_return': 0.036183, 'mean_absolute_return': 0.056553, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.10751}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.002461`, median `0.0017`, mae `0.01765`
- 5d: sample `20`, hit `0.45`, avg `-0.00079`, median `-0.000371`, mae `0.017331`
- 10d: sample `20`, hit `0.45`, avg `0.001691`, median `-0.003263`, mae `0.025255`
- 20d: sample `20`, hit `0.6`, avg `0.006173`, median `0.01666`, mae `0.047105`
- 60d: sample `20`, hit `0.8`, avg `0.057092`, median `0.074393`, mae `0.091328`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `0.00167`, median `-0.000756`, mae `0.014681`
- 5d: sample `60`, hit `0.4167`, avg `-0.002699`, median `-0.006048`, mae `0.019315`
- 10d: sample `60`, hit `0.4667`, avg `-0.000419`, median `-0.001222`, mae `0.021508`
- 20d: sample `60`, hit `0.7833`, avg `0.014823`, median `0.020751`, mae `0.031318`
- 60d: sample `60`, hit `0.75`, avg `0.041369`, median `0.060303`, mae `0.065364`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.002461`, median `0.0017`, mae `0.01765`
- 5d: sample `20`, hit `0.45`, avg `-0.00079`, median `-0.000371`, mae `0.017331`
- 10d: sample `20`, hit `0.45`, avg `0.001691`, median `-0.003263`, mae `0.025255`
- 20d: sample `20`, hit `0.6`, avg `0.006173`, median `0.01666`, mae `0.047105`
- 60d: sample `20`, hit `0.8`, avg `0.057092`, median `0.074393`, mae `0.091328`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.004147`, median `0.004243`, mae `0.016012`
- 5d: sample `40`, hit `0.45`, avg `-0.000599`, median `-0.004216`, mae `0.021101`
- 10d: sample `40`, hit `0.475`, avg `0.003131`, median `-0.001083`, mae `0.021102`
- 20d: sample `40`, hit `0.85`, avg `0.024925`, median `0.028626`, mae `0.031265`
- 60d: sample `40`, hit `0.825`, avg `0.058784`, median `0.069629`, mae `0.06977`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.002461`, median `0.0017`, mae `0.01765`
- 5d: sample `20`, hit `0.45`, avg `-0.00079`, median `-0.000371`, mae `0.017331`
- 10d: sample `20`, hit `0.45`, avg `0.001691`, median `-0.003263`, mae `0.025255`
- 20d: sample `20`, hit `0.6`, avg `0.006173`, median `0.01666`, mae `0.047105`
- 60d: sample `20`, hit `0.8`, avg `0.057092`, median `0.074393`, mae `0.091328`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.004147`, median `0.004243`, mae `0.016012`
- 5d: sample `40`, hit `0.45`, avg `-0.000599`, median `-0.004216`, mae `0.021101`
- 10d: sample `40`, hit `0.475`, avg `0.003131`, median `-0.001083`, mae `0.021102`
- 20d: sample `40`, hit `0.85`, avg `0.024925`, median `0.028626`, mae `0.031265`
- 60d: sample `40`, hit `0.825`, avg `0.058784`, median `0.069629`, mae `0.06977`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.002461`, median `0.0017`, mae `0.01765`
- 5d: sample `20`, hit `0.45`, avg `-0.00079`, median `-0.000371`, mae `0.017331`
- 10d: sample `20`, hit `0.45`, avg `0.001691`, median `-0.003263`, mae `0.025255`
- 20d: sample `20`, hit `0.6`, avg `0.006173`, median `0.01666`, mae `0.047105`
- 60d: sample `20`, hit `0.8`, avg `0.057092`, median `0.074393`, mae `0.091328`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.004147`, median `0.004243`, mae `0.016012`
- 5d: sample `40`, hit `0.45`, avg `-0.000599`, median `-0.004216`, mae `0.021101`
- 10d: sample `40`, hit `0.475`, avg `0.003131`, median `-0.001083`, mae `0.021102`
- 20d: sample `40`, hit `0.85`, avg `0.024925`, median `0.028626`, mae `0.031265`
- 60d: sample `40`, hit `0.825`, avg `0.058784`, median `0.069629`, mae `0.06977`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.002461`, median `0.0017`, mae `0.01765`
- 5d: sample `20`, hit `0.45`, avg `-0.00079`, median `-0.000371`, mae `0.017331`
- 10d: sample `20`, hit `0.45`, avg `0.001691`, median `-0.003263`, mae `0.025255`
- 20d: sample `20`, hit `0.6`, avg `0.006173`, median `0.01666`, mae `0.047105`
- 60d: sample `20`, hit `0.8`, avg `0.057092`, median `0.074393`, mae `0.091328`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003283`, median `-0.003921`, mae `0.012019`
- 5d: sample `20`, hit `0.35`, avg `-0.006899`, median `-0.010916`, mae `0.015744`
- 10d: sample `20`, hit `0.45`, avg `-0.00752`, median `-0.004417`, mae `0.022318`
- 20d: sample `20`, hit `0.65`, avg `-0.005379`, median `0.01251`, mae `0.031423`
- 60d: sample `20`, hit `0.6`, avg `0.006539`, median `0.036183`, mae `0.056553`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

### aligned_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.003598`, median `0.0017`, mae `0.016051`
- 5d: sample `40`, hit `0.375`, avg `-0.002873`, median `-0.006048`, mae `0.017125`
- 10d: sample `40`, hit `0.425`, avg `0.002451`, median `-0.00174`, mae `0.018314`
- 20d: sample `40`, hit `0.75`, avg `0.014485`, median `0.019987`, mae `0.035722`
- 60d: sample `40`, hit `0.875`, avg `0.062565`, median `0.073586`, mae `0.082099`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003283`, median `-0.003921`, mae `0.012019`
- 5d: sample `20`, hit `0.35`, avg `-0.006899`, median `-0.010916`, mae `0.015744`
- 10d: sample `20`, hit `0.45`, avg `-0.00752`, median `-0.004417`, mae `0.022318`
- 20d: sample `20`, hit `0.65`, avg `-0.005379`, median `0.01251`, mae `0.031423`
- 60d: sample `20`, hit `0.6`, avg `0.006539`, median `0.036183`, mae `0.056553`

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

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4875`, avg `0.001868`, median `-0.000756`, mae `0.015423`
- 5d: sample `80`, hit `0.425`, avg `-0.002222`, median `-0.005653`, mae `0.018819`
- 10d: sample `80`, hit `0.4625`, avg `0.000108`, median `-0.001663`, mae `0.022444`
- 20d: sample `80`, hit `0.7375`, avg `0.012661`, median `0.019987`, mae `0.035265`
- 60d: sample `80`, hit `0.7625`, avg `0.0453`, median `0.06458`, mae `0.071855`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.003585`, median `0.002296`, mae `0.016558`
- 5d: sample `60`, hit `0.45`, avg `-0.000663`, median `-0.003328`, mae `0.019844`
- 10d: sample `60`, hit `0.4667`, avg `0.002651`, median `-0.001222`, mae `0.022486`
- 20d: sample `60`, hit `0.7667`, avg `0.018674`, median `0.028065`, mae `0.036545`
- 60d: sample `60`, hit `0.8167`, avg `0.05822`, median `0.072889`, mae `0.076956`

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
