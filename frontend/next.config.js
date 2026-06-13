/** @type {import('next').NextConfig} */
const isGithubPages = process.env.GITHUB_PAGES === "true";

const nextConfig = {
  output: isGithubPages ? "export" : "standalone",
  basePath: isGithubPages ? "/market-predictor" : undefined,
  assetPrefix: isGithubPages ? "/market-predictor/" : undefined,
  trailingSlash: isGithubPages,
};

module.exports = nextConfig;
