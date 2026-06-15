"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import type { MouseEvent, ReactNode } from "react";
import type {
  CompactForecastPriceLevel,
  DataFreshnessStatus,
  ForecastPriceLevel,
  ForecastPriceLevelsBySymbol,
  HistoricalAnalogCase,
  PredictionDashboard,
  ScenarioRankingItem,
  SimulatedSymbolPaths,
} from "../lib/api";

const SYMBOL_ORDER = ["SPY", "QQQ", "IWM", "DIA"];
const PRICE_LEVEL_HORIZON_ORDER = ["1d", "3d", "5d", "10d", "20d", "60d"];
const HORIZON_ORDER = ["3d", "5d", "10d", "20d", "60d"];

const SCENARIO_LABELS: Record<string, string> = {
  bounce_path: "反抽情景",
  bearish_path: "失败反抽风险",
  expected_path: "综合期望路径",
  analog_average_path: "历史均值情景",

  stock_bounce: "个股反抽",
  stock_trend_repair: "个股趋势修复",
  stock_downside_continuation: "个股下跌延续",
  stock_failed_bounce: "个股失败反抽",
  stock_sideways: "个股震荡",
  stock_event_risk: "个股事件风险",
  stock_breakout: "个股突破",
  stock_breakdown: "个股跌破",
};

const SCENARIO_STROKES: Record<string, string> = {
  historical_price: "#d7e4e1",
  expected_path: "#38bdf8",
  bounce_path: "#22c55e",
  bearish_path: "#f87171",
  analog_average_path: "#f59e0b",
};

const SCENARIO_NAMES: Record<string, string> = {
  historical_price: "历史价格",
  expected_path: "综合期望",
  bounce_path: "反抽情景",
  bearish_path: "风险路径",
  analog_average_path: "历史均值",
};

type PathSeriesKey =
  | "historical_price"
  | "expected_path"
  | "bounce_path"
  | "bearish_path"
  | "analog_average_path";

type TooltipState = {
  index: number;
  left: number;
  top: number;
} | null;

type AnyRecord = Record<string, unknown>;

function isRecord(value: unknown): value is AnyRecord {
  return Boolean(value) && typeof value === "object" && !Array.isArray(value);
}

function asRecord(value: unknown): AnyRecord {
  return isRecord(value) ? value : {};
}

function asStringArray(value: unknown): string[] {
  return Array.isArray(value) ? value.filter((item): item is string => typeof item === "string") : [];
}

function asNumber(value: unknown): number | null {
  return typeof value === "number" && Number.isFinite(value) ? value : null;
}

function formatPrice(value: unknown): string {
  const n = asNumber(value);
  return n === null ? "数据缺失" : n.toFixed(2);
}

function formatPercent(value: unknown, digits = 0): string {
  const n = asNumber(value);
  return n === null ? "数据缺失" : `${(n * 100).toFixed(digits)}%`;
}

function formatSignedPercent(value: unknown, digits = 1): string {
  const n = asNumber(value);
  if (n === null) return "数据缺失";
  const sign = n > 0 ? "+" : "";
  return `${sign}${(n * 100).toFixed(digits)}%`;
}

function formatScore(value: unknown): string {
  const n = asNumber(value);
  return n === null ? "数据缺失" : `${Math.round(n)}/100`;
}

function formatGap(value: unknown): string {
  const n = asNumber(value);
  return n === null ? "数据缺失" : `${(n * 100).toFixed(1)} 个百分点`;
}

function cnSource(value: string | undefined): string {
  const map: Record<string, string> = {
    simulated_path: "路径模型",
    price_structure: "价格结构",
    volatility_band: "波动区间",
    confluence: "多来源共振",
    data_missing: "数据缺失",
  };
  return value ? map[value] ?? value : "数据缺失";
}

function shortDate(value: string | null | undefined): string {
  if (!value) return "数据缺失";
  return value.slice(0, 10);
}

function cnScenario(value: string | undefined): string {
  if (!value) return "数据缺失";
  return SCENARIO_LABELS[value] ?? value;
}

function cnCandidateType(value: string | undefined): string {
  const map: Record<string, string> = {
    upside_momentum: "上行动量",
    oversold_bounce: "超跌反抽",
    high_volatility_watch: "高波动观察",
    event_driven_move: "事件驱动",
    gap_continuation: "跳空延续",
    short_squeeze_proxy: "挤压代理",
    failed_bounce_risk: "失败反抽风险",
    downside_continuation: "下跌延续",
    no_edge: "暂无优势",
  };
  return value ? map[value] ?? value : "数据缺失";
}

function cnRadarLevel(value: string | undefined): string {
  const map: Record<string, string> = {
    NO_EDGE: "暂无优势",
    WATCH: "观察",
    MODERATE_OPPORTUNITY: "中等机会",
    HIGH_ELASTICITY: "高弹性",
    HIGH_RISK_HIGH_VOLATILITY: "高风险高波动",
  };
  return value ? map[value] ?? value : "数据缺失";
}

function formatPriceRange(value: unknown): string {
  const record = asRecord(value);
  const low = asNumber(record.low);
  const high = asNumber(record.high);
  if (low === null || high === null) return "数据缺失";
  return `${low.toFixed(2)} - ${high.toFixed(2)}`;
}

function cnEdgeStatus(value: string | undefined): string {
  const map: Record<string, string> = {
    STRONG_EDGE: "强预测优势",
    MODERATE_EDGE: "中等预测优势",
    WEAK_EDGE: "弱预测优势",
    NO_EDGE: "暂无预测优势",
    RISK_WARNING: "风险警报",
  };
  return value ? map[value] ?? value : "数据缺失";
}

function cnValidationStatus(value: string | undefined): string {
  const map: Record<string, string> = {
    not_yet_validated: "尚未验证",
    insufficient_samples: "样本不足",
    insufficient_forward_samples: "前向样本不足",
    insufficient_forward_evidence: "前向证据不足",
    historical_only_not_validated: "仅历史证据",
    promotion_candidate: "候选升级",
    active_model: "当前基准模型",
  };
  return value ? map[value] ?? value : "尚未验证";
}

function cnNarrativeDirection(value: string | undefined): string {
  const map: Record<string, string> = {
    supports_bounce: "支持反抽",
    supports_downside: "支持下跌延续",
    supports_trend_reversal: "支持趋势修复",
    supports_risk_expansion: "支持风险扩散",
    mixed: "混合",
  };
  return value ? map[value] ?? value : "数据缺失";
}

function cnEventCondition(value: string | undefined): string {
  const map: Record<string, string> = {
    geopolitical_risk_easing: "地缘风险缓和",
    geopolitical_risk_escalation: "地缘风险升级",
    oil_shock_relief: "油价压力释放",
    oil_shock_risk: "油价冲击风险",
    equity_futures_rally: "股指期货上涨",
    equity_futures_selloff: "股指期货走弱",
  };
  return value ? map[value] ?? value : "未知事件线索";
}

function badgeClass(status: string | undefined): string {
  const normalized = (status ?? "").toLowerCase();
  if (normalized.includes("strong_edge") || normalized.includes("support") || normalized.includes("active_model")) {
    return "border-emerald-400/35 bg-emerald-400/10 text-emerald-200";
  }
  if (normalized.includes("high_conviction") || normalized.includes("strong")) {
    return "border-emerald-400/35 bg-emerald-400/10 text-emerald-200";
  }
  if (normalized.includes("moderate") || normalized.includes("mixed") || normalized.includes("candidate")) {
    return "border-cyan-400/35 bg-cyan-400/10 text-cyan-200";
  }
  if (normalized.includes("watch") || normalized.includes("warning")) {
    return "border-amber-400/35 bg-amber-400/10 text-amber-200";
  }
  if (normalized.includes("weak") || normalized.includes("not_yet") || normalized.includes("insufficient")) {
    return "border-amber-400/35 bg-amber-400/10 text-amber-200";
  }
  if (normalized.includes("risk") || normalized.includes("conflict") || normalized.includes("failed") || normalized.includes("extreme")) {
    return "border-rose-400/35 bg-rose-400/10 text-rose-200";
  }
  return "border-white/15 bg-white/5 text-slate-300";
}

function getSymbols(dashboard: PredictionDashboard): Record<string, SimulatedSymbolPaths> {
  return dashboard.simulated_paths?.symbols ?? {};
}

function getSymbolList(dashboard: PredictionDashboard): SimulatedSymbolPaths[] {
  const symbols = getSymbols(dashboard);
  return SYMBOL_ORDER.map((symbol) => symbols[symbol]).filter(Boolean);
}

function getEdgeStatus(symbolData: SimulatedSymbolPaths | undefined): string {
  return symbolData?.market_edge_status?.market_edge_status ?? "NO_EDGE";
}

function getConfirmationScore(symbolData: SimulatedSymbolPaths | undefined): number | null {
  return (
    asNumber(symbolData?.signal_confirmation?.signal_confirmation_score) ??
    asNumber(symbolData?.signal_confirmation?.confirmation_score) ??
    asNumber(symbolData?.signal_confirmation_score)
  );
}

function getConfidenceScore(symbolData: SimulatedSymbolPaths | undefined): number | null {
  return asNumber(symbolData?.model_confidence?.confidence_score);
}

function getPrimary(symbolData: SimulatedSymbolPaths | undefined): ScenarioRankingItem | undefined {
  return symbolData?.scenario_ranking?.primary;
}

function getSecondary(symbolData: SimulatedSymbolPaths | undefined): ScenarioRankingItem | undefined {
  return symbolData?.scenario_ranking?.secondary;
}

function getTertiary(symbolData: SimulatedSymbolPaths | undefined): ScenarioRankingItem | undefined {
  return symbolData?.scenario_ranking?.tertiary;
}

function getScenarioProbability(symbolData: SimulatedSymbolPaths, scenario: string): number | null {
  const ranking = symbolData.scenario_ranking;
  const item = ranking?.all_scenarios?.find((entry) => entry.scenario === scenario);
  return (
    asNumber(item?.probability) ??
    (ranking?.primary?.scenario === scenario ? asNumber(ranking.primary.probability) : null) ??
    (ranking?.secondary?.scenario === scenario ? asNumber(ranking.secondary.probability) : null) ??
    (ranking?.tertiary?.scenario === scenario ? asNumber(ranking.tertiary.probability) : null)
  );
}

function getScenarioRank(symbolData: SimulatedSymbolPaths, scenario: string): string {
  const ranking = symbolData.scenario_ranking;
  if (ranking?.primary?.scenario === scenario) return "第一可能";
  if (ranking?.secondary?.scenario === scenario) return "第二可能";
  if (ranking?.tertiary?.scenario === scenario) return "风险路径";
  return "参考路径";
}

function getLineWidth(symbolData: SimulatedSymbolPaths, scenario: PathSeriesKey): number {
  if (scenario === "historical_price") return 2.6;
  const closeCall = Boolean(symbolData.scenario_ranking?.close_call);
  const ranking = symbolData.scenario_ranking;
  if (ranking?.primary?.scenario === scenario) return closeCall ? 3.2 : 4.8;
  if (ranking?.secondary?.scenario === scenario) return closeCall ? 3.0 : 3.2;
  if (ranking?.tertiary?.scenario === scenario) return 2.2;
  return 1.8;
}

function getSummarySentence(dashboard: PredictionDashboard, selected: SimulatedSymbolPaths | undefined): string {
  if (!selected) return "当前没有可展示的预测数据。";
  const symbols = getSymbolList(dashboard);
  const supportive = symbols
    .filter((item) => ["STRONG_EDGE", "MODERATE_EDGE"].includes(getEdgeStatus(item)))
    .map((item) => item.symbol);
  const conflicting = symbols
    .filter((item) => getEdgeStatus(item) === "RISK_WARNING" || item.scenario_ranking?.close_call)
    .map((item) => item.symbol);
  const primary = getPrimary(selected);
  const secondary = getSecondary(selected);
  const validated = getValidationStandards(dashboard);
  const validation = cnValidationStatus(validated.highPrecisionStatus);
  const supportText = supportive.length ? `${supportive.join(" / ")} 的路径支持较强` : "当前强支持指数有限";
  const conflictText = conflicting.length ? `${conflicting.join(" / ")} 存在分歧或风险提示` : "暂未出现明显路径分歧";

  return `当前主路径偏向${primary?.label ?? cnScenario(primary?.scenario)}，第二路径为${secondary?.label ?? cnScenario(secondary?.scenario)}。${supportText}，${conflictText}。模型状态：${validation}，仍以概率路径和前向验证为准。`;
}

function getValidationStandards(dashboard: PredictionDashboard) {
  const leaderboard = asRecord(dashboard.model_leaderboard);
  const standards = asRecord(leaderboard.validation_standards ?? asRecord(dashboard.model_promotion_status).validation_standards);
  const highPrecision = asRecord(standards.high_precision_standard);
  const stableAlpha = asRecord(standards.stable_alpha_standard);
  const validated = asRecord(standards.validated_forecasting_system_standard);
  const completed = asRecord(standards.forward_completed_samples_by_horizon);
  return {
    activeModel: String(leaderboard.active_model_version ?? asRecord(dashboard.model_promotion_status).active_model_version ?? "baseline_v1"),
    highPrecisionStatus: String(highPrecision.status ?? "not_yet_validated"),
    stableAlphaStatus: String(stableAlpha.status ?? "not_yet_validated"),
    validatedStatus: String(validated.status ?? "not_yet_validated"),
    completed,
  };
}

function getDataFreshnessStatus(dashboard: PredictionDashboard): DataFreshnessStatus | undefined {
  return dashboard.data_freshness_status;
}

function isDataStaleOrFailed(status: DataFreshnessStatus | undefined): boolean {
  const value = status?.data_freshness_status;
  return value === "stale" || value === "provider_failed";
}

function cnFreshnessStatus(value: string | undefined): string {
  const map: Record<string, string> = {
    fresh: "数据新鲜",
    stale: "数据过期",
    market_closed: "市场休市 / 未形成新交易日",
    provider_failed: "数据源失败",
  };
  return value ? map[value] ?? value : "新鲜度未知";
}

function getModelList(dashboard: PredictionDashboard): AnyRecord[] {
  const models = asRecord(dashboard.model_leaderboard).models;
  return Array.isArray(models) ? models.slice(0, 5) : [];
}

function buildPath(values: Array<number | null | undefined>, xFor: (index: number) => number, yFor: (value: number) => number): string {
  let path = "";
  let drawing = false;
  values.forEach((value, index) => {
    if (typeof value !== "number" || !Number.isFinite(value)) {
      drawing = false;
      return;
    }
    const command = drawing ? "L" : "M";
    path += `${command}${xFor(index).toFixed(2)},${yFor(value).toFixed(2)} `;
    drawing = true;
  });
  return path.trim();
}

function buildArea(
  upper: Array<number | null | undefined>,
  lower: Array<number | null | undefined>,
  xFor: (index: number) => number,
  yFor: (value: number) => number,
): string {
  const top: string[] = [];
  const bottom: string[] = [];
  upper.forEach((value, index) => {
    if (typeof value === "number" && Number.isFinite(value)) {
      top.push(`${xFor(index).toFixed(2)},${yFor(value).toFixed(2)}`);
    }
  });
  lower.forEach((value, index) => {
    if (typeof value === "number" && Number.isFinite(value)) {
      bottom.unshift(`${xFor(index).toFixed(2)},${yFor(value).toFixed(2)}`);
    }
  });
  if (!top.length || !bottom.length) return "";
  return `M${top.join(" L")} L${bottom.join(" L")} Z`;
}

function getChartDomain(symbolData: SimulatedSymbolPaths): [number, number] {
  const values: number[] = [];
  const paths = symbolData.paths;
  ([
    "historical_price",
    "expected_path",
    "bounce_path",
    "bearish_path",
    "analog_average_path",
    "confidence_band_upper",
    "confidence_band_lower",
  ] as const).forEach((key) => {
    paths[key]?.forEach((value) => {
      if (typeof value === "number" && Number.isFinite(value)) values.push(value);
    });
  });
  if (!values.length) return [0, 1];
  const min = Math.min(...values);
  const max = Math.max(...values);
  const pad = Math.max((max - min) * 0.12, max * 0.005, 1);
  return [min - pad, max + pad];
}

function getCurrentPrice(symbolData: SimulatedSymbolPaths): number | null {
  const direct = asNumber(symbolData.current_price);
  if (direct !== null) return direct;
  const historical = symbolData.paths?.historical_price ?? [];
  for (let i = historical.length - 1; i >= 0; i -= 1) {
    const value = asNumber(historical[i]);
    if (value !== null) return value;
  }
  return null;
}

