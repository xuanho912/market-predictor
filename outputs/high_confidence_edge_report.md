# High Confidence Edge Report

Generated at: `2026-06-16T08:39:51.365442+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004399`, median `0.006895`, mae `0.018596`
- 5d: sample `80`, hit `0.6125`, avg `0.001586`, median `0.007948`, mae `0.021588`
- 10d: sample `80`, hit `0.6`, avg `0.006877`, median `0.010271`, mae `0.027934`
- 20d: sample `80`, hit `0.75`, avg `0.012326`, median `0.01666`, mae `0.03149`
- 60d: sample `80`, hit `0.725`, avg `0.037145`, median `0.04511`, mae `0.061319`

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
- 3d: sample `8`, hit `0.75`, avg `0.012094`, median `0.020188`, mae `0.020789`
- 5d: sample `8`, hit `0.875`, avg `0.019425`, median `0.026456`, mae `0.025988`
- 10d: sample `8`, hit `0.75`, avg `0.024014`, median `0.036012`, mae `0.031736`
- 20d: sample `8`, hit `1.0`, avg `0.041763`, median `0.043456`, mae `0.041763`
- 60d: sample `8`, hit `1.0`, avg `0.096768`, median `0.099838`, mae `0.096768`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.012094`, median `0.020188`, mae `0.020789`
- 5d: sample `8`, hit `0.875`, avg `0.019425`, median `0.026456`, mae `0.025988`
- 10d: sample `8`, hit `0.75`, avg `0.024014`, median `0.036012`, mae `0.031736`
- 20d: sample `8`, hit `1.0`, avg `0.041763`, median `0.043456`, mae `0.041763`
- 60d: sample `8`, hit `1.0`, avg `0.096768`, median `0.099838`, mae `0.096768`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.004399, 'median_return': 0.006895, 'mean_absolute_return': 0.018596, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.001586, 'median_return': 0.007948, 'mean_absolute_return': 0.021588, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.006877, 'median_return': 0.010271, 'mean_absolute_return': 0.027934, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.012326, 'median_return': 0.01666, 'mean_absolute_return': 0.03149, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.037145, 'median_return': 0.04511, 'mean_absolute_return': 0.061319, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.211749}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.012094, 'median_return': 0.020188, 'mean_absolute_return': 0.020789, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.019425, 'median_return': 0.026456, 'mean_absolute_return': 0.025988, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.024014, 'median_return': 0.036012, 'mean_absolute_return': 0.031736, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.041763, 'median_return': 0.043456, 'mean_absolute_return': 0.041763, 'max_adverse_excursion': 0.02284, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.096768, 'median_return': 0.099838, 'mean_absolute_return': 0.096768, 'max_adverse_excursion': 0.055986, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.003544, 'median_return': 0.006315, 'mean_absolute_return': 0.018352, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': -0.000397, 'median_return': 0.004597, 'mean_absolute_return': 0.0211, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.004973, 'median_return': 0.004259, 'mean_absolute_return': 0.027512, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.009055, 'median_return': 0.015529, 'mean_absolute_return': 0.030348, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.030521, 'median_return': 0.041902, 'mean_absolute_return': 0.05738, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.211749}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6375}, '5d': {'sample_size': 80, 'hit_rate': 0.6125}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.75}, '60d': {'sample_size': 80, 'hit_rate': 0.725}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 48, 'both_miss': 32}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': 0.0, 'both_hit': 60, 'both_miss': 20}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': 0.0, 'both_hit': 58, 'both_miss': 22}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.004399, 'median_return': 0.006895, 'mean_absolute_return': 0.018596, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.001586, 'median_return': 0.007948, 'mean_absolute_return': 0.021588, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.006877, 'median_return': 0.010271, 'mean_absolute_return': 0.027934, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.012326, 'median_return': 0.01666, 'mean_absolute_return': 0.03149, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.037145, 'median_return': 0.04511, 'mean_absolute_return': 0.061319, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.211749}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004399`, median `0.006895`, mae `0.018596`
- 5d: sample `80`, hit `0.6125`, avg `0.001586`, median `0.007948`, mae `0.021588`
- 10d: sample `80`, hit `0.6`, avg `0.006877`, median `0.010271`, mae `0.027934`
- 20d: sample `80`, hit `0.75`, avg `0.012326`, median `0.01666`, mae `0.03149`
- 60d: sample `80`, hit `0.725`, avg `0.037145`, median `0.04511`, mae `0.061319`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004399`, median `0.006895`, mae `0.018596`
- 5d: sample `80`, hit `0.6125`, avg `0.001586`, median `0.007948`, mae `0.021588`
- 10d: sample `80`, hit `0.6`, avg `0.006877`, median `0.010271`, mae `0.027934`
- 20d: sample `80`, hit `0.75`, avg `0.012326`, median `0.01666`, mae `0.03149`
- 60d: sample `80`, hit `0.725`, avg `0.037145`, median `0.04511`, mae `0.061319`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004954`, median `0.009349`, mae `0.020726`
- 5d: sample `60`, hit `0.6167`, avg `0.001286`, median `0.008121`, mae `0.023346`
- 10d: sample `60`, hit `0.5833`, avg `0.007648`, median `0.013648`, mae `0.029452`
- 20d: sample `60`, hit `0.7833`, avg `0.015958`, median `0.01666`, mae `0.031234`
- 60d: sample `60`, hit `0.6667`, avg `0.03596`, median `0.046128`, mae `0.067028`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004399`, median `0.006895`, mae `0.018596`
- 5d: sample `80`, hit `0.6125`, avg `0.001586`, median `0.007948`, mae `0.021588`
- 10d: sample `80`, hit `0.6`, avg `0.006877`, median `0.010271`, mae `0.027934`
- 20d: sample `80`, hit `0.75`, avg `0.012326`, median `0.01666`, mae `0.03149`
- 60d: sample `80`, hit `0.725`, avg `0.037145`, median `0.04511`, mae `0.061319`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004954`, median `0.009349`, mae `0.020726`
- 5d: sample `60`, hit `0.6167`, avg `0.001286`, median `0.008121`, mae `0.023346`
- 10d: sample `60`, hit `0.5833`, avg `0.007648`, median `0.013648`, mae `0.029452`
- 20d: sample `60`, hit `0.7833`, avg `0.015958`, median `0.01666`, mae `0.031234`
- 60d: sample `60`, hit `0.6667`, avg `0.03596`, median `0.046128`, mae `0.067028`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.005901`, median `0.008733`, mae `0.01556`
- 5d: sample `40`, hit `0.7`, avg `0.00691`, median `0.009709`, mae `0.018255`
- 10d: sample `40`, hit `0.675`, avg `0.009776`, median `0.017226`, mae `0.027735`
- 20d: sample `40`, hit `0.725`, avg `0.013735`, median `0.026731`, mae `0.035905`
- 60d: sample `40`, hit `0.875`, avg `0.051653`, median `0.050311`, mae `0.057961`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.002897`, median `0.006895`, mae `0.021631`
- 5d: sample `40`, hit `0.525`, avg `-0.003738`, median `0.003238`, mae `0.024922`
- 10d: sample `40`, hit `0.525`, avg `0.003979`, median `0.00273`, mae `0.028134`
- 20d: sample `40`, hit `0.775`, avg `0.010916`, median `0.01128`, mae `0.027074`
- 60d: sample `40`, hit `0.575`, avg `0.022638`, median `0.02999`, mae `0.064677`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.005901`, median `0.008733`, mae `0.01556`
- 5d: sample `40`, hit `0.7`, avg `0.00691`, median `0.009709`, mae `0.018255`
- 10d: sample `40`, hit `0.675`, avg `0.009776`, median `0.017226`, mae `0.027735`
- 20d: sample `40`, hit `0.725`, avg `0.013735`, median `0.026731`, mae `0.035905`
- 60d: sample `40`, hit `0.875`, avg `0.051653`, median `0.050311`, mae `0.057961`

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
- 3d: sample `80`, hit `0.6375`, avg `0.004399`, median `0.006895`, mae `0.018596`
- 5d: sample `80`, hit `0.6125`, avg `0.001586`, median `0.007948`, mae `0.021588`
- 10d: sample `80`, hit `0.6`, avg `0.006877`, median `0.010271`, mae `0.027934`
- 20d: sample `80`, hit `0.75`, avg `0.012326`, median `0.01666`, mae `0.03149`
- 60d: sample `80`, hit `0.725`, avg `0.037145`, median `0.04511`, mae `0.061319`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004399`, median `0.006895`, mae `0.018596`
- 5d: sample `80`, hit `0.6125`, avg `0.001586`, median `0.007948`, mae `0.021588`
- 10d: sample `80`, hit `0.6`, avg `0.006877`, median `0.010271`, mae `0.027934`
- 20d: sample `80`, hit `0.75`, avg `0.012326`, median `0.01666`, mae `0.03149`
- 60d: sample `80`, hit `0.725`, avg `0.037145`, median `0.04511`, mae `0.061319`

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
