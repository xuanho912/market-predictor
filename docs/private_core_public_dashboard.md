# Private Core, Public Dashboard

Goal:

- keep the real research/code repository private,
- publish only the generated dashboard,
- keep API keys in GitHub Actions Secrets,
- keep normal phone usage through a fixed public URL.

## Recommended Structure

Use two repositories:

1. Private core repository:

```text
xuanho912/market-predictor
```

This keeps:

- backend code,
- model and feature engineering code,
- Alpha v1 and validation logic,
- Codex Skill files,
- research documents,
- GitHub Actions workflow,
- private caches and logs.

2. Public display repository:

```text
xuanho912/market-predictor-dashboard
```

This receives only generated static files from `outputs/public_dashboard_site`.
It should not contain backend code, scripts, `.agents`, `.github`, `.env`, model files, or API keys.

## What Remains Public

The public dashboard repository can expose:

- generated HTML, CSS, and JavaScript needed by the dashboard,
- generated JSON snapshots such as prediction dashboard data,
- the latest visible prediction results,
- the latest chart paths and data-quality labels.

Anything visible in the browser can still be copied or screenshotted. This setup protects the core work, not the already-published result.

## Required GitHub Settings

In the private core repo, open:

```text
Settings -> Secrets and variables -> Actions
```

Add or confirm this secret:

```text
FINNHUB_API_KEY
```

Add this secret:

```text
DASHBOARD_DEPLOY_TOKEN
```

Use a fine-grained GitHub token with the smallest scope possible:

- repository access: only `xuanho912/market-predictor-dashboard`,
- permission: Contents read and write.

Add these repository variables:

```text
PUBLIC_DASHBOARD_REPO=xuanho912/market-predictor-dashboard
PUBLIC_DASHBOARD_BRANCH=main
GITHUB_PAGES_BASE_PATH=/market-predictor-dashboard
```

If you later use a custom domain at the site root, set:

```text
GITHUB_PAGES_BASE_PATH=/
```

## Public Dashboard Repo Pages

In the public dashboard repo:

```text
Settings -> Pages
```

Set:

```text
Build and deployment -> Source -> Deploy from a branch
Branch -> main
Folder -> / (root)
```

The phone URL will normally be:

```text
https://xuanho912.github.io/market-predictor-dashboard/
```

## Daily Workflow

The private core workflow remains:

```text
.github/workflows/forward-alpha-v1.yml
```

On each run it:

1. downloads real market data where available,
2. runs the frozen forward-only tracker,
3. exports static dashboard JSON,
4. builds the static Next.js dashboard,
5. creates a sanitized public bundle,
6. scans the bundle for source code and secret markers,
7. pushes only that bundle to the public dashboard repo.

If `PUBLIC_DASHBOARD_REPO` is not configured, the public push step is skipped.

If `DASHBOARD_DEPLOY_TOKEN` is missing, the workflow does not expose anything; it emits a warning and skips public publishing.

## Safety Rules

- Do not put API keys in code.
- Do not put API keys in README files.
- Do not use `NEXT_PUBLIC_FINNHUB_API_KEY`.
- Do not let the frontend call Finnhub directly.
- Do not publish `backend/`, `scripts/`, `.agents/`, `.github/`, `.env`, `data/`, or model files to the public dashboard repo.
- Do not publish source maps.
- Do not change Alpha v1 threshold `0.32534311`.
- Do not upgrade Alpha v1 to confirmed alpha without forward validation.

## Does This Affect Normal Use?

Only a little:

- You still open one fixed URL on your phone.
- The dashboard still updates after GitHub Actions runs.
- The private core repo can be hidden from the public.
- The public site shows the latest generated result, not the core implementation.

The tradeoff:

- the public dashboard is static, not a live backend API,
- updates happen after the scheduled workflow completes,
- anyone with the public URL can see the displayed predictions.

For the current `RESEARCH ALPHA CANDIDATE` stage, this is the safest free structure.
