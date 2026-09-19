# High Confidence Edge Report

Generated at: `2026-09-19T01:09:37.761788+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `32`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `32`, gate `early_evidence`
- 5d: completed `32`, gate `early_evidence`
- 10d: completed `32`, gate `early_evidence`
- 20d: completed `32`, gate `early_evidence`
- 60d: completed `32`, gate `early_evidence`

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
- 3d: sample `80`, hit `0.5875`, avg `0.002804`, median `0.006042`, mae `0.017092`
- 5d: sample `80`, hit `0.575`, avg `0.004408`, median `0.008152`, mae `0.021338`
- 10d: sample `80`, hit `0.6625`, avg `0.011601`, median `0.011619`, mae `0.027394`
- 20d: sample `80`, hit `0.8`, avg `0.033731`, median `0.0344`, mae `0.044039`
- 60d: sample `80`, hit `0.8`, avg `0.070213`, median `0.092689`, mae `0.087502`

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
- 3d: sample `8`, hit `0.5`, avg `0.001029`, median `0.012272`, mae `0.017168`
- 5d: sample `8`, hit `0.625`, avg `0.001132`, median `0.007948`, mae `0.014508`
- 10d: sample `8`, hit `0.5`, avg `0.006385`, median `0.011031`, mae `0.016676`
- 20d: sample `8`, hit `1.0`, avg `0.052505`, median `0.058396`, mae `0.052505`
- 60d: sample `8`, hit `0.875`, avg `0.08582`, median `0.121826`, mae `0.097311`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.001029`, median `0.012272`, mae `0.017168`
- 5d: sample `8`, hit `0.625`, avg `0.001132`, median `0.007948`, mae `0.014508`
- 10d: sample `8`, hit `0.5`, avg `0.006385`, median `0.011031`, mae `0.016676`
- 20d: sample `8`, hit `1.0`, avg `0.052505`, median `0.058396`, mae `0.052505`
- 60d: sample `8`, hit `0.875`, avg `0.08582`, median `0.121826`, mae `0.097311`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.002804, 'median_return': 0.006042, 'mean_absolute_return': 0.017092, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.004408, 'median_return': 0.008152, 'mean_absolute_return': 0.021338, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.011601, 'median_return': 0.011619, 'mean_absolute_return': 0.027394, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.033731, 'median_return': 0.0344, 'mean_absolute_return': 0.044039, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.070213, 'median_return': 0.092689, 'mean_absolute_return': 0.087502, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001029, 'median_return': 0.012272, 'mean_absolute_return': 0.017168, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.001132, 'median_return': 0.007948, 'mean_absolute_return': 0.014508, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.006385, 'median_return': 0.011031, 'mean_absolute_return': 0.016676, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.052505, 'median_return': 0.058396, 'mean_absolute_return': 0.052505, 'max_adverse_excursion': 0.01983, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.08582, 'median_return': 0.121826, 'mean_absolute_return': 0.097311, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.003001, 'median_return': 0.006042, 'mean_absolute_return': 0.017083, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.004772, 'median_return': 0.010061, 'mean_absolute_return': 0.022097, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.012181, 'median_return': 0.013069, 'mean_absolute_return': 0.028585, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.031645, 'median_return': 0.033597, 'mean_absolute_return': 0.043098, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.068479, 'median_return': 0.092008, 'mean_absolute_return': 0.086412, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.6625}, '20d': {'sample_size': 80, 'hit_rate': 0.8}, '60d': {'sample_size': 80, 'hit_rate': 0.8}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.05, 'both_hit': 39, 'both_miss': 21}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.05, 'both_hit': 38, 'both_miss': 22}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.025, 'both_hit': 42, 'both_miss': 18}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.8, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': 0.075, 'both_hit': 51, 'both_miss': 9}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.8, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': 0.1, 'both_hit': 50, 'both_miss': 10}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.002804, 'median_return': 0.006042, 'mean_absolute_return': 0.017092, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.004408, 'median_return': 0.008152, 'mean_absolute_return': 0.021338, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.011601, 'median_return': 0.011619, 'mean_absolute_return': 0.027394, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.033731, 'median_return': 0.0344, 'mean_absolute_return': 0.044039, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.070213, 'median_return': 0.092689, 'mean_absolute_return': 0.087502, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.5875`, avg `0.002804`, median `0.006042`, mae `0.017092`
- 5d: sample `80`, hit `0.575`, avg `0.004408`, median `0.008152`, mae `0.021338`
- 10d: sample `80`, hit `0.6625`, avg `0.011601`, median `0.011619`, mae `0.027394`
- 20d: sample `80`, hit `0.8`, avg `0.033731`, median `0.0344`, mae `0.044039`
- 60d: sample `80`, hit `0.8`, avg `0.070213`, median `0.092689`, mae `0.087502`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.002804`, median `0.006042`, mae `0.017092`
- 5d: sample `80`, hit `0.575`, avg `0.004408`, median `0.008152`, mae `0.021338`
- 10d: sample `80`, hit `0.6625`, avg `0.011601`, median `0.011619`, mae `0.027394`
- 20d: sample `80`, hit `0.8`, avg `0.033731`, median `0.0344`, mae `0.044039`
- 60d: sample `80`, hit `0.8`, avg `0.070213`, median `0.092689`, mae `0.087502`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.003137`, median `0.009349`, mae `0.018997`
- 5d: sample `60`, hit `0.5833`, avg `0.004934`, median `0.010061`, mae `0.024148`
- 10d: sample `60`, hit `0.6333`, avg `0.014435`, median `0.018412`, mae `0.031966`
- 20d: sample `60`, hit `0.8`, avg `0.035517`, median `0.0344`, mae `0.04741`
- 60d: sample `60`, hit `0.7833`, avg `0.069008`, median `0.095628`, mae `0.089563`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.002804`, median `0.006042`, mae `0.017092`
- 5d: sample `80`, hit `0.575`, avg `0.004408`, median `0.008152`, mae `0.021338`
- 10d: sample `80`, hit `0.6625`, avg `0.011601`, median `0.011619`, mae `0.027394`
- 20d: sample `80`, hit `0.8`, avg `0.033731`, median `0.0344`, mae `0.044039`
- 60d: sample `80`, hit `0.8`, avg `0.070213`, median `0.092689`, mae `0.087502`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- 3d: sample `80`, hit `0.5875`, avg `0.002804`, median `0.006042`, mae `0.017092`
- 5d: sample `80`, hit `0.575`, avg `0.004408`, median `0.008152`, mae `0.021338`
- 10d: sample `80`, hit `0.6625`, avg `0.011601`, median `0.011619`, mae `0.027394`
- 20d: sample `80`, hit `0.8`, avg `0.033731`, median `0.0344`, mae `0.044039`
- 60d: sample `80`, hit `0.8`, avg `0.070213`, median `0.092689`, mae `0.087502`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.002804`, median `0.006042`, mae `0.017092`
- 5d: sample `80`, hit `0.575`, avg `0.004408`, median `0.008152`, mae `0.021338`
- 10d: sample `80`, hit `0.6625`, avg `0.011601`, median `0.011619`, mae `0.027394`
- 20d: sample `80`, hit `0.8`, avg `0.033731`, median `0.0344`, mae `0.044039`
- 60d: sample `80`, hit `0.8`, avg `0.070213`, median `0.092689`, mae `0.087502`

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
