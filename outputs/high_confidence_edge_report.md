# High Confidence Edge Report

Generated at: `2026-10-08T01:23:38.316963+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `84`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `84`, gate `moderate_evidence`
- 5d: completed `84`, gate `moderate_evidence`
- 10d: completed `84`, gate `moderate_evidence`
- 20d: completed `84`, gate `moderate_evidence`
- 60d: completed `84`, gate `moderate_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.00044`, median `0.002957`, mae `0.015092`
- 5d: sample `60`, hit `0.4833`, avg `0.000581`, median `-0.003262`, mae `0.018133`
- 10d: sample `60`, hit `0.6333`, avg `0.005338`, median `0.004196`, mae `0.017623`
- 20d: sample `60`, hit `0.85`, avg `0.034166`, median `0.032299`, mae `0.03786`
- 60d: sample `60`, hit `0.9333`, avg `0.086436`, median `0.099719`, mae `0.091678`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.008586`, median `-0.010335`, mae `0.018081`
- 5d: sample `20`, hit `0.35`, avg `-0.005507`, median `-0.005632`, mae `0.017963`
- 10d: sample `20`, hit `0.4`, avg `-0.003067`, median `-0.006032`, mae `0.031119`
- 20d: sample `20`, hit `0.45`, avg `-0.008393`, median `-0.009713`, mae `0.047912`
- 60d: sample `20`, hit `0.85`, avg `0.094735`, median `0.114377`, mae `0.109763`

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
- 3d: sample `8`, hit `0.625`, avg `0.000456`, median `0.003757`, mae `0.012601`
- 5d: sample `8`, hit `0.5`, avg `-0.000705`, median `0.007948`, mae `0.014293`
- 10d: sample `8`, hit `0.625`, avg `0.00041`, median `0.011031`, mae `0.02198`
- 20d: sample `8`, hit `0.75`, avg `0.033377`, median `0.043456`, mae `0.039686`
- 60d: sample `8`, hit `1.0`, avg `0.107041`, median `0.109494`, mae `0.107041`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.000456`, median `0.003757`, mae `0.012601`
- 5d: sample `8`, hit `0.5`, avg `-0.000705`, median `0.007948`, mae `0.014293`
- 10d: sample `8`, hit `0.625`, avg `0.00041`, median `0.011031`, mae `0.02198`
- 20d: sample `8`, hit `0.75`, avg `0.033377`, median `0.043456`, mae `0.039686`
- 60d: sample `8`, hit `1.0`, avg `0.107041`, median `0.109494`, mae `0.107041`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.00044, 'median_return': 0.002957, 'mean_absolute_return': 0.015092, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.037236}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': 0.000581, 'median_return': -0.003262, 'mean_absolute_return': 0.018133, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.005338, 'median_return': 0.004196, 'mean_absolute_return': 0.017623, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.85, 'avg_return': 0.034166, 'median_return': 0.032299, 'mean_absolute_return': 0.03786, 'max_adverse_excursion': -0.026142, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.9333, 'avg_return': 0.086436, 'median_return': 0.099719, 'mean_absolute_return': 0.091678, 'max_adverse_excursion': -0.078345, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.000456, 'median_return': 0.003757, 'mean_absolute_return': 0.012601, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.000705, 'median_return': 0.007948, 'mean_absolute_return': 0.014293, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.00041, 'median_return': 0.011031, 'mean_absolute_return': 0.02198, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.033377, 'median_return': 0.043456, 'mean_absolute_return': 0.039686, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.107041, 'median_return': 0.109494, 'mean_absolute_return': 0.107041, 'max_adverse_excursion': 0.084301, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.002069, 'median_return': -0.001227, 'mean_absolute_return': 0.016199, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.000967, 'median_return': -0.004957, 'mean_absolute_return': 0.018512, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.003551, 'median_return': 0.003921, 'mean_absolute_return': 0.020888, 'max_adverse_excursion': -0.053986, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.022432, 'median_return': 0.029348, 'mean_absolute_return': 0.040449, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.9028, 'avg_return': 0.086452, 'median_return': 0.10344, 'mean_absolute_return': 0.094995, 'max_adverse_excursion': -0.099444, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.625}, '20d': {'sample_size': 80, 'hit_rate': 0.775}, '60d': {'sample_size': 80, 'hit_rate': 0.7375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.05, 'both_hit': 25, 'both_miss': 15}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.025, 'both_hit': 23, 'both_miss': 17}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.025, 'both_hit': 29, 'both_miss': 11}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.775, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': 0.25, 'both_hit': 32, 'both_miss': 8}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.7375, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': 0.025, 'both_hit': 38, 'both_miss': 2}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.00044, 'median_return': 0.002957, 'mean_absolute_return': 0.015092, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.037236}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': 0.000581, 'median_return': -0.003262, 'mean_absolute_return': 0.018133, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.005338, 'median_return': 0.004196, 'mean_absolute_return': 0.017623, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.85, 'avg_return': 0.034166, 'median_return': 0.032299, 'mean_absolute_return': 0.03786, 'max_adverse_excursion': -0.026142, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.9333, 'avg_return': 0.086436, 'median_return': 0.099719, 'mean_absolute_return': 0.091678, 'max_adverse_excursion': -0.078345, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.008586, 'median_return': -0.010335, 'mean_absolute_return': 0.018081, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.005507, 'median_return': -0.005632, 'mean_absolute_return': 0.017963, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.003067, 'median_return': -0.006032, 'mean_absolute_return': 0.031119, 'max_adverse_excursion': -0.053986, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.008393, 'median_return': -0.009713, 'mean_absolute_return': 0.047912, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.067793}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.094735, 'median_return': 0.114377, 'mean_absolute_return': 0.109763, 'max_adverse_excursion': -0.099444, 'max_favorable_excursion': 0.176653}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00829`, median `0.012813`, mae `0.016125`
- 5d: sample `20`, hit `0.65`, avg `0.009507`, median `0.010241`, mae `0.019037`
- 10d: sample `20`, hit `0.75`, avg `0.012823`, median `0.013997`, mae `0.022479`
- 20d: sample `20`, hit `0.8`, avg `0.038432`, median `0.03801`, mae `0.042231`
- 60d: sample `20`, hit `0.95`, avg `0.095195`, median `0.099838`, mae `0.099791`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.0075`, median `-0.010023`, mae `0.017915`
- 5d: sample `40`, hit `0.325`, avg `-0.006024`, median `-0.010111`, mae `0.019397`
- 10d: sample `40`, hit `0.425`, avg `-0.001292`, median `-0.004767`, mae `0.024136`
- 20d: sample `40`, hit `0.7`, avg `0.013785`, median `0.027885`, mae `0.042103`
- 60d: sample `40`, hit `0.875`, avg `0.084123`, median `0.11278`, mae `0.096161`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00829`, median `0.012813`, mae `0.016125`
- 5d: sample `20`, hit `0.65`, avg `0.009507`, median `0.010241`, mae `0.019037`
- 10d: sample `20`, hit `0.75`, avg `0.012823`, median `0.013997`, mae `0.022479`
- 20d: sample `20`, hit `0.8`, avg `0.038432`, median `0.03801`, mae `0.042231`
- 60d: sample `20`, hit `0.95`, avg `0.095195`, median `0.099838`, mae `0.099791`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.006414`, median `-0.003676`, mae `0.017749`
- 5d: sample `20`, hit `0.3`, avg `-0.006541`, median `-0.0117`, mae `0.020832`
- 10d: sample `20`, hit `0.45`, avg `0.000483`, median `-0.00027`, mae `0.017152`
- 20d: sample `20`, hit `0.95`, avg `0.035963`, median `0.029298`, mae `0.036294`
- 60d: sample `20`, hit `0.9`, avg `0.073511`, median `0.075128`, mae `0.08256`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.006414`, median `-0.003676`, mae `0.017749`
- 5d: sample `20`, hit `0.3`, avg `-0.006541`, median `-0.0117`, mae `0.020832`
- 10d: sample `20`, hit `0.45`, avg `0.000483`, median `-0.00027`, mae `0.017152`
- 20d: sample `20`, hit `0.95`, avg `0.035963`, median `0.029298`, mae `0.036294`
- 60d: sample `20`, hit `0.9`, avg `0.073511`, median `0.075128`, mae `0.08256`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00829`, median `0.012813`, mae `0.016125`
- 5d: sample `20`, hit `0.65`, avg `0.009507`, median `0.010241`, mae `0.019037`
- 10d: sample `20`, hit `0.75`, avg `0.012823`, median `0.013997`, mae `0.022479`
- 20d: sample `20`, hit `0.8`, avg `0.038432`, median `0.03801`, mae `0.042231`
- 60d: sample `20`, hit `0.95`, avg `0.095195`, median `0.099838`, mae `0.099791`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003485`, median `-0.002225`, mae `0.014575`
- 5d: sample `40`, hit `0.4`, avg `-0.003882`, median `-0.010111`, mae `0.017681`
- 10d: sample `40`, hit `0.575`, avg `0.001596`, median `0.003262`, mae `0.015195`
- 20d: sample `40`, hit `0.875`, avg `0.032032`, median `0.032102`, mae `0.035674`
- 60d: sample `40`, hit `0.925`, avg `0.082056`, median `0.092194`, mae `0.087622`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.008586`, median `-0.010335`, mae `0.018081`
- 5d: sample `20`, hit `0.35`, avg `-0.005507`, median `-0.005632`, mae `0.017963`
- 10d: sample `20`, hit `0.4`, avg `-0.003067`, median `-0.006032`, mae `0.031119`
- 20d: sample `20`, hit `0.45`, avg `-0.008393`, median `-0.009713`, mae `0.047912`
- 60d: sample `20`, hit `0.85`, avg `0.094735`, median `0.114377`, mae `0.109763`

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
- 3d: sample `80`, hit `0.4875`, avg `-0.001816`, median `-0.001058`, mae `0.015839`
- 5d: sample `80`, hit `0.45`, avg `-0.000941`, median `-0.003796`, mae `0.01809`
- 10d: sample `80`, hit `0.575`, avg `0.003237`, median `0.003921`, mae `0.020997`
- 20d: sample `80`, hit `0.75`, avg `0.023526`, median `0.031464`, mae `0.040373`
- 60d: sample `80`, hit `0.9125`, avg `0.088511`, median `0.10344`, mae `0.096199`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.00044`, median `0.002957`, mae `0.015092`
- 5d: sample `60`, hit `0.4833`, avg `0.000581`, median `-0.003262`, mae `0.018133`
- 10d: sample `60`, hit `0.6333`, avg `0.005338`, median `0.004196`, mae `0.017623`
- 20d: sample `60`, hit `0.85`, avg `0.034166`, median `0.032299`, mae `0.03786`
- 60d: sample `60`, hit `0.9333`, avg `0.086436`, median `0.099719`, mae `0.091678`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4875`, avg `-0.001816`, median `-0.001058`, mae `0.015839`
- 5d: sample `80`, hit `0.45`, avg `-0.000941`, median `-0.003796`, mae `0.01809`
- 10d: sample `80`, hit `0.575`, avg `0.003237`, median `0.003921`, mae `0.020997`
- 20d: sample `80`, hit `0.75`, avg `0.023526`, median `0.031464`, mae `0.040373`
- 60d: sample `80`, hit `0.9125`, avg `0.088511`, median `0.10344`, mae `0.096199`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.00044`, median `0.002957`, mae `0.015092`
- 5d: sample `60`, hit `0.4833`, avg `0.000581`, median `-0.003262`, mae `0.018133`
- 10d: sample `60`, hit `0.6333`, avg `0.005338`, median `0.004196`, mae `0.017623`
- 20d: sample `60`, hit `0.85`, avg `0.034166`, median `0.032299`, mae `0.03786`
- 60d: sample `60`, hit `0.9333`, avg `0.086436`, median `0.099719`, mae `0.091678`

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
