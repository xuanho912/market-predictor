from __future__ import annotations

from typing import Any

from app.services.data_providers.auto_download import DownloadedSeries
from scripts.providers.flow_provider import fetch_flow_bundle, render_flow_status_markdown


def fetch_flow_positioning_bundle(*, series_by_symbol: dict[str, DownloadedSeries]) -> dict[str, Any]:
    """Return proxy-only flow/positioning evidence.

    This provider intentionally does not claim true fund-flow or true positioning.
    It wraps the existing ETF/rotation proxy provider under the explicit v5 name
    requested by the dashboard contract.
    """
    bundle = fetch_flow_bundle(series_by_symbol=series_by_symbol)
    bundle["provider"] = "flow_positioning_proxy"
    bundle["version"] = "v5_flow_positioning_proxy"
    summary = bundle.setdefault("summary", {})
    summary["true_flow_available"] = False
    summary["proxy_only"] = True
    summary["flow_proxy_only"] = True
    for payload in (bundle.get("symbols") or {}).values():
        payload["true_flow_available"] = False
        payload["proxy_only"] = True
        payload["is_proxy"] = True
    return bundle


def render_flow_positioning_status_markdown(bundle: dict[str, Any]) -> str:
    return render_flow_status_markdown(bundle).replace(
        "# Flow / Positioning Proxy Status",
        "# Flow / Positioning Proxy Status",
        1,
    )

