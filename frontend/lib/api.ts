type HorizonForecast = {
  horizon: string;
  up_probability: number;
  down_probability: number;
  sideways_probability: number;
  expected_return: number;
  max_upside_p50: number;
  max_downside_p50: number;
  confidence: number;
};

type TopReason = {
  title: string;
  layer: string;
  direction: string;
  evidence: string;
  contribution: number;
};

type SimilarDay = {
  date: string;
  similarity: number;
  regime: string;
  forward_20d_return: number;
  max_drawdown_20d: number;
};

type RiskSource = {
  source: string;
  score: number;
  contribution: number;
  evidence: string;
};

export type PredictionSnapshot = {
  forecast_timestamp: string;
  symbol: string;
  market_regime: string;
  model_version: string;
  feature_snapshot_version: string;
  horizons: HorizonForecast[];
  pullback_risk_score: number;
  crisis_risk_score: number;
  bounce_probability: number;
  bounce_quality_score: number;
  downside_continuation_probability: number;
  trend_reversal_probability: number;
  dead_cat_bounce_risk: number;
  top_reasons: TopReason[];
  historical_similar_days: SimilarDay[];
  risk_source_breakdown: RiskSource[];
};

export type AlphaV1Status = {
  signal_name: string;
  signal_version: string;
  status: "NO ALPHA" | "RESEARCH ALPHA CANDIDATE" | "FORWARD-VALIDATED ALPHA CANDIDATE";
  live_signal: boolean;
  threshold: number;
  latest_checked_date: string | null;
  latest_bounce_probability_by_symbol: Record<string, number | null>;
  distance_to_threshold_by_symbol: Record<string, number | null>;
  expected_validation_horizons: string[];
  risk_note: string;
  data_source_status?: string | null;
  signal_blocked_reason?: string | null;
  no_signal: string | null;
  validation_period: string;
};

export type HistoricalAnalogCase = {
  date: string;
  similarity_score: number;
  regime: string;
  bounce_probability: number;
  alpha_v1_triggered: boolean;
  forward_return_5d: number | null;
  forward_return_20d: number | null;
  forward_return_60d: number | null;
  max_adverse_excursion: number | null;
  max_favorable_excursion: number | null;
  key_shared_features: string[];
  key_differences: string[];
};

export type HistoricalAnalogReport = {
  symbol: string;
  as_of: string | null;
  current_regime: string;
  alpha_v1_status: string;
  data_source_status?: string;
  sample_count: number;
  low_sample_warning: boolean;
  current_bounce_probability?: number;
  distance_to_threshold?: number;
  current_alpha_v1_triggered?: boolean;
  top_similar_cases: HistoricalAnalogCase[];
  historical_distribution: Record<string, number | null>;
  interpretation: {
    supports_bounce_alpha: boolean;
    historical_support: "supportive" | "weak_or_conflicting";
    confidence_note: string;
    risk_note: string;
    not_proof_of_alpha: string;
  };
};

export type DataQualityReport = {
  generated_at: string;
  as_of: string | null;
  summary: {
    data_source_status: string;
    real_market_data: boolean;
    finnhub_available?: boolean;
    finnhub_missing?: boolean;
    finnhub_rate_limited?: boolean;
    yahoo_fallback_used?: boolean;
    fred_required?: boolean;
    options_required?: boolean;
    breadth_required?: boolean;
    flow_required?: boolean;
    fallback_used: boolean;
    synthetic_used: boolean;
    stale_data: boolean;
    missing_data: boolean;
    data_completeness_score: number;
    target_completeness_score?: number;
    unavailable_categories: string[];
    missing_key_sources?: string[];
    latest_date: string | null;
    quality_note?: string;
  };
  sources: Record<string, {
    symbol: string;
    source: string;
    status?: "available" | "partial" | "proxy" | "fallback" | "missing" | "stale" | "rate_limited" | "not_available";
    rows: number;
    latest_date: string | null;
    real_data: boolean;
    fallback_used: boolean;
    stale_data: boolean;
    missing_data: boolean;
    point_in_time_safe: boolean;
  }>;
  coverage_categories: Record<string, {
    status: "available" | "partial" | "proxy" | "fallback" | "missing" | "stale" | "rate_limited" | "not_available";
    detail: string;
    available_items: number;
    expected_items: number;
    real_data?: boolean;
    fallback_used?: boolean;
    proxy_used?: boolean;
  }>;
  notes: string[];
};