function getPriceLevelData(selected: SimulatedSymbolPaths | undefined): ForecastPriceLevelsBySymbol | undefined {
  return selected?.forecast_price_levels;
}

function getHorizonPriceTable(levels: ForecastPriceLevelsBySymbol | undefined) {
  return levels?.horizon_prices ?? levels?.forecast_price_table ?? {};
}

function getTriggerLevels(levels: ForecastPriceLevelsBySymbol | undefined) {
  return levels?.trigger_levels ?? levels?.path_trigger_levels;
}

function getLevelPrice(level: unknown): number | null {
  return asNumber(asRecord(level).price);
}

function getLevelMeaning(level: unknown): string {
  const row = asRecord(level);
  return String(row.meaning ?? row.condition ?? "数据缺失");
}

function getLevelDistance(level: unknown): number | null {
  const row = asRecord(level);
  return asNumber(row.distance_pct ?? row.distance_percent);
}

function getPriceLevelSource(level: unknown): string {
  const row = asRecord(level);
  return String(row.source_type ?? row.source ?? "data_missing");
}

function getPlainPricePointSentence(selected: SimulatedSymbolPaths | undefined): string | null {
  const levels = getPriceLevelData(selected);
  const triggers = getTriggerLevels(levels);
  if (!selected || !levels || !triggers) return null;
  const primary = getPrimary(selected);
  const confirmation = asRecord(triggers.primary_confirmation_level);
  const invalidation = asRecord(triggers.primary_invalidation_level);
  const risk = asRecord(triggers.risk_scenario_activation_level);
  const trend = asRecord(triggers.trend_reversal_confirmation_level);
  const bounceZone = asRecord(triggers.bounce_target_zone);
  const conservative = asNumber(bounceZone.conservative ?? asRecord(bounceZone.conservative_bounce_target).price);
  const base = asNumber(bounceZone.base ?? asRecord(bounceZone.base_bounce_target).price);
  const extended = asNumber(bounceZone.extended ?? asRecord(bounceZone.extended_bounce_target).price);
  const bounceText =
    conservative !== null && extended !== null
      ? `${formatPrice(conservative)}-${formatPrice(extended)}`
      : base !== null
        ? formatPrice(base)
        : "数据缺失";
  return `${selected.symbol} 当前最大概率路径是“${primary?.label ?? cnScenario(primary?.scenario)}”，概率 ${formatPercent(
    primary?.probability,
    1,
  )}。如果价格站上 ${formatPrice(confirmation.price)}，说明主路径开始兑现；如果跌破 ${formatPrice(
    invalidation.price,
  )}，主路径可信度下降；20d 基准反抽目标区在 ${bounceText}；若突破 ${formatPrice(
    trend.price,
  )}，趋势修复概率提高；若跌破 ${formatPrice(risk.price)}，风险路径权重会上升。这些是概率路径点位，不是确定预测，也不是买卖建议。`;
}

function getTooltipHorizon(selected: SimulatedSymbolPaths, index: number): string {
  const split = selected.paths.split_index ?? 0;
  const delta = index - split;
  if (delta <= 0) return "历史区间";
  return `${delta}d`;
}

function getTriggerRelevance(selected: SimulatedSymbolPaths, value: number | null): string {
  if (value === null) return "";
  const triggers = getTriggerLevels(getPriceLevelData(selected));
  if (!triggers) return "";
  const checks: Array<[unknown, string]> = [
    [triggers.primary_confirmation_level, "接近主路径确认价"],
    [triggers.primary_invalidation_level, "接近主路径失效价"],
    [triggers.risk_scenario_activation_level, "接近风险路径接管价"],
    [triggers.trend_reversal_confirmation_level, "接近趋势修复确认价"],
  ];
  for (const [level, label] of checks) {
    const price = getLevelPrice(level);
    if (price !== null && price !== 0 && Math.abs(value / price - 1) <= 0.004) return label;
  }
  return "";
}

function TerminalHeader({ dashboard }: { dashboard: PredictionDashboard }) {
  const freshness = getDataFreshnessStatus(dashboard);
  const latestDate = freshness?.latest_market_date ?? dashboard.as_of ?? dashboard.overview?.as_of;
  return (
    <header className="flex flex-col gap-4 border-b border-white/10 pb-5 lg:flex-row lg:items-end lg:justify-between">
      <div>
        <div className="text-xs uppercase tracking-[0.35em] text-cyan-300/75">Market Prediction Terminal</div>
        <h1 className="mt-2 text-3xl font-semibold tracking-tight text-white sm:text-4xl">市场预测终端</h1>
        <p className="mt-3 max-w-3xl text-sm leading-6 text-slate-300">
          展示大盘概率路径、情景排序、支持/冲突证据和前向验证状态。Alpha v1 仍是 Research Alpha Candidate，不是操作建议。
        </p>
      </div>
      <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
        <MiniStat label="核心行情日期" value={shortDate(latestDate)} tone="cyan" />
        <MiniStat
          label="数据完整度"
          value={formatScore(dashboard.data_quality_report?.summary?.data_completeness_score)}
          tone="emerald"
        />
        <MiniStat label="当前模型" value={getValidationStandards(dashboard).activeModel} tone="slate" />
      </div>
    </header>
  );
}

function MiniStat({ label, value, tone }: { label: string; value: string; tone: "cyan" | "emerald" | "slate" | "amber" }) {
  const toneClass =
    tone === "cyan"
      ? "text-cyan-200"
      : tone === "emerald"
        ? "text-emerald-200"
        : tone === "amber"
          ? "text-amber-200"
          : "text-slate-200";
  return (
    <div className="rounded-lg border border-white/10 bg-white/[0.04] px-4 py-3">
      <div className="text-[11px] uppercase tracking-[0.18em] text-slate-500">{label}</div>
      <div className={`mt-1 text-sm font-semibold ${toneClass}`}>{value}</div>
    </div>
  );
}

function DataFreshnessBanner({ dashboard }: { dashboard: PredictionDashboard }) {
  const freshness = getDataFreshnessStatus(dashboard);
  if (!freshness) {
    return (
      <section className="rounded-xl border border-amber-400/25 bg-amber-400/[0.08] p-4 text-sm leading-6 text-amber-100">
        数据新鲜度状态缺失。当前预测只能作为最近一次快照查看，不能视为今日判断。
      </section>
    );
  }
  const staleOrFailed = isDataStaleOrFailed(freshness);
  const className = staleOrFailed
    ? "border-rose-400/35 bg-rose-500/[0.10] text-rose-100"
    : "border-emerald-400/20 bg-emerald-400/[0.06] text-emerald-100";

  return (
    <section className={`rounded-xl border p-4 ${className}`}>
      <div className="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
        <div>
          <div className="text-xs uppercase tracking-[0.22em] opacity-75">Data Freshness Gate</div>
          <h2 className="mt-1 text-lg font-semibold">
            {staleOrFailed ? "数据已过期，当前预测不可作为今日判断" : cnFreshnessStatus(freshness.data_freshness_status)}
          </h2>
          <p className="mt-2 text-sm leading-6 opacity-90">{freshness.warning_message}</p>
        </div>
        <div className="grid gap-2 text-xs sm:grid-cols-3 lg:min-w-[420px]">
          <div className="rounded-lg border border-white/10 bg-black/20 p-3">
            <div className="opacity-65">最新核心行情</div>
            <div className="mt-1 font-semibold">{shortDate(freshness.latest_market_date)}</div>
          </div>
          <div className="rounded-lg border border-white/10 bg-black/20 p-3">
            <div className="opacity-65">应更新到</div>
            <div className="mt-1 font-semibold">{shortDate(freshness.expected_latest_trading_date)}</div>
          </div>
          <div className="rounded-lg border border-white/10 bg-black/20 p-3">
            <div className="opacity-65">滞后交易日</div>
            <div className="mt-1 font-semibold">{String(freshness.stale_days ?? "unknown")}</div>
          </div>
        </div>
      </div>
    </section>
  );
}

function ForecastSummary({ dashboard, selected }: { dashboard: PredictionDashboard; selected: SimulatedSymbolPaths | undefined }) {
  const validation = getValidationStandards(dashboard);
  const strongest = dashboard.overview?.strongest_symbol ?? selected?.symbol ?? "SPY";
  const edgeStatus = getEdgeStatus(selected);
  const confidence = getConfidenceScore(selected);
  const pricePointSentence = getPlainPricePointSentence(selected);

  return (
    <section className="grid gap-4 lg:grid-cols-[1.5fr_0.9fr_0.9fr]">
      <div className="rounded-xl border border-cyan-400/25 bg-cyan-400/[0.06] p-5 shadow-2xl shadow-black/20">
        <div className="text-xs uppercase tracking-[0.22em] text-cyan-200/80">Market Forecast Summary</div>
        <h2 className="mt-2 text-2xl font-semibold text-white">今日核心判断</h2>
        <p className="mt-3 text-sm leading-6 text-slate-200">{getSummarySentence(dashboard, selected)}</p>
        {pricePointSentence ? (
          <div className="mt-4 rounded-lg border border-cyan-300/20 bg-black/20 p-3 text-sm leading-6 text-cyan-50">
            <div className="mb-1 text-xs uppercase tracking-[0.18em] text-cyan-300/70">大白话价格点</div>
            {pricePointSentence}
          </div>
        ) : null}
        <div className="mt-5 grid gap-3 sm:grid-cols-3">
          <Metric label="今日 Edge" value={cnEdgeStatus(edgeStatus)} badge={edgeStatus} />
          <Metric label="最强指数" value={strongest} />
          <Metric label="模型可信度" value={formatScore(confidence)} />
        </div>
      </div>

      <div className="rounded-xl border border-white/10 bg-[#101819] p-5">
        <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Strongest Scenario</div>
        <div className="mt-3 text-2xl font-semibold text-white">{getPrimary(selected)?.label ?? "数据缺失"}</div>
        <div className="mt-2 text-4xl font-semibold text-emerald-300">{formatPercent(getPrimary(selected)?.probability, 1)}</div>
        <p className="mt-3 text-sm leading-6 text-slate-400">{getPrimary(selected)?.reason ?? "当前没有可解释的主路径理由。"}</p>
      </div>

      <div className="rounded-xl border border-white/10 bg-[#101819] p-5">
        <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Validation Status</div>
        <div className="mt-3 flex flex-wrap gap-2">
          <StatusBadge status={validation.highPrecisionStatus} label={`高精度：${cnValidationStatus(validation.highPrecisionStatus)}`} />
          <StatusBadge status={validation.stableAlphaStatus} label={`稳定 Alpha：${cnValidationStatus(validation.stableAlphaStatus)}`} />
          <StatusBadge status={validation.validatedStatus} label={`预测系统：${cnValidationStatus(validation.validatedStatus)}`} />
        </div>
        <p className="mt-4 text-sm leading-6 text-slate-400">
          前向样本不足时，页面必须保持 not yet validated。当前系统用于预测验证，不用于下单或仓位决策。
        </p>
      </div>
    </section>
  );
}

function Metric({ label, value, badge }: { label: string; value: string; badge?: string }) {
  return (
    <div className="rounded-lg border border-white/10 bg-black/20 p-3">
      <div className="text-xs text-slate-500">{label}</div>
      <div className="mt-1 text-base font-semibold text-white">
        {badge ? <StatusBadge status={badge} label={value} /> : value}
      </div>
    </div>
  );
}

function StatusBadge({ status, label }: { status?: string; label?: string }) {
  return (
    <span className={`inline-flex items-center rounded-full border px-2.5 py-1 text-xs font-medium ${badgeClass(status)}`}>
      {label ?? status ?? "数据缺失"}
    </span>
  );
}

const ALERT_TYPE_ORDER = [
  "Risk Expansion Alert",
  "Failed Bounce Alert",
  "Bounce Setup Alert",
  "Bottoming Setup Alert",
  "Trend Repair Alert",
];

function getSymbolAlerts(dashboard: PredictionDashboard, selected: SimulatedSymbolPaths | undefined): AnyRecord {
  if (!selected) return {};
  const topLevelAlerts = asRecord(dashboard.market_alerts);
  return asRecord(selected.market_alerts ?? asRecord(asRecord(topLevelAlerts.symbols)[selected.symbol]));
}

function getAlertByType(alerts: AnyRecord, alertType: string): AnyRecord {
  const rows = Array.isArray(alerts.alerts) ? alerts.alerts.map(asRecord) : [];
  return rows.find((item) => item.alert_type === alertType) ?? {};
}

function getSymbolConfluence(dashboard: PredictionDashboard, selected: SimulatedSymbolPaths | undefined): AnyRecord {
  if (!selected) return {};
  const bundle = asRecord(dashboard.confluence_score);
  return asRecord(selected.confluence ?? asRecord(asRecord(bundle.symbols)[selected.symbol]));
}

function getPriceVolumeStructure(dashboard: PredictionDashboard, selected: SimulatedSymbolPaths | undefined): AnyRecord {
  if (!selected) return {};
  const bundle = asRecord(dashboard.price_volume_structure);
  return asRecord(asRecord(bundle.symbols)[selected.symbol]);
}

function getCompletedSamplesText(dashboard: PredictionDashboard): string {
  const counts = asRecord(dashboard.forecast_accuracy_scorecard?.sample_counts);
  const completed = [
    asNumber(counts.completed_3d) ?? 0,
    asNumber(counts.completed_5d) ?? 0,
    asNumber(counts.completed_10d) ?? 0,
    asNumber(counts.completed_20d) ?? 0,
    asNumber(counts.completed_60d) ?? 0,
  ];
  return completed.map((value) => String(Math.round(value))).join(" / ");
}

function buildCommandCenterSentence(
  dashboard: PredictionDashboard,
  selected: SimulatedSymbolPaths | undefined,
  alerts: AnyRecord,
  confluence: AnyRecord,
): string {
  if (!selected) return "当前没有可展示的预测数据。";
  const primary = getPrimary(selected);
  const secondary = getSecondary(selected);
  const strongest = asRecord(alerts.strongest_alert);
  const strongestSymbol = dashboard.overview?.strongest_symbol ?? selected.symbol;
  const confluenceScore = formatScore(asNumber(confluence.confluence_score));
  const alertText = strongest.alert_type ? `${cnAlertType(String(strongest.alert_type))}（${cnAlertLevel(String(strongest.alert_level))}）` : "暂无强预警";
  return `${selected.symbol} 当前最大概率路径是 ${primary?.label ?? cnScenario(primary?.scenario)}，概率 ${formatPercent(
    primary?.probability,
    1,
  )}；第二路径是 ${secondary?.label ?? cnScenario(secondary?.scenario)}，概率 ${formatPercent(
    secondary?.probability,
    1,
  )}。当前最强指数为 ${strongestSymbol}，多源共振 ${confluenceScore}，强预警为 ${alertText}。结论仍处于前向验证期，优先观察关键价位是否确认或失效。`;
}

