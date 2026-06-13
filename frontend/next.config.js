/** @type {import('next').NextConfig} */
const isGithubPages = process.env.GITHUB_PAGES === "true";
const configuredBasePath = process.env.GITHUB_PAGES_BASE_PATH ?? "/market-predictor";
const normalizedBasePath =
  configuredBasePath === "/"
    ? ""
    : configuredBasePath.startsWith("/")
      ? configuredBasePath
      : `/${configuredBasePath}`;

const nextConfig = {
  output: isGithubPages ? "export" : "standalone",
  basePath: isGithubPages && normalizedBasePath ? normalizedBasePath : undefined,
  assetPrefix: isGithubPages && normalizedBasePath ? `${normalizedBasePath}/` : undefined,
  trailingSlash: isGithubPages,
};

module.exports = nextConfig;