export type BreadthUniverseStatus = {
  symbol: string;
  name: string;
  is_true_breadth: boolean;
  is_proxy: boolean;
  status: string;
  source: string;
  latest_date: string | null;
  constituents_expected: number | null;
  constituents_used: number | null;
  coverage_ratio: number | null;
  stale_constituents: boolean;
  stale_price_data: boolean;
  missing_ratio?: number | null;
  failed_tickers_sample?: string[];
  stale_tickers_sample?: string[];
  metrics: {
    percent_above_20d: number | null;
    percent_above_50d: number | null;
    percent_above_200d: number | null;
    advancers: number | null;
    decliners: number | null;
    advance_decline_ratio: number | null;
    up_volume_down_volume_ratio: number | null;
    new_highs_20d: number | null;
    new_lows_20d: number | null;
    new_highs_52w: number | null;
    new_lows_52w: number | null;
    percent_above_20d_change_5d: number | null;
    percent_above_50d_change_10d: number | null;
    improvement_acceleration: number | null;
  };
  scores: {
    breadth_improvement_score: number;
    breadth_deterioration_score: number;
    breadth_confirmation_score: number;
    breadth_conflict_score: number;
    breadth_quality_score: number;
  };
  data_note?: string;
};

export type BreadthStatus = {
  provider: string;
  version: string;
  generated_at: string;
  universe_order: string[];
  universes: Record<string, BreadthUniverseStatus>;
  summary: {
    provider_available: boolean;
    true_breadth_available: boolean;
    true_breadth_symbols: string[];
    breadth_proxy_only_symbols: string[];
    stale_data: boolean;
    stale_symbols: string[];
    average_breadth_quality_score: number;
    sector_proxy_available: boolean;
    data_note?: string;
  };
  warnings?: string[];
};

export type MarketStateName =
  | "risk_on"
  | "risk_off"
  | "oversold_bounce"
  | "failed_bounce_risk"
  | "downside_continuation"
  | "sideways"
  | "recovery"
  | "panic"
  | "no_edge";

export type MarketStateV2 = {
  version: string;
  primary_state: MarketStateName;
  states: Record<MarketStateName, {
    probability: number;
    reason: string;
    supporting_features: string[];
    conflicting_features: string[];
    confidence: number;
  }>;
  stress_inputs: Record<string, number>;
};

export type HistoricalSupportByHorizon = {
  by_horizon: Record<string, {
    support: "supportive" | "weak" | "neutral" | "low_sample";
    avg_return: number | null;
    median_return: number | null;
    hit_rate: number | null;
    worst_case: number | null;
    best_case: number | null;
    sample_count: number;
  }>;
  short_term_support: "supportive" | "weak" | "neutral" | "low_sample";
  medium_term_support: "supportive" | "weak" | "neutral" | "low_sample";
  worst_path_risk: "low" | "medium" | "high" | "unknown";
  analog_sample_quality: "low" | "medium" | "high";
  sample_count: number;
  low_sample_warning: boolean;
  historical_analogs_are_not_proof: boolean;
};

export type ModelConfidence = {
  confidence_score: number;
  confidence_level: "low" | "medium" | "high";
  components: Record<string, number>;
  why_confidence_is_limited: string[];
};

export type InternalResonance = {
  resonance_score: number;
  resonance_state: "aligned" | "mixed" | "surface_only" | "weak" | "unknown" | string;
  resonance_label: string;
  resonance_quality_score: number;
  broad_participation: boolean;
  surface_strength_without_participation: boolean;
  supports_bounce_or_repair: boolean;
  supports_downside_or_failed_bounce: boolean;
  components?: Record<string, number | string | boolean | null>;
  reason?: string | null;
  data_note?: string;
};

export type SignalAgreement = {
  signal_agreement_score: number;
  agreement_level: "weak" | "mixed" | "strong";
  supporting_signals: Array<{ name: string; score: number; detail: string }>;
  conflicting_signals: Array<{ name: string; score: number; detail: string }>;
  data_completeness_cap_applied?: boolean;
};

