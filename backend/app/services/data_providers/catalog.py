from __future__ import annotations

from dataclasses import dataclass

from app.services.feature_engineering.registry import FEATURE_GROUPS


@dataclass(frozen=True)
class ProviderSpec:
    provider_id: str
    feature_group: str
    required_coverage: tuple[str, ...]
    point_in_time_policy: str
    revision_policy: str

    def __post_init__(self) -> None:
        if self.feature_group not in FEATURE_GROUPS:
            raise ValueError(f"Unknown feature group: {self.feature_group}")


PROVIDER_CATALOG: tuple[ProviderSpec, ...] = (
    ProviderSpec("price_market_data", "price", ("index_ohlcv", "etf", "futures", "sector_indices", "factor_indices"), "exchange_timestamp", "adjustments_versioned"),
    ProviderSpec("volatility_surface", "volatility", ("vix", "vvix", "vix_futures_curve", "move", "implied_realized_vol", "skew", "tail_risk"), "exchange_timestamp", "vendor_snapshots_versioned"),
    ProviderSpec("credit_conditions", "credit", ("ig_oas", "hy_oas", "ccc_spread", "cds", "bank_cds", "leveraged_loans", "clo", "commercial_paper_spreads", "lending_standards"), "release_or_vendor_timestamp", "vintages_required"),
    ProviderSpec("rates_curve", "rates", ("fed_funds", "sofr", "3m", "2y", "5y", "10y", "30y", "real_rates", "inflation_expectations", "term_premium", "yield_curve"), "market_or_release_timestamp", "vintages_required_for_estimates"),
    ProviderSpec("liquidity_conditions", "liquidity", ("central_bank_balance_sheet", "bank_reserves", "reverse_repo", "tga", "repo_rates", "treasury_depth", "etf_discount_premium", "dollar_liquidity", "cross_currency_basis"), "release_or_vendor_timestamp", "vintages_required"),
    ProviderSpec("macro_vintages", "macro", ("gdp", "cpi", "pce", "ppi", "payrolls", "unemployment", "claims", "wages", "retail_sales", "industrial_production", "pmi", "ism", "building_permits", "consumer_confidence", "inventories"), "official_release_timestamp", "macro_vintages_required"),
    ProviderSpec("earnings_revisions", "earnings", ("eps_growth", "revenue_growth", "margins", "estimate_revisions", "earnings_surprises", "call_sentiment", "buybacks", "cash_flow_quality"), "vendor_timestamp", "estimate_history_required"),
    ProviderSpec("positioning_leverage", "positioning", ("margin_balance", "margin_debt", "cftc_cot", "cta", "risk_parity", "vol_control_funds", "etf_flows", "option_open_interest", "gamma_exposure", "short_interest"), "publication_timestamp", "publication_lag_required"),
    ProviderSpec("market_breadth", "breadth", ("advance_decline", "new_high_low", "pct_above_20_50_200d_ma", "equal_cap_weight", "small_large", "cyclical_defensive", "high_beta_low_vol"), "exchange_timestamp", "point_in_time_universe_required"),
    ProviderSpec("news_and_text", "news_text", ("central_bank_statements", "fomc", "earnings_calls", "announcements", "rating_reports", "filings", "headlines", "geopolitics", "social_media", "search_trends", "narrative_shifts"), "publication_timestamp", "edits_and_duplicates_versioned"),
    ProviderSpec("crypto_onchain", "onchain_crypto", ("btc_eth", "funding_rates", "open_interest", "liquidations", "stablecoin_supply", "exchange_net_flows", "active_addresses", "whale_wallets", "defi_liquidations"), "chain_or_exchange_timestamp", "finality_lag_documented"),
    ProviderSpec("alternative_data", "alternative_data", ("card_spending", "air_traffic", "hotels", "ports", "hiring", "app_activity", "ecommerce", "rent", "used_cars", "invoices", "sentiment"), "vendor_timestamp", "vendor_revision_policy_required"),
)
