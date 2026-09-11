# High Confidence Edge Report

Generated at: `2026-09-11T01:02:19.001656+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `8`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `8`, gate `insufficient`
- 5d: completed `8`, gate `insufficient`
- 10d: completed `8`, gate `insufficient`
- 20d: completed `8`, gate `insufficient`
- 60d: completed `8`, gate `insufficient`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.6875`, avg `0.006862`, median `0.012525`, mae `0.020745`
- 5d: sample `80`, hit `0.6125`, avg `0.008042`, median `0.012885`, mae `0.023597`
- 10d: sample `80`, hit `0.6875`, avg `0.014514`, median `0.017201`, mae `0.031666`
- 20d: sample `80`, hit `0.8`, avg `0.032202`, median `0.034726`, mae `0.045828`
- 60d: sample `80`, hit `0.7875`, avg `0.065843`, median `0.084216`, mae `0.092668`

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
- 3d: sample `8`, hit `0.375`, avg `-0.003677`, median `-0.001591`, mae `0.012859`
- 5d: sample `8`, hit `0.625`, avg `0.00159`, median `0.007948`, mae `0.016246`
- 10d: sample `8`, hit `0.625`, avg `0.010867`, median `0.020334`, mae `0.020093`
- 20d: sample `8`, hit `0.875`, avg `0.042186`, median `0.058396`, mae `0.043507`
- 60d: sample `8`, hit `1.0`, avg `0.097429`, median `0.121826`, mae `0.097429`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.003677`, median `-0.001591`, mae `0.012859`
- 5d: sample `8`, hit `0.625`, avg `0.00159`, median `0.007948`, mae `0.016246`
- 10d: sample `8`, hit `0.625`, avg `0.010867`, median `0.020334`, mae `0.020093`
- 20d: sample `8`, hit `0.875`, avg `0.042186`, median `0.058396`, mae `0.043507`
- 60d: sample `8`, hit `1.0`, avg `0.097429`, median `0.121826`, mae `0.097429`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.003677, 'median_return': -0.001591, 'mean_absolute_return': 0.012859, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.00159, 'median_return': 0.007948, 'mean_absolute_return': 0.016246, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.010867, 'median_return': 0.020334, 'mean_absolute_return': 0.020093, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.036071}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.042186, 'median_return': 0.058396, 'mean_absolute_return': 0.043507, 'max_adverse_excursion': -0.005283, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.097429, 'median_return': 0.121826, 'mean_absolute_return': 0.097429, 'max_adverse_excursion': 0.024156, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.008033, 'median_return': 0.013951, 'mean_absolute_return': 0.021621, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.04966}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.008759, 'median_return': 0.013852, 'mean_absolute_return': 0.024414, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.062217}, '10d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.014919, 'median_return': 0.017201, 'mean_absolute_return': 0.032951, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.098213}, '20d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.031093, 'median_return': 0.034704, 'mean_absolute_return': 0.046085, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.062334, 'median_return': 0.077143, 'mean_absolute_return': 0.092139, 'max_adverse_excursion': -0.171649, 'max_favorable_excursion': 0.220253}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.3125}, '5d': {'sample_size': 80, 'hit_rate': 0.3875}, '10d': {'sample_size': 80, 'hit_rate': 0.3125}, '20d': {'sample_size': 80, 'hit_rate': 0.2}, '60d': {'sample_size': 80, 'hit_rate': 0.2125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': -0.6, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_minus_secondary': -0.575, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.006862, 'median_return': 0.012525, 'mean_absolute_return': 0.020745, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.04966}, '5d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.008042, 'median_return': 0.012885, 'mean_absolute_return': 0.023597, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.062217}, '10d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.014514, 'median_return': 0.017201, 'mean_absolute_return': 0.031666, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.098213}, '20d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.032202, 'median_return': 0.034726, 'mean_absolute_return': 0.045828, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.065843, 'median_return': 0.084216, 'mean_absolute_return': 0.092668, 'max_adverse_excursion': -0.171649, 'max_favorable_excursion': 0.220253}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6875`, avg `0.006862`, median `0.012525`, mae `0.020745`
- 5d: sample `80`, hit `0.6125`, avg `0.008042`, median `0.012885`, mae `0.023597`
- 10d: sample `80`, hit `0.6875`, avg `0.014514`, median `0.017201`, mae `0.031666`
- 20d: sample `80`, hit `0.8`, avg `0.032202`, median `0.034726`, mae `0.045828`
- 60d: sample `80`, hit `0.7875`, avg `0.065843`, median `0.084216`, mae `0.092668`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.7333`, avg `0.008607`, median `0.013951`, mae `0.018937`
- 5d: sample `60`, hit `0.6333`, avg `0.010546`, median `0.013852`, mae `0.022337`
- 10d: sample `60`, hit `0.7333`, avg `0.016777`, median `0.017201`, mae `0.029292`
- 20d: sample `60`, hit `0.8333`, avg `0.03836`, median `0.039296`, mae `0.048966`
- 60d: sample `60`, hit `0.85`, avg `0.081728`, median `0.099512`, mae `0.096388`

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
- 3d: sample `80`, hit `0.6875`, avg `0.006862`, median `0.012525`, mae `0.020745`
- 5d: sample `80`, hit `0.6125`, avg `0.008042`, median `0.012885`, mae `0.023597`
- 10d: sample `80`, hit `0.6875`, avg `0.014514`, median `0.017201`, mae `0.031666`
- 20d: sample `80`, hit `0.8`, avg `0.032202`, median `0.034726`, mae `0.045828`
- 60d: sample `80`, hit `0.7875`, avg `0.065843`, median `0.084216`, mae `0.092668`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.6875`, avg `0.006862`, median `0.012525`, mae `0.020745`
- 5d: sample `80`, hit `0.6125`, avg `0.008042`, median `0.012885`, mae `0.023597`
- 10d: sample `80`, hit `0.6875`, avg `0.014514`, median `0.017201`, mae `0.031666`
- 20d: sample `80`, hit `0.8`, avg `0.032202`, median `0.034726`, mae `0.045828`
- 60d: sample `80`, hit `0.7875`, avg `0.065843`, median `0.084216`, mae `0.092668`

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