export type SignalConfirmation = {
  confirmation_score: number;
  signal_confirmation_score?: number;
  confirmation_level: "weak" | "mixed" | "strong" | string;
  supporting_evidence: Array<{ name: string; score: number; detail: string }>;
  conflicting_evidence: Array<{ name: string; score: number; detail: string }>;
  missing_evidence: Array<{ name: string; detail: string }>;
  data_completeness_cap_applied?: boolean;
  missing_evidence_cap_applied?: boolean;
};

export type PredictorOutput = {
  probability: number;
  confidence: number;
  main_drivers: string[];
  invalidation_conditions: string[];
  historical_analog_support: string;
  best_horizon: string;
  key_drivers?: string[];
  bounce_probability?: number;
  downside_continuation_probability?: number;
  trend_reversal_probability?: number;
  risk_expansion_probability?: number;
  break_level?: number | null;
  risk_triggers?: string[];
  confirmation_requirements?: string[];
  regime_support?: string;
  credit_risk?: number;
  volatility_risk?: number;
  liquidity_risk?: number;
  macro_event_risk?: number;
};

export type MarketEdgeStatus = {
  market_edge_status: "NO_EDGE" | "WEAK_EDGE" | "MODERATE_EDGE" | "STRONG_EDGE" | "RISK_WARNING";
  has_usable_prediction_edge_today: boolean;
  conditions: Record<string, boolean>;
  passed_conditions: number;
  summary: string;
  no_edge_note?: string;
  risk_warning?: boolean;
};

export type PathWeightModel = {
  base_path_weight: number;
  bounce_path_weight: number;
  bearish_path_weight: number;
  analog_path_weight: number;
  low_confidence_simulation: boolean;
  simulation_confidence_level: "low" | "medium" | "high";
  weight_factors: Record<string, number>;
  weight_source_notes: string[];
};

export type HorizonPredictionV2 = {
  expected_direction: string;
  expected_return: number;
  expected_return_range: [number, number];
  up_probability: number;
  down_probability: number;
  bounce_probability: number;
  failed_bounce_risk: number;
  confidence: number;
  historical_support: string;
};

export type MarketSymbolOverview = {
  symbol: string;
  name: string;
  current_price: number | null;
  market_state: MarketStateName;
  bounce_probability: number;
  downside_continuation_probability: number;
  trend_reversal_probability: number;
  historical_support: "supportive" | "weak_or_conflicting" | "neutral";
  live_signal: boolean;
  distance_to_threshold: number | null;
  as_of: string | null;
  data_source_status?: string | null;
  market_state_v2?: MarketStateV2;
  historical_support_by_horizon?: HistoricalSupportByHorizon;
  model_confidence?: ModelConfidence;
  prediction_horizons?: Record<string, HorizonPredictionV2>;
  current_integrated_judgment?: string;
  feature_snapshot_v2?: Record<string, unknown>;
  feature_snapshot_v3?: Record<string, unknown>;
  signal_agreement?: SignalAgreement;
  signal_confirmation?: SignalConfirmation;
  signal_confirmation_score?: number;
  internal_resonance?: InternalResonance;
  predictors?: Record<string, PredictorOutput>;
  predictors_v4?: Record<string, PredictorOutput>;
  market_edge_status?: MarketEdgeStatus;
  market_intelligence_version?: string;
  path_weight_model?: PathWeightModel;
  base_path_weight?: number;
  bounce_path_weight?: number;
  bearish_path_weight?: number;
  analog_path_weight?: number;
  low_confidence_simulation?: boolean;
  scenario_ranking?: ScenarioRanking;
};

export type ScenarioRankingItem = {
  scenario: "expected_path" | "bounce_path" | "bearish_path" | "analog_average_path" | string;
  label: string;
  probability: number;
  reason: string;
  expected_horizon: string;
  confidence: "low" | "medium" | "high" | string;
};

