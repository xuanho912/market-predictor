# High Confidence Edge Report

Generated at: `2026-10-27T02:01:43.050639+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `136`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `136`, gate `stronger_evidence`
- 5d: completed `136`, gate `stronger_evidence`
- 10d: completed `136`, gate `stronger_evidence`
- 20d: completed `136`, gate `stronger_evidence`
- 60d: completed `136`, gate `stronger_evidence`

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
- 3d: sample `60`, hit `0.5333`, avg `0.003049`, median `0.004243`, mae `0.01568`
- 5d: sample `60`, hit `0.5`, avg `0.001906`, median `0.001023`, mae `0.017591`
- 10d: sample `60`, hit `0.6167`, avg `0.009417`, median `0.009015`, mae `0.022354`
- 20d: sample `60`, hit `0.75`, avg `0.019065`, median `0.024811`, mae `0.03294`
- 60d: sample `60`, hit `0.85`, avg `0.048624`, median `0.05455`, mae `0.062878`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.007633`, median `0.010582`, mae `0.016586`
- 5d: sample `20`, hit `0.75`, avg `0.013617`, median `0.017768`, mae `0.018457`
- 10d: sample `20`, hit `0.85`, avg `0.021166`, median `0.0211`, mae `0.025982`
- 20d: sample `20`, hit `0.65`, avg `0.022436`, median `0.025424`, mae `0.036814`
- 60d: sample `20`, hit `0.85`, avg `0.026839`, median `0.02496`, mae `0.040851`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.002738`, median `0.006372`, mae `0.012774`
- 5d: sample `8`, hit `0.625`, avg `0.003635`, median `0.006571`, mae `0.014981`
- 10d: sample `8`, hit `0.625`, avg `0.008584`, median `0.019466`, mae `0.030668`
- 20d: sample `8`, hit `0.75`, avg `0.02459`, median `0.028859`, mae `0.028409`
- 60d: sample `8`, hit `0.75`, avg `0.026024`, median `0.041644`, mae `0.04503`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.005431`, median `0.004243`, mae `0.016669`
- 5d: sample `8`, hit `0.375`, avg `0.00416`, median `-0.006798`, mae `0.018732`
- 10d: sample `8`, hit `0.75`, avg `0.016234`, median `0.020918`, mae `0.02469`
- 20d: sample `8`, hit `0.875`, avg `0.035074`, median `0.031658`, mae `0.037455`
- 60d: sample `8`, hit `1.0`, avg `0.077269`, median `0.092646`, mae `0.077269`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005431, 'median_return': 0.004243, 'mean_absolute_return': 0.016669, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.00416, 'median_return': -0.006798, 'mean_absolute_return': 0.018732, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016234, 'median_return': 0.020918, 'mean_absolute_return': 0.02469, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.054167}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.035074, 'median_return': 0.031658, 'mean_absolute_return': 0.037455, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.077269, 'median_return': 0.092646, 'mean_absolute_return': 0.077269, 'max_adverse_excursion': 0.029831, 'max_favorable_excursion': 0.103268}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.004058, 'median_return': 0.006264, 'mean_absolute_return': 0.015821, 'max_adverse_excursion': -0.042672, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.004909, 'median_return': 0.006832, 'mean_absolute_return': 0.017705, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.011923, 'median_return': 0.011198, 'mean_absolute_return': 0.023102, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.018222, 'median_return': 0.019238, 'mean_absolute_return': 0.033514, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.093998}, '60d': {'sample_size': 72, 'hit_rate': 0.8333, 'avg_return': 0.03939, 'median_return': 0.043989, 'mean_absolute_return': 0.05516, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.188184}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.4625}, '10d': {'sample_size': 80, 'hit_rate': 0.35}, '20d': {'sample_size': 80, 'hit_rate': 0.4}, '60d': {'sample_size': 80, 'hit_rate': 0.3}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.4, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.005215, 'median_return': 0.006274, 'mean_absolute_return': 0.015166, 'max_adverse_excursion': -0.042672, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.006832, 'median_return': 0.007479, 'mean_absolute_return': 0.017104, 'max_adverse_excursion': -0.029067, 'max_favorable_excursion': 0.044543}, '10d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.014443, 'median_return': 0.012215, 'mean_absolute_return': 0.023518, 'max_adverse_excursion': -0.052222, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.023895, 'median_return': 0.027343, 'mean_absolute_return': 0.033999, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.093998}, '60d': {'sample_size': 60, 'hit_rate': 0.8667, 'avg_return': 0.042389, 'median_return': 0.052632, 'mean_absolute_return': 0.056262, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.10846}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': 0.001136, 'median_return': -0.00723, 'mean_absolute_return': 0.018126, 'max_adverse_excursion': -0.033574, 'max_favorable_excursion': 0.038776}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.001162, 'median_return': 0.001023, 'mean_absolute_return': 0.01992, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006086, 'median_return': 0.009975, 'mean_absolute_return': 0.022491, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.007945, 'median_return': 0.001802, 'mean_absolute_return': 0.033636, 'max_adverse_excursion': -0.055489, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.045545, 'median_return': 0.04945, 'mean_absolute_return': 0.060698, 'max_adverse_excursion': -0.099346, 'max_favorable_excursion': 0.188184}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.005215`, median `0.006274`, mae `0.015166`
- 5d: sample `60`, hit `0.5833`, avg `0.006832`, median `0.007479`, mae `0.017104`
- 10d: sample `60`, hit `0.6833`, avg `0.014443`, median `0.012215`, mae `0.023518`
- 20d: sample `60`, hit `0.7833`, avg `0.023895`, median `0.027343`, mae `0.033999`
- 60d: sample `60`, hit `0.8667`, avg `0.042389`, median `0.052632`, mae `0.056262`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `0.001136`, median `-0.00723`, mae `0.018126`
- 5d: sample `20`, hit `0.5`, avg `-0.001162`, median `0.001023`, mae `0.01992`
- 10d: sample `20`, hit `0.65`, avg `0.006086`, median `0.009975`, mae `0.022491`
- 20d: sample `20`, hit `0.55`, avg `0.007945`, median `0.001802`, mae `0.033636`
- 60d: sample `20`, hit `0.8`, avg `0.045545`, median `0.04945`, mae `0.060698`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002037`, median `0.006274`, mae `0.012151`
- 5d: sample `20`, hit `0.55`, avg `0.002329`, median `0.006571`, mae `0.014873`
- 10d: sample `20`, hit `0.55`, avg `0.00423`, median `0.007467`, mae `0.021445`
- 20d: sample `20`, hit `0.75`, avg `0.015729`, median `0.020066`, mae `0.030712`
- 60d: sample `20`, hit `0.8`, avg `0.027671`, median `0.041644`, mae `0.050447`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.005974`, median `0.004243`, mae `0.016762`
- 5d: sample `20`, hit `0.45`, avg `0.004551`, median `-0.003328`, mae `0.017981`
- 10d: sample `20`, hit `0.65`, avg `0.017933`, median `0.020918`, mae `0.023126`
- 20d: sample `20`, hit `0.95`, avg `0.03352`, median `0.028791`, mae `0.034473`
- 60d: sample `20`, hit `0.95`, avg `0.072656`, median `0.081091`, mae `0.077488`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002037`, median `0.006274`, mae `0.012151`
- 5d: sample `20`, hit `0.55`, avg `0.002329`, median `0.006571`, mae `0.014873`
- 10d: sample `20`, hit `0.55`, avg `0.00423`, median `0.007467`, mae `0.021445`
- 20d: sample `20`, hit `0.75`, avg `0.015729`, median `0.020066`, mae `0.030712`
- 60d: sample `20`, hit `0.8`, avg `0.027671`, median `0.041644`, mae `0.050447`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.005974`, median `0.004243`, mae `0.016762`
- 5d: sample `20`, hit `0.45`, avg `0.004551`, median `-0.003328`, mae `0.017981`
- 10d: sample `20`, hit `0.65`, avg `0.017933`, median `0.020918`, mae `0.023126`
- 20d: sample `20`, hit `0.95`, avg `0.03352`, median `0.028791`, mae `0.034473`
- 60d: sample `20`, hit `0.95`, avg `0.072656`, median `0.081091`, mae `0.077488`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `0.001136`, median `-0.00723`, mae `0.018126`
- 5d: sample `20`, hit `0.5`, avg `-0.001162`, median `0.001023`, mae `0.01992`
- 10d: sample `20`, hit `0.65`, avg `0.006086`, median `0.009975`, mae `0.022491`
- 20d: sample `20`, hit `0.55`, avg `0.007945`, median `0.001802`, mae `0.033636`
- 60d: sample `20`, hit `0.8`, avg `0.045545`, median `0.04945`, mae `0.060698`

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
- 3d: sample `80`, hit `0.575`, avg `0.004195`, median `0.005785`, mae `0.015906`
- 5d: sample `80`, hit `0.5625`, avg `0.004834`, median `0.006712`, mae `0.017808`
- 10d: sample `80`, hit `0.675`, avg `0.012354`, median `0.011198`, mae `0.023261`
- 20d: sample `80`, hit `0.725`, avg `0.019908`, median `0.024811`, mae `0.033908`
- 60d: sample `80`, hit `0.85`, avg `0.043178`, median `0.04945`, mae `0.057371`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002037`, median `0.006274`, mae `0.012151`
- 5d: sample `20`, hit `0.55`, avg `0.002329`, median `0.006571`, mae `0.014873`
- 10d: sample `20`, hit `0.55`, avg `0.00423`, median `0.007467`, mae `0.021445`
- 20d: sample `20`, hit `0.75`, avg `0.015729`, median `0.020066`, mae `0.030712`
- 60d: sample `20`, hit `0.8`, avg `0.027671`, median `0.041644`, mae `0.050447`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.575`, avg `0.004195`, median `0.005785`, mae `0.015906`
- 5d: sample `80`, hit `0.5625`, avg `0.004834`, median `0.006712`, mae `0.017808`
- 10d: sample `80`, hit `0.675`, avg `0.012354`, median `0.011198`, mae `0.023261`
- 20d: sample `80`, hit `0.725`, avg `0.019908`, median `0.024811`, mae `0.033908`
- 60d: sample `80`, hit `0.85`, avg `0.043178`, median `0.04945`, mae `0.057371`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002037`, median `0.006274`, mae `0.012151`
- 5d: sample `20`, hit `0.55`, avg `0.002329`, median `0.006571`, mae `0.014873`
- 10d: sample `20`, hit `0.55`, avg `0.00423`, median `0.007467`, mae `0.021445`
- 20d: sample `20`, hit `0.75`, avg `0.015729`, median `0.020066`, mae `0.030712`
- 60d: sample `20`, hit `0.8`, avg `0.027671`, median `0.041644`, mae `0.050447`

### risk_path_with_flow_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.575`, avg `0.004195`, median `0.005785`, mae `0.015906`
- 5d: sample `80`, hit `0.5625`, avg `0.004834`, median `0.006712`, mae `0.017808`
- 10d: sample `80`, hit `0.675`, avg `0.012354`, median `0.011198`, mae `0.023261`
- 20d: sample `80`, hit `0.725`, avg `0.019908`, median `0.024811`, mae `0.033908`
- 60d: sample `80`, hit `0.85`, avg `0.043178`, median `0.04945`, mae `0.057371`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
