"""Make the exported dashboard robust across GitHub Pages subpaths.

Next.js static export writes absolute asset URLs when a basePath is configured.
That is fragile for this project because the generated dashboard can be served
from the private repo path or from a separate public display repo. This script
keeps the generated data untouched, but rewrites static HTML so CSS/JS assets are
loaded relative to the current page. It also inlines the compiled CSS as a hard
fallback so the dashboard never degrades into unstyled HTML when Pages is served
from a different repository name.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CSS_LINK_RE = re.compile(
    r"<link(?=[^>]*\brel=[\"']stylesheet[\"'])(?=[^>]*\bhref=[\"']([^\"']+\.css(?:\?[^\"']*)?)[\"'])[^>]*>",
    re.IGNORECASE,
)
ASSET_URL_RE = re.compile(r"(?P<prefix>\b(?:href|src)=[\"'])(?P<url>/[^\"']+)(?P<suffix>[\"'])")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fix CSS/JS asset paths in a static dashboard export.")
    parser.add_argument("--site", default="frontend/out", help="Static site directory to patch.")
    return parser.parse_args()


def resolve_under_repo(path_value: str) -> Path:
    path = (REPO_ROOT / path_value).resolve()
    if not path.is_relative_to(REPO_ROOT):
        raise SystemExit(f"Refusing to patch a path outside repo: {path}")
    return path


def split_url(url: str) -> tuple[str, str]:
    for marker in ("?", "#"):
        if marker in url:
            path, rest = url.split(marker, 1)
            return path, marker + rest
    return url, ""


def site_file_from_url(site: Path, html_file: Path, url: str) -> Path | None:
    path_part, _ = split_url(url)
    if path_part.startswith(("http://", "https://", "data:")):
        return None
    if path_part.startswith("/"):
        parts = [part for part in path_part.strip("/").split("/") if part]
        candidates = [site.joinpath(*parts)]
        if parts and parts[0] != "_next":
            candidates.append(site.joinpath(*parts[1:]))
        for candidate in candidates:
            if candidate.exists() and candidate.is_file():
                return candidate
        return None
    candidate = (html_file.parent / path_part).resolve()
    if candidate.exists() and candidate.is_file() and candidate.is_relative_to(site):
        return candidate
    return None


def relative_asset_url(url: str) -> str:
    path_part, suffix = split_url(url)
    if not path_part.startswith("/"):
        return url
    parts = [part for part in path_part.strip("/").split("/") if part]
    if "_next" in parts:
        parts = parts[parts.index("_next") :]
    elif parts and parts[-1] in {"manifest.json", "sw.js", "favicon.ico", "icon.svg"}:
        parts = [parts[-1]]
    else:
        return url
    return "./" + "/".join(parts) + suffix


def inline_css(site: Path, html_file: Path, html: str) -> tuple[str, int]:
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        href = match.group(1)
        css_path = site_file_from_url(site, html_file, href)
        if css_path is None:
            return match.group(0)
        css = css_path.read_text(encoding="utf-8", errors="ignore")
        count += 1
        return f"<style data-inline-next-css=\"{css_path.name}\">\n{css}\n</style>"

    return CSS_LINK_RE.sub(replace, html), count


def rewrite_asset_paths(html: str) -> tuple[str, int]:
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        url = match.group("url")
        new_url = relative_asset_url(url)
        if new_url != url:
            count += 1
        return f"{match.group('prefix')}{new_url}{match.group('suffix')}"

    return ASSET_URL_RE.sub(replace, html), count


def patch_html_file(site: Path, html_file: Path) -> tuple[int, int]:
    html = html_file.read_text(encoding="utf-8", errors="ignore")
    html, css_count = inline_css(site, html_file, html)
    html, asset_count = rewrite_asset_paths(html)
    html_file.write_text(html, encoding="utf-8")
    return css_count, asset_count


def main() -> int:
    args = parse_args()
    site = resolve_under_repo(args.site)
    if not site.exists() or not site.is_dir():
        raise SystemExit(f"Static dashboard export is missing: {site}")

    html_files = sorted(site.rglob("*.html"))
    if not html_files:
        raise SystemExit(f"No HTML files found in static dashboard export: {site}")

    total_css = 0
    total_assets = 0
    for html_file in html_files:
        css_count, asset_count = patch_html_file(site, html_file)
        total_css += css_count
        total_assets += asset_count

    index_html = site / "index.html"
    if index_html.exists():
        html = index_html.read_text(encoding="utf-8", errors="ignore")
        if "data-inline-next-css" not in html:
            raise SystemExit("Static dashboard asset fix failed: index.html has no inlined CSS fallback.")
        if 'href="/' in html and "_next/" in html:
            raise SystemExit("Static dashboard asset fix failed: absolute _next href remains in index.html.")
        if 'src="/' in html and "_next/" in html:
            raise SystemExit("Static dashboard asset fix failed: absolute _next src remains in index.html.")

    print(
        "Static dashboard assets fixed: "
        f"{len(html_files)} html files, {total_css} css links inlined, {total_assets} asset URLs rewritten."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