export type ScenarioRanking = {
  primary: ScenarioRankingItem;
  secondary: ScenarioRankingItem;
  tertiary: ScenarioRankingItem;
  all_scenarios?: ScenarioRankingItem[];
  primary_secondary_gap: number;
  close_call: boolean;
  path_reliability?: "low" | "medium" | "high" | string;
  primary_to_secondary_switch_conditions?: string[];
  ranking_note?: string;
  close_call_note?: string;
};

export type SimulatedSymbolPaths = {
  symbol: string;
  name: string;
  current_price: number | null;
  market_state: string;
  live_signal: boolean;
  bounce_probability: number;
  downside_continuation_probability: number;
  trend_reversal_probability: number;
  historical_support: string;
  market_state_v2?: MarketStateV2;
  historical_support_by_horizon?: HistoricalSupportByHorizon;
  model_confidence?: ModelConfidence;
  prediction_horizons?: Record<string, HorizonPredictionV2>;
  current_integrated_judgment?: string;
  feature_snapshot_v3?: Record<string, unknown>;
  signal_agreement?: SignalAgreement;
  signal_confirmation?: SignalConfirmation;
  signal_confirmation_score?: number;
  internal_resonance?: InternalResonance;
  predictors?: Record<string, PredictorOutput>;
  predictors_v4?: Record<string, PredictorOutput>;
  market_edge_status?: MarketEdgeStatus;
  market_intelligence_version?: string;
  path_weight_model?: PathWeightModel;
  base_path_weight?: number;
  bounce_path_weight?: number;
  bearish_path_weight?: number;
  analog_path_weight?: number;
  low_confidence_simulation?: boolean;
  scenario_ranking?: ScenarioRanking;
  scenario_weights?: Record<string, number>;
  path_confidence?: "low" | "medium" | "high";
  path_source_notes?: string[];
  data_quality?: Record<string, unknown>;
  paths: {
    dates: string[];
    split_index: number;
    historical_price: Array<number | null>;
    expected_path: Array<number | null>;
    bounce_path: Array<number | null>;
    bearish_path: Array<number | null>;
    analog_average_path: Array<number | null>;
    confidence_band_upper: Array<number | null>;
    confidence_band_lower: Array<number | null>;
  };
  horizon_summary: Record<string, {
    expected_return: number;
    up_probability: number;
    down_probability: number;
    risk_note: string;
  }>;
  scenario_cards: Array<{
    name: string;
    name_cn: string;
    summary_cn: string;
    return_20d: number;
    probability_weight: number;
  }>;
  risk_invalidation_conditions: string[];
};

export type PredictionDashboard = {
  generated_by: string;
  source: string;
  as_of: string | null;
  status_note: string;
  data_quality_report?: DataQualityReport;
  breadth_status?: BreadthStatus;
  market_intelligence_v2?: {
    version: string;
    generated_at: string;
    data_quality_report: DataQualityReport;
    feature_snapshot_v2: Record<string, unknown>;
    model_confidence_by_symbol: Record<string, ModelConfidence>;
    warnings: string[];
  };
  market_intelligence_v3?: {
    version: string;
    generated_at: string;
    data_quality_report: DataQualityReport;
    feature_snapshot_v3: Record<string, unknown>;
    signal_agreement_by_symbol: Record<string, SignalAgreement>;
    predictor_outputs_by_symbol: Record<string, Record<string, PredictorOutput>>;
    model_confidence_by_symbol: Record<string, ModelConfidence>;
    edge_status_by_symbol: Record<string, MarketEdgeStatus>;
    high_confidence_signal_report: Record<string, unknown>;
    finnhub_status?: Record<string, unknown>;
    warnings: string[];
  };
  market_intelligence_v4?: {
    version: string;
    generated_at: string;
    data_quality_report: DataQualityReport;
    signal_confirmation_by_symbol: Record<string, SignalConfirmation>;
    predictor_outputs_by_symbol: Record<string, Record<string, PredictorOutput>>;
    model_confidence_by_symbol: Record<string, ModelConfidence>;
    edge_status_by_symbol: Record<string, MarketEdgeStatus>;
    high_confidence_edge_report: Record<string, unknown>;
    finnhub_status?: Record<string, unknown>;
    warnings: string[];
  };
  feature_snapshot_v2?: Record<string, unknown>;
  feature_snapshot_v3?: Record<string, unknown>;
  model_confidence_by_symbol?: Record<string, ModelConfidence>;
  high_confidence_signal_report?: Record<string, unknown>;
  high_confidence_edge_report?: Record<string, unknown>;
  overview: {
    as_of: string | null;
    strongest_symbol: string;
    dashboard_status: string;
    status_note: string;
    symbols: Record<string, MarketSymbolOverview>;
    data_quality_summary?: Record<string, unknown>;
    model_confidence_by_symbol?: Record<string, ModelConfidence>;
    signal_agreement_by_symbol?: Record<string, SignalAgreement>;
    edge_status_by_symbol?: Record<string, MarketEdgeStatus>;
  };
  simulated_paths: {
    as_of: string | null;
    disclaimer: string;
    symbols: Record<string, SimulatedSymbolPaths>;
    data_quality_summary?: Record<string, unknown>;
  };
  alpha_status: AlphaV1Status;
  forward_report: unknown;
  analogs: Record<string, HistoricalAnalogReport>;
};

