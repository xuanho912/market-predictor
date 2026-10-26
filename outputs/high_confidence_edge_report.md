# High Confidence Edge Report

Generated at: `2026-10-26T18:44:10.984207+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002037`, median `0.006274`, mae `0.012151`
- 5d: sample `20`, hit `0.55`, avg `0.002329`, median `0.006571`, mae `0.014873`
- 10d: sample `20`, hit `0.55`, avg `0.00423`, median `0.007467`, mae `0.021445`
- 20d: sample `20`, hit `0.75`, avg `0.015729`, median `0.020066`, mae `0.030712`
- 60d: sample `20`, hit `0.8`, avg `0.027671`, median `0.041644`, mae `0.050447`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.00497`, median `0.005785`, mae `0.016798`
- 5d: sample `60`, hit `0.5833`, avg `0.006188`, median `0.009561`, mae `0.018501`
- 10d: sample `60`, hit `0.7`, avg `0.014145`, median `0.011727`, mae `0.023611`
- 20d: sample `60`, hit `0.7`, avg `0.019055`, median `0.024811`, mae `0.033718`
- 60d: sample `60`, hit `0.8333`, avg `0.045948`, median `0.054522`, mae `0.05945`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.002037, 'median_return': 0.006274, 'mean_absolute_return': 0.012151, 'max_adverse_excursion': -0.023751, 'max_favorable_excursion': 0.022499}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.002329, 'median_return': 0.006571, 'mean_absolute_return': 0.014873, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.03068}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.00423, 'median_return': 0.007467, 'mean_absolute_return': 0.021445, 'max_adverse_excursion': -0.052222, 'max_favorable_excursion': 0.059334}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.015729, 'median_return': 0.020066, 'mean_absolute_return': 0.030712, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.027671, 'median_return': 0.041644, 'mean_absolute_return': 0.050447, 'max_adverse_excursion': -0.077263, 'max_favorable_excursion': 0.099148}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005431, 'median_return': 0.004243, 'mean_absolute_return': 0.016669, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.00416, 'median_return': -0.006798, 'mean_absolute_return': 0.018732, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016234, 'median_return': 0.020918, 'mean_absolute_return': 0.02469, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.054167}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.035074, 'median_return': 0.031658, 'mean_absolute_return': 0.037455, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.077269, 'median_return': 0.092646, 'mean_absolute_return': 0.077269, 'max_adverse_excursion': 0.029831, 'max_favorable_excursion': 0.103268}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.004104, 'median_return': 0.006264, 'mean_absolute_return': 0.015522, 'max_adverse_excursion': -0.042672, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.005342, 'median_return': 0.007479, 'mean_absolute_return': 0.017468, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.011159, 'median_return': 0.010559, 'mean_absolute_return': 0.02289, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.016351, 'median_return': 0.018139, 'mean_absolute_return': 0.032468, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.093998}, '60d': {'sample_size': 72, 'hit_rate': 0.8056, 'avg_return': 0.037391, 'median_return': 0.041644, 'mean_absolute_return': 0.054969, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.188184}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.7125}, '60d': {'sample_size': 80, 'hit_rate': 0.7}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.025, 'both_hit': 26, 'both_miss': 14}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.05, 'both_hit': 26, 'both_miss': 14}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.025, 'both_hit': 28, 'both_miss': 12}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.225, 'both_hit': 28, 'both_miss': 12}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.1, 'both_hit': 32, 'both_miss': 8}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.00497, 'median_return': 0.005785, 'mean_absolute_return': 0.016798, 'max_adverse_excursion': -0.042672, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.006188, 'median_return': 0.009561, 'mean_absolute_return': 0.018501, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.014145, 'median_return': 0.011727, 'mean_absolute_return': 0.023611, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.019055, 'median_return': 0.024811, 'mean_absolute_return': 0.033718, 'max_adverse_excursion': -0.055489, 'max_favorable_excursion': 0.093998}, '60d': {'sample_size': 60, 'hit_rate': 0.8333, 'avg_return': 0.045948, 'median_return': 0.054522, 'mean_absolute_return': 0.05945, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.188184}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.002037, 'median_return': 0.006274, 'mean_absolute_return': 0.012151, 'max_adverse_excursion': -0.023751, 'max_favorable_excursion': 0.022499}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.002329, 'median_return': 0.006571, 'mean_absolute_return': 0.014873, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.03068}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.00423, 'median_return': 0.007467, 'mean_absolute_return': 0.021445, 'max_adverse_excursion': -0.052222, 'max_favorable_excursion': 0.059334}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.015729, 'median_return': 0.020066, 'mean_absolute_return': 0.030712, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.027671, 'median_return': 0.041644, 'mean_absolute_return': 0.050447, 'max_adverse_excursion': -0.077263, 'max_favorable_excursion': 0.099148}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.004998`, median `0.006274`, mae `0.01495`
- 5d: sample `60`, hit `0.5833`, avg `0.006528`, median `0.007479`, mae `0.0168`
- 10d: sample `60`, hit `0.6833`, avg `0.014118`, median `0.012215`, mae `0.023193`
- 20d: sample `60`, hit `0.7833`, avg `0.02311`, median `0.027343`, mae `0.033214`
- 60d: sample `60`, hit `0.85`, avg `0.04192`, median `0.052632`, mae `0.056007`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.001952`, median `0.003865`, mae `0.017696`
- 5d: sample `20`, hit `0.55`, avg `0.00131`, median `0.004752`, mae `0.019979`
- 10d: sample `20`, hit `0.6`, avg `0.004311`, median `0.009015`, mae `0.022701`
- 20d: sample `20`, hit `0.5`, avg `0.003566`, median `0.00064`, mae `0.032225`
- 60d: sample `20`, hit `0.75`, avg `0.039755`, median `0.033062`, mae `0.060776`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.004998`, median `0.006274`, mae `0.01495`
- 5d: sample `60`, hit `0.5833`, avg `0.006528`, median `0.007479`, mae `0.0168`
- 10d: sample `60`, hit `0.6833`, avg `0.014118`, median `0.012215`, mae `0.023193`
- 20d: sample `60`, hit `0.7833`, avg `0.02311`, median `0.027343`, mae `0.033214`
- 60d: sample `60`, hit `0.85`, avg `0.04192`, median `0.052632`, mae `0.056007`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.004998`, median `0.006274`, mae `0.01495`
- 5d: sample `60`, hit `0.5833`, avg `0.006528`, median `0.007479`, mae `0.0168`
- 10d: sample `60`, hit `0.6833`, avg `0.014118`, median `0.012215`, mae `0.023193`
- 20d: sample `60`, hit `0.7833`, avg `0.02311`, median `0.027343`, mae `0.033214`
- 60d: sample `60`, hit `0.85`, avg `0.04192`, median `0.052632`, mae `0.056007`

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
- 3d: sample `20`, hit `0.5`, avg `0.001952`, median `0.003865`, mae `0.017696`
- 5d: sample `20`, hit `0.55`, avg `0.00131`, median `0.004752`, mae `0.019979`
- 10d: sample `20`, hit `0.6`, avg `0.004311`, median `0.009015`, mae `0.022701`
- 20d: sample `20`, hit `0.5`, avg `0.003566`, median `0.00064`, mae `0.032225`
- 60d: sample `20`, hit `0.75`, avg `0.039755`, median `0.033062`, mae `0.060776`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002037`, median `0.006274`, mae `0.012151`
- 5d: sample `20`, hit `0.55`, avg `0.002329`, median `0.006571`, mae `0.014873`
- 10d: sample `20`, hit `0.55`, avg `0.00423`, median `0.007467`, mae `0.021445`
- 20d: sample `20`, hit `0.75`, avg `0.015729`, median `0.020066`, mae `0.030712`
- 60d: sample `20`, hit `0.8`, avg `0.027671`, median `0.041644`, mae `0.050447`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.006479`, median `0.008854`, mae `0.016349`
- 5d: sample `40`, hit `0.6`, avg `0.008627`, median `0.012471`, mae `0.017763`
- 10d: sample `40`, hit `0.75`, avg `0.019062`, median `0.020918`, mae `0.024066`
- 20d: sample `40`, hit `0.8`, avg `0.0268`, median `0.028626`, mae `0.034465`
- 60d: sample `40`, hit `0.875`, avg `0.049044`, median `0.056786`, mae `0.058786`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002037`, median `0.006274`, mae `0.012151`
- 5d: sample `20`, hit `0.55`, avg `0.002329`, median `0.006571`, mae `0.014873`
- 10d: sample `20`, hit `0.55`, avg `0.00423`, median `0.007467`, mae `0.021445`
- 20d: sample `20`, hit `0.75`, avg `0.015729`, median `0.020066`, mae `0.030712`
- 60d: sample `20`, hit `0.8`, avg `0.027671`, median `0.041644`, mae `0.050447`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.004237`, median `0.005785`, mae `0.015636`
- 5d: sample `80`, hit `0.575`, avg `0.005223`, median `0.006832`, mae `0.017594`
- 10d: sample `80`, hit `0.6625`, avg `0.011666`, median `0.010559`, mae `0.02307`
- 20d: sample `80`, hit `0.7125`, avg `0.018224`, median `0.020066`, mae `0.032967`
- 60d: sample `80`, hit `0.825`, avg `0.041379`, median `0.048296`, mae `0.057199`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.004998`, median `0.006274`, mae `0.01495`
- 5d: sample `60`, hit `0.5833`, avg `0.006528`, median `0.007479`, mae `0.0168`
- 10d: sample `60`, hit `0.6833`, avg `0.014118`, median `0.012215`, mae `0.023193`
- 20d: sample `60`, hit `0.7833`, avg `0.02311`, median `0.027343`, mae `0.033214`
- 60d: sample `60`, hit `0.85`, avg `0.04192`, median `0.052632`, mae `0.056007`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.004468`, median `0.006264`, mae `0.016816`
- 5d: sample `40`, hit `0.65`, avg `0.007007`, median `0.011107`, mae `0.018761`
- 10d: sample `40`, hit `0.725`, avg `0.012251`, median `0.011727`, mae `0.023854`
- 20d: sample `40`, hit `0.575`, avg `0.011823`, median `0.003824`, mae `0.033341`
- 60d: sample `40`, hit `0.775`, avg `0.032594`, median `0.029229`, mae `0.05043`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