function ForecastCommandCenter({
  dashboard,
  selected,
}: {
  dashboard: PredictionDashboard;
  selected: SimulatedSymbolPaths | undefined;
}) {
  if (!selected) return null;
  const validation = getValidationStandards(dashboard);
  const ranking = selected.scenario_ranking;
  const primary = getPrimary(selected);
  const secondary = getSecondary(selected);
  const tertiary = getTertiary(selected);
  const alerts = getSymbolAlerts(dashboard, selected);
  const strongestAlert = asRecord(alerts.strongest_alert);
  const confluence = getSymbolConfluence(dashboard, selected);
  const pv = getPriceVolumeStructure(dashboard, selected);
  const candle = asRecord(pv.candle);
  const volume = asRecord(pv.volume);
  const triggers = getTriggerLevels(getPriceLevelData(selected));
  const confirmation = asRecord(triggers?.primary_confirmation_level);
  const invalidation = asRecord(triggers?.primary_invalidation_level);
  const riskActivation = asRecord(triggers?.risk_scenario_activation_level);
  const trendRepair = asRecord(triggers?.trend_reversal_confirmation_level);
  const bounceZone = asRecord(triggers?.bounce_target_zone);
  const support = normalizeEvidence(strongestAlert.supporting_evidence ?? confluence.supporting_evidence);
  const conflict = normalizeEvidence(strongestAlert.conflicting_evidence ?? confluence.conflicting_evidence);
  const required = asStringArray(strongestAlert.required_confirmation);
  const invalidationConditions = asStringArray(strongestAlert.invalidation_conditions);
  const volumeZScore = asNumber(volume.volume_z_score);
  const pvSupports =
    (asNumber(pv.price_structure_score) ?? 0) >= 55 ||
    (asNumber(pv.volume_confirmation_score) ?? 0) >= 55 ||
    (asNumber(pv.reversal_candle_score) ?? 0) >= 55;

  return (
    <section className="rounded-2xl border border-cyan-300/20 bg-[#0c1718] p-5 shadow-2xl shadow-black/30">
      <div className="flex flex-col gap-4 xl:flex-row xl:items-start xl:justify-between">
        <div className="max-w-4xl">
          <div className="text-xs uppercase tracking-[0.24em] text-cyan-200/80">Forecast Command Center</div>
          <h2 className="mt-2 text-2xl font-semibold text-white">今日预测指挥中心</h2>
          <p className="mt-3 text-sm leading-6 text-slate-200">{buildCommandCenterSentence(dashboard, selected, alerts, confluence)}</p>
        </div>
        <div className="flex flex-wrap gap-2">
          <StatusBadge status={getEdgeStatus(selected)} label={cnEdgeStatus(getEdgeStatus(selected))} />
          <StatusBadge status={validation.highPrecisionStatus} label={cnValidationStatus(validation.highPrecisionStatus)} />
          <StatusBadge status={String(strongestAlert.alert_level ?? "NO_ALERT")} label={cnAlertLevel(String(strongestAlert.alert_level ?? "NO_ALERT"))} />
        </div>
      </div>

      <div className="mt-5 grid gap-4 xl:grid-cols-[1.15fr_0.85fr]">
        <div className="grid gap-3 md:grid-cols-3">
          <div className="rounded-xl border border-emerald-300/20 bg-emerald-300/[0.07] p-4">
            <div className="text-xs uppercase tracking-[0.18em] text-emerald-200/80">最可能路径</div>
            <div className="mt-2 text-xl font-semibold text-white">{primary?.label ?? cnScenario(primary?.scenario)}</div>
            <div className="mt-2 text-3xl font-semibold text-emerald-200">{formatPercent(primary?.probability, 1)}</div>
            <p className="mt-3 text-xs leading-5 text-slate-300">{primary?.reason ?? "主路径理由数据缺失。"}</p>
          </div>
          <div className="rounded-xl border border-cyan-300/20 bg-cyan-300/[0.06] p-4">
            <div className="text-xs uppercase tracking-[0.18em] text-cyan-200/80">第二路径</div>
            <div className="mt-2 text-xl font-semibold text-white">{secondary?.label ?? cnScenario(secondary?.scenario)}</div>
            <div className="mt-2 text-3xl font-semibold text-cyan-200">{formatPercent(secondary?.probability, 1)}</div>
            <p className="mt-3 text-xs leading-5 text-slate-300">主次差距：{formatGap(ranking?.primary_secondary_gap)}。{ranking?.close_call ? "路径分歧较大。" : "主路径有一定领先。"}</p>
          </div>
          <div className="rounded-xl border border-rose-300/20 bg-rose-300/[0.06] p-4">
            <div className="text-xs uppercase tracking-[0.18em] text-rose-200/80">风险路径</div>
            <div className="mt-2 text-xl font-semibold text-white">{tertiary?.label ?? cnScenario(tertiary?.scenario)}</div>
            <div className="mt-2 text-3xl font-semibold text-rose-200">{formatPercent(tertiary?.probability, 1)}</div>
            <p className="mt-3 text-xs leading-5 text-slate-300">{tertiary?.reason ?? "风险路径理由数据缺失。"}</p>
          </div>
        </div>

        <div className="rounded-xl border border-white/10 bg-black/20 p-4">
          <div className="flex items-start justify-between gap-3">
            <div>
              <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Validation</div>
              <div className="mt-1 text-lg font-semibold text-white">模型验证状态</div>
            </div>
            <StatusBadge status={validation.validatedStatus} label={cnValidationStatus(validation.validatedStatus)} />
          </div>
          <div className="mt-4 grid grid-cols-2 gap-3 text-sm">
            <Metric label="Active model" value={validation.activeModel} />
            <Metric label="完成样本 3/5/10/20/60d" value={getCompletedSamplesText(dashboard)} />
            <Metric label="模型可信度" value={formatScore(getConfidenceScore(selected))} />
            <Metric label="确认分数" value={formatScore(getConfirmationScore(selected))} />
          </div>
          <p className="mt-3 text-xs leading-5 text-amber-100">
            当前仍需前向样本验证；alert 和多源共振只是预测确认层，不会覆盖 baseline_v1。
          </p>
        </div>
      </div>

      <div className="mt-4 grid gap-4 xl:grid-cols-[1fr_1fr_1fr]">
        <div className="rounded-xl border border-white/10 bg-black/20 p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Strong Alert Panel</div>
          <h3 className="mt-1 text-lg font-semibold text-white">强预警状态</h3>
          <div className="mt-3 grid gap-2">
            {ALERT_TYPE_ORDER.map((type) => {
              const alert = getAlertByType(alerts, type);
              const level = String(alert.alert_level ?? "NO_ALERT");
              return (
                <div key={type} className="flex items-center justify-between gap-3 rounded-lg border border-white/10 bg-white/[0.03] px-3 py-2">
                  <span className="text-sm text-slate-200">{cnAlertType(type)}</span>
                  <div className="flex items-center gap-2">
                    <span className="text-xs text-slate-500">{formatScore(asNumber(alert.alert_score))}</span>
                    <StatusBadge status={level} label={cnAlertLevel(level)} />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        <div className="rounded-xl border border-white/10 bg-black/20 p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Price + Volume Structure</div>
          <h3 className="mt-1 text-lg font-semibold text-white">K线与成交量确认</h3>
          <div className="mt-3 grid grid-cols-2 gap-3">
            <Metric label="K线类型" value={String(candle.latest_candle_type ?? "数据缺失")} />
            <Metric label="是否支持主路径" value={pvSupports ? "支持" : "不足"} badge={pvSupports ? "supportive" : "weak"} />
            <Metric label="价格结构" value={formatScore(asNumber(pv.price_structure_score))} />
            <Metric label="成交量确认" value={formatScore(asNumber(pv.volume_confirmation_score))} />
            <Metric label="反转K线" value={formatScore(asNumber(pv.reversal_candle_score))} />
            <Metric label="跌破风险" value={formatScore(asNumber(pv.breakdown_risk_score))} />
          </div>
          <p className="mt-3 text-xs leading-5 text-slate-400">
            量能 z-score：{volumeZScore === null ? "数据缺失" : volumeZScore.toFixed(2)}；该层只用于路径确认，不是操作指令。
          </p>
        </div>

        <div className="rounded-xl border border-white/10 bg-black/20 p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Key Levels</div>
          <h3 className="mt-1 text-lg font-semibold text-white">路径切换价位</h3>
          <div className="mt-3 grid grid-cols-2 gap-3">
            <CompactLevel label="主路径确认" level={confirmation} />
            <CompactLevel label="主路径失效" level={invalidation} />
            <CompactLevel label="风险接管" level={riskActivation} />
            <CompactLevel label="趋势修复" level={trendRepair} />
          </div>
          <div className="mt-3 rounded-lg border border-white/10 bg-white/[0.03] p-3 text-xs leading-5 text-slate-300">
            反抽目标区：保守 {formatPrice(bounceZone.conservative)} / 基准 {formatPrice(bounceZone.base)} / 扩展 {formatPrice(bounceZone.extended)}
          </div>
        </div>
      </div>

      <div className="mt-4 grid gap-4 lg:grid-cols-2">
        <MiniEvidenceList title="多源支持证据" tone="supportive" items={support} empty="暂无足够支持证据" />
        <MiniEvidenceList title="多源冲突证据" tone="conflicting" items={conflict} empty="暂无明显冲突证据" />
      </div>

      <div className="mt-4 grid gap-4 lg:grid-cols-2">
        <SimpleList title="需要确认" items={required} empty="暂无额外确认条件" />
        <SimpleList title="主路径失效 / 切换条件" items={invalidationConditions} empty="暂无明确失效条件" />
      </div>
    </section>
  );
}

function IndexCards({
  symbols,
  selectedSymbol,
  onSelect,
}: {
  symbols: SimulatedSymbolPaths[];
  selectedSymbol: string;
  onSelect: (symbol: string) => void;
}) {
  return (
    <section>
      <div className="mb-3 flex items-end justify-between gap-3">
        <div>
          <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Index Overview</div>
          <h2 className="mt-1 text-xl font-semibold text-white">四大指数预测概览</h2>
        </div>
        <div className="hidden text-xs text-slate-500 sm:block">点击卡片切换图表和情景说明</div>
      </div>
      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
        {symbols.map((item) => {
          const primary = getPrimary(item);
          const secondary = getSecondary(item);
          const selected = item.symbol === selectedSymbol;
          return (
            <button
              key={item.symbol}
              className={`text-left transition hover:-translate-y-0.5 hover:border-cyan-300/50 ${
                selected ? "border-cyan-300/60 bg-cyan-300/[0.08]" : "border-white/10 bg-[#101819]"
              } rounded-xl border p-4 shadow-xl shadow-black/10`}
              onClick={() => onSelect(item.symbol)}
              type="button"
            >
              <div className="flex items-start justify-between gap-3">
                <div className="flex items-center gap-3">
                  <div className="grid h-11 w-11 place-items-center rounded-full bg-white text-sm font-black text-slate-950">
                    {item.symbol}
                  </div>
                  <div>
                    <div className="text-lg font-semibold text-white">{item.symbol}</div>
                    <div className="text-xs text-slate-400">{item.name}</div>
                  </div>
                </div>
                <StatusBadge status={getEdgeStatus(item)} label={cnEdgeStatus(getEdgeStatus(item))} />
              </div>

              <div className="mt-4 grid grid-cols-2 gap-3 text-sm">
                <CardDatum label="收盘价" value={formatPrice(getCurrentPrice(item))} />
                <CardDatum label="主路径" value={primary?.label ?? "数据缺失"} />
                <CardDatum label="主路径概率" value={formatPercent(primary?.probability, 1)} accent="emerald" />
                <CardDatum label="第二路径" value={secondary?.label ?? "数据缺失"} />
                <CardDatum label="主次差距" value={formatGap(item.scenario_ranking?.primary_secondary_gap)} />
                <CardDatum label="确认分" value={formatScore(getConfirmationScore(item))} accent="cyan" />
              </div>
            </button>
          );
        })}
      </div>
    </section>
  );
}

function CardDatum({ label, value, accent }: { label: string; value: string; accent?: "emerald" | "cyan" }) {
  return (
    <div>
      <div className="text-[11px] text-slate-500">{label}</div>
      <div className={`mt-0.5 font-medium ${accent === "emerald" ? "text-emerald-200" : accent === "cyan" ? "text-cyan-200" : "text-slate-100"}`}>
        {value}
      </div>
    </div>
  );
}

function ScenarioRankingPanel({ selected }: { selected: SimulatedSymbolPaths | undefined }) {
  const ranking = selected?.scenario_ranking;
  if (!selected || !ranking) {
    return (
      <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
        <h2 className="text-lg font-semibold text-white">最可能路径排序</h2>
        <p className="mt-3 text-sm text-slate-400">当前没有情景排序数据。</p>
      </section>
    );
  }

  const rows = [
    { title: "第一可能", item: ranking.primary, tone: "emerald" },
    { title: "第二可能", item: ranking.secondary, tone: "cyan" },
    { title: "风险路径", item: ranking.tertiary, tone: "rose" },
  ];

  return (
    <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Scenario Probability Ranking</div>
          <h2 className="mt-1 text-xl font-semibold text-white">最可能路径排序</h2>
        </div>
        <div className="flex flex-wrap gap-2">
          <StatusBadge
            status={ranking.close_call ? "weak" : "supportive"}
            label={ranking.close_call ? "路径分歧较大" : `主次差距 ${formatGap(ranking.primary_secondary_gap)}`}
          />
          <StatusBadge status={ranking.path_reliability} label={`可靠度：${ranking.path_reliability ?? "数据缺失"}`} />
        </div>
      </div>

      <div className="mt-4 grid gap-3 lg:grid-cols-3">
        {rows.map(({ title, item, tone }) => (
          <div key={title} className="rounded-lg border border-white/10 bg-black/20 p-4">
            <div className="flex items-center justify-between gap-2">
              <div className="text-xs uppercase tracking-[0.18em] text-slate-500">{title}</div>
              <div
                className={`text-lg font-semibold ${
                  tone === "emerald" ? "text-emerald-300" : tone === "cyan" ? "text-cyan-300" : "text-rose-300"
                }`}
              >
                {formatPercent(item?.probability, 1)}
              </div>
            </div>
            <div className="mt-2 text-lg font-semibold text-white">{item?.label ?? cnScenario(item?.scenario)}</div>
            <p className="mt-2 text-sm leading-6 text-slate-400">{item?.reason ?? "缺少路径解释。"}</p>
          </div>
        ))}
      </div>

      {ranking.close_call ? (
        <div className="mt-4 rounded-lg border border-amber-400/25 bg-amber-400/10 p-3 text-sm text-amber-100">
          路径分歧较大，不宜过度押注单一路径。请重点观察失效条件是否触发。
        </div>
      ) : null}
    </section>
  );
}

function PredictionChart({ selected }: { selected: SimulatedSymbolPaths | undefined }) {
  const svgRef = useRef<SVGSVGElement | null>(null);
  const [tooltip, setTooltip] = useState<TooltipState>(null);

  if (!selected?.paths?.dates?.length) {
    return (
      <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
        <h2 className="text-xl font-semibold text-white">概率路径图</h2>
        <p className="mt-3 text-sm text-slate-400">当前没有可绘制的路径数据。</p>
      </section>
    );
  }

  const width = 1100;
  const height = 620;
  const margin = { top: 42, right: 34, bottom: 66, left: 76 };
  const dates = selected.paths.dates;
  const splitIndex = Math.max(0, Math.min(selected.paths.split_index ?? dates.length - 1, dates.length - 1));
  const [minY, maxY] = getChartDomain(selected);
  const chartWidth = width - margin.left - margin.right;
  const chartHeight = height - margin.top - margin.bottom;
  const xFor = (index: number) => margin.left + (dates.length <= 1 ? 0 : (index / (dates.length - 1)) * chartWidth);
  const yFor = (value: number) => margin.top + ((maxY - value) / (maxY - minY || 1)) * chartHeight;
  const current = getCurrentPrice(selected);

  const series: PathSeriesKey[] = ["historical_price", "expected_path", "bounce_path", "bearish_path", "analog_average_path"];
  const area = buildArea(selected.paths.confidence_band_upper, selected.paths.confidence_band_lower, xFor, yFor);

  const onMove = (event: MouseEvent<SVGSVGElement>) => {
    const rect = svgRef.current?.getBoundingClientRect();
    if (!rect) return;
    const svgX = (event.clientX - rect.left) * (width / rect.width);
    const index = Math.max(0, Math.min(dates.length - 1, Math.round(((svgX - margin.left) / chartWidth) * (dates.length - 1))));
    setTooltip({
      index,
      left: event.clientX - rect.left,
      top: event.clientY - rect.top,
    });
  };

  const tooltipRows = tooltip
    ? series
        .map((key) => {
          const value = asNumber(selected.paths[key]?.[tooltip.index]);
          return {
            key,
            value,
            probability: getScenarioProbability(selected, key),
            rank: getScenarioRank(selected, key),
            expectedReturn: current !== null && value !== null ? value / current - 1 : null,
            triggerRelevance: getTriggerRelevance(selected, value),
          };
        })
        .filter((row) => row.value !== null)
    : [];
  const tooltipHorizon = tooltip ? getTooltipHorizon(selected, tooltip.index) : "";

  return (
    <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
        <div className="mb-4 flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
          <div>
            <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Past + Simulated Future Path</div>
            <h2 className="mt-1 text-xl font-semibold text-white">{selected.symbol} 概率路径图</h2>
          </div>
          <div className="text-xs leading-5 text-slate-400">
            未来路径是概率情景，不是确定预测。鼠标悬停可查看每一天价格。
          </div>
        </div>

        <div className="relative">
          <svg
            ref={svgRef}
            className="h-[430px] w-full overflow-visible rounded-lg bg-[#0a1112] sm:h-[520px] xl:h-[620px]"
            onMouseLeave={() => setTooltip(null)}
            onMouseMove={onMove}
            role="img"
            viewBox={`0 0 ${width} ${height}`}
            preserveAspectRatio="none"
          >
            <defs>
              <linearGradient id="confidenceFill" x1="0" x2="0" y1="0" y2="1">
                <stop offset="0%" stopColor="#38bdf8" stopOpacity="0.18" />
                <stop offset="100%" stopColor="#38bdf8" stopOpacity="0.03" />
              </linearGradient>
            </defs>

            {[0, 0.25, 0.5, 0.75, 1].map((tick) => {
              const y = margin.top + tick * chartHeight;
              const value = maxY - tick * (maxY - minY);
              return (
                <g key={tick}>
                  <line stroke="#1f3031" strokeWidth="1" x1={margin.left} x2={width - margin.right} y1={y} y2={y} />
                  <text fill="#78908e" fontSize="11" x={12} y={y + 4}>
                    {value.toFixed(2)}
                  </text>
                </g>
              );
            })}

            {area ? <path d={area} fill="url(#confidenceFill)" /> : null}

            <line
              stroke="#94a3b8"
              strokeDasharray="4 6"
              strokeWidth="1.5"
              x1={xFor(splitIndex)}
              x2={xFor(splitIndex)}
              y1={margin.top - 8}
              y2={height - margin.bottom + 12}
            />
            <text fill="#94a3b8" fontSize="12" x={xFor(splitIndex) + 8} y={margin.top - 12}>
              当前
            </text>

            {HORIZON_ORDER.map((horizon) => {
              const offset = Number.parseInt(horizon, 10);
              const index = Math.min(dates.length - 1, splitIndex + offset);
              return (
                <g key={horizon}>
                  <line
                    stroke="#334155"
                    strokeDasharray="3 7"
                    strokeWidth="1"
                    x1={xFor(index)}
                    x2={xFor(index)}
                    y1={margin.top}
                    y2={height - margin.bottom}
                  />
                  <text fill="#8aa09d" fontSize="11" textAnchor="middle" x={xFor(index)} y={height - 18}>
                    {horizon}
                  </text>
                </g>
              );
            })}

            {series.map((key) => {
              const path = buildPath(selected.paths[key], xFor, yFor);
              if (!path) return null;
              const isHistorical = key === "historical_price";
              const rank = getScenarioRank(selected, key);
              return (
                <path
                  key={key}
                  d={path}
                  fill="none"
                  opacity={isHistorical ? 1 : rank === "参考路径" ? 0.72 : 0.95}
                  stroke={SCENARIO_STROKES[key]}
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={getLineWidth(selected, key)}
                />
              );
            })}

            {current !== null ? (
              <>
                <line
                  stroke="#2dd4bf"
                  strokeDasharray="2 6"
                  strokeOpacity="0.65"
                  strokeWidth="1"
                  x1={margin.left}
                  x2={width - margin.right}
                  y1={yFor(current)}
                  y2={yFor(current)}
                />
                <text fill="#99f6e4" fontSize="12" x={width - margin.right - 88} y={yFor(current) - 8}>
                  现价 {current.toFixed(2)}
                </text>
              </>
            ) : null}

            {tooltip ? (
              <line
                stroke="#e2e8f0"
                strokeDasharray="3 5"
                strokeOpacity="0.55"
                strokeWidth="1"
                x1={xFor(tooltip.index)}
                x2={xFor(tooltip.index)}
                y1={margin.top}
                y2={height - margin.bottom}
              />
            ) : null}
          </svg>

          {tooltip && tooltipRows.length ? (
            <div
              className="pointer-events-none absolute z-20 min-w-64 rounded-lg border border-white/10 bg-[#071111]/95 p-3 text-xs shadow-2xl shadow-black/50"
              style={{
                left: Math.min(Math.max(tooltip.left + 12, 8), 680),
                top: Math.max(tooltip.top - 8, 8),
              }}
            >
              <div className="mb-2 font-semibold text-white">{dates[tooltip.index]}</div>
              <div className="mb-2 text-slate-400">周期：{tooltipHorizon}</div>
              <div className="space-y-1.5">
                {tooltipRows.map((row) => (
                  <div key={row.key} className="rounded-md border border-white/5 bg-white/[0.03] p-2">
                    <div className="grid grid-cols-[0.8rem_1fr_auto] items-center gap-2">
                      <span className="h-2 w-2 rounded-full" style={{ backgroundColor: SCENARIO_STROKES[row.key] }} />
                      <span className="text-slate-300">
                        {SCENARIO_NAMES[row.key]} · {row.rank}
                        {row.key !== "historical_price" ? ` · ${formatPercent(row.probability, 1)}` : ""}
                      </span>
                      <span className="font-semibold text-white">{formatPrice(row.value)}</span>
                    </div>
                    <div className="mt-1 flex flex-wrap gap-2 pl-5 text-[11px] text-slate-400">
                      <span>预期收益 {formatSignedPercent(row.expectedReturn, 1)}</span>
                      {row.triggerRelevance ? <span className="text-amber-200">{row.triggerRelevance}</span> : null}
                    </div>
                  </div>
                ))}
              </div>
              {current !== null ? (
                <div className="mt-2 border-t border-white/10 pt-2 text-slate-400">
                  相对当前价：{formatSignedPercent(((tooltipRows[0]?.value ?? current) - current) / current, 1)}
                </div>
              ) : null}
            </div>
          ) : null}
        </div>

        <div className="mt-4 flex flex-wrap gap-3 text-xs text-slate-400">
          {series.map((key) => (
            <div key={key} className="flex items-center gap-2">
              <span className="h-2.5 w-6 rounded-full" style={{ backgroundColor: SCENARIO_STROKES[key] }} />
              {SCENARIO_NAMES[key]}
              {key !== "historical_price" ? ` · ${getScenarioRank(selected, key)}` : ""}
            </div>
          ))}
        </div>
      <ChartExplanation selected={selected} />
    </section>
  );
}

function ChartExplanation({ selected }: { selected: SimulatedSymbolPaths }) {
  const primary = getPrimary(selected);
  const secondary = getSecondary(selected);
  const tertiary = getTertiary(selected);
  const primarySwitchers = asStringArray(selected.scenario_ranking?.primary_to_secondary_switch_conditions);
  const fallbackSwitchers = asStringArray(asRecord(selected.scenario_ranking).switching_conditions);
  const invalidationSwitchers = asStringArray(selected.risk_invalidation_conditions);
  const switchers = primarySwitchers.length ? primarySwitchers : fallbackSwitchers.length ? fallbackSwitchers : invalidationSwitchers;

  return (
    <div className="mt-5 border-t border-white/10 pt-4">
      <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Path Explanation</div>
      <h3 className="mt-1 text-lg font-semibold text-white">为什么这样排序</h3>
      <div className="mt-4 grid gap-3 lg:grid-cols-3">
        <ReasonBlock title="主路径" scenario={primary} />
        <ReasonBlock title="第二路径" scenario={secondary} />
        <ReasonBlock title="风险路径" scenario={tertiary} />
      </div>
      <div className="mt-4 rounded-lg border border-rose-400/20 bg-rose-400/[0.07] p-3">
        <div className="text-sm font-semibold text-rose-100">主路径失效条件</div>
        <ul className="mt-2 space-y-1 text-sm text-slate-300">
          {switchers.length ? switchers.slice(0, 5).map((item) => <li key={item}>· {item}</li>) : <li>· 数据缺失</li>}
        </ul>
      </div>
    </div>
  );
}

function ReasonBlock({ title, scenario }: { title: string; scenario?: ScenarioRankingItem }) {
  return (
    <div>
      <div className="text-xs text-slate-500">{title}</div>
      <div className="mt-1 flex items-center justify-between gap-3">
        <div className="font-semibold text-white">{scenario?.label ?? cnScenario(scenario?.scenario)}</div>
        <div className="text-sm font-semibold text-cyan-200">{formatPercent(scenario?.probability, 1)}</div>
      </div>
      <p className="mt-1 text-sm leading-6 text-slate-400">{scenario?.reason ?? "缺少解释。"}</p>
    </div>
  );
}

function ForecastPriceLevelsPanel({ selected }: { selected: SimulatedSymbolPaths | undefined }) {
  const levels = selected?.forecast_price_levels;
  if (!selected || !levels) {
    return (
      <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
        <h2 className="text-xl font-semibold text-white">预测价格点位</h2>
        <p className="mt-3 text-sm text-slate-400">当前没有价格点位数据。下一次 GitHub Actions 生成后会显示。</p>
      </section>
    );
  }
  const triggers = getTriggerLevels(levels);
  const table = getHorizonPriceTable(levels);
  const bounceZone = asRecord(triggers?.bounce_target_zone);
  const failedZone = asRecord(triggers?.failed_bounce_warning_zone);
  const validationStatus = String(asRecord(asRecord(selected.data_quality).validation_status).high_precision_status ?? "not_yet_validated");

  return (
    <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
      <div className="flex flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Forecast Price Levels</div>
          <h2 className="mt-1 text-xl font-semibold text-white">{selected.symbol} 预测价格点位</h2>
          <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-400">
            价格点位是概率路径和历史相似情景生成的情景参考，不是确定预测，也不是买卖建议。
          </p>
          {validationStatus === "not_yet_validated" ? (
            <p className="mt-2 text-xs leading-5 text-amber-200">当前价格点位尚未经过足够前向样本验证。</p>
          ) : null}
        </div>
        <div className="rounded-lg border border-white/10 bg-black/20 p-3 text-sm">
          <div className="text-xs text-slate-500">当前价</div>
          <div className="mt-1 text-2xl font-semibold text-white">{formatPrice(levels.current_price)}</div>
        </div>
      </div>

      <div className="mt-5 overflow-x-auto rounded-lg border border-white/10">
        <table className="min-w-[920px] w-full text-left text-sm">
          <thead className="bg-white/[0.04] text-xs uppercase tracking-[0.14em] text-slate-500">
            <tr>
              <th className="px-3 py-3">周期</th>
              <th className="px-3 py-3">综合期望价</th>
              <th className="px-3 py-3">期望收益</th>
              <th className="px-3 py-3">主路径价</th>
              <th className="px-3 py-3">第二路径价</th>
              <th className="px-3 py-3">风险路径价</th>
              <th className="px-3 py-3">置信区间</th>
              <th className="px-3 py-3">主路径权重</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/10">
            {PRICE_LEVEL_HORIZON_ORDER.map((horizon) => {
              const row = table[horizon];
              return (
                <tr key={horizon} className="text-slate-300">
                  <td className="px-3 py-3 font-semibold text-white">{horizon}</td>
                  <td className="px-3 py-3">{formatPrice(row?.expected_price)}</td>
                  <td className="px-3 py-3">{formatSignedPercent(row?.expected_return)}</td>
                  <td className="px-3 py-3 text-emerald-200">{formatPrice(row?.primary_scenario_price)}</td>
                  <td className="px-3 py-3 text-cyan-200">{formatPrice(row?.secondary_scenario_price)}</td>
                  <td className="px-3 py-3 text-rose-200">{formatPrice(row?.risk_scenario_price)}</td>
                  <td className="px-3 py-3">
                    {formatPrice(row?.lower_confidence_price)} - {formatPrice(row?.upper_confidence_price)}
                  </td>
                  <td className="px-3 py-3">{formatPercent(row?.probability_of_reaching_primary_price, 1)}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      <div className="mt-5 grid gap-3 lg:grid-cols-4">
        <LevelCard title="主路径确认价" level={triggers?.primary_confirmation_level} tone="emerald" />
        <LevelCard title="主路径失效价" level={triggers?.primary_invalidation_level} tone="amber" />
        <LevelCard title="风险路径接管价" level={triggers?.risk_scenario_activation_level} tone="rose" />
        <LevelCard title="趋势修复确认价" level={triggers?.trend_reversal_confirmation_level} tone="cyan" />
      </div>

      <div className="mt-4 grid gap-4 lg:grid-cols-2">
        <div className="rounded-lg border border-white/10 bg-black/20 p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Bounce Target Zone</div>
          <h3 className="mt-1 text-lg font-semibold text-white">反抽情景点位区</h3>
          <div className="mt-3 grid gap-3 sm:grid-cols-3">
            <CompactLevel label="保守" level={bounceZone.conservative ?? bounceZone.conservative_bounce_target} />
            <CompactLevel label="基准" level={bounceZone.base ?? bounceZone.base_bounce_target} />
            <CompactLevel label="扩展" level={bounceZone.extended ?? bounceZone.extended_bounce_target} />
          </div>
        </div>
        <div className="rounded-lg border border-white/10 bg-black/20 p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Failed Bounce Warning Zone</div>
          <h3 className="mt-1 text-lg font-semibold text-white">失败反抽警戒区</h3>
          <div className="mt-3 grid gap-3 sm:grid-cols-2">
            <CompactLevel label="第一警戒" level={failedZone.first_warning ?? failedZone.first_warning_level} />
            <CompactLevel label="关键警戒" level={failedZone.critical_warning ?? failedZone.critical_warning_level} />
          </div>
        </div>
      </div>

      <p className="mt-4 text-xs leading-5 text-slate-500">
        来源说明：路径模型 = simulated_path，价格结构 = recent high/low 与均线，波动区间 = realized volatility / confidence band，多来源共振 = 多个来源点位接近。
      </p>
    </section>
  );
}

function LevelCard({
  title,
  level,
  tone,
}: {
  title: string;
  level?: ForecastPriceLevel | CompactForecastPriceLevel;
  tone: "emerald" | "amber" | "rose" | "cyan";
}) {
  const color =
    tone === "emerald"
      ? "text-emerald-200"
      : tone === "amber"
        ? "text-amber-200"
        : tone === "rose"
          ? "text-rose-200"
          : "text-cyan-200";
  return (
    <div className="rounded-lg border border-white/10 bg-black/20 p-4">
      <div className="text-xs text-slate-500">{title}</div>
      <div className={`mt-2 text-2xl font-semibold ${color}`}>{formatPrice(level?.price)}</div>
      <div className="mt-2 flex flex-wrap gap-2">
        <StatusBadge status={getPriceLevelSource(level)} label={cnSource(getPriceLevelSource(level))} />
        <span className="rounded-full border border-white/10 bg-white/[0.04] px-2.5 py-1 text-xs text-slate-300">
          距当前 {formatSignedPercent(getLevelDistance(level))}
        </span>
      </div>
      <p className="mt-3 text-xs leading-5 text-slate-400">{getLevelMeaning(level)}</p>
    </div>
  );
}

function CompactLevel({ label, level }: { label: string; level?: ForecastPriceLevel | number | unknown }) {
  const price = typeof level === "number" ? level : getLevelPrice(level);
  const distance = typeof level === "number" ? null : getLevelDistance(level);
  const source = typeof level === "number" ? "simulated_path" : getPriceLevelSource(level);
  return (
    <div className="rounded-lg border border-white/10 bg-white/[0.03] p-3">
      <div className="text-xs text-slate-500">{label}</div>
      <div className="mt-1 text-lg font-semibold text-white">{formatPrice(price)}</div>
      <div className="mt-1 text-xs text-slate-400">{distance === null ? "距离见上方触发价" : formatSignedPercent(distance)}</div>
      <div className="mt-2 text-[11px] text-slate-500">{cnSource(source)}</div>
    </div>
  );
}

function getAlphaInputEvidence(dashboard: PredictionDashboard, selected: SimulatedSymbolPaths | undefined) {
  if (!selected) return null;
  const alpha = asRecord(dashboard.alpha_status);
  const forecastSignals = Array.isArray(alpha.forecast_signals) ? alpha.forecast_signals.map(asRecord) : [];
  const signal = forecastSignals.find((item) => String(item.symbol) === selected.symbol);
  const latestBySymbol = asRecord(alpha.latest_bounce_probability_by_symbol);
  const probability = asNumber(signal?.bounce_probability ?? latestBySymbol[selected.symbol]);
  const threshold = asNumber(alpha.threshold);
  const active = Boolean(signal);
  return {
    active,
    probability,
    threshold,
    status: String(alpha.status ?? "RESEARCH ALPHA CANDIDATE"),
  };
}

function EvidenceSections({
  dashboard,
  selected,
}: {
  dashboard: PredictionDashboard;
  selected: SimulatedSymbolPaths | undefined;
}) {
  if (!selected) return null;
  const confirmation = selected.signal_confirmation;
  const supporting = confirmation?.supporting_evidence ?? selected.signal_agreement?.supporting_signals ?? [];
  const conflicting = confirmation?.conflicting_evidence ?? selected.signal_agreement?.conflicting_signals ?? [];
  const missing = confirmation?.missing_evidence ?? [];
  const invalidation = selected.risk_invalidation_conditions ?? selected.scenario_ranking?.primary_to_secondary_switch_conditions ?? [];
  const alphaInput = getAlphaInputEvidence(dashboard, selected);

  return (
    <section className="space-y-4">
      {alphaInput ? (
        <div className="rounded-xl border border-white/10 bg-[#101819] p-4">
          <div className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Forecast Input Evidence</div>
              <div className="mt-1 text-sm font-semibold text-white">
                Alpha v1 bounce forecast input: {alphaInput.active ? "active" : "inactive"}
              </div>
            </div>
            <div className="flex flex-wrap gap-2">
              <StatusBadge status={alphaInput.active ? "supportive" : "missing"} label={alphaInput.active ? "active" : "inactive"} />
              <StatusBadge status="not_yet_validated" label={alphaInput.status} />
            </div>
          </div>
          <p className="mt-2 text-xs leading-5 text-slate-400">
            bounce probability {formatPercent(alphaInput.probability, 1)} / threshold {formatPercent(alphaInput.threshold, 1)}。
            这只是反抽情景输入证据，不是独立主模块，也不是 confirmed alpha。
          </p>
        </div>
      ) : null}

      <div className="grid gap-4 lg:grid-cols-3">
        <EvidenceCard title="支持证据" tone="supportive" items={supporting} empty="暂无明确支持证据" />
        <EvidenceCard title="冲突证据" tone="conflicting" items={conflicting} empty="暂无明显冲突证据" />
        <div className="rounded-xl border border-white/10 bg-[#101819] p-5">
          <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Invalidation Conditions</div>
          <h3 className="mt-1 text-lg font-semibold text-white">需要观察的失效条件</h3>
          <ul className="mt-4 space-y-2 text-sm leading-6 text-slate-300">
            {invalidation.length ? invalidation.slice(0, 6).map((item) => <li key={item}>· {item}</li>) : <li>· 数据缺失</li>}
          </ul>
          {missing.length ? (
            <div className="mt-4 rounded-lg border border-white/10 bg-white/[0.03] p-3 text-xs leading-5 text-slate-400">
              缺失证据：{missing.map((item) => item.name).join(" / ")}
            </div>
          ) : null}
        </div>
      </div>
    </section>
  );
}

function NewsEventIntelligencePanel({
  dashboard,
  selected,
}: {
  dashboard: PredictionDashboard;
  selected: SimulatedSymbolPaths | undefined;
}) {
  const symbolNews = selected?.news_event_intelligence;
  const bundle = asRecord(dashboard.news_event_status);
  const narrative = asRecord(symbolNews?.market_narrative ?? bundle.market_narrative);
  const reaction = asRecord(symbolNews?.price_reaction_confirmation ?? bundle.price_reaction_confirmation);
  const impact = asRecord(symbolNews?.symbol_impact);
  const effect = asRecord(symbolNews?.prediction_logic_effect);
  const calendarRisk = asRecord(symbolNews?.economic_calendar_risk ?? bundle.economic_calendar_risk);
  const events = (symbolNews?.major_events ?? (Array.isArray(bundle.major_events) ? bundle.major_events : [])) as Array<Record<string, unknown>>;
  const status = String(symbolNews?.status ?? bundle.status ?? "missing");
  const direction = String(narrative.narrative_direction ?? "mixed");
  const newsDirection = String(symbolNews?.news_direction ?? bundle.news_direction ?? "mixed");
  const eventRiskLevel = String(symbolNews?.event_risk_level ?? bundle.event_risk_level ?? "low");
  const validationType = String(symbolNews?.validation_type ?? bundle.validation_type ?? dashboard.validation_type ?? "daily");
  const affectedAssets = Array.isArray(narrative.affected_symbols) ? narrative.affected_symbols.map(String) : [];
  const conditionTags = asStringArray(narrative.detected_event_conditions);
  const supports = Boolean(impact.news_supports_primary_scenario);
  const conflicts = Boolean(impact.news_conflicts_primary_scenario);
  const confirmed = Boolean(reaction.price_reaction_confirmed);
  const primaryChanged = Boolean(effect.primary_scenario_changed);

  return (
    <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <div className="text-xs uppercase tracking-[0.22em] text-slate-500">News / Event Intelligence</div>
          <h2 className="mt-1 text-xl font-semibold text-white">新闻事件智能层</h2>
        </div>
        <div className="flex flex-wrap gap-2">
          <StatusBadge status={status} label={status === "news_event_partial" || status === "no_major_event" ? "新闻部分可用" : status} />
          <StatusBadge status={eventRiskLevel} label={`事件风险：${eventRiskLevel}`} />
          <StatusBadge status={validationType} label={validationType === "event_refresh" ? "重大事件手动刷新" : "每日刷新"} />
          <StatusBadge
            status={confirmed ? "supportive" : "mixed"}
            label={confirmed ? "价格已确认" : "价格未充分确认"}
          />
        </div>
      </div>

      <div className="mt-4 grid gap-4 lg:grid-cols-[1.1fr_0.9fr]">
        <div className="rounded-lg border border-white/10 bg-black/20 p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Market Narrative</div>
          <div className="mt-2 text-lg font-semibold text-white">{String(narrative.market_narrative ?? "no_clear_narrative")}</div>
          <p className="mt-2 text-sm leading-6 text-slate-300">
            {String(symbolNews?.dashboard_note ?? bundle.dashboard_note ?? narrative.summary ?? "当前新闻层没有足够清晰的市场叙事。")}
          </p>
          <div className="mt-3 grid gap-2 sm:grid-cols-4">
            <Metric label="叙事强度" value={formatScore(asNumber(narrative.narrative_strength))} />
            <Metric label="方向" value={cnNarrativeDirection(direction)} />
            <Metric label="价格确认" value={formatScore(asNumber(reaction.confirmation_score))} />
            <Metric label="宏观事件风险" value={formatScore(asNumber(calendarRisk.macro_event_risk_score))} />
          </div>
          <div className="mt-3 flex flex-wrap gap-2 text-xs text-slate-400">
            <span>新闻方向：{newsDirection === "risk_on" ? "risk-on" : newsDirection === "risk_off" ? "risk-off" : "mixed"}</span>
            <span>受影响资产：{affectedAssets.length ? affectedAssets.join(" / ") : "数据缺失"}</span>
            {conditionTags.length ? <span>识别到的事件线索：{conditionTags.map(cnEventCondition).join(" / ")}</span> : null}
            <span>重大事件数：{String(bundle.major_event_count ?? events.length ?? 0)}</span>
          </div>
        </div>

        <div className="rounded-lg border border-white/10 bg-black/20 p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Path Impact</div>
          <h3 className="mt-1 text-lg font-semibold text-white">{selected?.symbol ?? "SPY"} 路径影响</h3>
          <div className="mt-3 flex flex-wrap gap-2">
            <StatusBadge status={supports ? "supportive" : "neutral"} label={supports ? "支持主路径" : "未支持主路径"} />
            <StatusBadge status={conflicts ? "conflicting" : "neutral"} label={conflicts ? "与主路径冲突" : "无明显冲突"} />
            <StatusBadge status={primaryChanged ? "mixed" : "neutral"} label={primaryChanged ? "主路径被事件影响" : "主路径未切换"} />
          </div>
          <p className="mt-3 text-sm leading-6 text-slate-300">
            {String(impact.explanation ?? "新闻层当前只作为解释和确认输入，不直接替代主路径排序。")}
          </p>
          <div className="mt-3 grid gap-2 sm:grid-cols-3">
            <Metric label="主路径变化" value={primaryChanged ? `${String(effect.before_primary_scenario)} → ${String(effect.after_primary_scenario)}` : "未切换"} />
            <Metric label="主路径概率变化" value={formatSignedPercent(asNumber(effect.primary_probability_delta), 1)} />
            <Metric label="确认分变化" value={effect.confirmation_delta == null ? "数据缺失" : `${String(effect.confirmation_delta)} 分`} />
          </div>
          <p className="mt-3 text-xs leading-5 text-slate-500">
            新闻事件只会在重大事件且价格反应确认时小幅影响短线概率路径；如果只是标题利好但 VIX、HYG/LQD、指数价格没有确认，系统会提高分歧和失败反抽观察权重。
          </p>
          {reaction.contradiction_warning ? (
            <div className="mt-3 rounded-lg border border-amber-400/20 bg-amber-400/[0.08] p-3 text-sm text-amber-100">
              {String(reaction.contradiction_warning)}
            </div>
          ) : null}
        </div>
      </div>

      <div className="mt-4 grid gap-3 lg:grid-cols-2">
        {events.length ? (
          events.slice(0, 4).map((event, index) => (
            <div key={`${String(event.headline)}-${index}`} className="rounded-lg border border-white/10 bg-white/[0.03] p-3">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <StatusBadge status={String(event.event_type ?? "unknown")} label={String(event.event_type ?? "unknown")} />
                <span className="text-xs text-slate-500">{String(event.source ?? "unknown source")}</span>
              </div>
              <p className="mt-2 text-sm leading-6 text-slate-200">{String(event.headline ?? "无标题")}</p>
              <div className="mt-2 flex flex-wrap gap-2 text-xs text-slate-400">
                <span>方向：{String(event.expected_market_direction ?? "unknown")}</span>
                <span>影响资产：{Array.isArray(event.affected_assets) ? event.affected_assets.map(String).slice(0, 8).join(" / ") : "unknown"}</span>
                {asStringArray(event.detected_event_conditions).length ? (
                  <span>事件线索：{asStringArray(event.detected_event_conditions).map(cnEventCondition).join(" / ")}</span>
                ) : null}
                <span>重要性：{formatScore(asNumber(event.importance_score))}</span>
                <span>新鲜度：{formatScore(asNumber(event.freshness_score))}</span>
              </div>
            </div>
          ))
        ) : (
          <div className="rounded-lg border border-white/10 bg-white/[0.03] p-3 text-sm text-slate-400">
            暂无可用于路径判断的重大新闻事件。新闻源失败时会显示 missing / provider_failed，不会用旧新闻冒充最新。
          </div>
        )}
      </div>
      <p className="mt-4 text-xs leading-5 text-slate-500">
        新闻事件智能层用于解释“为什么路径可能被支持或冲突”，不是独立预测模型，也不是买卖建议；其有效性仍需前向验证。
      </p>
    </section>
  );
}

function cnAlertType(value: string | undefined): string {
  const map: Record<string, string> = {
    "Risk Expansion Alert": "风险扩散预警",
    "Failed Bounce Alert": "反抽失败预警",
    "Bounce Setup Alert": "反抽预警",
    "Bottoming Setup Alert": "疑似底部预警",
    "Trend Repair Alert": "趋势修复预警",
  };
  return value ? map[value] ?? value : "暂无强预警";
}

function cnAlertLevel(value: string | undefined): string {
  const map: Record<string, string> = {
    NO_ALERT: "无预警",
    WATCH: "观察",
    WARNING: "预警",
    HIGH_CONVICTION: "高共振",
    EXTREME: "极端预警",
  };
  return value ? map[value] ?? value : "无预警";
}

function cnConfluenceLevel(value: string | undefined): string {
  const map: Record<string, string> = {
    weak: "弱",
    mixed: "分歧",
    moderate: "中等",
    strong: "强",
  };
  return value ? map[value] ?? value : "数据缺失";
}

function cnDominantPath(value: string | undefined): string {
  const map: Record<string, string> = {
    bounce: "反抽",
    failed_bounce: "失败反抽",
    downside: "下跌延续",
    trend_repair: "趋势修复",
    no_edge: "暂无优势",
  };
  return value ? map[value] ?? value : "数据缺失";
}

function normalizeEvidence(value: unknown): AnyRecord[] {
  return Array.isArray(value) ? value.map(asRecord).filter((item) => Object.keys(item).length > 0) : [];
}

function evidenceTitle(item: AnyRecord): string {
  return String(item.name ?? item.source ?? item.type ?? "证据");
}

function evidenceDetail(item: AnyRecord): string {
  return String(item.detail ?? item.reason ?? item.note ?? "暂无详细解释");
}

function MarketAlertConfluencePanel({
  dashboard,
  selected,
}: {
  dashboard: PredictionDashboard;
  selected: SimulatedSymbolPaths | undefined;
}) {
  if (!selected) return null;
  const topLevelAlerts = asRecord(dashboard.market_alerts);
  const symbolAlerts = asRecord(selected.market_alerts ?? asRecord(asRecord(topLevelAlerts.symbols)[selected.symbol]));
  const topAlert = asRecord(symbolAlerts.strongest_alert ?? asRecord(topLevelAlerts.summary).strongest_alert);
  const confluenceBundle = asRecord(dashboard.confluence_score);
  const confluence = asRecord(selected.confluence ?? asRecord(asRecord(confluenceBundle.symbols)[selected.symbol]));
  const alertType = String(topAlert.alert_type ?? "NO_ALERT");
  const alertLevel = String(topAlert.alert_level ?? "NO_ALERT");
  const alertScore = asNumber(topAlert.alert_score);
  const support = normalizeEvidence(topAlert.supporting_evidence ?? confluence.supporting_evidence);
  const conflict = normalizeEvidence(topAlert.conflicting_evidence ?? confluence.conflicting_evidence);
  const required = asStringArray(topAlert.required_confirmation);
  const invalidation = asStringArray(topAlert.invalidation_conditions);
  const relatedLevels = asRecord(topAlert.related_price_levels);
  const confluenceScore = asNumber(confluence.confluence_score);
  const confluenceLevel = String(confluence.confluence_level ?? "mixed");
  const dominantPath = String(confluence.dominant_path ?? "no_edge");
  const summary = String(confluence.confluence_summary ?? "多源共振层用于判断当前主路径是否获得价格、成交量、宽度、信用、期权、flow、新闻和历史相似情景共同支持。");

  return (
    <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
      <div className="flex flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Market Alert & Confluence</div>
          <h2 className="mt-1 text-xl font-semibold text-white">{selected.symbol} 强预警与多源共振</h2>
          <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-400">
            这是预测确认层，只回答“当前路径有没有强预警和多源共振”，不是交易信号，也不是买卖建议。
          </p>
        </div>
        <div className="flex flex-wrap gap-2">
          <StatusBadge status={alertLevel} label={cnAlertLevel(alertLevel)} />
          <StatusBadge status={confluenceLevel} label={`共振：${cnConfluenceLevel(confluenceLevel)}`} />
          <StatusBadge status={dominantPath} label={`主导路径：${cnDominantPath(dominantPath)}`} />
        </div>
      </div>

      <div className="mt-4 grid gap-4 lg:grid-cols-[0.9fr_1.1fr]">
        <div className="rounded-lg border border-white/10 bg-black/20 p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Strongest Alert</div>
          <div className="mt-2 text-2xl font-semibold text-white">{cnAlertType(alertType)}</div>
          <div className="mt-4 grid gap-3 sm:grid-cols-3">
            <Metric label="预警强度" value={cnAlertLevel(alertLevel)} />
            <Metric label="预警评分" value={formatScore(alertScore)} />
            <Metric label="验证状态" value={String(topAlert.validation_status ?? "not_yet_validated")} />
          </div>
          <p className="mt-4 text-sm leading-6 text-slate-400">
            {String(topAlert.confidence ?? "当前预警仍需要前向验证。强预警必须由多个来源共同确认，不能由单一指标触发。")}
          </p>
        </div>

        <div className="rounded-lg border border-white/10 bg-black/20 p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Confluence Score</div>
          <div className="mt-2 flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
            <div className="text-4xl font-semibold text-cyan-100">{formatScore(confluenceScore)}</div>
            <div className="text-sm text-slate-400">主导路径：{cnDominantPath(dominantPath)}</div>
          </div>
          <p className="mt-4 text-sm leading-6 text-slate-300">{summary}</p>
          <div className="mt-4 grid gap-2 sm:grid-cols-3">
            <Metric label="主路径确认价" value={formatPrice(asRecord(relatedLevels.primary_confirmation_level).price)} />
            <Metric label="主路径失效价" value={formatPrice(asRecord(relatedLevels.primary_invalidation_level).price)} />
            <Metric label="风险路径接管价" value={formatPrice(asRecord(relatedLevels.risk_scenario_activation_level).price)} />
          </div>
        </div>
      </div>

      <div className="mt-4 grid gap-4 lg:grid-cols-2">
        <MiniEvidenceList title="最重要支持证据" tone="supportive" items={support} empty="暂无足够多源支持证据" />
        <MiniEvidenceList title="最重要冲突证据" tone="conflicting" items={conflict} empty="暂无明显冲突证据" />
      </div>

      <div className="mt-4 grid gap-4 lg:grid-cols-2">
        <SimpleList title="需要确认" items={required} empty="暂无额外确认条件" />
        <SimpleList title="路径失效 / 切换条件" items={invalidation} empty="暂无明确失效条件" />
      </div>
    </section>
  );
}

function MiniEvidenceList({
  title,
  tone,
  items,
  empty,
}: {
  title: string;
  tone: "supportive" | "conflicting";
  items: AnyRecord[];
  empty: string;
}) {
  const color = tone === "supportive" ? "text-emerald-200" : "text-rose-200";
  return (
    <div className="rounded-lg border border-white/10 bg-white/[0.03] p-4">
      <h3 className="text-sm font-semibold text-white">{title}</h3>
      <div className="mt-3 space-y-2">
        {items.length ? (
          items.slice(0, 5).map((item, index) => (
            <div key={`${evidenceTitle(item)}-${index}`} className="rounded-lg border border-white/10 bg-black/20 p-3">
              <div className="flex items-center justify-between gap-3">
                <div className={`text-sm font-semibold ${color}`}>{evidenceTitle(item)}</div>
                {asNumber(item.score) !== null ? <div className="text-xs text-slate-400">{formatScore(asNumber(item.score))}</div> : null}
              </div>
              <p className="mt-1 text-xs leading-5 text-slate-400">{evidenceDetail(item)}</p>
            </div>
          ))
        ) : (
          <div className="text-sm text-slate-400">{empty}</div>
        )}
      </div>
    </div>
  );
}

function SimpleList({ title, items, empty }: { title: string; items: string[]; empty: string }) {
  return (
    <div className="rounded-lg border border-white/10 bg-white/[0.03] p-4">
      <h3 className="text-sm font-semibold text-white">{title}</h3>
      <ul className="mt-3 space-y-2 text-sm leading-6 text-slate-300">
        {items.length ? items.slice(0, 6).map((item) => <li key={item}>· {item}</li>) : <li>{empty}</li>}
      </ul>
    </div>
  );
}

function EvidenceCard({
  title,
  tone,
  items,
  empty,
}: {
  title: string;
  tone: "supportive" | "conflicting";
  items: Array<{ name: string; score?: number; detail?: string }>;
  empty: string;
}) {
  const toneClass = tone === "supportive" ? "text-emerald-200" : "text-rose-200";
  return (
    <div className="rounded-xl border border-white/10 bg-[#101819] p-5">
      <div className="text-xs uppercase tracking-[0.22em] text-slate-500">{tone === "supportive" ? "Supporting Signals" : "Conflicting Signals"}</div>
      <h3 className="mt-1 text-lg font-semibold text-white">{title}</h3>
      <div className="mt-4 space-y-3">
        {items.length ? (
          items.slice(0, 6).map((item) => (
            <div key={`${item.name}-${item.detail}`} className="rounded-lg border border-white/10 bg-black/20 p-3">
              <div className="flex items-center justify-between gap-3">
                <div className={`text-sm font-semibold ${toneClass}`}>{item.name}</div>
                {typeof item.score === "number" ? <div className="text-xs text-slate-400">{Math.round(item.score * 100)}%</div> : null}
              </div>
              <p className="mt-1 text-xs leading-5 text-slate-400">{item.detail ?? "无详细说明"}</p>
            </div>
          ))
        ) : (
          <div className="text-sm text-slate-400">{empty}</div>
        )}
      </div>
    </div>
  );
}

function HorizonTable({ selected }: { selected: SimulatedSymbolPaths | undefined }) {
  const rows = (selected?.horizon_summary ?? selected?.prediction_horizons ?? {}) as Record<string, unknown>;
  return (
    <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
      <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Forecast Horizons</div>
      <h2 className="mt-1 text-xl font-semibold text-white">未来周期概率摘要</h2>
      <div className="mt-4 grid gap-3 md:grid-cols-5">
        {HORIZON_ORDER.map((horizon) => {
          const row = asRecord(rows[horizon]);
          return (
            <div key={horizon} className="rounded-lg border border-white/10 bg-black/20 p-3">
              <div className="text-sm font-semibold text-white">{horizon}</div>
              <div className="mt-3 space-y-2 text-xs text-slate-400">
                <div className="flex justify-between gap-2">
                  <span>期望收益</span>
                  <span className="font-semibold text-slate-100">{formatSignedPercent(row.expected_return)}</span>
                </div>
                <div className="flex justify-between gap-2">
                  <span>上行概率</span>
                  <span className="text-emerald-200">{formatPercent(row.up_probability)}</span>
                </div>
                <div className="flex justify-between gap-2">
                  <span>下行概率</span>
                  <span className="text-rose-200">{formatPercent(row.down_probability)}</span>
                </div>
              </div>
              <p className="mt-3 text-xs leading-5 text-slate-500">{String(row.risk_note ?? row.expected_direction ?? "前向验证中")}</p>
            </div>
          );
        })}
      </div>
    </section>
  );
}

function HistoricalAnalogs({ dashboard, symbol }: { dashboard: PredictionDashboard; symbol: string }) {
  const report = dashboard.analogs?.[symbol];
  const cases: HistoricalAnalogCase[] = report?.top_similar_cases ?? [];
  const distribution = asRecord(report?.historical_distribution);

  return (
    <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Historical Analogs</div>
          <h2 className="mt-1 text-xl font-semibold text-white">历史相似情景</h2>
        </div>
        <StatusBadge
          status={report?.low_sample_warning ? "weak" : report?.interpretation?.historical_support}
          label={report?.low_sample_warning ? "样本偏少" : `样本数 ${report?.sample_count ?? "数据缺失"}`}
        />
      </div>
      <div className="mt-4 grid gap-3 lg:grid-cols-[1fr_1fr]">
        <div className="grid gap-3 sm:grid-cols-3">
          <Metric label="5d 均值" value={formatSignedPercent(distribution.avg_return_5d)} />
          <Metric label="20d 均值" value={formatSignedPercent(distribution.avg_return_20d)} />
          <Metric label="60d 均值" value={formatSignedPercent(distribution.avg_return_60d)} />
        </div>
        <p className="rounded-lg border border-white/10 bg-black/20 p-3 text-sm leading-6 text-slate-400">
          历史相似只用于解释和条件分布，不等于未来会重复。若与前向验证冲突，以前向验证为准。
        </p>
      </div>

      <div className="mt-4 grid gap-3 md:grid-cols-2 xl:grid-cols-5">
        {cases.slice(0, 5).map((item) => (
          <div key={`${item.date}-${item.similarity_score}`} className="rounded-lg border border-white/10 bg-black/20 p-3">
            <div className="flex items-start justify-between gap-2">
              <div>
                <div className="font-semibold text-white">{item.date}</div>
                <div className="text-xs text-slate-500">{item.regime}</div>
              </div>
              <div className="text-sm font-semibold text-cyan-200">{formatPercent(item.similarity_score, 0)}</div>
            </div>
            <div className="mt-3 space-y-1 text-xs text-slate-400">
              <div>5d：{formatSignedPercent(item.forward_return_5d)}</div>
              <div>20d：{formatSignedPercent(item.forward_return_20d)}</div>
              <div>最大不利：{formatSignedPercent(item.max_adverse_excursion)}</div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

function DataQuality({ dashboard }: { dashboard: PredictionDashboard }) {
  const report = dashboard.data_quality_report;
  const categories = report?.coverage_categories ?? {};
  const categoryRows = Object.entries(categories).slice(0, 10);

  return (
    <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Data Quality</div>
          <h2 className="mt-1 text-xl font-semibold text-white">数据质量</h2>
        </div>
        <div className="text-3xl font-semibold text-emerald-200">{formatScore(report?.summary?.data_completeness_score)}</div>
      </div>
      <div className="mt-4 grid gap-2 md:grid-cols-5">
        {categoryRows.map(([name, item]) => (
          <div key={name} className="rounded-lg border border-white/10 bg-black/20 p-3">
            <div className="text-xs uppercase tracking-[0.14em] text-slate-500">{name}</div>
            <div className="mt-2">
              <StatusBadge status={item.status} label={item.status === "proxy" ? "proxy only" : item.status} />
            </div>
          </div>
        ))}
      </div>
      <p className="mt-4 text-sm text-slate-400">
        缺失或 proxy 数据会限制模型可信度，不会被显示成 0% 或假装已接入。
      </p>
    </section>
  );
}

function ForecastAccuracy({ dashboard }: { dashboard: PredictionDashboard }) {
  const scorecard = dashboard.forecast_accuracy_scorecard;
  const counts = scorecard?.sample_counts ?? {};
  const validation = getValidationStandards(dashboard);
  const warning =
    scorecard?.validation_warning ??
    "当前预测准确度仍未被前向样本验证，不能称为 high precision / stable alpha / validated forecasting system。";
  return (
    <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Forecast Accuracy</div>
          <h2 className="mt-1 text-xl font-semibold text-white">前向验证状态</h2>
        </div>
        <StatusBadge status={validation.highPrecisionStatus} label={cnValidationStatus(validation.highPrecisionStatus)} />
      </div>
      <div className="mt-4 grid gap-3 sm:grid-cols-3 lg:grid-cols-7">
        <Metric label="总记录" value={String(counts.total_forecasts ?? 0)} />
        <Metric label="待回填" value={String(counts.pending_forecasts ?? 0)} />
        <Metric label="3d 完成" value={String(counts.completed_3d ?? 0)} />
        <Metric label="5d 完成" value={String(counts.completed_5d ?? 0)} />
        <Metric label="10d 完成" value={String(counts.completed_10d ?? 0)} />
        <Metric label="20d 完成" value={String(counts.completed_20d ?? 0)} />
        <Metric label="60d 完成" value={String(counts.completed_60d ?? 0)} />
      </div>
      <div className="mt-3">
        <StatusBadge status={scorecard?.current_evidence_level} label={`证据等级：${cnValidationStatus(scorecard?.current_evidence_level)}`} />
      </div>
      <div className="mt-4 rounded-lg border border-amber-400/20 bg-amber-400/[0.07] p-3 text-sm leading-6 text-amber-100">
        {warning}
      </div>
    </section>
  );
}

function ModelLeaderboard({ dashboard }: { dashboard: PredictionDashboard }) {
  const models = getModelList(dashboard);
  const validation = getValidationStandards(dashboard);

  return (
    <section className="rounded-xl border border-white/10 bg-[#101819] p-5">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Model Leaderboard</div>
          <h2 className="mt-1 text-xl font-semibold text-white">模型验证看板</h2>
        </div>
        <StatusBadge status="active_model" label={`Active: ${validation.activeModel}`} />
      </div>
      <div className="mt-4 overflow-x-auto">
        <table className="min-w-full text-left text-sm">
          <thead className="border-b border-white/10 text-xs uppercase tracking-[0.16em] text-slate-500">
            <tr>
              <th className="py-3 pr-4">模型</th>
              <th className="py-3 pr-4">角色</th>
              <th className="py-3 pr-4">状态</th>
              <th className="py-3 pr-4">待验证</th>
              <th className="py-3 pr-4">完成样本</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/10">
            {models.map((model) => (
              <tr key={String(model.model_version)} className="text-slate-300">
                <td className="py-3 pr-4 font-semibold text-white">{String(model.model_version)}</td>
                <td className="py-3 pr-4">{String(model.role ?? "数据缺失")}</td>
                <td className="py-3 pr-4">
                  <StatusBadge status={String(model.promotion_status ?? model.status)} label={cnValidationStatus(String(model.promotion_status ?? model.status))} />
                </td>
                <td className="py-3 pr-4">{String(model.pending_forecasts ?? 0)}</td>
                <td className="py-3 pr-4">{String(model.completed_forecasts ?? 0)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

function StockEvidenceList({
  title,
  items,
  tone,
  empty,
}: {
  title: string;
  items: string[];
  tone: "supportive" | "conflicting" | "neutral";
  empty: string;
}) {
  const toneClass =
    tone === "supportive"
      ? "border-emerald-400/20 bg-emerald-400/[0.06] text-emerald-100"
      : tone === "conflicting"
        ? "border-rose-400/20 bg-rose-400/[0.06] text-rose-100"
        : "border-slate-500/20 bg-slate-500/[0.06] text-slate-200";
  return (
    <div className="rounded-xl border border-white/10 bg-black/20 p-4">
      <div className="text-xs uppercase tracking-[0.18em] text-slate-500">{title}</div>
      <div className="mt-3 space-y-2">
        {(items.length ? items : [empty]).slice(0, 6).map((item) => (
          <div key={item} className={`rounded-lg border px-3 py-2 text-xs leading-5 ${toneClass}`}>
            {item}
          </div>
        ))}
      </div>
    </div>
  );
}


function StockPredictionSection({ dashboard }: { dashboard: PredictionDashboard }) {
  const stockDashboard = asRecord(dashboard.stock_prediction_dashboard);
  const topStockPayload = asRecord(stockDashboard.top_stock_candidates ?? dashboard.top_stock_candidates);
  const topCandidates = Array.isArray(topStockPayload.top_candidates)
    ? topStockPayload.top_candidates.map((item) => asRecord(item))
    : [];
  const radarCommand = asRecord(topStockPayload.command_center);
  const symbols = asRecord(stockDashboard.symbols);
  const rows = useMemo(() => Object.entries(symbols).slice(0, 50), [symbols]);
  const [query, setQuery] = useState("");
  const [selectedStock, setSelectedStock] = useState(rows[0]?.[0] ?? "");
  const filteredRows = useMemo(() => {
    const q = query.trim().toUpperCase();
    if (!q) return rows;
    return rows.filter(([symbol, raw]) => {
      const payload = asRecord(raw);
      return symbol.toUpperCase().includes(q) || String(payload.company_name ?? "").toUpperCase().includes(q);
    });
  }, [query, rows]);

  useEffect(() => {
    if (!rows.length) return;
    if (!rows.some(([symbol]) => symbol === selectedStock)) {
      setSelectedStock(rows[0][0]);
    }
  }, [rows, selectedStock]);

  if (!rows.length) return null;

  const summary = asRecord(stockDashboard.summary);
  const selectedEntry = rows.find(([symbol]) => symbol === selectedStock) ?? filteredRows[0] ?? rows[0];
  const selectedSymbol = selectedEntry?.[0] ?? rows[0][0];
  const selected = asRecord(selectedEntry?.[1]);
  const selectedRanking = asRecord(selected.scenario_ranking);
  const selectedPrimary = asRecord(selectedRanking.primary);
  const selectedSecondary = asRecord(selectedRanking.secondary);
  const selectedRisk = asRecord(selectedRanking.risk);
  const selectedContext = asRecord(selected.market_context_for_stock);
  const selectedConfluence = asRecord(selected.stock_confluence);
  const moduleScores = Object.entries(asRecord(selectedConfluence.module_scores));
  const selectedAlerts = asRecord(selected.stock_alerts);
  const strongestAlert = asRecord(selectedAlerts.strongest_alert);
  const selectedAnalogs = asRecord(selected.historical_analogs);
  const selectedLevels = asRecord(asRecord(selected.forecast_price_levels).trigger_levels);
  const priceTable = asRecord(asRecord(selected.forecast_price_levels).forecast_price_table);
  const dataQuality = asRecord(selected.data_quality);
  const support = asStringArray(selectedConfluence.supporting_evidence);
  const conflict = asStringArray(selectedConfluence.conflicting_evidence);
  const missing = asStringArray(selectedConfluence.missing_evidence).length
    ? asStringArray(selectedConfluence.missing_evidence)
    : asStringArray(selected.missing_data);

  return (
    <section className="rounded-2xl border border-white/10 bg-[#101819] p-5">
      <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Stock Prediction Module</div>
          <h2 className="mt-1 text-xl font-semibold text-white">大盘环境下的个股雷达</h2>
          <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-400">
            页面先判断大盘，再看个股。个股路径必须经过“大盘背景 → 板块过滤 → 个股证据”的层级确认；缺失的新闻、财报、基本面和个股期权会降低置信度，不会被伪造成可用数据。
          </p>
        </div>
        <div className="flex flex-wrap gap-2">
          <StatusBadge status="not_yet_validated" label="个股模块：尚未前向验证" />
          <StatusBadge status="active_model" label={`模型：${String(stockDashboard.model_version ?? "stock_baseline_v1")}`} />
        </div>
      </div>

      <div className="mt-5 rounded-xl border border-cyan-300/20 bg-cyan-300/[0.06] p-4">
        <div className="flex flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
          <div>
            <div className="text-xs uppercase tracking-[0.22em] text-cyan-200/70">Next-Day Stock Radar Command Center</div>
            <h3 className="mt-1 text-2xl font-semibold text-white">次日高弹性股票候选雷达</h3>
            <p className="mt-2 max-w-4xl text-sm leading-6 text-slate-300">
              先筛选明天最值得盯的候选，再点开单股详情。雷达只判断概率路径、波动区间和证据共振，不提供买卖、仓位或止损建议。
            </p>
          </div>
          <div className="grid min-w-[260px] grid-cols-2 gap-3">
            <Metric label="雷达状态" value={String(radarCommand.radar_status ?? "not_yet_validated")} />
            <Metric label="Top 1" value={String(radarCommand.top_candidate ?? "数据缺失")} />
            <Metric label="Top 3" value={Array.isArray(radarCommand.top3_candidates) ? radarCommand.top3_candidates.join(" / ") : "数据缺失"} />
            <Metric label="验证状态" value={String(radarCommand.validation_status ?? "not_yet_validated")} />
          </div>
        </div>

        <div className="mt-4 overflow-x-auto">
          <table className="w-full min-w-[1120px] text-left text-sm">
            <thead className="text-xs uppercase tracking-[0.14em] text-slate-500">
              <tr>
                <th className="py-2 pr-3">Rank</th>
                <th className="py-2 pr-3">Ticker</th>
                <th className="py-2 pr-3">类型</th>
                <th className="py-2 pr-3">雷达分</th>
                <th className="py-2 pr-3">弹性</th>
                <th className="py-2 pr-3">共振</th>
                <th className="py-2 pr-3">催化</th>
                <th className="py-2 pr-3">风险</th>
                <th className="py-2 pr-3">次日区间</th>
                <th className="py-2 pr-3">触发价</th>
                <th className="py-2 pr-3">失效价</th>
                <th className="py-2 pr-3">原因</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-white/10">
              {topCandidates.slice(0, 20).map((candidate) => {
                const ticker = String(candidate.ticker ?? "");
                return (
                  <tr
                    key={`${candidate.rank}-${ticker}`}
                    className="cursor-pointer text-slate-200 transition hover:bg-white/[0.04]"
                    onClick={() => ticker && setSelectedStock(ticker)}
                  >
                    <td className="py-2 pr-3 text-slate-400">{String(candidate.rank ?? "-")}</td>
                    <td className="py-2 pr-3 font-semibold text-white">{ticker}</td>
                    <td className="py-2 pr-3">{cnCandidateType(String(candidate.candidate_type ?? ""))}</td>
                    <td className="py-2 pr-3 text-cyan-100">{formatScore(asNumber(candidate.final_radar_score))}</td>
                    <td className="py-2 pr-3">{formatScore(asNumber(candidate.elasticity_score))}</td>
                    <td className="py-2 pr-3">{formatScore(asNumber(candidate.confluence_score))}</td>
                    <td className="py-2 pr-3">{formatScore(asNumber(candidate.catalyst_score))}</td>
                    <td className="py-2 pr-3 text-amber-100">{formatScore(asNumber(candidate.risk_score))}</td>
                    <td className="py-2 pr-3">{formatPriceRange(candidate.expected_next_day_range)}</td>
                    <td className="py-2 pr-3 text-emerald-100">{formatPrice(candidate.upside_trigger_level)}</td>
                    <td className="py-2 pr-3 text-rose-100">{formatPrice(candidate.invalidation_level)}</td>
                    <td className="max-w-[300px] py-2 pr-3 text-xs leading-5 text-slate-400">{String(candidate.one_line_reason ?? "")}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          {!topCandidates.length ? (
            <div className="py-6 text-sm text-slate-400">暂无 Top Candidates。请等待 GitHub Actions 生成 top-stock-candidates.json。</div>
          ) : null}
        </div>
        <div className="mt-3 flex flex-wrap gap-2 text-xs text-slate-400">
          <StatusBadge status="not_yet_validated" label="雷达仍处于前向验证期" />
          <span>新闻 / 财报 / 个股期权缺失时，catalyst_score 和置信度会被压低。</span>
        </div>
      </div>

      <div className="mt-5 grid gap-4 lg:grid-cols-[minmax(0,1fr)_320px]">
        <div>
          <label className="text-xs uppercase tracking-[0.18em] text-slate-500" htmlFor="stock-selector">
            Stock Selector
          </label>
          <input
            id="stock-selector"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="搜索 ticker，例如 JD / KC / NVDA / TSLA / AMD / AAPL"
            className="mt-2 w-full rounded-xl border border-white/10 bg-black/30 px-4 py-3 text-sm text-white outline-none transition placeholder:text-slate-600 focus:border-cyan-300/60"
          />
          <p className="mt-2 text-xs leading-5 text-slate-500">
            静态页面只能在已生成的 universe 中切换。新增股票请修改 config/stock_watchlist.json，或在 GitHub Actions 手动运行时填写 ticker_list。
          </p>
        </div>
        <div className="rounded-xl border border-white/10 bg-black/20 p-4 text-sm text-slate-300">
          <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Universe</div>
          <div className="mt-2 grid grid-cols-2 gap-3">
            <Metric label="已生成股票" value={String(summary.watchlist_size ?? rows.length)} />
            <Metric label="可用股票" value={String(summary.supported_symbols ?? rows.length)} />
          </div>
        </div>
      </div>

      <div className="mt-4 grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
        {(filteredRows.length ? filteredRows : rows).map(([symbol, raw]) => {
          const payload = asRecord(raw);
          const ranking = asRecord(payload.scenario_ranking);
          const primary = asRecord(ranking.primary);
          const secondary = asRecord(ranking.secondary);
          const risk = asRecord(ranking.risk);
          const context = asRecord(payload.market_context_for_stock);
          const confluence = asRecord(payload.stock_confluence);
          const quality = asRecord(payload.data_quality);
          const logo = String(payload.logo ?? "");
          const selectedCard = selectedSymbol === symbol;
          return (
            <button
              key={symbol}
              type="button"
              onClick={() => setSelectedStock(symbol)}
              className={`rounded-xl border p-4 text-left transition hover:-translate-y-0.5 hover:border-cyan-300/50 ${
                selectedCard ? "border-cyan-300/70 bg-cyan-300/[0.08]" : "border-white/10 bg-black/20"
              }`}
            >
              <div className="flex items-start justify-between gap-3">
                <div className="flex items-center gap-3">
                  {logo ? (
                    <img src={logo} alt={`${symbol} logo`} className="h-10 w-10 rounded-full bg-white object-contain p-1" />
                  ) : (
                    <div className="grid h-10 w-10 place-items-center rounded-full bg-white text-xs font-black text-slate-950">{symbol}</div>
                  )}
                  <div>
                    <div className="text-lg font-semibold text-white">{symbol}</div>
                    <div className="text-xs text-slate-500">{String(payload.company_name ?? symbol)}</div>
                  </div>
                </div>
                <StatusBadge status={String(payload.data_status ?? "missing")} label={String(payload.data_status ?? "missing")} />
              </div>
              <div className="mt-4 grid grid-cols-2 gap-3 text-sm">
                <Metric label="当前价格" value={formatPrice(payload.current_price)} />
                <Metric label="Benchmark" value={String(payload.benchmark ?? "QQQ")} />
                <Metric label="主路径" value={String(primary.label ?? cnScenario(String(primary.scenario ?? "")))} />
                <Metric label="主路径概率" value={formatPercent(primary.probability, 1)} />
                <Metric label="第二路径" value={String(secondary.label ?? cnScenario(String(secondary.scenario ?? "")))} />
                <Metric label="风险路径" value={String(risk.label ?? cnScenario(String(risk.scenario ?? "")))} />
                <Metric label="共振评分" value={formatScore(asNumber(confluence.stock_confluence_score))} />
                <Metric label="数据质量" value={formatScore(asNumber(quality.score))} />
              </div>
              <div className="mt-3 text-xs leading-5 text-slate-400">
                大盘背景：{String(context.context ?? "数据缺失")}；验证：{String(payload.validation_status ?? "not_yet_validated")}
              </div>
            </button>
          );
        })}
      </div>

      <div className="mt-5 grid gap-4 xl:grid-cols-[minmax(0,1fr)_340px]">
        <div className="rounded-xl border border-white/10 bg-black/20 p-4">
          <div className="flex flex-wrap items-start justify-between gap-3">
            <div>
              <div className="text-xs uppercase tracking-[0.2em] text-slate-500">Stock Command Center</div>
              <h3 className="mt-1 text-2xl font-semibold text-white">{selectedSymbol} 个股详细分析</h3>
              <p className="mt-2 text-sm leading-6 text-slate-300">
                {selectedSymbol} 当前主路径是 {String(selectedPrimary.label ?? cnScenario(String(selectedPrimary.scenario ?? "")))}（{formatPercent(selectedPrimary.probability, 1)}），
                第二路径是 {String(selectedSecondary.label ?? cnScenario(String(selectedSecondary.scenario ?? "")))}。
                大盘背景为 {String(selectedContext.context ?? "数据缺失")}，个股多源共振 {formatScore(asNumber(selectedConfluence.stock_confluence_score))}。
                该模块仍是 not_yet_validated，只用于概率路径解释，不是买卖建议。
              </p>
            </div>
            <div className="flex flex-wrap gap-2">
              <StatusBadge status={String(selectedConfluence.confluence_level ?? "mixed")} label={`共振：${String(selectedConfluence.confluence_level ?? "mixed")}`} />
              <StatusBadge status={String(strongestAlert.alert_level ?? "NO_ALERT")} label={`预警：${cnAlertLevel(String(strongestAlert.alert_level ?? "NO_ALERT"))}`} />
            </div>
          </div>

          <div className="mt-4 grid gap-4 lg:grid-cols-[minmax(0,1fr)_280px]">
            <StockPathChart selected={selected} />
            <div className="rounded-xl border border-white/10 bg-white/[0.03] p-4">
              <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Scenario Ranking</div>
              <div className="mt-3 space-y-3 text-sm">
                <Metric label="主路径" value={`${String(selectedPrimary.label ?? cnScenario(String(selectedPrimary.scenario ?? "")))} / ${formatPercent(selectedPrimary.probability, 1)}`} />
                <Metric label="第二路径" value={`${String(selectedSecondary.label ?? cnScenario(String(selectedSecondary.scenario ?? "")))} / ${formatPercent(selectedSecondary.probability, 1)}`} />
                <Metric label="风险路径" value={`${String(selectedRisk.label ?? cnScenario(String(selectedRisk.scenario ?? "")))} / ${formatPercent(selectedRisk.probability, 1)}`} />
              </div>
            </div>
          </div>

          <div className="mt-4 overflow-x-auto">
            <table className="w-full min-w-[760px] text-left text-sm">
              <thead className="text-xs uppercase tracking-[0.14em] text-slate-500">
                <tr>
                  <th className="py-2 pr-3">??</th>
                  <th className="py-2 pr-3">综合预期</th>
                  <th className="py-2 pr-3">主路径价</th>
                  <th className="py-2 pr-3">第二路径价</th>
                  <th className="py-2 pr-3">风险路径价</th>
                  <th className="py-2 pr-3">??</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-white/10">
                {PRICE_LEVEL_HORIZON_ORDER.map((horizon) => {
                  const row = asRecord(priceTable[horizon]);
                  return (
                    <tr key={horizon} className="text-slate-200">
                      <td className="py-2 pr-3 text-slate-400">{horizon}</td>
                      <td className="py-2 pr-3">{formatPrice(row.expected_price)}</td>
                      <td className="py-2 pr-3 text-emerald-200">{formatPrice(row.primary_scenario_price)}</td>
                      <td className="py-2 pr-3 text-cyan-200">{formatPrice(row.secondary_scenario_price)}</td>
                      <td className="py-2 pr-3 text-rose-200">{formatPrice(row.risk_scenario_price)}</td>
                      <td className="py-2 pr-3">{formatPrice(row.lower_confidence_price)} - {formatPrice(row.upper_confidence_price)}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>

        <aside className="space-y-3">
          <div className="rounded-xl border border-white/10 bg-black/20 p-4">
            <div className="text-xs uppercase tracking-[0.2em] text-slate-500">Key Levels</div>
            <div className="mt-3 grid grid-cols-2 gap-3 text-sm">
              <Metric label="确认价" value={formatPrice(asRecord(selectedLevels.primary_confirmation_level).price)} />
              <Metric label="失效价" value={formatPrice(asRecord(selectedLevels.primary_invalidation_level).price)} />
              <Metric label="风险接管" value={formatPrice(asRecord(selectedLevels.risk_scenario_activation_level).price)} />
              <Metric label="趋势修复" value={formatPrice(asRecord(selectedLevels.trend_repair_confirmation_level).price)} />
              <Metric label="突破价" value={formatPrice(asRecord(selectedLevels.breakout_level).price)} />
              <Metric label="跌破价" value={formatPrice(asRecord(selectedLevels.breakdown_level).price)} />
              <Metric label="最近支撑" value={formatPrice(asRecord(selectedLevels.nearest_support).price)} />
              <Metric label="最近阻力" value={formatPrice(asRecord(selectedLevels.nearest_resistance).price)} />
            </div>
            <p className="mt-3 text-xs leading-5 text-amber-100">价格点位是概率路径参考，不是买卖建议。</p>
          </div>
          <div className="rounded-xl border border-white/10 bg-black/20 p-4">
            <div className="text-xs uppercase tracking-[0.2em] text-slate-500">Stock Alert</div>
            <div className="mt-2 text-lg font-semibold text-white">{String(strongestAlert.alert_type ?? "NO_ALERT")}</div>
            <div className="mt-1 text-sm text-slate-400">{String(strongestAlert.one_line_reason ?? "等待更多数据确认。")}</div>
            <div className="mt-3 grid grid-cols-2 gap-3">
              <Metric label="预警等级" value={cnAlertLevel(String(strongestAlert.alert_level ?? "NO_ALERT"))} />
              <Metric label="预警评分" value={formatScore(asNumber(strongestAlert.alert_score))} />
            </div>
          </div>
          <div className="rounded-xl border border-white/10 bg-black/20 p-4">
            <div className="text-xs uppercase tracking-[0.2em] text-slate-500">Data Quality</div>
            <div className="mt-3 grid grid-cols-2 gap-3 text-sm">
              <Metric label="??" value={String(dataQuality.price_available ?? false)} />
              <Metric label="成交量" value={String(dataQuality.volume_available ?? false)} />
              <Metric label="?? profile" value={String(dataQuality.company_profile ?? "missing")} />
              <Metric label="公司新闻" value={String(dataQuality.company_news ?? "missing")} />
              <Metric label="基本面" value={String(dataQuality.fundamentals ?? "missing")} />
              <Metric label="个股期权" value={String(dataQuality.single_stock_options ?? "missing")} />
            </div>
          </div>
          <div className="rounded-xl border border-white/10 bg-black/20 p-4">
            <div className="text-xs uppercase tracking-[0.2em] text-slate-500">Historical Analogs</div>
            <div className="mt-2 text-sm text-slate-300">
              支持度：{String(selectedAnalogs.analog_support ?? "low sample")} / 样本：{String(selectedAnalogs.sample_count ?? 0)}
            </div>
            <div className="mt-1 text-xs text-slate-500">历史相似只用于解释，不等于已验证 alpha。</div>
          </div>
        </aside>
      </div>

      <div className="mt-4 grid gap-3 lg:grid-cols-3">
        <StockEvidenceList title="支持主路径的证据" items={support} tone="supportive" empty="暂无足够支持证据" />
        <StockEvidenceList title="冲突证据" items={conflict} tone="conflicting" empty="暂无明显冲突证据" />
        <StockEvidenceList title="缺失 / proxy 数据" items={missing.length ? missing : ["无主要缺失项"]} tone="neutral" empty="无主要缺失项" />
      </div>

      <div className="mt-4 rounded-xl border border-white/10 bg-black/20 p-4">
        <div className="text-xs uppercase tracking-[0.2em] text-slate-500">Confluence Breakdown</div>
        <div className="mt-3 grid gap-3 md:grid-cols-2 xl:grid-cols-3">
          {moduleScores.map(([key, raw]) => {
            const module = asRecord(raw);
            return (
              <div key={key} className="rounded-lg border border-white/10 bg-white/[0.03] p-3">
                <div className="flex items-start justify-between gap-3">
                  <div className="text-sm font-semibold text-white">{stockModuleLabel(key)}</div>
                  <StatusBadge status={String(module.status ?? "missing")} label={String(module.status ?? "missing")} />
                </div>
                <div className="mt-2 text-xl font-semibold text-cyan-100">{formatScore(asNumber(module.score))}</div>
                <div className="mt-2 text-xs leading-5 text-slate-400">{String(module.evidence ?? "暂无证据")}</div>
                <div className="mt-1 text-xs leading-5 text-slate-500">{String(module.reason ?? "")}</div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}

function StockPathChart({ selected }: { selected: AnyRecord }) {
  const paths = asRecord(selected.simulated_paths);
  const dates = Array.isArray(paths.dates) ? paths.dates.map(String) : [];
  const series = [
    { key: "historical_price", label: "历史价格", color: "#d7e4e1", width: 2.1 },
    { key: "primary_path", label: "主路径", color: "#22c55e", width: 3.4 },
    { key: "secondary_path", label: "第二路径", color: "#38bdf8", width: 2.4 },
    { key: "risk_path", label: "风险路径", color: "#f87171", width: 2.0 },
  ];
  const valuesByKey: Record<string, Array<number | null>> = {};
  series.forEach((item) => {
    valuesByKey[item.key] = stockPathValues(paths[item.key]);
  });
  const allValues = Object.values(valuesByKey).flat().filter((value): value is number => typeof value === "number" && Number.isFinite(value));
  if (!dates.length || !allValues.length) {
    return <div className="rounded-xl border border-white/10 bg-black/20 p-4 text-sm text-slate-400">个股路径数据缺失。</div>;
  }
  const width = 760;
  const height = 320;
  const pad = 28;
  const min = Math.min(...allValues);
  const max = Math.max(...allValues);
  const span = Math.max(max - min, 0.01);
  const x = (index: number) => pad + (index / Math.max(dates.length - 1, 1)) * (width - pad * 2);
  const y = (value: number) => height - pad - ((value - min) / span) * (height - pad * 2);
  const makePath = (values: Array<number | null>) => {
    let d = "";
    values.forEach((value, index) => {
      if (value === null || !Number.isFinite(value)) return;
      d += `${d.endsWith(" ") || d === "" ? "M" : "L"}${x(index).toFixed(1)},${y(value).toFixed(1)} `;
    });
    return d.trim();
  };
  const historicalValues = stockPathValues(paths.historical_price);
  let currentIndex = -1;
  historicalValues.forEach((value, index) => {
    if (value !== null) currentIndex = index;
  });
  return (
    <div className="rounded-xl border border-white/10 bg-[#071111] p-4">
      <div className="mb-3 flex items-start justify-between gap-3">
        <div>
          <div className="text-xs uppercase tracking-[0.18em] text-slate-500">Stock Future Path</div>
          <div className="mt-1 text-lg font-semibold text-white">个股概率路径图</div>
        </div>
        <div className="text-xs leading-5 text-slate-500">主路径最突出，第二路径次之；风险路径保留。</div>
      </div>
      <svg viewBox={`0 0 ${width} ${height}`} className="h-[320px] w-full rounded-lg bg-black/20">
        <line x1={pad} y1={pad} x2={pad} y2={height - pad} stroke="#334155" strokeWidth="1" />
        <line x1={pad} y1={height - pad} x2={width - pad} y2={height - pad} stroke="#334155" strokeWidth="1" />
        {currentIndex >= 0 ? <line x1={x(currentIndex)} y1={pad} x2={x(currentIndex)} y2={height - pad} stroke="#94a3b8" strokeDasharray="4 5" /> : null}
        {series.map((item) => (
          <path key={item.key} d={makePath(valuesByKey[item.key] ?? [])} fill="none" stroke={item.color} strokeWidth={item.width} strokeLinecap="round" strokeLinejoin="round" />
        ))}
      </svg>
      <div className="mt-3 flex flex-wrap gap-3 text-xs text-slate-300">
        {series.map((item) => (
          <span key={item.key} className="inline-flex items-center gap-2">
            <span className="h-2 w-6 rounded-full" style={{ backgroundColor: item.color }} /> {item.label}
          </span>
        ))}
      </div>
    </div>
  );
}

function stockPathValues(value: unknown): Array<number | null> {
  if (!Array.isArray(value)) return [];
  return value.map((item) => (typeof item === "number" && Number.isFinite(item) ? item : null));
}

function stockModuleLabel(key: string): string {
  const map: Record<string, string> = {
    market_context: "大盘背景",
    sector_context: "板块过滤",
    price_structure: "价格结构",
    volume_structure: "成交量结构",
    relative_strength: "相对强弱",
    news_event: "新闻 / 事件",
    fundamentals_earnings: "基本面 / 财报",
    options_volatility: "期权 / 波动率",
    historical_analog: "历史相似",
  };
  return map[key] ?? key;
}

function ForecastCommandCenterCompact({
  dashboard,
  selected,
}: {
  dashboard: PredictionDashboard;
  selected: SimulatedSymbolPaths | undefined;
}) {
  if (!selected) return null;
  const validation = getValidationStandards(dashboard);
  const ranking = selected.scenario_ranking;
  const primary = getPrimary(selected);
  const secondary = getSecondary(selected);
  const tertiary = getTertiary(selected);
  const alerts = getSymbolAlerts(dashboard, selected);
  const strongestAlert = asRecord(alerts.strongest_alert);
  const confluence = getSymbolConfluence(dashboard, selected);
  const edgeStatus = getEdgeStatus(selected);
  const strongestSymbol = dashboard.overview?.strongest_symbol ?? selected.symbol;

  return (
    <section className="rounded-2xl border border-cyan-300/20 bg-[#0c1718] p-5 shadow-2xl shadow-black/30">
      <div className="grid gap-5 xl:grid-cols-[minmax(0,1.15fr)_0.85fr]">
        <div>
          <div className="text-xs uppercase tracking-[0.24em] text-cyan-200/80">Forecast Command Center</div>
          <h2 className="mt-2 text-2xl font-semibold text-white">预测指挥中心</h2>
          <p className="mt-3 max-w-4xl text-sm leading-6 text-slate-200">
            {buildCommandCenterSentence(dashboard, selected, alerts, confluence)}
          </p>
          <div className="mt-4 flex flex-wrap gap-2">
            <StatusBadge status={edgeStatus} label={cnEdgeStatus(edgeStatus)} />
            <StatusBadge status={validation.validatedStatus} label={cnValidationStatus(validation.validatedStatus)} />
            <StatusBadge
              status={String(strongestAlert.alert_level ?? "NO_ALERT")}
              label={cnAlertLevel(String(strongestAlert.alert_level ?? "NO_ALERT"))}
            />
          </div>
        </div>

        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 xl:grid-cols-2">
          <Metric label="最强指数" value={strongestSymbol} />
          <Metric label="Edge status" value={cnEdgeStatus(edgeStatus)} badge={edgeStatus} />
          <Metric label="模型可信度" value={formatScore(getConfidenceScore(selected))} />
          <Metric label="信号确认" value={formatScore(getConfirmationScore(selected))} />
          <Metric label="多源共振" value={formatScore(asNumber(confluence.confluence_score))} />
          <Metric label="前向验证" value={cnValidationStatus(validation.highPrecisionStatus)} badge={validation.highPrecisionStatus} />
        </div>
      </div>

      <div className="mt-5 grid gap-3 lg:grid-cols-3">
        <div className="rounded-xl border border-emerald-300/20 bg-emerald-300/[0.07] p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-emerald-200/80">最可能路径</div>
          <div className="mt-2 text-xl font-semibold text-white">{primary?.label ?? cnScenario(primary?.scenario)}</div>
          <div className="mt-2 text-3xl font-semibold text-emerald-200">{formatPercent(primary?.probability, 1)}</div>
          <p className="mt-3 text-xs leading-5 text-slate-300">{primary?.reason ?? "主路径理由数据缺失。"}</p>
        </div>
        <div className="rounded-xl border border-cyan-300/20 bg-cyan-300/[0.06] p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-cyan-200/80">第二路径</div>
          <div className="mt-2 text-xl font-semibold text-white">{secondary?.label ?? cnScenario(secondary?.scenario)}</div>
          <div className="mt-2 text-3xl font-semibold text-cyan-200">{formatPercent(secondary?.probability, 1)}</div>
          <p className="mt-3 text-xs leading-5 text-slate-300">
            主次差距：{formatGap(ranking?.primary_secondary_gap)}。{ranking?.close_call ? "路径分歧较大。" : "主路径有一定领先。"}
          </p>
        </div>
        <div className="rounded-xl border border-rose-300/20 bg-rose-300/[0.06] p-4">
          <div className="text-xs uppercase tracking-[0.18em] text-rose-200/80">风险路径</div>
          <div className="mt-2 text-xl font-semibold text-white">{tertiary?.label ?? cnScenario(tertiary?.scenario)}</div>
          <div className="mt-2 text-3xl font-semibold text-rose-200">{formatPercent(tertiary?.probability, 1)}</div>
          <p className="mt-3 text-xs leading-5 text-slate-300">{tertiary?.reason ?? "风险路径理由数据缺失。"}</p>
        </div>
      </div>

      <p className="mt-3 text-xs leading-5 text-amber-100">
        当前预测仍处于前向验证期。这里展示的是概率路径和情景价位，不是确定预测，也不是买卖建议。
      </p>
    </section>
  );
}

function getAlertOneLineReason(alert: AnyRecord): string {
  const support = normalizeEvidence(alert.supporting_evidence);
  const conflict = normalizeEvidence(alert.conflicting_evidence);
  const first = support[0] ?? conflict[0];
  if (first) return evidenceDetail(first);
  return String(alert.reason ?? alert.confidence ?? "等待更多数据确认。");
}

function AlertRail({
  dashboard,
  selected,
  className = "",
}: {
  dashboard: PredictionDashboard;
  selected: SimulatedSymbolPaths | undefined;
  className?: string;
}) {
  if (!selected) return null;
  const alerts = getSymbolAlerts(dashboard, selected);
  const rows = ALERT_TYPE_ORDER.map((type) => {
    const alert = getAlertByType(alerts, type);
    const affected = asStringArray(alert.affected_symbols);
    return {
      type,
      level: String(alert.alert_level ?? "NO_ALERT"),
      score: asNumber(alert.alert_score),
      affected,
      reason: getAlertOneLineReason(alert),
    };
  });

  return (
    <aside className={className}>
      <details className="rounded-2xl border border-white/10 bg-[#101819] p-4 xl:hidden">
        <summary className="cursor-pointer text-sm font-semibold text-white">今日预警摘要</summary>
        <div className="mt-3 space-y-2">
          {rows.map((row) => (
            <AlertRailRow key={row.type} row={row} />
          ))}
        </div>
      </details>

      <section className="hidden rounded-2xl border border-white/10 bg-[#101819] p-4 xl:sticky xl:top-5 xl:block">
        <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Alert Rail</div>
        <h3 className="mt-1 text-lg font-semibold text-white">今日预警</h3>
        <p className="mt-2 text-xs leading-5 text-slate-500">预警只显示摘要，详细解释已后置。</p>
        <div className="mt-3 space-y-2">
          {rows.map((row) => (
            <AlertRailRow key={row.type} row={row} />
          ))}
        </div>
      </section>
    </aside>
  );
}

function AlertRailRow({
  row,
}: {
  row: {
    type: string;
    level: string;
    score: number | null;
    affected: string[];
    reason: string;
  };
}) {
  return (
    <details className="rounded-xl border border-white/10 bg-black/20 p-3">
      <summary className="cursor-pointer list-none">
        <div className="flex items-start justify-between gap-3">
          <div>
            <div className="text-sm font-semibold text-slate-100">{cnAlertType(row.type)}</div>
            <div className="mt-1 text-xs text-slate-500">
              {formatScore(row.score)}
              {row.affected.length ? ` · ${row.affected.slice(0, 4).join(" / ")}` : ""}
            </div>
          </div>
          <StatusBadge status={row.level} label={cnAlertLevel(row.level)} />
        </div>
      </summary>
      <p className="mt-2 text-xs leading-5 text-slate-400">{row.reason}</p>
    </details>
  );
}

function DisclosureSection({
  title,
  subtitle,
  children,
  defaultOpen = false,
}: {
  title: string;
  subtitle?: string;
  children: ReactNode;
  defaultOpen?: boolean;
}) {
  return (
    <details open={defaultOpen} className="rounded-2xl border border-white/10 bg-[#0d1516] p-4">
      <summary className="cursor-pointer list-none">
        <div className="flex flex-col gap-1 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <div className="text-xs uppercase tracking-[0.22em] text-slate-500">Details</div>
            <h2 className="mt-1 text-lg font-semibold text-white">{title}</h2>
          </div>
          <span className="text-xs text-slate-500">点击展开 / 收起</span>
        </div>
        {subtitle ? <p className="mt-2 text-sm leading-6 text-slate-400">{subtitle}</p> : null}
      </summary>
      <div className="mt-4 flex flex-col gap-5">{children}</div>
    </details>
  );
}

export function MarketDashboard({ dashboard }: { dashboard: PredictionDashboard }) {
  const [data, setData] = useState(dashboard);
  const initialSymbol = dashboard.overview?.strongest_symbol && getSymbols(dashboard)[dashboard.overview.strongest_symbol]
    ? dashboard.overview.strongest_symbol
    : "SPY";
  const [selectedSymbol, setSelectedSymbol] = useState(initialSymbol);

  useEffect(() => {
    let active = true;
    const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
    const loadLatest = async () => {
      try {
        const response = await fetch(`${basePath}/prediction-dashboard.json?ts=${Date.now()}`, { cache: "no-store" });
        if (!response.ok) return;
        const nextData = (await response.json()) as PredictionDashboard;
        if (active) setData(nextData);
      } catch {
        // Keep the server-rendered snapshot if the static JSON cannot be refreshed.
      }
    };
    loadLatest();
    const interval = window.setInterval(loadLatest, 5 * 60 * 1000);
    return () => {
      active = false;
      window.clearInterval(interval);
    };
  }, []);

  const symbols = useMemo(() => getSymbolList(data), [data]);
  const selected = getSymbols(data)[selectedSymbol] ?? symbols[0];

  useEffect(() => {
    if (!selected && symbols[0]) {
      setSelectedSymbol(symbols[0].symbol);
    }
  }, [selected, symbols]);

  return (
    <main className="min-h-screen bg-[radial-gradient(circle_at_top_left,_rgba(20,184,166,0.16),_transparent_28rem),linear-gradient(180deg,#071111_0%,#0b1112_42%,#071111_100%)] px-4 py-5 text-slate-100 sm:px-6 lg:px-10">
      <div className="mx-auto flex max-w-7xl flex-col gap-5">
        <TerminalHeader dashboard={data} />
        <DataFreshnessBanner dashboard={data} />
        <ForecastCommandCenterCompact dashboard={data} selected={selected} />
        <IndexCards symbols={symbols} selectedSymbol={selected?.symbol ?? selectedSymbol} onSelect={setSelectedSymbol} />

        <div className="grid gap-5 xl:grid-cols-[minmax(0,1fr)_320px]">
          <AlertRail dashboard={data} selected={selected} className="xl:order-2" />
          <div className="flex flex-col gap-5 xl:order-1">
            <PredictionChart selected={selected} />
            <ForecastPriceLevelsPanel selected={selected} />
          </div>
        </div>

        <EvidenceSections dashboard={data} selected={selected} />
        <StockPredictionSection dashboard={data} />

        <DisclosureSection
          title="查看推理细节"
          subtitle="情景排序、新闻事件、周期概率和多源共振细节放在这里，默认后置，避免抢占第一屏。"
        >
          <ForecastSummary dashboard={data} selected={selected} />
          <ScenarioRankingPanel selected={selected} />
          <MarketAlertConfluencePanel dashboard={data} selected={selected} />
          <NewsEventIntelligencePanel dashboard={data} selected={selected} />
          <HorizonTable selected={selected} />
        </DisclosureSection>

        <DisclosureSection
          title="查看历史相似"
          subtitle="历史相似情景是解释层，不放在第一屏；它帮助理解当前路径，但不能替代前向验证。"
        >
          <HistoricalAnalogs dashboard={data} symbol={selected?.symbol ?? selectedSymbol} />
        </DisclosureSection>

        <DisclosureSection
          title="查看模型验证"
          subtitle="这里展示前向样本、命中率、baseline/challenger 和是否达到高精度标准。样本不足时必须保持 not_yet_validated。"
        >
          <ForecastAccuracy dashboard={data} />
          <ModelLeaderboard dashboard={data} />
        </DisclosureSection>

        <DisclosureSection
          title="查看数据质量"
          subtitle="数据源、proxy、missing、provider 状态属于审计层，默认放在页面底部。"
        >
          <DataQuality dashboard={data} />
        </DisclosureSection>
      </div>
    </main>
  );
}