const fallbackPrediction: PredictionSnapshot = {
  forecast_timestamp: new Date().toISOString(),
  symbol: "SPY",
  market_regime: "unknown",
  model_version: "frontend-fallback",
  feature_snapshot_version: "frontend-fallback",
  horizons: ["1d", "3d", "5d", "10d", "20d", "60d"].map((horizon) => ({
    horizon,
    up_probability: 0,
    down_probability: 0,
    sideways_probability: 1,
    expected_return: 0,
    max_upside_p50: 0,
    max_downside_p50: 0,
    confidence: 0,
  })),
  pullback_risk_score: 0,
  crisis_risk_score: 0,
  bounce_probability: 0,
  bounce_quality_score: 0,
  downside_continuation_probability: 0,
  trend_reversal_probability: 0,
  dead_cat_bounce_risk: 0,
  top_reasons: [],
  historical_similar_days: [],
  risk_source_breakdown: [],
};

const fallbackAlphaV1Status: AlphaV1Status = {
  signal_name: "bounce_probability_top_decile_v1",
  signal_version: "alpha_v1",
  status: "RESEARCH ALPHA CANDIDATE",
  live_signal: false,
  threshold: 0.32534311,
  latest_checked_date: null,
  latest_bounce_probability_by_symbol: {},
  distance_to_threshold_by_symbol: {},
  expected_validation_horizons: ["3d", "5d", "10d", "20d", "60d"],
  risk_note: "Research alpha candidate only. Forward-only observation; not paper trading and not live trading.",
  data_source_status: "unknown",
  signal_blocked_reason: null,
  no_signal: "no live signal",
  validation_period: "forward_only",
};

const fallbackHistoricalAnalogReport: HistoricalAnalogReport = {
  symbol: "SPY",
  as_of: null,
  current_regime: "unknown",
  alpha_v1_status: "RESEARCH ALPHA CANDIDATE",
  data_source_status: "unknown",
  sample_count: 0,
  low_sample_warning: true,
  top_similar_cases: [],
  historical_distribution: { sample_count: 0 },
  interpretation: {
    supports_bounce_alpha: false,
    historical_support: "weak_or_conflicting",
    confidence_note: "Historical analog data is unavailable.",
    risk_note: "Historical analogs are not proof of alpha.",
    not_proof_of_alpha: "Historical analogs are not proof of alpha.",
  },
};

const fallbackDashboard: PredictionDashboard = {
  generated_by: "frontend-fallback",
  source: "frontend-fallback",
  as_of: null,
  status_note: "暂无可用的预测面板数据。",
  overview: {
    as_of: null,
    strongest_symbol: "SPY",
    dashboard_status: "no_data",
    status_note: "暂无可用的预测面板数据。",
    symbols: {},
  },
  simulated_paths: {
    as_of: null,
    disclaimer: "模拟路径是概率情景，不是确定性预测。",
    symbols: {},
  },
  alpha_status: fallbackAlphaV1Status,
  forward_report: null,
  analogs: {},
};

const staticDataBaseUrl =
  process.env.NEXT_PUBLIC_STATIC_DATA_BASE_URL ??
  "https://raw.githubusercontent.com/xuanho912/market-predictor/main/frontend/public";

export async function getLatestPrediction(symbol = "SPY"): Promise<PredictionSnapshot> {
  const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL;
  if (!baseUrl) {
    return { ...fallbackPrediction, symbol };
  }
  try {
    const response = await fetch(`${baseUrl}/api/prediction/latest?symbol=${symbol}`, {
      next: { revalidate: 60 },
    });
    if (!response.ok) {
      return fallbackPrediction;
    }
    return response.json();
  } catch {
    return fallbackPrediction;
  }
}

export async function getAlphaV1Status(): Promise<AlphaV1Status> {
  const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL;
  if (!baseUrl) {
    return getStaticAlphaV1Status();
  }
  try {
    const response = await fetch(`${baseUrl}/api/alpha/v1/status`, {
      next: { revalidate: 60 },
    });
    if (!response.ok) {
      return getStaticAlphaV1Status();
    }
    return response.json();
  } catch {
    return getStaticAlphaV1Status();
  }
}

export async function getAlphaV1Analogs(symbol = "SPY"): Promise<HistoricalAnalogReport> {
  const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL;
  if (!baseUrl) {
    return getStaticAlphaV1Analogs(symbol);
  }
  try {
    const response = await fetch(`${baseUrl}/api/analogs/alpha-v1?symbol=${symbol}&top_k=20`, {
      next: { revalidate: 300 },
    });
    if (!response.ok) {
      return getStaticAlphaV1Analogs(symbol);
    }
    return response.json();
  } catch {
    return getStaticAlphaV1Analogs(symbol);
  }
}

export async function getPredictionDashboard(): Promise<PredictionDashboard> {
  const localPayload = await readLocalStaticJson<PredictionDashboard>("prediction-dashboard.json");
  if (localPayload?.overview?.symbols) {
    return localPayload;
  }
  try {
    const response = await fetch(`${staticDataBaseUrl}/prediction-dashboard.json`, {
      next: { revalidate: 300 },
    });
    if (!response.ok) {
      return fallbackDashboard;
    }
    return response.json();
  } catch {
    return fallbackDashboard;
  }
}

async function getStaticAlphaV1Status(): Promise<AlphaV1Status> {
  try {
    const localPayload = await readLocalStaticJson<{ alpha_status?: AlphaV1Status }>("alpha-v1-status.json");
    if (localPayload?.alpha_status) {
      return localPayload.alpha_status;
    }
    const response = await fetch(`${staticDataBaseUrl}/alpha-v1-status.json`, {
      next: { revalidate: 300 },
    });
    if (!response.ok) {
      return fallbackAlphaV1Status;
    }
    const payload = await response.json();
    return payload.alpha_status ?? fallbackAlphaV1Status;
  } catch {
    return fallbackAlphaV1Status;
  }
}

async function getStaticAlphaV1Analogs(symbol = "SPY"): Promise<HistoricalAnalogReport> {
  try {
    const localPayload = await readLocalStaticJson<{ analogs?: Record<string, HistoricalAnalogReport> }>("alpha-v1-analogs.json");
    if (localPayload?.analogs?.[symbol]) {
      return localPayload.analogs[symbol];
    }
    const response = await fetch(`${staticDataBaseUrl}/alpha-v1-analogs.json`, {
      next: { revalidate: 300 },
    });
    if (!response.ok) {
      return { ...fallbackHistoricalAnalogReport, symbol };
    }
    const payload = await response.json();
    return payload.analogs?.[symbol] ?? { ...fallbackHistoricalAnalogReport, symbol };
  } catch {
    return { ...fallbackHistoricalAnalogReport, symbol };
  }
}

async function readLocalStaticJson<T>(filename: string): Promise<T | null> {
  if (typeof window !== "undefined") {
    return null;
  }
  try {
    const fs = await import("node:fs/promises");
    const path = await import("node:path");
    const filePath = path.join(process.cwd(), "public", filename);
    const text = await fs.readFile(filePath, "utf-8");
    return JSON.parse(text) as T;
  } catch {
    return null;
  }
}
